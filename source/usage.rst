Usage
-----

In order to use Princess you can either download the package from
Github or check out the repository and build it yourself.

Currentl llvm-13 is required for the compiler to run.
It is expected to find the compiler on the path, so you need
to hook it up like that. On Windows it calls ``clang`` and on
linux ``clang-13``. Make sure that it is supplied via the PATH.

There is currently no build for the VSCode extension available as
it is in very early stages of development. If you want to use it, you can
checkout the repo and use ``vsce package`` to create a .vsix package which
you can install in your VSCode environment. Currently there is no support
for other editors, but you may adapt the .tmlanguage file you find inside
of the VSCode extension, if your editor supports it.

The princess compiler itself supports the Language Server Protocol, so you
might be able to adapt it for other editors as well.

The command line arguments are as follows:

.. csv-table:: 
    :escape: #

    ``--ast``, Print the AST of the program as JSON
    ``--tokens``, Print the parsed tokens as JSON
    ``--typed-ast``, Print the typechecked AST as JSON
    ``--continue-on-output``, Continue compiling if any of the previous settings are applied
    ``--include``, Add directory to the include search path
    ``--define``, Add a globally available define like -DTest
    ``--link-directory``, Add search directory for linked libraries
    ``--link-library``, Load library
    ``--link-flag``, Pass flags directly to the linker
    ``--clang``, Pass flag directly to clang
    ``--buildfolder``, Specify an output directory to put temporary files in (defaults to .princess)
    ``--outfile``, Specifies an output file
    ``--debug``, Compiles debug information
    ``--rdynamic``, Inserts symbol information (for stack traces)
    ``--dependency-graph``, Print a dependency graph and abort compilation
    ``--version``, Print the version of the compiler
    ``--verbose``, Print additional verbose output
    ``--progress``, Print a progress bar
    ``--language-server``, Start the language server
    ``--no-incremental``, Compile without incremental support
    ``--name``, Set the name for the main file (if not main)
    ``--no-stdlib``, Compile without the standard library

This information can also be printed with the ``--help`` flag.

In order to compile a file, simply pass it as an argument to ``princess``, with any additional
arguments supplied.

.. warning:: 
    Do note that the default mode of the compiler is incremental compilation.
    This can speed up compilation significantly for big projects, but it might 
    fails sometimes. If the compiler segfaults, try compiling with \--no-incremental first
    before submitting a bug report.