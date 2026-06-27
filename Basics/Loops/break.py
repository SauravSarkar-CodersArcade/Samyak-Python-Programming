# The moment code encounters a break statement,
# it breaks the loop & goes out of the loop
# It will not execute anything after the break statement
for i in range(6):
    if i == 3:
        break
    print(i)

