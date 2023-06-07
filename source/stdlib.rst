Standard library
----------------
std
~~~

Types
^^^^^
.. code-block:: princess

    type File = *cstd::s__iobuf
.. code-block:: princess

    type UnixTime = uint64

Variables
^^^^^^^^^
.. code-block:: princess

    const PATH_MAX: int = 260
.. code-block:: princess

    const MAX_UINT8: uint8 = 255
.. code-block:: princess

    const MAX_UINT16: uint16 = 65535
.. code-block:: princess

    const MAX_UINT32: uint32 = 4294967295
.. code-block:: princess

    const MAX_UINT64: uint64 = 18446744073709551616
.. code-block:: princess

    const MIN_INT8: int8 = -128
.. code-block:: princess

    const MIN_INT16: int16 = -32768
.. code-block:: princess

    const MIN_INT32: int32 = -2147483648
.. code-block:: princess

    const MIN_INT64: int64 = ...
.. code-block:: princess

    const MAX_INT8: int8 = 127
.. code-block:: princess

    const MAX_INT16: int16 = 32767
.. code-block:: princess

    const MAX_INT32: int32 = 2147483647
.. code-block:: princess

    const MAX_INT64: int64 = 9223372036854775808
.. code-block:: princess

    const SEEK_SET: int = 0
.. code-block:: princess

    const SEEK_CUR: int = 1
.. code-block:: princess

    const SEEK_END: int = 2

Functions
^^^^^^^^^
.. code-block:: princess

    def stdin() -> File

.. code-block:: princess

    def stdout() -> File

.. code-block:: princess

    def stderr() -> File

.. code-block:: princess

    def combine_hashes(hashes: uint64) -> uint64

.. code-block:: princess

    def parse_int(str: String) -> int

.. code-block:: princess

    def to_array(gen: &runtime::Generator(type T)) -> &[T]

.. code-block:: princess

    def print(args: ) -> int

.. code-block:: princess

    def error(args: ) -> int

.. code-block:: princess

    def fprint(file: File, args: ) -> int

.. code-block:: princess

    def fprint(file: File, str: Str) -> int

.. code-block:: princess

    def abort(s: String)
.. code-block:: princess

    def delete(v: type *T)
.. code-block:: princess

    def delete(v: type [T])
.. code-block:: princess

    def new(t: type T) -> *T

.. code-block:: princess

    def concat(base: string, to_append: string)
.. code-block:: princess

    def allocate(size: size_t) -> 

.. code-block:: princess

    def allocate(type T) -> *T

.. code-block:: princess

    def allocate(type T, size: size_t) -> [T]

.. code-block:: princess

    def zero_allocate(size: size_t) -> 

.. code-block:: princess

    def zero_allocate(type T) -> *T

.. code-block:: princess

    def zero_allocate(type T, size: size_t) -> [T]

.. code-block:: princess

    def allocate_ref(type T, size: size_t) -> &[T]

.. code-block:: princess

    def reallocate(value: type *T, size: size_t) -> *T

.. code-block:: princess

    def free(value: type [T])
.. code-block:: princess

    def open(file_path: String, mode: String) -> File

.. code-block:: princess

    def reopen(file_path: String, mode: String, file: File) -> File

.. code-block:: princess

    def close(file: File) -> int

.. code-block:: princess

    def read(file: File, buffer: type [T]) -> size_t

.. code-block:: princess

    def read(file: File, buffer: type [T], size: size_t) -> size_t

.. code-block:: princess

    def read(file: File, ptr: type *T) -> size_t

.. code-block:: princess

    def read_str(file: File) -> Str

.. code-block:: princess

    def flush(file: File)
.. code-block:: princess

    def write(file: File, buffer: type [T]) -> size_t

.. code-block:: princess

    def write(file: File, buffer: type [T], size: size_t) -> size_t

.. code-block:: princess

    def write(file: File, ptr: type *T) -> size_t

.. code-block:: princess

    def write(file: File, c: char) -> size_t

.. code-block:: princess

    def write_str(file: File, str: String) -> size_t

.. code-block:: princess

    def read_line(file: File, str: string)
.. code-block:: princess

    def seek(file: File, offset: long, whence: int) -> int

