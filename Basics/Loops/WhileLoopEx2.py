# Password with retry limit
password = "secret@123"
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    guess = input('Enter your password: ')
    if guess == password:
        print('Access Granted!')
        break
    attempts += 1
    print(f'Incorrect Password! {max_attempts - attempts} attempts left.')

if attempts == max_attempts:
    print('Too many attempts! Access Locked. 🔐')
