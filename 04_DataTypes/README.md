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
3. Hexadecimal -> Start with a `0`, add a 'x' or 'X' and then your number in base 16. Examples:
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

A `string` is a sequence of characters available on the computer, computers do not deal with characters, they deal with numbers (binary). Even though you may see characters on your screen, internally it is stored and manipulated as a combination of 0's and 1's.

This conversion of character to a number is called _encoding_, and the reverse process is _decoding_. ASCII and Unicode are some of the popular encoding used.

In Python, `string` is a sequence of Unicode character. Unicode was introduced to include every character in all languages and bring uniformity in encoding.

#### Notation

A `string` can be created with one of the next three ways:

1. m_string = 'Hello'
2. m_string = "Hello"
3. m_string = '''Hello'''

Additional to this, you can create multiline `strings` and something called _docstrings_.

#### Multiline and Docstrings

A multiline string is a `string` that holds more than 1 line of text, this is denoted by the separation between lines with and _enter_.

```
m_string = """This
is
a multiline string

You can notice the space between lines.

"""
```

A _docstring_ is a multiline `string` that is below a _definition_ or a _class_, it's function is to give documentation to the developer about what's the usage of that _definition_ or _class_. This will be more clear in future topics.

## Lists

A list is a sequence of _elements_ inside a square brackets `[]` and separated by commas. 

The _elements_ that you can put in a `list` are any kind of data to hold, for now you know `booleans`, `numbers`, `strings` and `lists`. So the next are valid lists:

```
list3 = [True, False, None]
list1 = [1, 2, 4, -1]
list2 = ["sier", "ernesto", "christian"]

mixed = [True, "Pablo", 3 + 5j]

nested = [None, 5j, -0.09, '''Shi''', 0B101011, [-1, True, "sier"]]
```

As you can see, `lists` can hold ANY data value or even other defined elements, we will see in the future that lists are one of the most powerful data structures.

### Accessing List elements

You have various options to access the elements of a `list`, the elements are zero-indexed, this means that the first element will have an index of 0, the second will have index of 1 and so on...

* 0 -> 1
* 1 -> 2
* ...
* n - 1 -> n

So, if you have `n` elements inside your list, you can access the last element in the list using an index of `n-1`

If your `k` element on the list is another list you can also access elements in this nested list using this notation: `my_list[k][0]`

It's important to notice that you cannot access an index that is outside of the size of the list, this means that if you have a list holding `n` elements, your last index is always `n - 1` and trying access `n + k` where `k >= 0` will give you an error.

It's also possible to use negative indexes to access a element in a list, with this you can access the list backwards, but the rule applies equally: **You cannot access an element out of the index**

```
m_list = ["S","i","er",".."]
m_list[-1] # ".."
m_list[-2] # "er"
m_list[-3] # "i"
m_list[-4] # "S"
m_list[-5] # Error.
```

### Slices of lists

You can create copies of a list using `slices`. A slice is a sublist taken from the original list. 

To obtain this sublist you only need to access the elements that you want from a indexed range:

```
m_list = [1,4,7,0,11]
m_sublist = m_list[1:3]
m_sublist # [4,7]
```

The notation of the slice is flexible, so you can chose an start, or not, and you can chose an end, or not.

```
m_list[0:3] # Elements from position 0 to third element, not inclusive
m_list[:3] # Elements from start to third element, not inclusive
m_list[1:] # Elements from position 1 to end of the list, inclusive 
m_list[:] # All the elements.
```

### Mutable vs immutable

An important detail to see it's that `lists` are mutable, this means that the list can change the size of values or the content at certain position.

To change a value you only need to replace it using `=` -> `m_list[2] = "perrin"`

Other _data-types_ are immutable, which means that you cannot change the content once they are created.

### Helpers and methods

Python by itself has some bult-in functions, this will be explained in future topics but for now, let's talk about two functions: `len()` and `list()`

#### len()

The function `len` works with multiple types of data, this data has to be iterable or can contain multiple elements, this means that a `string` or a `list` can be passed to `len`. Once called `len` will return an `int` that represents the total elements inside the data structure.

