# Other Types

Even when this aren't recognized as types in common languages, in python the next elements are recognized as data types:

* Functions
* Lambdas
* Exceptions

The next part of the course tries to explain this elements and how they work.

## Functions

A function is a set of steps that are frequently used, because of this, you need to abstract a way to repeat the steps every time you need them without skipping how they work.

Usually the functions are ways to work some specific data every time they appear, modify the recived data and then return a result of the modification. Functions can recive and send data, when data is passed to a function, the data is called **parameter** and inside of the function they are known as **argument**. 

To define a function you have to use the reserved word: `def` and give a name to your function. 

```python
def my_function():
    # Body of the function
```

If you need parameters, they have to defined by name inside of the parenthesis of the name:

```python
def my_param_function(param1, param2, param3):
    # Body
```

### Arguments for functions

The arguments to a function doesn't necessary have to be of a certain type and they can also be omitted if the function defines a default value to every argument. Also you can annotate which is the type of your parameters and what it's the value of return of the function, but adding this not means that the function will work like it's annotated. 

```python
def default_values(param1 = 2, param2 = ""):
    # Body for your function
    
def my_annotated_func(param1: int, param2: str):
    # Body for the function
    
def my_annotated_return() -> list:
    # Body
```

And also, you can mix this concepts to get a better annotated and working function, but remember that beign annotated doesn't mean that it will work as it says. 

Also this makes python more readable, a lot of python programmers use the phrase: 

> "We're all consenting adults here"

That belongs to the python philosophy.

### Indentation

For now, we have seen the concept of how to declare a function, but not how the body of the function actually is. 

Well, at the same way the control flow structures use indentation to _determine_ which blocks of code applies to them, functions use the indentation to mark where they start and where they end.

Inside a block of code of a function yo can also have more blocks of code. For example for control flow, for loops or even for more functions, yes, you can have functions inside a function... but this is another topic...

With all of this in mind, let's imagine a function that takes two numbers and returns the sum of both:

```python
def sum_two_numbers(x = 0, y = 0):
    return x + y
```

As you can see in the above example, the function is using the default value for the parameters and its using the reserved word `return` to give back to the calling the result of his operation... and we know all of this because it's indented inside of the function, if that indentation wasn't there, then an error will be displayed, because you can only `return` from inside of functions.

### Documentation on functions

Inside a function, you can have a documentation block, which is a comment made with a triple pair of: `"`  (quotes) this documentation is useful because it becomes part of the function by itself, so you can access it when running the interpreter or via: `my_func.__doc__`

Some built-in functions use this attribute to show help about a function.

### Built-in functions

This part is hard to explain, because there's a lot of built-in functions, so let's just put some words on what's a buil-in function:

A built-in function is a function that python already has defined, so you can use it anywhere without having to define how it works or with which values it work. For example, we have seen `len()` that works with _iterable data types_ or `type()` that returns a string saying which type is certain variable. The complete list of _built-in_ functions is very big, so we are gonna talk a little more about it in next topics.

### Calling a function

Once you have declared a function, how do you call it? Well, it's easy, as you may imagine from past examples, you only need to put the name of your function plus a set of parenthesis, this tells python: "hey, please run the set of steps called _X_ with this data".

```python
def my_function(x):
    # Code...
    x += 5
    # More code...
    return x

my_function(5)
```

As you can see in here, we are calling the function called _my_function_, it operates with a given value _x_ and tries to add 5 to that value and then return the new value of _x_. A few lines below we can see that to call the function we use the name of the fucntion plus a pair of parenthesis with a value between them. This is how we pass the value to the function to say: "HERE YOU ARE FUNCTION, MAKE ME FEEL PROUD".

With this in mind we have a few possible questions:

* What happens with the value returned from the function?
* What happens if I don't return?
* What if I want to return more than a value from the function?
* Where or when is _x_ available?

Well, this and more question may be around your head now, we try to answer some of them.

### Returning values.

After a "return statement" what happens with the returned value from the function?

Well... you have options, first it's to store it in a variable so you can handle or use it later, for example:

```python
def sum_two_numbers(x, y):
    return x + y

z = sum_two_numbers(5,7)
z # Will show 12
```

But also you can use the returned value as parameter to other function:

```python
def plus_5(x):
    return x + 5

def multiply_by_2(r):
    return r * 2

z = multiply_by_2(plus_5(10))
z # Will be 30, because (10 + 5) * 2
```

And now... what happens if I don't return?

Actually... nothing happens or to be more precise: `None` happens. This means, if you don't have anything else to do inside your function and never return and you are trying to assing a value from a calling... the assigned value is `None`

```python
def not_returning():
    pass

v = not_returning()
v # None
```

We talked about this `None` that is a valid value to represent that something exists but has no value/meaning.

Wait a minute... and what's that `pass` word? Well, we talked about it a few topics before. `pass` it's a way to say: "nothing to do here..." and then... do nothing  or _pass over it_ `¯\_(ツ)_/¯`

