Types
-----

Type definitions in the Princess language may be aliased as follows:

.. code-block:: princess

    type MyInt = int
    // You can now use MyInt in place of int
    type MyStruct = struct { a: int }
    // This is a regular type definition. 
    // While it is possible to use the
    // right hand side as a regular type, 
    // it will not yield the expected result 
    // as no structure would implement said type

Numeric types
~~~~~~~~~~~~~

Predefined platform dependant numeric types are as follows:

.. csv-table:: 
    
    ``char``, 8 bit character type
    ``byte``, 8 bit signed integer type
    ``ubyte``, 8 bit unsigned integer type
    ``short``, 16 bit signed integer type
    ``ushort``, 16 bit unsigned integer type
    ``int``, 32 bit signed integer type
    ``uint``, 32 bit unsigned integer type
    ``long``, 64 bit signed integer type
    ``ulong``, 64 bit unsigned integer type
    ``float``, 32 bit floating point type
    ``double``, 64 bit floating point type

The sizes are specific to a Linux environment, these might change on other platforms.
Most notably, on Windows long is actually 32 bit.

In addition to these there are also predefined integer types with specific sizes:

.. csv-table::
    :escape: #

    Signed integer types:, ``int8``#, ``int16``#, ``int32``#, ``int64``#, ``int128``
    Unsigned integer types:, ``uint8``#, ``uint16``#, ``uint32``#, ``uint64``#, ``uint128``
    Floating point types:, ``float32``#, ``float64``#, ``float80``

Use these if you need a specific size.

Additionally, if you need a size that isn't predefined, you can use ``word`` and ``unsigned word``
as follows:

.. code-block:: princess

    type int256 = word(265)
    type uint256 = unsigned word(265)

Integer literals are at maximum 64 bit, so you probably need bit shifts to initialize these.

Boolean type
~~~~~~~~~~~~
The boolean Type in Princess is called `bool`. It is 8 bits wide.
If you want to use your type to convert to bool, implement an implicit function
for it. It is standard practice to use conversions to bool when testing for presence of an object.

.. code-block:: princess

    let foo: &int = null

    // Encouraged
    if foo {
    }

    // Discouraged
    if foo != null {
    }

    let s: Str = ""

    // This tests if the string is not empty
    if s {
    }

Strings
~~~~~~~

String literals do have the type ``[char]`` or ``string`` which is a deprecated alias for it.
A string literal is zero terminated. You can access a String's length with the ``length`` function.
``string.size`` is the array field and contains the trailing zero

In the standard library (strings.pr), there are several additional String types. The interface ``String``
is what should be used if a string is used as a parameter. This is because the other String types implement
that interface. While a regular ``[char]`` is mutable, the ``String`` interface
does not define a mutator function. There is an implicit function that converts a regular ``[char]`` to that type. Do note
that the result of that conversion is a ``StringSlice`` which points at the original ``[char]``'s data.
This means that no copy is made and that if the original is freed, the slice becomes invalid.

A ``StringSlice`` is essentially a view of another String. When a normal ``String`` is converted to a ``StringSlice``
it keeps a reference to that ``String`` in memory, so that it won't be freed.

The most useful String type is ``Str``. This is what should essentially be used when storing Strings inside
of structures. When you are using an internal method, which is not exposed to an API you may also accept
that String type to avoid costly conversions. ``Str`` also has a small string optimization built in, which
is useful to avoid heap allocations.

.. code-block:: princess 
    
    import strings

    let my_string: [char] = "Some string"
    let str: Str = to_str(my_string)

    let slc = str.slice(0, 4)
    assert slc == "Some"

    def first_character(s: String) -> char {
        return s(0)
    }

    assert first_character(my_string) == 'S'
    assert first_character(str) == 'S'

String concatenation is done via another type ``StringBuffer``. ``String`` implicitly converts to
it. In order to append strings, simply use the overloaded add-operator. 
If you want your type to be convertable to ``String``, simply implement the interface ``ToString`` for it.

.. code-block:: princess

    type Employee = struct {
        name: Str // Do use Str here
        age: int
    }

    export def to_string(employee: &Employee) -> String {
        return "Employee name: " + employee.name + 
            " age: " + employee.age
    }

    let employee = [ name = "Bob", age = 35 ] !&Employee

    var hello: StringBuffer = "Hello "
    hello += employee + "!"

    let s = to_str(hello)
    print(s, "\n")

    // Output:
    // Hello Employee name: Bob age: 35!

Structure types
~~~~~~~~~~~~~~~

A structure is essentially an aggregate type that contains
multiple elements. While it is allowed to use an empty struct,
this currently fails as llvm doesn't like empty structs.

