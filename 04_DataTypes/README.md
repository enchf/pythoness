# Data types

## Built-in

* Booleans (True, False)
* Numbers (int, float, complex)
* Strings ("...", '...')
* Lists (Anything that is listed between \[\] and separated with a comma for example: `[1, 3.0, 5, True, "Sier"]`). _more on lists later_ 
* Tuple (A tuple is like a list, but with the difference that a tuple is inmutable and is denoted with  `(...)` instead of `[]`). _more on tuples later_
* Dictionary (A dictionary is a data type that works as map or an assignment between "keys" and "values", they are denoted with `{}`). _more on dictionaries later_

## Notes

It's important to mention that from now on we'll be using two _built-in_ functions that will help us to determine the _type_ of a value and also others to see it in the screen. This two functions are:

* `type` -> return the name of the _type_ of the data value 
* `print` -> puts what we pass to it on the screen.

The details of how this work will be more easy to understand in future chapters, for now you only need to understand that:

```
type(5) # Will return <type 'int'>

print(5) # Will put literally on the screen: 5
```

### Numbers

Numbers represent mathematical values, this mean numbers in general, the most common are the **int** and the **float** which represents the common values that appears in operations. 

Float numbers also are represented with exponential notation. For example 32.9+e21 

Complex numbers involve a _real_ and an _imaginary_ part, this numbers have different operations and are available in python as a native data type. This kind of numbers are written like `R + Ij` where _R_ represents the _real_ part with a `+` and the _imaginary_ part in this case, noted by a _I_. The _imaginary_ part is a real number which must also include a _j_ to denote that is the imaginary part, this _j_ could also be upper case.  

#### Prefix system

There's a popular usage of Python in the last years: Computer/Data Science. This is because python has a very well managed use of numbers and also because python allows you to use different notations and operations between different _bases_. This means that as mentioned before, you can work with binary, octal, exponential or hexadecimal notation without problem.

This notation is easy to remember because it uses letters instead of numbers:

1. Binary -> Start with a `0` and then add a 'b' or 'B' and finally put your binary number. Examples:
	1. `0b101 -> 5` `0B1001 -> 9`  `0b101010 -> 42`
2. Octal -> Start with a `0`, add a 'O' or 'o' and then put your number in base 8. Examples:
	1. `0o10 -> 5` `0O11 -> 9` `0o40 -> 42`
2. Hexadecimal -> Start with a `0`, add a 'x' or 'X' and then your number in base 16. Examples:
	1. `0x5 -> 5` `0X9` `0x2A`
	
#### Type Conversion

Usually when you perform operations between numbers you get with numbers of different types, for example you end adding **int**s to **float**s or even adding complex expecting **int**s as result.

To work with this the rule is easy, no matter the order of the operation, the result always involve the more complex type, for example, a sum of **int** always give you an **int** but operating an **int** with a **float** always give you a **float** so the order is easy:

> int -> float -> complex

On the other hand, if you want to get a certain type even when a different result will show up, you can use some functions (yep, more on this later) to transform values from one type to another.

So if you have a value returned as **float** after operating **float** with **float** or with **int** you can transform or truncate this value to a **int** just putting: `int(your_value)`

```
value_as_int = int(5.0/2)
```

This will truncate the value to the closest value to 0. This means that in the case of: `int(-5/2.0)` this will truncate to -2 instead of -3 because python will try to go the closest to 0.

#### Precision problem

As someone already notice or told you, python has a "_problem_" with **float**s, this _problem_ is visible if you do:

```
(1.1 + 2.2) == 3.3 # Will return False
```

It turns out that **floating-point** numbers are implemented in computer hardware as binary fractions, as computer only understands binary (0 and 1). Due to this reason, most of the decimal fractions we know, cannot be accurately stored in our computer.

Let's take an example. We cannot represent the _fraction_ 1/3 as a decimal number. This will give 0.33333333... which is infinitely long, and we can only approximate it.

Turns out decimal fraction 0.1 will result into an infinitely long binary fraction of 0.000110011001100110011... and our computer only stores a finite number of it.

This will only approximate 0.1 but never be equal. Hence, it is the limitation of our computer hardware and not an error in Python.

This issue can be solved using certain modules that will be covered in future topics (`decimal` and `fraction` modules)

## Strings



## Lists








