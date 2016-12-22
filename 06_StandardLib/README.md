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

## Calling External Programs

## Email

## Network & HTTP

## Dates

## Zip Files