A structure type is defined as follows:

.. code-block:: princess

    type MyStruct = struct {
        a: Str
        b: int
        // Structs may be nested
        c: struct {
            a: int
            b: double
        }
    }

All fields of a structure are accessable from outside
of the current module, there is no notion of private fields.

Unions are a special type of struct where each element occupies
the same memory location:

.. code-block:: princess
    
    type Union = struct #union {
        a: int
        b: double
    }

A union occupies the size of the largest member. While in C it is
not allowed to write to one member and read from another, this is perfectly
valid in Princess. It is up to you to find a good use for that though.

You can create instances of structs by using a cast like this:

.. code-block:: princess
    
    type MyStruct { a: int; b: double }

    let s = [ a = 10, b = 10.5 ] !MyStruct

You can leave out elements and they will be zero-initialized.
Unlike functions calls, every attribute needs to be assigned by name.
You can get around this for your own data types by defining your own constructor function.

Enum types
~~~~~~~~~~

Like in C it is also possible to define enum types. Members of the
enum are accessed with the ``::`` like on modules. An enum might
optionally define a type which it maps to. By default all enums behave
like the ``int`` type.

Enums also auto generate a ``to_string`` method which return a ``[char]`` that
equates to the enum name.

.. code-block:: princess

    type MyEnum = enum {
        FOO; BAR
        BAZ = 20 // You may assign values
    }

    // This enum maps to int64
    type MyOtherEnum = enum: int64 {
        A; B; C; D
    }

    let a: MyEnum = MyEnum::BAR
    assert a == 1
    assert a.to_string() == "BAR"

Pointers
~~~~~~~~

Pointers work like in C, they are essentially a type that stores a memory address.
You can take the address of a variable by using the ``*`` operator. You can get the value
of a pointer by using the ``@`` operator. The type of pointers is essentially ``*T``.

The type may be ommited, in that case it is similar to a void pointer in C.

.. code-block:: princess

    var a = 20
    let b: *int = *a
    @b = 10
    print(a, "\n") // This should print 10
    
    let c: * = b // This is a void pointer
    // You may not get the value, 
    // you have to cast it
    // before you are able to do that
    let d = @(c !*int)

References
~~~~~~~~~~

References are essentially a reference count together with the data and a type member.
It is highly encouraged to use those instead of manual memory management. When the reference
count reaches zero, the memory is automatically cleaned up. You may define a destructor to
make sure to clean up the memory.

In order to create a reference to a type, simply cast it to a reference of the same type. 
This will copy the data and create a valid reference. Note however that creating a
constructor function which does this is standard practice.

For situations where a reference cycle might be created, use ``weak_ref(T)`` in order
to break the cycle. In the future there might be a garbage collector which deals with
those cases.

There might be references of a specific interface. These do call the correct method defined on
the current type of the object stored in that reference when calling the functions defined on the interface.

You may use ``ref_type()`` to get the type of a specific reference.
References may also have no type, in this case use `&` to create a void reference.

.. code-block:: princess
    
    type A = struct { a: int }

    // This gets printed twice, once by when the
    // reference gets destroyed
    // and the other time when the bare struct is
    // converted to a reference.
    export def destruct(a: *A) {
        print("Destroying A: ", a.a, "\n")
    }

    // This gets automatically cleaned up
    let a = [ a = 10 ] !&A

.. _interfaces:

Interfaces
~~~~~~~~~~

Interfaces are basically contracts for which menthods need to be defined on a Type in order
to be able to use it in place of that interface.

There are essentially two ways to use interfaces. One is to use the bare interface. This is
only allowed as a function parameter and essentially creates a polymorphic function. This is
similar to concepts in C++.

.. code-block:: princess
    
    type A = struct { name: Str }

    type AsStr = interface {
        def as_str -> Str
    }
    
    def as_str(a: A) -> Str {
        return a.name
    }

    def as_str(a: int) -> Str {
        return to_string(a)
    }

    def print(a: AsStr) {
        print(a.as_str(), "\n")
    }

    let a = [ name = "Foo" ] !A
    let b = 20

    print(a)
    print(b)

    // This prints:
    // Foo
    // 20

In this case, no operation is performed at runtime, instead the polymorphic function print gets
compiled into two separate instances, one accepting ``ìnt`` and the other one accepting ``A``.

The second ways to use interfaces is to use a reference of that interface. This allows for dynamic
dispatch. The way this is implemented is essentially using the fact that references have a 
baked in type reference. When using a reference to an interface, it compiles a function that accepts
that interface which does have a switch based on the type id of the reference passed in. Using that it
it decides which concrete function to call.