.. code-block:: princess

    def tell(file: File) -> long

.. code-block:: princess

    def strlen(str: string) -> size_t

.. code-block:: princess

    def max(a: double, b: double) -> double

.. code-block:: princess

    def min(a: double, b: double) -> double

.. code-block:: princess

    def memcopy(src: , dest: , size: size_t) -> 

.. code-block:: princess

    def system(command: String) -> int

.. code-block:: princess

    def getenv(str: String) -> Str

.. code-block:: princess

    def mkdir(path: String)
.. code-block:: princess

    def dirname(file: String) -> Str

.. code-block:: princess

    def basename(file: String) -> Str

.. code-block:: princess

    def executable_file() -> Str

.. code-block:: princess

    def absolute_path(pathname: String) -> Str

.. code-block:: princess

    def tmpfolder(name: String) -> Str

.. code-block:: princess

    def read_all(fh: File) -> Str

.. code-block:: princess

    def read_all_pipe(pipe: File) -> Str

.. code-block:: princess

    def filetime_to_unix(ft: windows::s__FILETIME) -> UnixTime

.. code-block:: princess

    def modified_time(file: File) -> UnixTime

.. code-block:: princess

    def created_time(file: File) -> UnixTime

.. code-block:: princess

    def print_stacktrace()

arena
~~~~~

Types
^^^^^
.. code-block:: princess

    type Arena = struct {
        start: *Region
        end: *Region
        region_capacity: size_t
    }

Functions
^^^^^^^^^
.. code-block:: princess

    def make(capacity: size_t) -> &Arena

.. code-block:: princess

    def allocate(arena: &Arena, type T) -> *T

.. code-block:: princess

    def allocate(arena: &Arena, size: size_t) -> 

.. code-block:: princess

    def free(arena: &Arena)

getopt
~~~~~~

Types
^^^^^
.. code-block:: princess

    type ValueKind = enum {
        STRING
        ARRAY
        BOOLEAN
    }
.. code-block:: princess

    type Value = struct {
        next: &Value
        kind: ValueKind
    }
.. code-block:: princess

    type Option = struct {
        shortop: char
        longop: String
        nargs: int
        repeat: bool
        default: &Value
        is_set: bool
        value: &Value
        help: String
        metavar: String
    }
.. code-block:: princess

    type OptionParser = struct {
        options: [Option]
        description: String
    }

Functions
^^^^^^^^^
.. code-block:: princess

    def destruct(value: *Value)
.. code-block:: princess

    def option_repeat(shortop: char, longop: String) -> Option

.. code-block:: princess

    def option_repeat(shortop: char, longop: String, nargs: int) -> Option

.. code-block:: princess

    def option_repeat(shortop: char, longop: String, default: [String]) -> Option

.. code-block:: princess

    def option_repeat(shortop: char, longop: String, nargs: int, default: [[String]]) -> Option

.. code-block:: princess

    def option_repeat(longop: String) -> Option

.. code-block:: princess

    def option_repeat(longop: String, nargs: int) -> Option

.. code-block:: princess

    def option_repeat(longop: String, default: [String]) -> Option

.. code-block:: princess

    def option_repeat(longop: String, nargs: int, default: [[String]]) -> Option

.. code-block:: princess

    def option(shortop: char, longop: String, nargs: int, default: [String]) -> Option

.. code-block:: princess

    def option(shortop: char, longop: String, default: bool) -> Option

.. code-block:: princess

    def option(shortop: char, longop: String, default: String) -> Option

.. code-block:: princess

    def option(shortop: char, longop: String, nargs: int) -> Option

.. code-block:: princess

    def option(shortop: char, longop: String) -> Option

.. code-block:: princess

    def option(longop: String, nargs: int, default: [String]) -> Option

.. code-block:: princess

    def option(longop: String, default: bool) -> Option

.. code-block:: princess

    def option(longop: String, default: String) -> Option

.. code-block:: princess

    def option(longop: String, nargs: int) -> Option

.. code-block:: princess

    def option(longop: String) -> Option

.. code-block:: princess

    def set_help(option: Option, help: String) -> Option

.. code-block:: princess

    def set_metavar(option: Option, metavar: String) -> Option

.. code-block:: princess

    def make_parser(options: [Option], description: String) -> OptionParser

