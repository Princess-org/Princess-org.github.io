Statements and Expressions
--------------------------

Variables
~~~~~~~~~

There are three keywords to define variables: ``var``, ``let`` and ``const``.
``var`` and ``let`` get assigned at runtime and ``const`` gets evaluated at compile time.
``let`` may only be assigned during its declaration, otherwise the value is supposed to be
a constant.

Variables in global scope might additionally be specified with ``export`` to make other
modules able to refer to them.

Additionally, the ``#extern`` pragma may be applied. Normally variables are prefixed
by the module name in the form of ``module::name`` in the resulting binary. If
extern is specified, only the name of the variable is used as the name inside the binary.

.. code-block:: princess

    // Let must be assigned a value
    let a = 20
    // a = 30 // This is illegal because 
    // let creates a constant

    // You may assign multiple values at once
    var b, c = 10, 30

    // You can define the type 
    // of a variable like this
    var d: int64 = 4

    // This variable is a compile time constant
    const MY_CONST = 10 * 20
    //               ~~~~~~~
    //      This runs at compile time

    // This variable is exported
    export var special = 20

A variable that is called ``_`` may be defined multiple times. Accessing it is not recommended
but it is going to return the last written value. This is useful for discarding certain arguments:

.. code-block:: princess

    def a_lot_of_stuff -> int, int, int {
        return 10, 20, 30
    }

    let a, _, _ = a_lot_of_stuff()

Cast expression
~~~~~~~~~~~~~~~

You can convert between types using the cast expression.
It looks like this:

.. code-block:: princess

    let a: double = 20.5
    let b = a !int

Do note that sometimes there might be data loss. 

If you want to convert the bit pattern, then you have to use pointers. 
Unlike in C, an operation like this is not undefined behavior, 
so you are safe to do it that way.

If statements
~~~~~~~~~~~~~

The if statements in Princess work just like in any other programming language.
Do note that you do *not* need parenthesis around the condition. Do note that
every if statement needs to be followed by ``{}``.

.. code-block:: princess

    var a = 20

    if a > 15 {
        print("A is bigger than 15\n")
    } else if a > 10 {
        print("A is bigger than 10\n")
    } else {
        print("A is something else!\n")
    }

Additionally there is an if expression which works like this:

.. code-block:: princess

    let a = 20 if 10 == 20 else 30

It works basically like the ternary operator in C just with a more sensible syntax.

Static if
~~~~~~~~~

Static ifs work just like normal if statements, except that the expression gets evaluated
at compile time. This means that the body of the if statement is getting substituted
in the constant evaluation stage. Only the parser needs to be happy about
the contents, and the branches that are cut out don't get typechecked.
Do note that an ``#if`` statement doesn't create a new scope but instead everything inside
is of the parent scope. That means variables defined inside of it are visible from outside.

.. code-block:: princess

    #if defined WIN32 {
        def my_code() -> int { return 1 }
    } else {
        def my_code() -> int { return 2 }
    }

Switch statement
~~~~~~~~~~~~~~~~

The switch statement currently only works for integral types and enums.
Unlike in C, there is no fallthrough. You can specify multiple
values in a single case, or use ranges to match multiple values.
Do note that the case labels need to be compile time constants.

There might optionally be one case label without arguments, 
which is called when none of the other cases match.

.. code-block:: princess

    var i = 20
    switch i {
        case 10, 20: print("Good number")
        case 20..40: print("Bad number")
        case: print("I don't know about this")
    }

Loops
~~~~~

In Princess there are three kinds of loops. ``while``, ``loop`` and ``for``.
Additionally you may exit a looop with ``break`` or go to the next iteration with ``continue``.

.. code-block:: princess

    var i = 0
    loop {
        if i == 2 { continue }
        print(i, " ")
        i += 1
        if i == 10 { break }
    }
    print("\n")

A ``loop`` is basically analog to ``while true``. It executes forever until a ``break`` is
used to exit the loop.

A while loop executes while a condition holds true:

.. code-block::

    var i = 0
    while i < 10 {
        print(i, " ")
        i += 1
    }
    print("\n")

A for loop might go over a range, or the values in a generator.

.. code-block:: 

    for var i in 0..10 {
        print(i, " ")
    }
    print("\n")

Assert
~~~~~~

Assert is basically a way to make sure that a condition is true, and abort
in the case of failure. This is to make sure that the program is in a safe state,
and not to return errors to the user of your program. When an assertion is failing,
it is printing the message specified and a stack trace. Do note that assertions
behave a bit differently inside of tests, see the section on :ref:`this <tests>` for more information.

.. code-block:: princess

    // This simply fails (unreachable code)
    assert
    // This fails if the condition is met
    assert 1 + 5 == 6
    // This also prints a message
    assert 10 == 20, "This fails"

