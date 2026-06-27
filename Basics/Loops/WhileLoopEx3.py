"""
Process a list of numbers & find:
1. Positive sum
2. Negative sum
3. Zero Count
"""
numbers = [1, -5, 10, -3, 8, -2, 0, 6, 0]
positive_sum = 0
negative_sum = 0
zero_count = 0
index = 0
while index < len(numbers):
    num = numbers[index]
    if num > 0:
        positive_sum += num
    elif num < 0:
        negative_sum += num
    else:
        zero_count += 1
    index += 1

print(f"Positive Sum: {positive_sum}")
print(f"Negative Sum: {negative_sum}")
print(f"Zero Count: {zero_count}")
