# Python Language Syntax

So far we have seen some features and important things on the language, but we haven't seen the language by itself.
This chapter introduces the most common elements of the language python syntax.

## Identifiers

As a high-level language, python has the advantage of using variables, this allows you to hold a certain variable value in a named reference. For example, if you create a program which asks users for their name, every user that uses your program will be putting something different and if you want to use that value in another part of your program like in a message, a toast or maybe a profile, you need to hold that value at least one time and wait for the need of using it.

Well, python allows the naming of variable with certain characteristics. This is easy to remember, because you don't need to remember a lot of rules.

This rules are only 5 and they are easy to remember:

1. Identifiers can be a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore (_).
2. Adding to the first rule: Identifiers **CANNOT** start with a digit.
3. Reserved words/Keywords (more on this ahead) **CANNOT** be used as identifiers.
4. **NO** special characters/symbols can be used as identifiers.
5. Identifiers can be of **ANY** length

### Case sensitivity

It's important to notice that python is a *case sensitive* language, this means that a identifier like: `var_user_name1` it's different from: `var_USER_name1` and also different from: `Var_user_name1` and so on.

## Reserved Words / Keywords

We mentioned previously that python contains some words that cannot be used as identifiers, this means that this group of words already have a meaning on the language and using them as identifiers could lead to mistakes when operating. 
For this reason, python doesn't allow you the usage of this words, and it's important to know which words are available or not.

Python provides a module called `keyword` that contains a list of this defined words. Don't worry if you don't get this code right now, it's here only to exemplify:

```python
# Yes, you have a module to check for keywords...
import keyword

# And you can obtain the full list for your python installation
for word in keyword.kwlist:
    print(word)
```

This will give us all the reserved words:

* False
* None
* True
* and
* as
* assert
* break
* class
* continue
* def
* del
* elif
* else
* except
* finally
* for
* from
* global
* if
* import
* in
* is
* lambda
* nonlocal
* not
* or
* pass
* raise
* return
* try
* while
* with
* yield

As you can see, there are a lot of reserved words, we'll try to explain their usage.

##### False

Word used for boolean and logical operations. This denotes when something is false, like in the sentence: `the red color is blue`.

##### None

This word has a special meaning in python, because it's used as a result for operations that didn't returned something, or when trying to represent something that exists but it's empty.

##### True

Used as a boolean or logical result, denotes when something is true, like in the sentence: `the word "dog" starts with a "d"`.

##### and

Used as an operator on logical operations, this word will be explained on the "logical operator" section.

##### as

This word is used to give an alias to a module, this will be explained in the modules section.

##### assert

The assert keyword is used for debugging purposes. We can use it for testing conditions that are obvious to us. For example, we have a program that calculates salaries. We know that the salary cannot be less than zero. So we might put such an assertion to the code. If the assertion fails, the interpreter will complain. More on this on the Unit Testing section.

##### break

We use break when we are on loops or in some block of code inside a loop and we want to stop the execution of the subsequent iterations. This will be explained in the "loops" section.

##### class

This word is used to define a class in python, this sounds redundant right now, but will be explained on the OOP section.

##### continue

It is used to interrupt the current cycle, without jumping out of the whole cycle. It initiates a new iteration in the same cycle if possible.

##### def

This word is used to define functions and methods. This will be explained in other topics.

##### if

The word if works with an expression, when the expression is valid and his value is `True` then the block below the if is executed. This will be explained in the "Control flow" topic.

##### elif 

Works similar to the `if`, but it needs to be a compliment for an if statement. More of this on the "control flow" topic.

##### else

This word is used with an if statement, when the expression after the `if` is not `True` the block after the else is executed. More on this in the "Control flow" topic.

##### except

This word is used when you need to work with an Exception, this will be explained in the "Exception Handling" topic.

##### finally

This word is used when you need to work with an Exception, this will be explained in the "Exception Handling" topic.

##### for

Used to denote a loop. More on the "Control flow" topic.

