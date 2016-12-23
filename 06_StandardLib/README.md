# Python Standard Library

The use of Standard Library is fundamental when dealing with files, 
email, network connections and so on. We will cover some of the most
important topics to let you start using these libraries.
 
## Sys

To let you use the standard sys library, you should import the module as below:

```python
    import sys
    
    or
    
    from sys import ...
```

Important features to be used from sys library:

| Feature | Usage | Notes |
|---------|-------|---------|
| sys.argv | Get the command line arguments passed to a Python script | They start after the _python_ command. For example argv[0] could be the script filename |
| sys.exit([arg]) | Exits Python with a exit status code | 0 or None are _successful terminations_, others (strings, 1) are exit code errors |
| sys.getsizeof(object) | Gets the size of an object in bytes | A second argument can be specified to set a default value (if the object does not provide this information) |
| sys.path | A list of strings that specifies the search path for modules, initialized from the environment variable PYTHONPATH | The first item of this list, path[0], is the directory containing the script that was used to invoke the Python interpreter |
| sys.stdin, stdout, stderr | File objects used by the interpreter for standard input, output and errors | stdin is generally invoked by input(), and stdout by print() |

Get more information about available functions and objects from the [official documentation](https://docs.python.org/3/library/sys.html).

## StdIO

Reading from the standard input and output streams is encapsulated in few functions as from Python 3:

### Reading from standard input

There are several ways to read from standard input. Some of these functions are improvements for common tasks.

#### input

Python has a built-in function called _input_ to read strings from the console.

```python
i = input()
# Hello World!
print(i) 
# Hello World!
x = input('--->')
# ---> Custom prompt
print(x)
# Custom prompt
```

#### Converting types from standard input

Python has the following functions to convert strings to a specific data type:

* int(): Converts a string to integer
* float(): Converts a string to a floating-point number
* bool(): Convert _truthy/falsy_ objects to boolean (None, False, 0, 0.0, empty sequence ('', (), []), empty map {}).

```python
x = int(input())
```

### Print command - standard output

Apart from the basic usage of print (simply passing the argument to be printed), it has four optional useful arguments:

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

| Argument | Description | Usage |
|----------|-------------|-------|
| *objects | A list of objects comma-separated as arguments | print(1,2,3) |
| sep | Object separator when printing | print(1,2,3,sep='-') |
| end | Will print all objects separated by sep _followed by_ end | print(1,2,3,sep='-',end='***') |
| file | The file argument must be an object with a write(string) method; if it is not present or None, sys.stdout will be used. | |
| flush | Try to force flushing the buffer content into the destination stream | print(1,2,3,end='**',flush=True) | 

Note: print cannot be used for binaries.

## IO

We will cover basic operations for working with files with two libraries: _open_ and _fileinput_.

### open

Open is a built-in function that can easily create file streams (text or binary). It is configured by a parameter called
_mode_, which indicates the type of the file (read or binary) and how the file will be used (read-only, write, append).

Sample usage:

```python
f = open("filename", "r", encoding="utf-8")

or 

with open("file","r") as f:
    pass
```

The first argument is the file name and the second argument is the opening mode. There are more optional parameters but
for simplicity we will cover only these two and _encoding_, which is a string indicating (as its name says) the file
encoding type.

Options for mode:

| Character | Type | Usage |
|-----------|------|-------|
| r | Opening mode | Open for read only (default) |
| w | Opening mode | Open for writing, truncating the file first |
| x | Opening mode | Exclusive creation, failing if the file already exists |
| a | Opening mode | Open for writing, appending to the end if the file exists |
| b | File type | Binary file |
| t | File type | Text file |

We have different API's for each file type. For text files, the API refers to the class 
[TextIOBase](https://docs.python.org/3/library/io.html#io.TextIOBase), and for binaries the API refers to the class
[BuffededIOBase](https://docs.python.org/3/library/io.html#io.BufferedIOBase).

For an extensive detail on the open function, take a look at the [official documentation](https://docs.python.org/3/library/functions.html#open).

### fileinput

Fileinput is an special module that allows to iterate over an input or even more standard input. The first argument 
can be a list of files (see below) or if empty standard input.

```python
import fileinput
for line in fileinput.input():
    print(line)
    
or

with fileinput.input(files=('file1.txt', 'file2.txt')) as f:
    for line in f:
        print(line)
    print("Lines of " + fileinput.filename())
```

When iterating, fileinput provides helper functions as global state of the file being iterated. We can see above that 
after getting the reference to a file, we invoked fileinput.filename() as a global state to get the file name and print
it to the standard output. This is a list of functions that can be used in that way:

| Function | Description |
|----------|-------------|
| filename() | Name of the current file being read |
| lineno() | Cumulative line numbers being read |
| filelineno() | Cumulative line number of the file being read |
| isfirstline() | True if its the first line being read of the file, false otherwise |
| nextfile() | Close the current file and go to the next if any |
| close() | Close the sequence |

More functions available at [fileinput documentation](https://docs.python.org/3/library/fileinput.html#fileinput.input).

## Zip Files

Python provides a class to work with ZIP files called _ZipFile_. This class encapsulates basic and common operations to
be done with zip files. ZipFile class can be instantiated in the following way:
 
```python
from zipfile import ZipFile
with ZipFile('all.zip', 'w') as myzip:
    myzip.write('anotherfile.txt')
```

Syntax is similar to what we saw in _open_ function: The first argument is the name of the file and the second argument
is the mode. It accepts r (read only), w (write), x (exclusive open for creation and writing) and a (appending) as 
opening modes. Here are the most used functions and below an usage sample.

| Function | Description |
| zipfile.is_zipfile(filename) | Checks whether a file is a zip file. This function is not part of Zipfile class and can be invoked directly |
| ZipFile.close() | Closes the archive. If changes are done and close is not invoked, those changes will be lost |
| ZipFile.namelist() | Returns a list of archive members by name |
| ZipFile.open(name, mode='r', pwd=None) | Opens a file from the zip file. Accepts the same arguments in mode and also an (optional) password |
| ZipFile.extract(name, path=None, pwd=None) | Extracts the specified file at path (if not specified, at the same directory) |
| ZipFile.extractAll(path=None, members=None, pwd=None) | Extracts all the files or a subset specified by _members_ |
| ZipFile.read(name, pwd=None) | Read the bytes of the file _name_ |
| ZipFile.write(file, arcname=None, compress_type=None) | Writes a file to the archive, with (optional) name _arcname_ and a specified compression type |
| ZipFile.setpassword(pwd) | Set a password as default for all operations over the file |

For the full documentation, go to the [zipfile API docs](https://docs.python.org/3/library/zipfile.html).

## Calling External Programs

```python
```

## Email

```python
```

## Network & HTTP

```python
```

## Dates

```python
```

## Regex

```python
```