.. code-block:: princess

    def get_value(parser: *OptionParser, name: String) -> &Value

.. code-block:: princess

    def get_value_as_vec(parser: *OptionParser, name: String) -> &Vector(&Value)

.. code-block:: princess

    def parse(option_parser: *OptionParser, args: [string]) -> bool


io
~~

Variables
^^^^^^^^^
.. code-block:: princess

    var stderr_orig: *s__iobuf = ...
.. code-block:: princess

    var stdout_orig: *s__iobuf = ...

Functions
^^^^^^^^^
.. code-block:: princess

    def redirect_stderr_to_file(file: String)
.. code-block:: princess

    def redirect_stdout_to_file(file: String)
.. code-block:: princess

    def restore_stderr()
.. code-block:: princess

    def restore_stdout()
.. code-block:: princess

    def pipe() -> File, File

.. code-block:: princess

    def is_a_tty(file: File) -> bool


json
~~~~

Types
^^^^^
.. code-block:: princess

    type Type = enum {
        NIL
        OBJECT
        ARRAY
        STRING
        NUMBER
        TRUE
        FALSE
        KEY
    }
.. code-block:: princess

    type Status = enum {
        JSON_NULL
        JSON_EMPTY
        JSON_OK
        JSON_ERROR
    }
.. code-block:: princess

    type Data = struct #union {
        number: double
        str: Str
        b: bool
    }
.. code-block:: princess

    type JsonTreeNode = struct {
        tpe: Type
        parent: *JsonTreeNode
        data: Data
        children: &Vector(JsonTreeNode)
    }
.. code-block:: princess

    type Json = struct {
        status: Status
        root: JsonTreeNode
    }

Functions
^^^^^^^^^
.. code-block:: princess

    def destruct(this: *JsonTreeNode)
.. code-block:: princess

    def construct(copy: *JsonTreeNode, this: *JsonTreeNode)
.. code-block:: princess

    def __eq__(this: &Json, other: &Json) -> bool

.. code-block:: princess

    def __ne__(this: &Json, other: &Json) -> bool

.. code-block:: princess

    def make_array() -> &Json

.. code-block:: princess

    def make_object() -> &Json

.. code-block:: princess

    def make_null() -> &Json

.. code-block:: princess

    def push(tree: &Json, item: &Json)
.. code-block:: princess

    def push(tree: &Json, item: double)
.. code-block:: princess

    def push(tree: &Json, item: bool)
.. code-block:: princess

    def push(tree: &Json, item: String)
.. code-block:: princess

    def set_item(tree: &Json, key: String, item: &Json)
.. code-block:: princess

    def set_item(tree: &Json, key: String, item: double)
.. code-block:: princess

    def set_item(tree: &Json, key: String, item: bool)
.. code-block:: princess

    def set_item(tree: &Json, key: String, item: String)
.. code-block:: princess

    def length(tree: &Json) -> size_t

.. code-block:: princess

    def has_item(tree: &Json, str: String) -> bool

.. code-block:: princess

    def get_item(tree: &Json, str: String) -> &Json

.. code-block:: princess

    def has_item(tree: &Json, index: size_t) -> bool

.. code-block:: princess

    def get_item(tree: &Json, index: size_t) -> &Json

.. code-block:: princess

    def as_bool(tree: &Json) -> bool

.. code-block:: princess

    def as_int(tree: &Json) -> int

.. code-block:: princess

    def as_double(tree: &Json) -> double

.. code-block:: princess

    def as_string(tree: &Json) -> Str

.. code-block:: princess

    def is_bool(tree: &Json) -> bool

.. code-block:: princess

    def is_double(tree: &Json) -> bool

.. code-block:: princess

    def is_string(tree: &Json) -> bool

.. code-block:: princess

    def is_null(tree: &Json) -> bool

.. code-block:: princess

    def is_object(tree: &Json) -> bool

.. code-block:: princess

    def is_array(tree: &Json) -> bool

.. code-block:: princess

    def serialize(obj: type *T) -> &Json

.. code-block:: princess

    def deserialize(json: &Json, type T) -> Optional(T)

.. code-block:: princess

    def to_string(tree: &Json) -> String

.. code-block:: princess

    def destruct(self: *Json)
