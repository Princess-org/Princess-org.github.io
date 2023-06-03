from pygments.lexer import RegexLexer, include, bygroups
from pygments.token import *

class PrincessLexer(RegexLexer):
    name = "Princess"
    aliases = ["princess"]
    filenames = ["*.pr"]

    tokens = {
        "root": [
            (r"/\*", Comment.Multiline, "comment"),
            (r"//.*?$", Comment.Singleline),
            (r'"""\n', String, 'multiline_string'),
            (r'"', String, 'string'),
            (r"'\\.'|'[^\\]'|'\\u[0-9a-fA-F]{4}'", String.Char),
            (r'(\.)((?:[^\W\d]|\$)[\w$]*)', bygroups(Punctuation, Name.Attribute)),
            (r'#\w*', Keyword),
            (r'(unsigned|word|bool|char|byte|short|int|long|ubyte|ushort|uint|ulong|'
             r'int8|int16|int32|int64|uint8|uint16|uint32|uint64|float|double|float32|float64|size_t|string)\b', Keyword.Type),
            (r'\b(import)\b(\s*)', bygroups(Keyword.Namespace, Whitespace), 'import'),
            (r'(assert|break|case|continue|in|else|loop|for|yield|defer|as|'
             r'if|go_to|return|switch|while|export|var|let|def|type|weak_ref)\b', Keyword),
            (r'(import)\b(def|var|const)\b', bygroups(Keyword, Keyword.Declaration)),
            (r'(true|false|null)\b', Keyword.Constant),
            (r'(struct|interface|enum|const)\b', Keyword.Declaration),
            (r'[a-zA-Z_$]\w*', Name),
            (r'([0-9][0-9_]*\.([0-9][0-9_]*)?|'
             r'\.[0-9][0-9_]*)'
             r'([eE][+\-]?[0-9][0-9_]*)?[fFdD]?|'
             r'[0-9][eE][+\-]?[0-9][0-9_]*[fFdD]?|'
             r'[0-9]([eE][+\-]?[0-9][0-9_]*)?[fFdD]|'
             r'0[xX]([0-9a-fA-F][0-9a-fA-F_]*\.?|'
             r'([0-9a-fA-F][0-9a-fA-F_]*)?\.[0-9a-fA-F][0-9a-fA-F_]*)'
             r'[pP][+\-]?[0-9][0-9_]*[fFdD]?', Number.Float),
            (r'0[xX][0-9a-fA-F][0-9a-fA-F_]*[lL]?', Number.Hex),
            (r'0[bB][01][01_]*[lL]?', Number.Bin),
            (r'0[0-7_]+[lL]?', Number.Oct),
            (r'0|[1-9][0-9_]*[lL]?', Number.Integer),
            (r'[~^*!%&\[\]<>|+=/?-@]', Operator),
            (r'->', Operator),
            (r'[{}();:.,]', Punctuation),
            (r'[^\S\n]+', Whitespace)
        ],
        "import": [
            (r"([a-zA-Z_$]\w*)(\s*)(,)", bygroups(Name.Namespace, Whitespace, Punctuation)),
            (r"([a-zA-Z_$]\w*)", Name.Namespace, "#pop"),
            (r'[^\S\n]+', Whitespace)
        ],
        "comment": [
            (r"[^*/]+", Comment.Multiline),
            (r"/\*", Comment.Multiline, "#push"),
            (r"\*/", Comment.Multiline, "#pop"),
            (r"[*/]", Comment.Multiline)
        ],
        "multiline_string": [
            (r'"""', String, "#pop"),
            (r'"', String),
            include("string")
        ],
        "string": [
            (r'[^\\"]+', String),
            (r'\\\\', String),
            (r'\\"', String),
            (r'\\', String),
            (r'"', String, "#pop")
        ]
    }