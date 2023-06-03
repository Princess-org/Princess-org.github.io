Modules
-------

Imports
~~~~~~~

Every file created with the ``.pr`` extension is considered a Princess source file.
Imports are always relative to the current file, unless the import is prefixed by
``::``, in which case it is a top level module.

Do note that the main module is always called "main", and can be imported as
such, even if the actual file name is different. The current file
is specified in the ``__file__`` variable.

Imports might currently only work at top level. It is good practice to define
imports at the beginning of a file.

.. code-block:: princess

    import my_module
    import set as alias // Imports may be renamed
    import map

    def main {
        let my_map = map::make(int)
        let s = alias::make(int)
    }
    main

Only functions and variables marked with ``export`` may be used from other modules.

Do note that imported functions and variables may be refered by their
actual name *or* by simply the function name. Note however, that if you only use the
function name, you may get an ambiguous reference error if there are multiple functions
with the same name and the same parameters imported.

It is therefore good practice to use the full name whenever possible.
Since a function call ``a.foo()`` is equivalent to ``foo(a)``, you are technically only
using the function name and not the fully qualified name when accessing functions in that
way. 

Technically you could write ``a.module::foo()`` but this is considered bad practice
and if you import two functions that clash in such a way, it is better to use ``module::foo(a)``.

Re-Export
~~~~~~~~~

It is possible to re-export (exported) functions and variables from other
modules. This is done using the ``from module export function``. Do note that you can specify
multiple functions, and also use the wildcard ``*`` to export all functions from that file.
This can be useful if you want to split your API over various files but you still want to
export all functionality from a single module.

.. code-block:: princess

    from strings export *

Standard imports
~~~~~~~~~~~~~~~~

There are certain files which get imported into every module.
These are: ``cstd.pr``, ``std.pr``, ``runtime.pr`` and ``optional.pr``.
This is because these files contain code which is required to be present for
certain language features.

You can however skip these by using the ``--no-stdlib`` flag. But note that not
all of the language features keep working if you do this.

Importing C functions
~~~~~~~~~~~~~~~~~~~~~

Currently there is no direct way to import functions from C or other programming
languages. You need to either write the headers yourself using ``#extern`` or
you may use the gencstd.py file provided by the compiler to generate the headers for you.

Do note that the standard C library is already provided via ``cstd.pr``. On linux, you also
have access to most of the linux headers defined via ``linux.pr``, and on windows you have
the windows headers from ``windows.pr``.

In the future it is going to be possible to import C header files directly.