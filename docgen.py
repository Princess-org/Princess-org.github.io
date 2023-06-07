import requests
import shutil
import os
import sys
import subprocess
import json
import textwrap
import pypandoc

ZIP_URL = "https://github.com/Princess-org/Princess/archive/refs/heads/master.zip"
PATH = "compiler/Princess-master"

DOCS = [
    "std",
    "arena",
    "getopt",
    "io",
    "json",
    "map",
    "optional",
    "process",
    "set",
    "shared",
    "strings",
    "vector",
    "runtime"
]

def download_source():
    zip_file = "princess.zip"
    data = requests.get(ZIP_URL)
    open(zip_file, "wb").write(data.content)
    shutil.unpack_archive(zip_file, "compiler")
    os.remove(zip_file)

def download_compiler():
    os.environ["LIBRARY_PATH"] = "."
    sys.argv = ["build.py", "download"]
    process = subprocess.Popen([sys.executable, "build.py", "download"], cwd = "compiler/Princess-master")
    process.wait()

def generate_json():
    process = subprocess.Popen([f"{PATH}/bin/princess", "--typed-ast", "--emit-only-functions", "--no-incremental", "./docall.pr"], stdout = subprocess.PIPE)
    out, err = process.communicate()
    if process.returncode != 0:
        print("Couldn't create documentation!", file = sys.stderr)
        exit(1)
    
    with open("docall.json", "wb") as fp:
        fp.write(out)

def ident_to_str(ident):
    return "::".join(ident["path"])

def type_to_str(value):
    if value["kind"] == "Identifier":
        return ident_to_str(value)
    elif value["kind"] == "Struct" or value["kind"] == "Union":
        ret = "struct {\n" if value["kind"] == "Struct" else "struct #union {\n"
        body = ""
        for member in value["body"]:
            if member["kind"] == "IdDeclStruct":
                body += ident_to_str(member["ident"]) + ": " + type_to_str(member["tpe"]) + "\n"
            elif member["kind"] == "Struct":
                body += type_to_str(member) + "\n"
        ret += textwrap.indent(body, "    ")
        ret += "}"
        return ret
    elif value["kind"] == "PtrT":
        if value["tpe"]:
            tpe = type_to_str(value["tpe"])
        else: tpe = None
        return "*" + tpe if tpe else ""
    elif value["kind"] == "RefT":
        if value["tpe"]:
            tpe = type_to_str(value["tpe"])
        else: tpe = None
        return "&" + tpe if tpe else ""
    elif value["kind"] == "ArrayT":
        return "[" + type_to_str(value["tpe"]) + "]"
    elif value["kind"] == "TypeConstructor":
        args = ", ".join(map(type_to_str, value["args"]))
        return ident_to_str(value["name"]) + "(" + args  + ")"
    elif value["kind"] == "FunctionT":
        ret = "(" + ", ".join(map(type_to_str, value["args"])) + ") -> "
        ret += "(" + ", ".join(map(type_to_str, value["ret"])) + ")"
        return ret
    elif value["kind"] == "Enum":
        ret = "enum {\n"
        body = ""
        for member in value["body"]:
            body += ident_to_str(member["ident"])
            value = value_to_str(member["value"])
            if value:
                body += " = " + value
            body += "\n"

        ret += textwrap.indent(body, "    ")
        ret += "}"
        return ret
    elif value["kind"] == "StructuralT":
        ret = "interface {\n"
        body = ""
        for member in value["body"]:
            body += "def " + ident_to_str(member["name"])
            body += "(" + ", ".join(map(lambda par: ident_to_str(par["name"]) + ": " + type_to_str(par["tpe"]), member["params"])) + ")"
            if member["returns"]:
                body += " -> "
                body += ", ".join(map(type_to_str, member["returns"]))
                body += "\n"
        ret += textwrap.indent(body, "    ")
        ret += "}"
        return ret
    elif value["kind"] == "TypeT":
        return "type " + type_to_str(value["expr"])
    else:
        return value["kind"]