.. code-block:: princess

    def parse(str: String) -> &Json


map
~~~

Types
^^^^^
.. code-block:: princess

    type Entry(type K, type V) = struct {
        key: K
        value: V
        next: &Entry(K, V)
        l_prev: weak_ref(Entry(K, V))
        l_next: weak_ref(Entry(K, V))
    }
.. code-block:: princess

    type Map(type K, type V) = struct {
        size: size_t
        entries: [&Entry(K, V)]
        tail: weak_ref(Entry(K, V))
        head: weak_ref(Entry(K, V))
    }
.. code-block:: princess

    type SMap(type V) = Map(Str, V)

Functions
^^^^^^^^^
.. code-block:: princess

    def construct(copy: *Map(type K, type V), this: *Map(K, V))
.. code-block:: princess

    def destruct(map: *Map(type K, type V))
.. code-block:: princess

    def hash(i: size_t) -> size_t

.. code-block:: princess

    def make(type K, type V, size: size_t) -> &Map(K, V)

.. code-block:: princess

    def make(type V, size: size_t) -> &SMap(V)

.. code-block:: princess

    def make(type K, type V) -> &Map(K, V)

.. code-block:: princess

    def make(type V) -> &SMap(V)

.. code-block:: princess

    def get(map: &Map(type K, type V), key: K) -> Optional(V)

.. code-block:: princess

    def get_or_default(map: &Map(type K, type V), key: K, default: V) -> V

.. code-block:: princess

    def get_item(map: &Map(type K, type V), key: K) -> V

.. code-block:: princess

    def contains(map: &Map(type K, type V), key: K) -> bool

.. code-block:: princess

    def set_item(map: &Map(type K, type V), key: K, value: V)
.. code-block:: princess

    def remove(map: &Map(type K, type V), key: K)
.. code-block:: princess

    def size(map: &Map(type K, type V)) -> size_t

.. code-block:: princess

    def keys(map: &Map(type K, type V)) -> &[K]

.. code-block:: princess

    def reverse_keys(map: &Map(type K, type V)) -> &[K]

.. code-block:: princess

    def clear(map: &Map(type K, type V))

optional
~~~~~~~~

Types
^^^^^
.. code-block:: princess

    type Optional(type V) = struct {
        exists: bool
        value: V
    }

Functions
^^^^^^^^^
.. code-block:: princess

    def none(type V) -> Optional(V)

.. code-block:: princess

    def some(value: type V) -> Optional(V)

.. code-block:: princess

    def get(this: Optional(type T)) -> T

.. code-block:: princess

    def get_or_default(this: Optional(type T), default: T) -> T


process
~~~~~~~

Types
^^^^^
.. code-block:: princess

    type Process = struct {
        exit_code: int
        running: bool
        si: windows::s__STARTUPINFOA
        pi: windows::s__PROCESS_INFORMATION
    }

Functions
^^^^^^^^^
.. code-block:: princess

    def spawn(exe: String, args: &[String], stdin: File, stdout: File, stderr: File) -> Process

.. code-block:: princess

    def wait(process: *Process, timeout: ulong)
.. code-block:: princess

    def dispose(process: *Process)

set
~~~

Types
^^^^^
.. code-block:: princess

    type Set(type T) = map::Map(T, )
.. code-block:: princess

    type SSet = Set(Str)

Functions
^^^^^^^^^
.. code-block:: princess

    def make(type T) -> &Set(T)

.. code-block:: princess

    def make() -> &SSet

.. code-block:: princess

    def add(set: &Set(type T), value: T)
.. code-block:: princess

    def add_all(set: &Set(type T), other: &Set(T))

shared
~~~~~~

Types
^^^^^
.. code-block:: princess

    type SymbolKind = enum {
        OBJECT
        FUNCTION
    }
.. code-block:: princess

    type Symbol = struct {
        kind: SymbolKind
        name: Str
        value: 
    }
.. code-block:: princess

    type Library = struct {
        path: Str
        handle: 
        symbols: &[Symbol]
    }

Functions
^^^^^^^^^
.. code-block:: princess

    def find_symbol(library: *Library, name: String) -> Optional(Symbol)

.. code-block:: princess

    def load(path: String, init: bool) -> Library

