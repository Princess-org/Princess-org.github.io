Grammar
-------

Keywords
~~~~~~~~

Keywords as defined by the language are the following:

.. code:: none

    export, type, struct, interface, def, in, 
    null, return, break, go_to, case, switch, 
    label, if, else, for, while, continue, 
    yield, const, do, word, unsigned, enum, 
    size_of, offset_of, import, defined, type_of,
    align_of, as, loop, this, and, or, not,
    defer, is, weak_ref, implicit

These may not be used as identifier names.

Compiler macros start with a hash, they are used in various places
where it wasn't warranted to use a keyword. Notable examples are
``#union`` and ``#test``. These are handled like keywords in the parser
so they may appear in different places.

Identifiers
~~~~~~~~~~~

Identifiers can be defined according to the regex:
``[A-za-z_][A-za-z0-9_]*``

Do note that the identifier ``_`` behaves in a special way,
this is explained in the section about variables.

String Literals
~~~~~~~~~~~~~~~

String literals may be defined using double quotes.
The following escape sequences are allowed inside of string literals:

.. csv-table:: 

    ``\a``, Ascii bell
    ``\b``, Backspace
    ``\f``, Form feed
    ``\n``, New line
    ``\r``, Carriage return
    ``\t``, Tabulator
    ``\v``, Vertical tabulator
    ``\0``, Null byte
    ``\"``, Double quote
    ``\'``, Single quote
    ``\\``, Backslash
    ``\xFF``, Character with value as defined by the hexadecimal number
    ``\uFFFF``, Uncode character in the range of 0 to 65535
    ``\UFFFFFFFF``, Unicode character in the full range of unicode
    
Additionally triple quoted strings may be used that span over multiple lines.
Do note that all whitespace contained in these strings is encoded.

Character literals are enclosed with single quotes. The same escape sequences
are allowed for characters (except for the two unicode escape sequences). Do note
that a char is defined as a single byte, and not a unicode character.

Numeric Literals
~~~~~~~~~~~~~~~~

Numbers can be defined as follows:

.. code-block:: princess

    // These are all of type int
    1000   // This is a regular number
    0xFF   // Hexadecimal number
    0o77   // Octal number
    0b1100 // Binary number

    1000.5 // This if of type double
    10e20  // Scientific notation is allowed

Internally, integers are stored as ``uint64``, which means you can convert
them to larger types.

Comments
~~~~~~~~

.. code-block:: princess

    // This is a single line comment

    /* Multi line comments 
        /* may be nested */ 
    */

Expressions
~~~~~~~~~~~

In general, no semicolons are used. This means that an expression
ends when it is done parsing, that is the parser does not expect additional input.
This means that in order for an expression to span multiple lines it either has
to be wrapped in parenthesis or an operator has to appear at the end of a line:

.. code-block:: princess

    // This does not work
    10
    + 20

    // This is legal
    10 +
    20

    // This is also legal
    (10
    + 20)

    // And this
    return 10,
        20

While these rules may appear to be confusing at first, you will certainly get used to it
when writing more code.

Additionally, you may use semicolons to separate multiple expressions on the same line.

Operators
~~~~~~~~~

Operators largely work as they do in other programming languages.
The two special Operators in Princess are `++` and `\--` which are
dedicated pointer arithmetic operators. This allows operator overloading
on pointer types while also keeping pointer arithmetic.

The precedence of the binary operators is as follows:

.. csv-table:: 
    :escape: #

    10, ``!``                                   , cast expression
     9, ``&``#, ``|``#, ``^``#, ``<<``#, ``>>`` , bitwise operators
     8, ``*``#, ``/``#, ``%``                   , multiplication
     7, ``+``#, ``-``#, ``++``#, ``--``         , addition
     6, ``>``#, ``<``#, ``>=``#, ``<=``         , comparison
     5, ``and``                                 , logical and
     4, ``or``                                  , logical or
     3, ``..=``#, ``..``                        , ranges
     2, ``+=``#, ``*=``#, etc                   , assign operator composition
     1, ``=``                                   , assignments