```
m_list = [4,7,9,"Sierisimo"]

size = len(m_list)

print(size) # Will show 4, because m_list has 4 elements

size_str = len(m_list[3])

print(size_str) # Will show 9, because "Sierisimo" has 9 characters
```

#### list()

`list` function will turn a data that is iterable or a sequence into a list, this will help you to get the elements of a sequence as a list, for example from a string:

```
my_name = "Sierisimo"

my_letters = list(my_name) # Will return a list with: ['S', 'i', 'e', 'r', 'i', 's', 'i', 'm', 'o']
```

This function is helpful if you need a mutable data type or if you want to work with a list instead of your data source.

#### Methods

We don't want to discuss this now because it will get better when we talk about OOP. For now, **_you can think on a method as an operation that certain elements can do by itself. This means that you can ask for some work and the element will work with their own data._**.

##### Dot notation 

Lists have their own set of _methods_ that helps working with their data. To access this _methods_ we use the `dot notation`, this notation works like this: `element.method()` let's see what does this mean:

* element -> The element that we want to use, in this case the list. 
* . -> With the dot, we are accessing to something in the element, it's important to notice that this only work on composite/compound/complex data, like a list, that is actually a group of data.
* method -> It's the name of the thing that we want to use, in the case of methods they are usually verbs, for example if we are using something from, let's say, a human, we can access to some action that a human can do, like eating, with: `human.eat()`
* () -> This part denotes this is a method and no other thing, this will get clear in future topics. For now, understand that this will call an action and we actually can pass something to this action to work. Taking the last example, if we want a human to eat something we can pass it to the method with: `human.eat(a_carrot)` 

Now that we understand which is a _method_ and _dot notation_ let's see what _methods_ a list have:

* append(_element_) -> Add an element to the end of the list

  ```
  v = [2,4,9]
  v.append("Sier") # [2, 4, 9, "Sier"]
  ```

* extend(_iterable_) -> Pass another _iterable_ data source and it will expand your list.

  ```python
  v = [3, 5, -1, 'perrito', 'a']
  v.extend("Sier") # [3, 5, -1, 'perrito', 'a', 'S', 'i', 'e', 'r']
  ```

* insert(_index_, _element_) -> Put a certain _element_ into the position indicated by _index_, if _index_ is bigger than the size of the list the _element_ is added to the end of the list otherwise the element is added in the position and the elements on the next indexes are moved one space.

  ```python
  v = [3, 5, -1, 'perrito', 'a']
  v.insert(0,2) # [-2, 3, 5, -1, 'perrito', 'a']
  v.insert(12, 0) # [-2, 3, 5, -1, 'perrito', 'a', 0]	
  ```

* remove(_element_) -> Remove an _element_ from the list, if the element is not in the list an error is showed.

  ```python
  v = [3, 5, -1, 'perrito', 'a']
  v.remove("perrito") # [-2, 3, 5, -1, 'a']
  ```

* pop() -> Returns the last element on the list and removes it from the list. If no elements are present on the list, it shows an error.

  ```python
  v = [3, 5, -1, 'a']
  v.pop() # 'a'
  v # [3, 5, -1]
  ```

* clear() -> Removes all elements from the list

  ```
  v = [3, 5, -1, 'a']
  v.clear() # []
  ```

* index(_element_) -> Check for the index of a value inside of the list, if the list doesn't contain the _element_ it shows an error, else it returns an `int`

  ```python
  v = [2, 5, "Sier"]

  v.index(5)
  v.index("Ernesto")
  ```

* count(_element_) -> Returns the number of occurrence of certain _element_ inside the list.

  ```python
  v = [2,4,2,8,0,2]
  v.count(2) # Returns 3
  ```

* sort() -> Makes the list to be sorted by the ascending and natural order of his elements. The elements must be of the same type to obtain all the elements ordered, if they aren't, then the list will try to order the elements and show an error for incompatible types. In case that an ascending order is "confusing" the list will order by the natural order of the elements.

  ```python
  v = [5,6,9,0,-1,3]
  v.sort()
  v # [-1, 0, 3, 5, 6, 9]
  ```

