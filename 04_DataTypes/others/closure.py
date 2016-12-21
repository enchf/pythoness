# Define a function that returns a new function that recives a value
# And returns the value multiplied by a previous setted value
def create_multiply_by(num):
    def multi_by(x):
        return x * num
    return multi_by

# We use that function to create other functions that have specified ways to work
multiply_by_two = create_multiply_by(2)
multiply_by_three = create_multiply_by(3)

print(multiply_by_two(4))
print(multiply_by_three(50))