.. code-block:: princess

    def close(library: *Library, finalize: bool)

strings
~~~~~~~

Types
^^^^^
.. code-block:: princess

    type Str = struct #union {
        long_str: LongString
        short_str: ShortString
    }
.. code-block:: princess

    type StringBuffer = struct {
        prev: &StringBuffer
        data: Str
        offset: size_t
    }
.. code-block:: princess

    type StringSlice = struct {
        parent: String
        data: *char
        offset: size_t
        count: size_t
    }
.. code-block:: princess

    type IString = interface {
        def length() -> size_t
        def get_item(i: size_t) -> char
    }
.. code-block:: princess

    type String = &IString
.. code-block:: princess

    type ToString = interface {
        def to_string() -> String
    }

Functions
^^^^^^^^^
.. code-block:: princess

    def length(s: [char]) -> size_t

.. code-block:: princess

    def length(s: &[char]) -> size_t

.. code-block:: princess

    def get_item(s: &[char], i: size_t) -> char

.. code-block:: princess

    def hash(str: Str) -> size_t

.. code-block:: princess

    def to_bool(s: Str) -> bool

.. code-block:: princess

    def is_short_str(s: *Str) -> bool

.. code-block:: princess

    def get_internal_buffer(s: *Str) -> *char

.. code-block:: princess

    def to_str(s: &string) -> Str

.. code-block:: princess

    def to_str(s: string) -> Str

.. code-block:: princess

    def to_str(len: size_t, value: *char) -> Str

.. code-block:: princess

    def to_str(s: String) -> Str

.. code-block:: princess

    def length(s: Str) -> size_t

.. code-block:: princess

    def length(s: &Str) -> size_t

.. code-block:: princess

    def get_item(s: Str, i: size_t) -> char

.. code-block:: princess

    def get_item(s: &Str, i: size_t) -> char

.. code-block:: princess

    def construct(copy: *Str, this: *Str)
.. code-block:: princess

    def destruct(this: *Str)
.. code-block:: princess

    def length(s: StringBuffer) -> size_t

.. code-block:: princess

    def to_str(s: StringBuffer) -> Str

.. code-block:: princess

    def to_buffer(s: String) -> StringBuffer

.. code-block:: princess

    def to_buffer(s: Str) -> StringBuffer

.. code-block:: princess

    def to_buffer(s: StringSlice) -> StringBuffer

.. code-block:: princess

    def to_buffer(s: &string) -> StringBuffer

.. code-block:: princess

    def to_buffer(s: string) -> StringBuffer

.. code-block:: princess

    def __add__(s: StringBuffer, o: &ToString) -> StringBuffer

.. code-block:: princess

    def __add__(s: StringBuffer, o: Str) -> StringBuffer

.. code-block:: princess

    def __add__(s: StringBuffer, o: StringSlice) -> StringBuffer

.. code-block:: princess

    def __add__(s: StringBuffer, o: String) -> StringBuffer

.. code-block:: princess

    def __add__(s: StringBuffer, o: &string) -> StringBuffer

.. code-block:: princess

    def __add__(s: StringBuffer, o: string) -> StringBuffer

.. code-block:: princess

    def __add__(s: &ToString, o: StringBuffer) -> StringBuffer

.. code-block:: princess

    def __add__(s: StringBuffer, o: StringBuffer) -> StringBuffer

.. code-block:: princess

    def __iadd__(s: StringBuffer, o: &ToString) -> StringBuffer

.. code-block:: princess

    def __iadd__(s: StringBuffer, o: Str) -> StringBuffer

.. code-block:: princess

    def __iadd__(s: StringBuffer, o: StringSlice) -> StringBuffer

.. code-block:: princess

    def __iadd__(s: StringBuffer, o: String) -> StringBuffer

.. code-block:: princess

    def __iadd__(s: StringBuffer, o: &string) -> StringBuffer

.. code-block:: princess

    def __iadd__(s: StringBuffer, o: string) -> StringBuffer

.. code-block:: princess

    def __iadd__(s: StringBuffer, o: StringBuffer) -> StringBuffer

.. code-block:: princess

    def to_string(s: StringBuffer) -> String

.. code-block:: princess

    def to_string(s: string) -> String