###### from

Used to import a certain part of a module, more on this on the "Modules" topic.

##### global

If we want to access variables defined outside functions, we use the global keyword.

##### import

Used to import a module, more on this on the "Modules" topic.

##### in

Used to check if some value is inside a structure. More of this in the "Operators" topic.

##### is

Used to check if some value correspond to certain class or is from certain type. More of this in the "Operators" topic.

##### lambda

The lambda keyword creates a new anonymous function. More of this on the "Data types" topic.

##### nonlocal 

Used to bind a variable in inner functions to a different scope. More of this in the "Control Structures" topic.

##### not

Used as a logical operator, more of this in the "Operators" module.

##### or

Used as a logical operator, more of this in the "Operators" module.

##### pass

Used to denote that some part of code will not do anything, more of this in the "Data types" topic.

##### raise

This word is used when an exception is needed, this will be explained in the "Exception Handling" topic.

##### return

Used to pass a value from a function to the caller of the function. More of this in the "Control Structures" topic.

##### try

This word is used when you need to work with some code that eventually `raise` and Exception, this will be explained in the "Exception Handling" topic.

##### while

Used to denote a loop. More on the "Control flow" topic.

##### with

Used to change the context of a block of code. More on the "Control flow" topic.

##### yield

This keyword is used with generators. Will be explained in detail in the "Data types" topic.

## Basic Operators

### Arithmetic Operators

#### Operator for Addition: +

This operator is used to add values on either side of the operator, a basic example could be:

```python
# Assume that a variable called 'x' has been declared before with a value of 10 and a variable 'y' has been declared before with a value of 20

x + y # Will result in 30
```

(If you want to corroborate this, you can execute python from a terminal and write: `10 + 20` it will prompt 30)

#### Operator for Subtraction: -

This operator works with two values, it subtracts the right hand operand from the left operand strictly.

```python
# Assume that a variable called 'x' has been declared before with a value of 10 and a variable 'y' has been declared before with a value of 20

x - y # Will result in 10
```

#### Operator for Multiplication: \*

The `*` operator multiplies values on either side of the operator.

```python
# Assume that a variable called 'x' has been declared before with a value of 10 and a variable 'y' has been declared before with a value of 20

x * y # Will result in 60
```

#### Operator for Division: /

The operator requires two values, one on the right and one on the left, then the operator divides the left hand operand by the right hand operand.

```python
# Assume that a variable called 'x' has been declared before with a value of 100 and a variable 'y' has been declared before with a value of 20

x / y # Will result in 5
```

#### Operator for Modulus: %

Divides left hand operand by right hand operand and returns remainder

```python
# Assume that a variable called 'x' has been declared before with a value of 35 and a variable 'y' has been declared before with a value of 3

x % y # Will result in 2
```

#### Operator for Exponent: \*\*

Performs exponential (power) calculation on operands, takes the left operand to the power of the right operand.


```python
# Assume that a variable called 'x' has been declared before with a value of 5 and a variable 'y' has been declared before with a value of 3

x ** y # Will result in 125
```

#### Operator for Floor division: //

This operator helps you when dealing with floating point numbers and integers. It takes a common division and rounds to the floor and in the case of the division is negative it looks like it take to the ceil, but actually goes to the result that is more away from zero.

```python
# Assume that a variable called 'x' has been declared before with a value of 5 and a variable 'y' has been declared before with a value of 3

x // y # Will result in 1

# If you use floating point numbers:

5.0 // 3 # Result: 1.0

5 // 3.0 # Result: 1.0

5 // -3 # Result: -2
```

### Comparison Operators

#### Operator for Equality: ==

If the values of two operands **are equal**, then the condition becomes `True`.

#### Operator for inequality: != or <>

If values of two operands are **not** equal, then condition becomes `True`

#### Operator for size: >

If the operand on the **left** is bigger than the operand on the **right** the condition becomes `True`

#### Operator for size: < 

If the operand on the **right** is bigger than the operand on the **left** the condition becomes `True`

