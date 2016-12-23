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
|----------|-------------|
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

The _subprocess_ module allows you to spawn new processes, connect to their input/output/error pipes, 
and obtain their return codes. It encapsulates all operation into the run command (see description and example below),
for previous versions of _subprocess_ check the [older high level API](https://docs.python.org/3/library/subprocess.html#call-function-trio).

Example of usage:

```python
import subprocess

subprocess.run(["ls", "-l"]) # Only runs, does not capture output.
subprocess.run(["ls", "-l"], stdout=subprocess.PIPE) # Captures the output setting a PIPE to stdout.
```

More arguments and be set and configured for this function. For more details, 
check [subprocess official documentation](https://docs.python.org/3/library/subprocess.html)

## Email

The easiest way to send e-mail in Python is through the _smtplib_ module. It requires a SMTP server running 
to be invoked from Python library to allow us the send operation.

A smtp object can be get from the SMTP function and the hostname:

```python
import smtplib
smtpobj = smtplib.SMTP("localhost")
```

After this, we can invoke _sendemail_ function to prepare a message:

```python
import smtplib
try:
    smtpobj = smtplib.SMTP('localhost')
    smtpobj.sendmail("sender@email", ["receivers@email", "receivers_@email"], "message")         
    print("Successfully sent email")
except smtplib.SMTPException:
    print("Error: unable to send email")
```

For more extensive details, look at the [official documentation](https://docs.python.org/3/library/smtplib.html).

## Network & HTTP

Python enables the communication with HTTP protocol through the class _HTTPConnection_, located at http.client module.
Also enables other kind of connections, like HTTPS. To keep it simple and pragmatic, we will show an example for normal
HTTP connection.

First of all, a connection is obtained using the host and the port:

```python
import http.client

connection = http.client.HTTPConnection("localhost", 8080)
```

This connection object can be used to perform a wide set of operations, being _request_ and _getresponse_ the fundamental
ones. The former allows you to perform an HTTP request, while the latter allows you to parse and get data from the server
response. Below you will find a table of useful methods:

| Class.Method | Description |
|--------|-------------|
| HttpConnection.request(method, url, body=None, headers={}) | Performs the request using the _method_ against the relative _url_. A request _body_ and _headers_ can be set |
| HttpConnection.getresponse() | Called after a request is sent, returns an [HTTPResponse](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse) object |
| HttpConnection.close() | Closes the connection with the server |
| HttpRequest.read() | Reads and returns the response body. Also the method readinto(b) allows to put the response into the buffer _b_ |
| HttpRequest.getheader(name) | Returns the header with the specified _name_ |
| HttpRequest.status | Response status |
| HttpRequest.reason | Response reason |

Usage sample:

```python
import http.client
conn = http.client.HTTPSConnection("server.url")
conn.request("GET", "/index.html")
r1 = conn.getresponse()
print(r1.status, r1.reason)
```

## Dates

```python
```

## Regex

Regular expressions are a very wide topic in a programming language. They allow you to create string patterns to be
matched in strings, instead of parsing directly the string to identify certain stuff. Things like identifying numbers,
emails, formats, to determine if a string ends or starts with certain pattern of characters, can be done quickly (but
sometimes a bit tricky) using regular expressions.

A very simple usage is the following, which checks if a string is composed only by numbers. If there is no match, 
_match_ method returns _None_:

```python
import re
x = re.compile("[0-9]+")
print(x.match("12345"))
```

A list of important and interesting methods and meta-characters (characters used to build the regular expression, 
*henceforth regex*) are compiled below:

| Expression | Belongs to | Description |
|------------|------------|-------------|
| re.compile(pattern) | re class | Compiles a pattern and returns a regex object. Another way to get a regex is with this syntax: r'-pattern-here-' | 
| re.search(pattern, string) | re class | Search for a pattern in a string |
| match(string) | regex object | Tries to match a regex into a string. Returns a _match object_ |
| m.group(*indexes) | match object | Return a single string or a tuple of length of _indexes_ with all the matched groups in the string |
| m.start(group), m.end(group) | match object | Return the start and end positions of the substring matched by _group_ | 
| [ ] | meta-character | Used for ranges or groups of characters: [abc] match any of a, b or c, while [a-z] matches any between a and z |  
| ( ) | meta-character | Group expressions to have subgroups of the matched string |
| \w \W | meta-character | Lower case matches alphanumeric strings, upper matches non-alphanumerics |
| \d \D | meta-character | Lower matches digit strings, upper matches non-digit |
| \s \S | meta-character | Lower matches whitespace strings, upper non-whitespace |
| ^ $ | meta-character | ^ indicates the beginning of the string, $ indicates the end |
| * + | meta-character | At the end of a pattern, * indicates 0 or more occurrences, while + indicates 1 or more occurrences |

The [full documentation](https://docs.python.org/3/howto/regex.html) for regular expressions in Python is available in
a guide form. To leverage this small training, and if you are interested in deeper concepts, take a look into the official
guide.
