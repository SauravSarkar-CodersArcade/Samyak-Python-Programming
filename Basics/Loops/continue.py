# The moment code encounters a continue statement,
# it skips the current value & goes to the next value
# It will execute all values just skipping the current value
for i in range(6):
    if i == 3:
        continue
    print(i)