Functions
~~~~~~~~~

Functions may be defined at top level with the keyword `def` like this:
The arguments are specified in parenthesis after the function name and
are of the form "name": "type". Do note that the types need to be defined
here and can't be inferred like for variables. 

The return type is optionally
defined by using an arrow followed by one or more return types.

.. code-block:: princess

    def add(a: int, b: int) -> int {
        return a + b
    }

    def foo -> int {
        return 10
    }

Do note that functions may be defined in any order, so this is perfectly valid:

.. code-block:: princess 

    hello

    def hello {
        print("Hello World!\n")
    }

Note however that this does not apply to compile time code. Inside of a const or
a function that is called at compile time, the function may only refer to code that
has already been defined. This might not be a problem if you import a module as
everything in there has been defined already, but watch out if using compile time code
in the same module.

You might mark a function with ``implicit``. When trying to convert from a type A into a type B
it is going to search for an implicit function that is imported into the current scope.

.. code-block:: princess

    type A = struct { s: Str }

    implicit def to_string(a: A) -> Str {
        return a.s
    }

    let a = { "Hello" } !A
    let b: Str = a // implicit call here

Just like variables, ``#extern`` may be used on a function, this does exactly the same thing.

Functions may optionally be defined without a body, this might be useful if you are referring
to a function that is provided by an external library.

A windows only functionality is the ``#dllimport`` and ``#dllexport`` flags which do import
a function from a DLL or export it when creating a DLL.

Additionally a function may have a variable amount of parameters. For this you either define the
last argument as ``...`` or together with a type like this: ``a: int...``. The first form
is only useful when calling to C as there is no way to read out the arguments which are supplied
in that way. The second form passes an array of type ``[int]`` in this case. The function may
also be called with an array as the last argument, which does pass the array as varargs.

.. warning:: Do note that the array gets cleaned up by the calling function after
    calling your function, so you need to copy it if you plan 
    to store it in a global variable.

.. code-block:: princess

    def some_function(...) {}

    some_function(10, "string", -2.5)

    def sum(args: int...) -> int {
        var sum = 0
        for var arg in args {
            sum += arg
        }
        return sum
    }

Functions may be overloaded, that is they might have the same name but accept different arguments:

.. code-block:: princess

    def add(a: int, b: int) -> int {
        return a + b
    }

    def add(a: double, b: double) -> double {
        return a + b
    }

    add(10, 5) // This calls the first function
    add(10.5, 5.2) // second function

An overloaded function may be accessed by using the parameters directly on the identifier:

.. code-block:: princess

    let a = *add::(double, double)
    let b = *add::(int, int)

Polymorphic Functions
~~~~~~~~~~~~~~~~~~~~~

A function may become polymorphic if it gets specialized with a specific type at compile time.
Currently there are a few ways to create polymorphic functions. One is by accepting a
specific type like so:

.. code-block:: princess

    def my_function(type A) -> A {
        return {} !A
    }

This essentially means, that a type is provided to the function at compile time. So multiple
versions of this function get created if different types get specified here.
Do note that ``A`` is only valid after its creation, so you can not refer to the type ``A``
from an argument that is prior to the type argument.

There is also a way to accept arguments of a type directly like so:

.. code-block:: princess

    def my_function(a: type T) -> T

This will take the type that is supplied as the argument itself.
You can also provide types that are more complex:

.. code-block:: princess

    def my_function(a: type [T]) -> T

This essentially means that the function only accepts arrays as a parameter.

The other way of creating polymorphic functions is by using interfaces. More on that
see the section about :ref:`Interfaces <interfaces>`.


Operator Overloading
~~~~~~~~~~~~~~~~~~~~

A function may refer to an overloaded operator if it is using that operator as a name.
These functions get converted to have a different name in the final output and can be
referenced as that.

Do note that neither pointer arithmetic nor the ``and``, ``or`` or the ``.`` operator
can be overloaded. Additionally, the reference ``*`` and dereference ``@`` operators
may not be overloaded either.

``::`` also looks like an operator but it is actually part of an
identifier.

