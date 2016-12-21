def my_func():
    x = 10
    print("Value inside function:", x)


x = 20
my_func()
print("Value outside function:", x)


def my_second_function(x):
    print(x)

my_second_function(30)
print(x)

def my_third_func():
    global x
    x *= 2
    print(x)

my_third_func()
print(x)