#### Operator for size or equality: >=

If the operand on the left is **bigger** or equals to the operand on the right the condition becomes `True`

#### Operator for size or equality: <=

If the operand on the left is **smaller** or equals to the operand on the right the condition becomes `True`

### Operators for Assignment

#### Operator: =

Assigns values from right side operands to left side operand

`c = a + b # assigns value of a + b into c`

#### Operator: +=

It adds right operand to the left operand and assign the result to left operand.

```python
c = 20
c += 30 # Similar to: c = c + 30 or c = 20 + 30

# c now has the value of 50
```

#### Operator: -=

It subtracts right operand from the left operand and assign the result to left operand

```python
c = 20
c -= 30 # Similar to: c = c - 30 or c = 20 -30

# c now has the value of -10
```

#### Operator: *=

It multiplies right operand with the left operand and assign the result to left operand

```python
c = 20
c *= 30 # Similar to: c = c * 30 or c = 20 * 30

# c now has the value of 60
```

#### Operator: /=

It divides left operand with the right operand and assign the result to left operand

```python
c = 20
c /= 2 # Similar to: c = c / 2 or c = 20 / 2

# c now has the value of 10
```

#### Operator: %=

It takes modulus using two operands and assign the result to left operand

```python
c = 20
c %= 3 # Similar to: c = c % 3 or c = 20 % 3

# c now has the value of 2
```

#### Operator: **=

Performs exponential (power) calculation on operators and assign value to the left operand

```python
c = 2
c **= 3 # Similar to: c = c ** 3 or c = 20 ** 3

# c now has the value of 8
```

#### Operator: //=

It performs floor division on operators and assign value to the left operand

```python
c = 3
c //= 2 # Similar to: c = c // 2 or c = 3 // 2

# c now has the value of 1
```

### Bitwise Operators

#### Operator: & (AND)

Operator copies a bit to the result if it exists in both operands 	

```
(1 & 1) # 1  
(1 & 0) # 0
(0 & 1) # 0
(0 & 0) # 0

```

#### Operator: | (OR)

It copies a bit if it exists in either operand.


```
(1 | 1) # 1  
(1 | 0) # 1
(0 | 1) # 1
(0 | 0) # 0

```

#### Operator: ^ (XOR)

It copies the bit if it is set in one operand but not both


```
(1 | 1) # 0  
(1 | 0) # 1
(0 | 1) # 1
(0 | 0) # 0

```

#### Operator: ~ (NOT)

It is unary and has the effect of 'flipping' bits.


```
(~1) # 0
(~0) # 1

```

#### Operator: << (Left Shift)

The left operands value is moved left by the number of bits specified by the right operand.


```
(2 << 4) # Means: Take the binary value of 2 (10) and move it 4 spaces to the left (add zeros) resulting in: 100000 or 32 in decimal

```

#### Operator: << (Left Shift)

The left operands value is moved left by the number of bits specified by the right operand.


```
(32 >> 4) # Means: Take the binary value of 32 (100000) and move it 4 spaces to the right (add zeros) resulting in: 000010 or 2 in decimal

```

### Logical Operators

#### Operator: and

If both the operands are true then condition becomes true

```
True and True # Result in True
True and False # Result in False
False and True # Result in False
False and False # Result in False
```

#### Operator: or

If any of the two operands are non-zero then condition becomes true

```
True and True # Result in True
True and False # Result in True
False and True # Result in True
False and False # Result in False
```


#### Operator: not

Used to reverse the logical state of its operand

```
not True # False
not False # True

# It works with logical values
not (True and False) # True

# It could also works with some "falsy" values
not "String" # False
```

### Membership Operators

#### Operator: in

Evaluates to true if it finds a variable in the specified sequence and false otherwise.

```
# Imagine that we have a collection/sequence/list of elements denotated by: [ 1, 2, 3, ...]
# If a value is in the list, in will return True

3 in [1,2,3,4] # True because 3 is in this list
5 in [1,2,3,4] # False, because 5 is not in the list
```

