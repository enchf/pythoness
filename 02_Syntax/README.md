# Python Language Syntax

So far we have seen some features and important things on the language, but we haven't seen the language by itself.
This chapter introduces the most common elements of the language python syntax. 

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

## Data types

### Built-in

* Booleans (True, False)
* Numbers (int, long, float, complex)
* Strings ("...", '...')
* Lists (Anything that is listed between \[\] and separated with a comma for example: `[1, 3.0, 5, True, "Sier"]`). _more on lists later_ 
* Tuple (A tuple is like a list, but with the difference that a tuple is inmutable and is denoted with  `(...)` instead of `[]`). _more on tuples later_
* Dictionary (A dictionary is a data type that works as map or an assignment between "keys" and "values", they are denoted with `{}`). _more on dictionaries later_


#### Numbers

Numbers represent mathematic values, this mean numbers in general, the most common are the **int** and the **float** which represents the common values that appears in operations. When a numbers is to big to fit in a int it is transformed automatically into a _long_ which is a big number, it also can be represented as an octal notation or a number finished with an "L".

Float numbers also are represented with exponential notation.

 