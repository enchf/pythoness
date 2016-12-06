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


### if...else

The first kind of _flow control_ is the _if_. 

What the _if_ does is give you the option to execute when something is available/true and skip when not. 

So that's the reason for a `else` to exists, imagine:

> You have a job and your boss orders you to work if it's monday... what will you do the rest of the week?

Well, the right thing to do is add a `else` clausule, this helps you to work in other cases:

> You have a job and your boss orders you to work if it's monday any other case, just help others.

Let's see a code example:

```python
z = x + y

if z < 10:
	startHomeWork()
else:
	goToSleep()
```

This example shows how `if` and `else` works together, when the sum of `x` and `y` is less than 10 we must start our homework, otherwise we should go to sleep.

But what about other values? What happens when we don't have something to test directly like a numeric value against other? That's when Falsy (~~and truthly~~) values come in play.

#### Falsy

Python as well as other _interpreted_ languages implements something called _truthy_ and _falsy_ values, this means that it has values that aren't actually a `True` or `False` but the language operates when they exist. Python actually test for _truth_ when talking about this values.

The following values are considered `False`:

* None
* False
* zero of any numeric type, for example, 0, 0.0, 0j.
* any empty sequence, for example, '', (), []. More on this on Data types
* any empty mapping/dictionary, for example, {}. More on dictionaries on Data types topic
* instances of user-defined classes, if the class defines a __bool__() or __len__() method, when that method returns the integer zero or bool value False. More on this on OOP

All other values are evaluted to `True` unless stated before. Functions that return a numeric value of 0 or `False` are `False` any other case is `True`

### elif

But whit all of this in mind... what happens when we have more than one condition or maybe more than one case?

It's when `elif` enters the game.

`elif` works as an aditional `if` without getting out of the flow, this means that we can check for multiple cases and execute just what we want.

```python
message = ""

if age < 13:
	message = "You cannot enter to this movie"
elif age >= 13 and age < 18:
	message = "You can only enter with an adult"
else:
	message = "You can enter to this movie" 
```

As you may notice we need an additional condition to some case, with elif we are allowing the execution of this condition in the cases where the first one is not happening.

Also, as you can see, we are using the `and` operator to join two conditions in one sentence, this is: `when the age is greater or equals to 13 but also is less than 18`.

You can use as many `elif` conditions in a `if` _flow_. 
As a last note, just notice that `if` doesn't care about what's inside of it's body, this means that you can choose to use another `if` inside of an if.

```python
first = ""
second = ""
third = ""

if True:
    first = "Hello"
    if False or False:
        second = " my name is"

        if True:
            third = " Christian"
        elif False and False:
            third = " Ernesto"
        else:
            third = " Christopher"
    elif True or False:
        second = " my alias is"

        if False and not True:
            third = " Lenny"
        elif None:
            third = " Epammuel"
        else:
            third = " Sier"
    else:
        second = " I have no name"
else:
    first = "Bye"

# What's the value for: first ?
# What's the value for: second ?
# What's the value for: third ?
```

### _for_ loop

A loop is like a cycle... something that will repeat until something breaks it.
For example the cycle of life:

* Born
* Grow
* Reproduce
* Die

Well, this thing called `for` is helpful because we can repeat everything we want when this is inside of the _block of code_ of the loop (_see? now it makes more sense to indent our code_). 

The general form of a `for` loop will look like these:

```python
for var in sequence_of_values:
	# body to execute
	# another posible statement...
	# etc.
```

Let's look at this part by part because it can get tricky:

The `for` part is mandatory for a `for` loop, with this word you setle that a for is going to be executed. 

Then you need a variable (~~or variables as we see in the future~~) to catch the values that will be emited by the for on every iteration, in this example it is represented by a variable with the name `var`.

Then you HAVE TO indicate to the for from where it will take the values to assign to `var`, you use the _reserved word (wink wink)_ `in` which takes values from an operand on his right, in this case we use `sequence_of_values` which as his name says is a sequence of values, this sequence can be from various types that we try to cover on other topics, for now let's assume that anything wrapped between \[\], \(\) or "" is a sequence and can be iterate on the `for`.

And finally you have the body of your `for` loop. This body will be executed _n-times_ which means that if you have a sequence of 10 values, then your `for` loop will execute 10 times. So, for any item in your _sequence_ you'll get that value assigned to `var` and then you body is executed, once you have assigned every value in your sequence your `for` stops and your code continues from outside of the body.

Again, similar to the `if`, the `for` doesn't care about his body unless it contains a `break` or a `continue` because... well, you already read it on the "**Reserved Words**" topic.

Let's see at some examples of a for execution:

```python
for num in [1,2,4,5,-1,9,-10]:
	num
```

```python
for num in (1,2,3,5,7,10,15,-10,-11,-32, 50, 100):
	if num >= 50:
		break
	else:
		if num % 2:
			num
		else:
			continue
		"Odd printed"
```

#### else

The `for` loop can work with an aditional thing, a else clausule, this clausule will execute every time the elements on the _sequence_ are exhausted. This means that if the `for` doesn't have any other element on the _sequence_ then the `else` will execute. On other hand, if a `break` happens before the `for` finishes working with the sequence, the `else` will not execute.

Let's see an example:

```python
for letter in "Perrito bonito":
    letter
else:
    " :)"
```

This example will print on the screen:

```
P
e
r
r
i
t
o

b
o
n
i
t
o
 :)
```

There are other ways to iterate over elements, but this covers almost all, the other ways involves calling functions and this will be covered in future topics.

### while loop

The other way to iterate or work in a loop is with a `while` loop, this loop is a kind of mix between an `if` and a `for`.

The common form of a `while` loop is:

```python
while EXPRESSION:
	# body
	# more body
```

As you see, it's almost the same than a `for` but it will continue unless one of two thing happen:
1. A `break` occurs in the body
2. The EXPRESSION stops beign `True`

This means that a while can easly go to infinite iterations if we don't take care of the body.

An easy example of this is:

```python
counter = 0

while counter < 3:
    counter
    counter += 1
```

This will show on the terminal:

```
0
1
2
```

Because at some point count goes to value of 3 and then, it stops beign `< 3` and the EXPRESSION: `counter < 3` stops beign True.

The `while` loop can work with an `else` like the `for` loop and the `if` clausule.


```python
counter = 0

while counter < 3:
    counter
    counter += 1
else:
	counter
	"Counter nows holds a 3"
```

This `else` clausule will be executed once the EXPRESSION stops beign `True` and no `break` statement happend on the execution of the body.

### pass

The `pass` clausule will work as an indicator of 

> nothing is happening inside the body

This could be useful for declaring loops that iterate over something, empty clausules or define functions that will do nothing but maybe in the future will. 

This pass is mostly used on functional programming and OOP and could be more comprensible in future topics. 

* * * *

NOW THAT WE HAVE CONTROL OVER THE FLOW OF OUR CODE... let's start with more complex things...