def value_to_str(value):
    if value == None: return None
    if value["kind"] == "Integer":
        return str(int(value["value"]))
    elif value["kind"] == "String":
        return '"' + value["value"] + '"'
    elif value["kind"] == "Float":
        return str(value["value"])
    elif value["kind"] == "Boolean":
        return str(value["value"])
    elif value["kind"] == "USub":
        return "-" + value_to_str(value["expr"]) # TODO Quotes where necessary

    return "..." # We don't know what to do with this

def param_to_str(par):
    res = ""
    if par["kw"] == "TYPE":
        res += "type "

    res += ident_to_str(par["name"])
    if par["tpe"]:
        res += ": " + type_to_str(par["tpe"])
    return res

def tc_param_to_str(par):
    res = "type "
    res += ident_to_str(par["name"])
    if par["tpe"]:
        res += ": " + type_to_str(par["tpe"])
    return res

def print_doc(doc, fp):
    print(file = fp)
    print(pypandoc.convert_text(doc, "rst", format = "md"), file = fp)

def generate_documentation():
    with open("docall.json", "r") as fp:
        data = json.load(fp)
        
        with open(f"source/stdlib.rst", "w") as fp:
            print("Standard library", file = fp)
            print("----------------", file = fp)
            for doc in DOCS:
                print(doc, file = fp)
                print("~" * len(doc), file = fp)
                print(file = fp)

                functions = []
                variables = []
                types = []

                body = data[doc]["body"]
                for symbol in body:
                    if symbol["share"] == "EXPORT" or symbol["share"] == "BOTH":
                        if symbol["kind"] == "Def":
                            functions.append(symbol)
                        elif symbol["kind"] == "VarDecl":
                            variables.append(symbol)
                        elif symbol["kind"] == "TypeDecl":
                            types.append(symbol)

                if types:
                    print("Types", file = fp)
                    print("^^^^^", file = fp)

                    for symbol in types:
                        for i, type in enumerate(symbol["left"]):
                            tpe = symbol["right"][i]
                            print(".. code-block:: princess\n", file = fp)
                            if type["kind"] == "Identifier":
                                name = ident_to_str(type)
                                res = f"type {name} = {type_to_str(tpe)}"
                                print(textwrap.indent(res, "    "), file = fp)
                            elif type["kind"] == "TypeConstructor":
                                name = ident_to_str(type["name"])
                                res = f"type {name}({', '.join(map(tc_param_to_str, type['args']))}) = {type_to_str(tpe)}"
                                print(textwrap.indent(res, "    "), file = fp)

                        if "doc" in symbol:
                            print_doc(symbol["doc"], fp)

                    print(file = fp)

                if variables:
                    print("Variables", file = fp)
                    print("^^^^^^^^^", file = fp)

                    for symbol in variables:
                        kw = symbol["kw"].lower()
                        right = symbol["right"]
                        left = symbol["left"]
                        for i, var in enumerate(left):
                            value = "..."
                            if i < len(right):
                                r = right[i]
                                value = value_to_str(r)

                            if var["kind"] == "IdDecl":
                                print(".. code-block:: princess\n", file = fp)
                                ident = var["value"]
                                tpe = ident["type_tag"]["name"]
                                name = ident_to_str(ident)
                                print(f"    {kw} {name}: {tpe} = {value}", file = fp)
                        
                        if "doc" in symbol:
                            print_doc(symbol["doc"], fp)   

                    print(file = fp)

                if functions:
                    print("Functions", file = fp)
                    print("^^^^^^^^^", file = fp)

                    for symbol in functions:
                        name = ident_to_str(symbol["name"])
                        print(".. code-block:: princess\n", file = fp)
                        body = "    def " + ident_to_str(symbol["name"])
                        body += "(" + ", ".join(map(param_to_str, symbol["params"])) + ")"
                        if symbol["returns"]:
                            body += " -> "
                            body += ", ".join(map(type_to_str, symbol["returns"]))
                            body += "\n"
                        print(body, file = fp)

                        if "doc" in symbol:
                            print_doc(symbol["doc"], fp)

                    print(file = fp)

                    


def main():
    download_source()
    download_compiler()
    generate_json()
    generate_documentation()

if __name__ == "__main__":
    main()