while True:
    age = input('Enter your age (1-100):')
    if age.isdigit() and 1 <= int(age) <= 100:
        age = int(age)
        break
    print('Invalid Age! Please enter a number b/w 1 & 100.')


print(f'Your age is {age}')