Well and what about the case when I want to return multiple values from a function? You can actually do it, and how you get this values represents how do you use it in the future.

The first way is simply to return this values in one sentence and assign them to a variable:

```python
def three_vals():
    return 1,3,"Sier"

variab = three_vals()
```

If you now check how this values are in `variab` or you decide to use a more proffessional way to check a the type of a variable ~~wink,wink~~ you can use: `type(variab)` and with this you'll notice that the return value is assigned to a `tuple` (uff... good thing that we saw `tuples` previously).

But what if we don't want a tuple and we want all the values separated? WEEEEELLLL this is also posible using "decomposition":

```python
def two_vals():
    return 2,[]

a_num, a_list = two_vals()
```

And you can declare which variables will hold which values, the thing with this kind of move, it's that you always have to put the exact number of holders for the return value, this means: if your function will return 6 values, then you have to assign 6 variables, one per returning from the function.

And this could lead to tedious or unreadable code, so... your last option is use a list and return the list:

```python
def returns_list():
    return [1,3,4,"sier"]

returning_values = returns_list()
```

Actually you can return also a `tuple` but... you know, `list` is mutable.

And now the other pending question: where does the argument of a function is alive? Well, this can be explained explaining **scope**

### Scope

The scope represents where something has meaning, where it exists and where it's valid.

For example, imagine if I ask you: "_hey have you seen Christian?_"

Here is a world of posible answers:

-_Yes he's on his place_

-_Christian? My cousin? Do you know him?_

-_Who?_

And so on... why? because maybe you know a person called _Christian_ or maybe not, but the interesting part in here is if we both know the same _Christian_.

Well this is something that also happens in functions:

```python
def f():
    if x > 5:
        return z
    else:
        return y
```

Where is `x` defined? What about the other variables `z` and `y` ?  and we have a worst case:

```python
x = "Ernesto"

def f(x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"
```

What?? Are you saying that `x % 2` represent something like: `"Ernesto" % 2` and this returns an `int`? Well... nope, scope in python is based on some rules:

* A variable that it's outside a function is _global_
* A variable that it's declared inside a function is _local_
* A variable that it's an argument of a function it's _local_
* A _global_ variable that is reasigned inside a function actually represents the creation of a new _local_ variable with the same name
* A _local_ variable it's not accesible outside their declared function and the bound between name and value it's loose after the function finishes.
* Usage of _global_ variables and reasignations requieres the usage of the _reserved word_ `global`

You can check an example in [Scope.py](./scope.py)

### Functions as variables or data

Given the form of python to operate it's also posible to use functions as values for other functions or even as data.

When you _def_ ine a function you create a boud in the memory to it's name and you can actually use this bound/name in other places as it was a variable:

```python
def py_is_fun():
    pass

if py_is_fun: # Valid sentence, because py_is_fun is a truthy value
    # Do Stuff
```

And this helps you a lot to make your programms more "_dynamic_"

```python
def executor_of_functions(fun):
    # Do stuff...
    fun() # Call the passed function
    # Do more stuff
    
def some_function():
    # Do own stuff
    
executor_of_functions(some_function)
```

You can imagine the posibilities this brings, it's helpful if you want to make usage of python a litle more "functional" but also gives the posibility of some advanced techniques like:

### Closures

A closure it's a technique with a very common usage in other languages, mostly in JavaScript, it refers to a function having a function in his body and this second function (a.k.a **child function**) makes usage of the first function (a.k.a **parent function**) arguments or variables... it's more easy to understand with code:

```python
def parent_function():
    my_num = 32
    
    def child_function():
        # Do stuff...
        x = my_num % 3
        # Do more stuff...
        return x
	
    return child_function

modified = parent_function()
```

This code maybe looks weird but once understanded it leads to powerful techniques for using functions, callbacks, scopes and other complex usage of the versatility of python.

Basically at the end of the code, `modified` becomes a function that can use `my_num` without knowing the original value. 

An important note in this kind of technique is that the variable used in `parent` function becomes _read-only_ or _immutable_ which means that a modification to this variable it's not posible.

Other great example could be visible in [Closure.py](./closure.py)

Sometimes this techniques looks like a lot of overhead to just acomplish a fast and continous execution of code... so... presenting: Lambdas.

## Lambdas

A lambda is a way to express a small function that doesn't need a big body to do something interesting, it means, a single expression, this is usually helpful when one of the params to a function is another function.

The syntax is easy:

```python
lambda arguments: expression
```

The easiest example is that if you need to define a function to always do something simple, you can use a lambda:

```python
double_number = lambda x: x*2

double_number(5) # Return 10
```

You may notice that lambda expressions always return a value and the body is a single expression. Well, lambdas are useful also when you don't want to define a full function for a function calling, the classical example is the `filter()` function that takes a function and a list and applies the function to all the elements in the list. Your filter function should return a truthly value.

```python
even_numbers = list(filter(lambda x: x % 2 == 0, [1,2,3,4,5,6]))
even_numbers # [2,4,6]
```



## Exceptions