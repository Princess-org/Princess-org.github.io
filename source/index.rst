Princess: Coding like royalty
==================================================

.. warning:: 
   Do note that this language is in the early alpha stages.
   Not everything mentioned in this documentation is already implemented.
   The syntax might change at any point, proceed with caution!

.. code:: princess

   let i = 7

   def mod(a: int, base: int) -> int {
      return ((a % base) + base) % base
   }

   // Uniform call syntax
   assert i.mod(3) == 1

   import strings
   type Person = struct {
      name: Str
      age: uint
   }

   // Define to_string to be able to print Person
   export def to_string(person: &Person) -> String {
      return person.name + ": " + person.age
   }

   let person = { name = "Bob", age = 42 } !Person
   print(person, "\n")

   // Compile time parameter type T
   def my_size_of(type T) -> size_t {
      // Full reflection support
      return T.size
   }

   assert my_size_of(Person) == 32

.. toctree::
   :maxdepth: 2

   VSCode Extension <https://github.com/Princess-org/vscode-Princess>

.. 
   * :ref:`genindex`
	* :ref:`search`
