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

### open

### fileinput

### tempfile


## Zip Files

## Calling External Programs

## Email

## Network & HTTP

## Dates

## Regex