### Identity Operators

#### Operator: is

Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.

```
5 is 5 # True
3 is 5 # False
```

### Precedence Operators

A real program will have a lot of sentences, equations, functions and operators, this operators usually come together in a single line, for example: `x = 5 + 3 * 2` and as you can see we have three operators in a single line. The question starts in here: How are they taken? in order from left to right or right to left? What will be the value of x? 

Well, Python as well as other languages implements some rules on the precedence on operators, this precedence keeps the coherence over the language. Listed in order of precedence bellow are the operators, in case of tie the first used operator will be used, for example: `c = 5 + 1 - 2` will be evaluated as:

```
5+1 # 6
6-2 # 3
c = 3
```

##### Order of precedence

1. ** (Exponentiation)
2. ~ (bitwise not)
3. * (multiplication), / (division), % (modulus), // (floor division)
4. + (sum), - (subtraction)
5. >> (Right bitwise shift), << (Left bitwise shift)
6. & (Bitwise AND)
7. ^ (Bitswise XOR), | (Bitwise OR)
8. <= (Less or equals), < (Less than), > (Bigger than), >= (Bigger or equals)
9. <> (Different of), != (Different of), == (Equals to)
10. = (Assignment), %= (Modulus assignment), /= (Division assignment), //= (Floor division assignment), -= (Subtraction assignment), += (Sum assignment), *= (Multiplication assignment) **= (Exponential Assignment)
11. is, is not (The second one counts as one operator)
12. in, not in (The second one counts as one operator)
13. not, or, and

## Indentation

In python you need to be careful with the _style_ of your code because python doesn't manage scopes as other languages.
The scope in python depends on where is the code starting and how many spaces/tabs are you using. Now that we mention the _tabs vs spaces war_ you should start using spaces... why? because is more _**pythonic**_ and you can read about it [here in the PEP-008](https://www.python.org/dev/peps/pep-0008/#tabs-or-spaces)

**Once you start coding you cannot mix the way you indent, so if you choose to use tabs instead of spaces (~~don't~~) you cannot go back unless you change every part of the code where you put tabs. This also applies to the number of spaces, if you choose to use 2 instead of 4, you are going to change everything when you decide to use another number of spaces.**

But well... once we clarified that **4 SPACES IS THE COOLEST THING** we can talk about the scope and blocks of code.

### Scope

The scope is where something is valid/lives. This means, that if I ask you about Sier or Ernesto, you'll know that we're talking about the authors of this text, but if I ask you for Jossue maybe you'll get confused because maybe you know someone called Jossue that I don't or maybe you don't know any Jossue at all. That's scope! (~~you can think of scope as context~~)

Some special things in python have their own scope and you need to indent ~~preferably with 4 spaces~~ to specify that some code is related to certain scope.

Let's look to an _non-code_/_pseudo-code_ example:

```
# Imagine that using "declare" we can create a person:
declare sier
declare ernesto

# Now imagine that using "group" we can talk with people in a certain group
group friends:
	# This line is inside of the "friends" scope
    sier is awesome # True
    ernesto is cool # True
    
    declare chacon
    
    chacon is cool # True
    
 # Outside of the "friends scope"
chacon is cool # This will fail, because chacon only exists inside friends.
```

This will be totally explained and more detailed in the "Data types" topic and in the "OOP" topic.

### Blocks 

As well as the **scope** we can have a "blocks" of code, which represent that certain part of the code will only work if is inside a certain part.

This sounds dizzy but is easier to see with another non-code example:

```
when is Wednesday:
    go_for_burritos()
    
when is Friday:
    go_for_beers()
```

This example shows some _pseudo code_ to represent a block of code. We don't go for burritos unless it's Wednesday and we don't go for beers unless it's Friday. That execution will only happen when the day is right and in no other case. In here we see that the blocks belongs to a pre-condition. This will be more comprehensible when we touch "Control flow" topic.