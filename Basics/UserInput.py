"""
Type Conversion:
1. Implicit Type Conversion -> Internally
2. Explicit Type Conversion -> Externally | Manual
"""
name = input('Enter your name: ')  # Auto
age = int(input('Enter your age: '))  # Manual
# In Python any user input using input function is str
print(type(name), type(age))
# Method 1: Type Conversion
print('My name is ' + name + ' and my age is ' +
      str(age))
# Method 2: Formatted String f
# {var} Placeholder => var_value
print(f'My name is {name} and my age is {age}')
# Method 3: format() function
# {index} Placeholder => index -> 0,1,2,3, and so on
print('My name is {2} and my age is {3}'.format(name, age, "Samyak", 22))
