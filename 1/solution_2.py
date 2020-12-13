""" Solution to exercise 2, day 1, advent of code. """

def find_three_numbers_summing_to(numbers, sum):
    N = len(numbers)
    for i in range(N):
        for j in range(N):
            if j <= i:
                continue
            for k in range(N):
                if k <= j:
                    continue
                if numbers[i] + numbers[j] + numbers[k] == sum:
                    return numbers[i]*numbers[j]*numbers[k]

    return None

file_name = "numbers.txt"
sum = 2020
from lib import load_file_to_list
numbers = load_file_to_list(file_name)
product = find_three_numbers_summing_to(numbers, sum)

if product is not None:
    print("Numbers satisfying condition found. Product = {}.".format(product))
else:
    print("No numbers satisfying condition found.")