.. code-block:: princess

    type A = struct { a: int }
    type B = struct { b: int }
    
    type I = interface {
        def foo -> int
    }

    // Implementation of I for A and B
    def foo(a: &A) -> int {
        return 10
    }

    def foo(b: &B) -> int {
        return 20
    }

    let a = [] !&A
    let b = [] !&B

    var c: &I = a
    assert c.foo() == 10
    assert ref_type(c) == type &A
    c = b
    assert c.foo() == 20
    assert ref_type(c) == type &B

Arrays
~~~~~~

In Princess there are two kinds of arrays. One of them is a static array, which is basically
a structure which contains a certain number of elements. These types are defined as follows:

.. code-block:: princess

    let a: [4; int] = [1, 2, 3, 4]

It is also possible to deduce the number of elements based on the array assigned to that
variable. For that use the ``?`` instead of the number of elements.

.. code-block:: princess

    let a: [?; int] = [1, 2, 3, 4, 5, 6]

These arrays are copied by value when passed to a function.

The second kind of arrays are dynamic arrays. These do not specify a size, but instead contain
a reference to a block of memory. This means the contents of these arrays are not copied when
passed to a function. These arrays necessarily have to be freed with ``delete(arr)``,
when they are created with ``allocate(T, size)`` or ``zero_allocate(T, size)``.

You can however pass a static array in place of a dynamic array. These do refer to the static
allocation and do *not* have to be freed.

.. code-block:: princess

    var a: [int]
    a = [1, 2, 3, 4]
    // Do not call delete on this!

    let b: [int] = zero_allocate(int, 10)
    b(0) = 10
    b(0) = 20

    print(b, "\n")
    // This needs to be freed!
    delete(b)

Arrays are accessed using the function call syntax. Assignments are also done that way:

.. code-block:: princess

    var a = [1, 2, 3 ,4]
    a(0) = 10
    print(a(0), a(1))

You can define these on custom types using the functions ``apply`` and ``update``:

.. code-block:: princess

    type Vector3 = struct { data: [3; int] }

    export def vec3(x: int, y: int, z: int) -> &Vector3 {
        return [ data = [x, y, z] ] !Vector3
    }

    export def apply(v: &Vector3, index: size_t) -> int {
        assert index < 3
        return v.data(index)
    }

    export def update(v: &Vector3, index: size_t, value: int) {
        assert index < 3
        v.data(index) = value
    }
    
    // Make our vector here
    let v = vec3(10, 20, 30)
    v(0) = 2
    print(v(0), v(1), v(2), "\n")

Function types
~~~~~~~~~~~~~~

You can take the address of any function with ``*``. The type of plain functions looks like this:
``def [A, B] -> [C, D]``. This function takes types A and B as arguments and returns C and D.
You can leave out the parenthesis if it is one type or drop them entirely if there's no type.

There is a second function type, the closure type, which is the same just without the def:
``[A, B] -> [C, D]``. This is the type that closures have. Dot not use the address operator to refer
to these, just using the function name is right.

Because you can also assign normal functions to closure types, 
you should use this type when accepting functions. That way it is possible to pass both a 
closure and a normal function.

.. code-block:: princess

    var a: def ->
    var b: -> int

    def main {
        let foo = 20
        def my_closure -> int {
            return foo
        }
        b = my_closure
    }
    a = *main

    a()
    assert b() == 20

Ranges
~~~~~~

Ranges are defined using the Syntax ``x..y`` or ``x..=y`` where the first one means
everything from x to y - 1 and the other one includes y.

Ranges are only valid inside of ``for`` loops and ``switch`` statements,
this is likely going to change in the future.

Tuples
~~~~~~

Tuple types are defined using the Syntax ``[A, B, C]``. You can create a new tuple similar
to an array with array sytnax: ``let x: [int, double] = [10, 20.0]``.
You can assign a static array to a tuple and the other way around, provided that they are compatible.
So say ``[3; int] <-> [int, int, int]``.

You may destructure a tuple similar to the return value of a function that returns multiple values.

.. code-block:: princess
    let x = [1, 2.5, 4]
    let a, b, c = x

In fact, if you define a function that returns a tuple, it is literally the same as returning multiple values.
In the future, only the tuple syntax may be accepted so keep that in mind.

Generic Types
~~~~~~~~~~~~~

A type may be made generic by giving the ``type`` declaration parameters:

.. code-block:: princess

    type Container(type T) = struct {
    	v: T
    }

    let c = [ v = 10 ] !Container(int)

You may accept a generic type as a parameter by either referring to the whole name
or by using ``type`` parameters to accept any polymorphic type. A function
like this is also made polymorphic:

.. code-block:: princess

    def retrieve_value(c: Container(type T)) -> T {
        return c.v
    }