.. csv-table:: 

    Unary Additon, \+         , ``def __pos__``
    Binary Additon, \+        , ``def __add__``
    Unary Subtraction, \-     , ``def __neg__``
    Binary Subtraction, \-    , ``def __sub__``
    Multiplication, \*        , ``def __mul__``
    Division, /               , ``def __div__``
    Modulo, %                 , ``def __mod__``
    Right Shift, \>\>         , ``def __rshift__``
    Left Shift, <<            , ``def __lshift__``
    Bitwise and, &            , ``def __and__``
    Bitwise or, \|            , ``def __or__``
    Bitwise xor, ^            , ``def __xor__``
    Bitwise negation, ~       , ``def __invert__``
    Less than, <              , ``def __lt__``
    Greater than, >           , ``def __gt__``
    Less or equal, <=         , ``def __le__``
    Bigger or equal, >=       , ``def __ge__``
    Equal, ==                 , ``def __eq__``
    Not equal, !=             , ``def __ne__``
    Compound assignment, -=   , ``def __isub__``
    Compound assignment, +=   , ``def __iadd__``
    Compound assignment, \*=  , ``def __imul__``
    Compound assignment, /=   , ``def __idiv__``
    Compound assignment, %=   , ``def __imod__``
    Compound assignment, >>=  , ``def __irshift__``
    Compound assignment, <<=  , ``def __ilshift__``
    Compound assignment, &=   , ``def __iand__``
    Compound assignment, \|=  , ``def __ior__``
    Compound assignment, ^=   , ``def __ixor_-``

Tests
~~~~~

A function may be marked with ``#test``, this renames the function by prepending ``__test::``
to it and adds an extra context parameter called env. The built in testrunner can compile a file with
test functions in it and it is basically going to run a separate process to call these functions.
This means that a segmentation fault or similar is not going to bring down the entire test
runner.

The env parameter essentially looks like this and is defined in runtime.pr:

.. code-block:: princess

    export type TestEnvironment = struct {
        out: def () -> &string
        err: def () -> &string
        assertion_handler: def (bool, *char) -> ()
    }

Out and err return the captured standard output and standard error, so that the
test can make assumptions based on these. Calling any of these functions will reset
the buffer, which means that when calling it again it is not going to return
text that has been printed prior to the first call.

.. code-block:: princess

    def #test test_random_stuff {
        assert 10 == 10

        print("Hello World")

        assert env.out() == "Hello World"
    } 

.. _tests: 

``assert`` statements will evaluate and call ``env.assertion_handler`` instead of aborting
the program outright.

Generators
~~~~~~~~~~

Generators are basically coroutines that may return multiple values. Any function can become
a generator by using a ``yield`` statement in its body. The return type of the function is
going to be ``runtime::Generator(T)`` with T being the specified return value of the function.

Generators can be used manually by calling ``generator.next()`` which returns an ``Optional(T)``.
When this ``Optional`` is empty, the Generator was done processing.

Alternatively you may use a for loop to iterate over a generator.

.. code-block:: princess

    def generator -> int {
        yield 1
        yield 2
        return 3 // A return stops the generator 
                 // and returns a last value
    }

    for var i in generator {
        print(i, " ")
    }
    print("\n")

You may also use ``yield from`` inside a generator to chain generators together, this is basically
equivalent to using a for loop and yielding every value from the generator.

Closures
~~~~~~~~

Functions defined inside of other functions are basically closures.
They have the type ``(A, B) -> (C, D)``.

A closure has access to the variables of the outer function but only
as copies. It is possible however to refer to the addresses of variables
outside of the closure. You can use this to modify variables from outside
of the closure. 

.. warning:: Do note however that the lifetime of these variables is
    not extended. When the calling functon returns, these variables are gone.

.. code-block:: princess

    def main {
        var a = 5
        var b = 20
        def closure {
            assert b == 20
            let pa = *a
            assert @pa == 10
        }
        b = 30
        a = 10

        closure()
    }
    main

Function calls
~~~~~~~~~~~~~~

Function calls in Princess are the function name followed by an open parenthesis and a
closing parenthesis. Do note that functions with zero arguments may be called without
the parenthesis. This means that if you want to take a reference of a function, you
need to use the address of ``*`` operator.

A function call might optionally use named arguments at the end of the argument list.
These might be mixed with normal function calls as needed. The order of the named arguments
is not fixed, you may call them in any order.

.. code-block:: princess

    def my_function(a: int, b: double, option: bool) {}

    my_function(10, 1.5, option = false)

Constructors and Destructors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Do note that there are two extra magic methods in Princess to
support RAII and valid copying. Do note that both of these functions
must be marked ``export``

The first is the copy constructor. This gets called whenver a value is copied.
It receives a pointer to the new object as the first argument and a pointer to your object 
as the second argument. Do note that if a copy constructor is defined, 
the object's data is not getting cloned, you have to do that yourself!

The second special function is the destructor. It gets called whenver your object
gets out of scope. You can use it to clean up resources. It gets a pointer to your object
as the only argument.

.. code-block:: princess

    type MyStruct {
        a: *int
    }

    def make_my_struct(a: int) {
        let ptr = allocate(int)
        @ptr = a
        return { ptr } !MyStruct
    } -> MyStruct

    export def construct(
        copy: *MyStruct, this: *MyStruct) {

        copy.a = allocate(int)
        @copy.a = @this.a
    }

    export def destruct(this: *MyStruct) {
        free(this.ptr)
    }