.. code-block:: princess

    def to_string(s: &string) -> String

.. code-block:: princess

    def to_bool(s: StringSlice) -> bool

.. code-block:: princess

    def length(s: StringSlice) -> size_t

.. code-block:: princess

    def length(s: &StringSlice) -> size_t

.. code-block:: princess

    def get_item(s: StringSlice, i: size_t) -> char

.. code-block:: princess

    def get_item(s: &StringSlice, i: size_t) -> char

.. code-block:: princess

    def to_str(s: StringSlice) -> Str

.. code-block:: princess

    def __eq__(s1: IString, s2: IString) -> bool

.. code-block:: princess

    def __eq__(s1: IString, s2: [char]) -> bool

.. code-block:: princess

    def __eq__(s1: [char], s2: IString) -> bool

.. code-block:: princess

    def __eq__(s1: [char], s2: [char]) -> bool

.. code-block:: princess

    def __eq__(s1: Str, s2: Str) -> bool

.. code-block:: princess

    def __ne__(s1: IString, s2: IString) -> bool

.. code-block:: princess

    def __ne__(s1: IString, s2: [char]) -> bool

.. code-block:: princess

    def __ne__(s1: [char], s2: IString) -> bool

.. code-block:: princess

    def __ne__(s1: [char], s2: [char]) -> bool

.. code-block:: princess

    def __ne__(s1: Str, s2: Str) -> bool

.. code-block:: princess

    def to_slice(s: [char]) -> StringSlice

.. code-block:: princess

    def to_slice(s: String) -> StringSlice

.. code-block:: princess

    def to_slice(s: Str) -> StringSlice

.. code-block:: princess

    def slice(s: [char], frm: size_t, to: size_t) -> StringSlice

.. code-block:: princess

    def slice(s: Str, frm: size_t, to: size_t) -> StringSlice

.. code-block:: princess

    def slice(s: String, frm: size_t, to: size_t) -> StringSlice

.. code-block:: princess

    def to_array(s: String) -> &[char]

.. code-block:: princess

    def chars(s: String) -> char

.. code-block:: princess

    def to_string(sign: int, n: uint64) -> String

.. code-block:: princess

    def to_string(a: &int64) -> String

.. code-block:: princess

    def to_string(a: &int32) -> String

.. code-block:: princess

    def to_string(a: &int16) -> String

.. code-block:: princess

    def to_string(a: &int8) -> String

.. code-block:: princess

    def to_string(a: &uint64) -> String

.. code-block:: princess

    def to_string(a: &uint32) -> String

.. code-block:: princess

    def to_string(a: &uint16) -> String

.. code-block:: princess

    def to_string(a: &uint8) -> String

.. code-block:: princess

    def to_string(a: &bool) -> String

.. code-block:: princess

    def to_string(a: &char) -> String

.. code-block:: princess

    def to_string(value: &float) -> String

.. code-block:: princess

    def to_string(value: &double) -> String

.. code-block:: princess

    def make_string(ptr: *char) -> Str

.. code-block:: princess

    def remove(str: String, i: size_t) -> Str

.. code-block:: princess

    def remove(str: String, start: size_t, count: size_t) -> Str

.. code-block:: princess

    def insert(str: String, i: size_t, s: String) -> Str

.. code-block:: princess

    def insert(str: String, i: size_t, c: char) -> Str

.. code-block:: princess

    def substring(str: String, start: size_t, end: size_t) -> Str

.. code-block:: princess

    def substring(str: String, start: size_t) -> Str

.. code-block:: princess

    def index_of(str: String, substring: String, start: size_t) -> int64

.. code-block:: princess

    def last_index_of(str: String, substring: String) -> int64

.. code-block:: princess

    def ends_with(str: String, suffix: String) -> bool

.. code-block:: princess

    def starts_with(str: String, pre: String) -> bool

.. code-block:: princess

    def strip_margin(s: String) -> Str

.. code-block:: princess

    def match(pattern: String, candidate: String) -> bool

.. code-block:: princess

    def utf8_encode(code_point: uint64) -> Str

.. code-block:: princess

    def int_to_hex_str(n: uint64, prefix: bool) -> Str

.. code-block:: princess

    def iterate(str: String) -> char


