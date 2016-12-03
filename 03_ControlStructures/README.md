# Control Structures

So far we have talked about what's python, how to install it, which tool will help us on working (IDEs) and also in topic 2 we covered Identifiers, Reserved words, operators, indentations, scopes, blocks and comments... but everything is just messed up if we don't start giving structure and flow to our code. So let's start talking about **Control structures** and how to work with real code.

## Variables

A variable is a holder for a value, this value could be any of the valid Data types available in python, this holder must have a valid identifier. We talked about identifiers before, now it's the time to put them on work!

When a variable is declared, you don't necessary have to put the _type_ of the value that the variable will be holding, python infer which type is and then creates the binding internally.

Also, variables in python are "Dynamic typed" which means that a variable originally holding a text can suddenly hold a number and then change again into a list of objects. This helps you to write faster your code but also could lead to big mistakes.

Creating a variable is very easy, you just have to use the _assignment operator_ `=` and a valid identifier plus a value.

```
my_variable = 2
othe_variable = "A text"
```

To change the value of a variable is as simple as just reassign the variable: 

```
my_variable = 2

# other stuff
....

my_variable = 5

# other stuff
....

my_variable = "Text"
```

As you see, it's easy to work with variables, to see the value of a variable we just need to put the name of the variable:

```
var = 2

var # Will put 2 on the screen
```

You can use this advantage to use variables instead of values:

```
x = 2
y = 3
z = x + y

z # Will put 5 in the screen
```

With this in mind you can start imaging how much possibilities this open like asking for input and working with remote values.

## Flow Control

Software doesn't have a single task usually and you don't get the output on the screen always and also as we saw before on the indentation parts, sometimes the execution have to be related to a context or to a certain state of the software. Python contains some keywords and operations that will help you to organize your code better and to give more options to the execution.