* reverse() -> Makes the list to be backwards of his original state. This means that last element now it's the first and first it's the last an so on. This could be useful if you want different sorting than ascending.

  ```python
   v = [5,8,9]
   v.reverse()
   v # [9,8,5]
  ```

* copy() -> Returns a copy of this list, the advantage of this is that modifying the copy doesn't affect the original list.

  ```python
  v = [4,5,6]
  t = v.copy()

  v.append(7)
  t.append(0)

  v # [4,5,6,7]
  t # [4,5,6,0]
  ```

### List Comprehension

The list comprehension is one of the coolest features of python at lists, this features is a fast way to create lists from sentences that usually require a lot of statements.

The syntax is like this:

```python
list-name = [value-statement for-statement for-body]
```

Let's see what is this feature:

* _list-name_ will be the name of your list
* _value-statement_ will be a small statent or how this will be stored.
* _for-statement_ is a `for` loop that will run and create the values that you want on your `value-statement`
* _for-body_ is a possible body that may implies `if` statements

Example:

```python
pow2 = [2 ** x for x in [1,2,3,4,5]]
pow2 # [2, 4, 8, 16, 32]
```

In this example is visible how this works, the _value-statement_ turns to be: `2 ** x` and this is what the final value will be. The for only tooks every element on the list after the `in` and pass it as `x` to the _value-statement_.

You can think of this as:

```python
pow2 = []
for x in [1,2,3,4,5]:
   pow2.append(2 ** x)
```

## Tuples

And then, you have _tuples_, a _tuple_ is basically a **list** but with one small BUT VERY IMPORTANT difference: it's immutable.

What does this means? What's the importance and the usage on an immutable data? Well, let's say that you can have a _list_ and pass it around functions or process but without the worry of losing data.

Also, this structure beign immutable gives a boost on performance when iterating over the elements. Also, if you plan on using some elements as keys, or for example, constants, tuples are your answer.

### Create a tuple

This part can be tricky, but it's easier once it's learned.

You have the literal option and the function option:

#### Literal

To create a tuple, you must indicate the elements inside a parenthesis:

```python
my_tuple = (1,2,3)
```

But what happens if you want a tuple with a single element? If you write `r = (1)` you don't get a _tuple_ instead you get an `int` and this is visible using: `type(r)` which return some text indicating that it's a `integer` 

Then, how? Easy, when creating a _tuple_ of a single element, indicate that the second element doesn't exist: `r = (1,)` see? adding the `,` it's like saying: "Hey... here could be another element... but it isn't"

#### function tuple()

The function for creating a _tuple_ is just called: `tuple(i)` and it recives a parameter `i`  which is an _iterable_ object, like lists... yes, you can turn a list into a tuple just calling this function.

```python
my_list = [1, 2, 3]
my_tuple = tuple(my_list) # (1,2,3)
```

The advantage of this is that once we want to "lock" a list, we can just simply turn it into a tuple, like having a party and no allowing more invites.

### Tuple indexing

This will be fast: Accessing to elements in a tuple is as easy as in a List.

That's it, using the `[index]` notation and creating slices with: `:` it's the same.

### Tuple methods

Tuples only have two methods and they are pretty straigth forward:

* count(x) -> Returns the times the element _x_ is inside of the tuple
* index(x) -> Returns the index where _x_ is located.

Also, the other _built-in_ functions that work with iterable like `len()` or `str()` work with tuples. More on this in the built-in section.

### Operators

There's an specific case that we have to mention, tuples are immutable but you can use some operators to create new tuples, this operators are: `+` and `*`

Using `+` with both operands as tuples returns a third tuple with the elements of both tuples

```python
j = (1, 3, 5)
k = (2, 4, 6)
t = j + k
t # (1, 3, 5, 2, 4, 6)
```

And using the `*` returns a new tuple with the elements inside the tuple repetead in the order they are the _right operand_ times.