vector
~~~~~~

Types
^^^^^
.. code-block:: princess

    type Vector(type T) = struct {
        length: size_t
        data: [T]
    }

Functions
^^^^^^^^^
.. code-block:: princess

    def destruct(this: *Vector(type T))
.. code-block:: princess

    def construct(copy: *Vector(type T), this: *Vector(T))
.. code-block:: princess

    def make(type T) -> &Vector(T)

.. code-block:: princess

    def resize(vec: &Vector(type T), size: size_t)
.. code-block:: princess

    def length(vec: &Vector(type T)) -> size_t

.. code-block:: princess

    def get(vec: &Vector(type T), index: size_t) -> *T

.. code-block:: princess

    def get_item(vec: &Vector(type T), index: size_t) -> T

.. code-block:: princess

    def set_item(vec: &Vector(type T), index: size_t, val: T)
.. code-block:: princess

    def push(vec: &Vector(type T), elem: T)
.. code-block:: princess

    def prepend(vec: &Vector(type T), elem: T)
.. code-block:: princess

    def peek(vec: &Vector(type T)) -> T

.. code-block:: princess

    def pop(vec: &Vector(type T)) -> T

.. code-block:: princess

    def head(vec: &Vector(type T)) -> T

.. code-block:: princess

    def head_vec(vec: &Vector(type T)) -> &Vector(T)

.. code-block:: princess

    def tail(vec: &Vector(type T)) -> &Vector(T)

.. code-block:: princess

    def copy(vec: &Vector(type T)) -> &Vector(T)

.. code-block:: princess

    def insert(vec: &Vector(type T), index: size_t, elem: T)
.. code-block:: princess

    def insert(vec: &Vector(type T), index: size_t, vec2: &Vector(T))
.. code-block:: princess

    def remove(vec: &Vector(type T), index: size_t)
.. code-block:: princess

    def iterate(vec: &Vector(type T)) -> T

.. code-block:: princess

    def iterate_ref(vec: &Vector(type T)) -> *T

.. code-block:: princess

    def to_array(vec: &Vector(type T)) -> &[T]


runtime
~~~~~~~

Types
^^^^^
.. code-block:: princess

    type TestEnvironment = struct {
        out: () -> (&string)
        err: () -> (&string)
        assertion_handler: (bool, *char) -> ()
    }
.. code-block:: princess

    type Generator(type T) = struct {
        implementation: (&Generator(T)) -> (optional::Optional(T))
        context: 
        free_context: () -> ()
        is_at_end: bool
    }
.. code-block:: princess

    type TypeKind = enum {
        BOOL
        WORD
        FLOAT
        STRUCT
        UNION
        ARRAY
        STATIC_ARRAY
        POINTER
        REFERENCE
        FUNCTION
        ENUM
        CHAR
        STRUCTURAL
        OPAQUE
        WEAK_REF
        TYPE
    }
.. code-block:: princess

    type Function = struct {
        name: string
        exported: bool
        module: string
        parameter_t: [*Type]
        return_t: [*Type]
    }
.. code-block:: princess

    type Type = struct {
        kind: TypeKind
        name: string
        unsig: bool
        length: size_t
        tpe: *Type
        size: size_t
        align: size_t
        fields: [Field]
        parameters: [*Type]
        returns: [*Type]
        enum_values: [EnumValue]
        module: string
        structural_members: [Function]
        type_members: [Function]
        id: int64
    }
.. code-block:: princess

    type EnumValue = struct {
        name: string
        value: int64
    }
.. code-block:: princess

    type Field = struct {
        name: string
        offset: size_t
        tpe: *Type
    }
.. code-block:: princess

    type Ref = struct {
        ref_count: *int64
        value: 
        tpe: *Type
    }

Functions
^^^^^^^^^
.. code-block:: princess

    def destruct(this: *Generator(type T))
.. code-block:: princess

    def next(generator: &Generator(type T)) -> optional::Optional(T)

.. code-block:: princess

    def implements(A: *Type, B: *Type) -> bool

.. code-block:: princess

    def ref_type(a: Ref) -> *Type

.. code-block:: princess

    def equals(a: *Type, b: *Type) -> bool

.. code-block:: princess

    def reference(tpe: *Type) -> *Type


