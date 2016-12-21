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

Indentation



Functions & Scopes, Lambdas, Exceptions