```python
j = ("Sier", "Ernesto")
k = j * 3
k # ("Sier", "Ernesto", "Sier", "Ernesto", "Sier", "Ernesto")
```

## Set

A _set_ is basically a data structure where the inner elements doesn't repeat. They are unique.

For creating a set you only have to use: `name = {element1, element2, ...}`

It's important to notice that the elements in a set must be immutable, this means that putting a list inside of a set it's not possible. But set by themselves aren't immutable, this means that you can add or remove elements, even there are special operations available for sets, like _union_ and _intersection_.

The Sets will be covered in future versions of this document, for now, just think that most of the built-in functions defined before also work with sets.

## Dictionary

A dictionary is a data structure that contains a group of combined _key_:_value_ elements, this means that the access to the elements in the dictionary are made by the _key_ and not by index.

In other languages this is called a **map** but the correctness of the name applies for dictionary.

In a dictionary in python you can assign any value to a key, the only rule is that the key **MUST** be an immutable data type. This means basically 3 types of keys: `number`, `string` and `tuple`.

The values aren't so prohibitibe, this means that you can assign numbers, strings, tuples, lists, objects, functions and even other dictionarys to a single key.

Just remember that your key MUST be unique, this means that if you are planning on using the same key for multiple values you may loose the values.

To creat a dictionary you only need to define the key:value relations between `{}`

```python
mDict = {}
oDict = {
    2: "perrito", 
    "dogo": 3, 
    (1,2): [-1], 
    "d": {1:1} 
}
```

### Accessing elements on a Dictionary

To access elements in a dictionary you have two options, one is the `[]` notation using the _key_ instead of an index or using the method: `dictionary.get` where `dictionary` corresponds to your dictionary.

### Methods on Dictionaries

| Method                 | Description                              |
| ---------------------- | ---------------------------------------- |
| ` clear()`             | Remove all items form the dictionary.    |
| ` copy()`              | Given the nature of the dictionary, to operate over it's elements without affecting the original nature it's necessary to create a copy and letting the original to |
| `get(key, default)`    | Return the value of _key_. If _key_ does not exit, return _default_ (defaults to `None`). |
| `fromkeys(seq)`        | Return a new dictionary with keys from _seq_. This method is used most of the time with a _list_ |
| ` items()`             | Return a new view of the dictionary's items (key, value). |
| ` keys()`              | Return a new view of the dictionary's keys. |
| ` pop(key[,d])`        | Remove the item with _key_ and return its value or _d_ if _key_ is not found. If _d_ is not provided and _key_ is not found, raises `KeyError`. |
| ` popitem()`           | Remove and return an arbitary item (key, value). Raises `KeyError` if the dictionary is empty. |
| ` setdefault(key[,d])` | If key is in the dictionary, return its value. If not, insert key with a value of d and return d (defaults to `None`). |
| ` update([other])`     | Update the dictionary with the key/value pairs from other, overwriting existing keys. |
| ` values()`            | Return a new view of the dictionary's values |

### Dictionary comprehension

A Dictionary can be created as well as with the built-in functions or literal notation but it also is posible to use the "comprehension" notation previously discussed in lists.

The only difference is that you must provide a way to create the key and a way to create the value:

```python
odd_squares = {x: x*x for x in range(11) if x%2 == 1}
```

### Built-in functions

Some of the python built-in functions are available to use with dictionaries, this functions are:

| Function    | Description                              |
| ----------- | ---------------------------------------- |
| `all()`     | Return `True` if all keys of the dictionary are true (or if the dictionary is empty). |
| ` any()`    | Return `True` if any key of the dictionary is true. If the dictionary is empty, return `False.` |
| ` len()`    | Return the length (the number of items) in the dictionary. |
| ` cmp()`    | Compares items of two dictionaries.      |
| ` sorted()` | Return a new sorted list of keys in the dictionary. |

This covers almost all the _basic_ data-types that Python has built-in, some other types are available via modules and libraries or even by OOP... but that topics will be discussed later.