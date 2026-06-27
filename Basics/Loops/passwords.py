passwords = ['2026', 'Java', 'python', 'RVCE']

pwd = input('Enter the password:')

# if pwd in passwords:
#     print('Access Granted')
# else:
#     print('Access Denied')

if pwd not in passwords:
    print('Access Denied')
else:
    print('Access Granted')


