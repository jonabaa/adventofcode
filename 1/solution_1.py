""" Solution for exercise 1, day1, advent of code. """

def check_numbers(numbers):
    N = len(numbers)
    for i in range(N):
        for j in range(N):
            if j <= i:
                continue
            if numbers[i] + numbers[j] == 2020:
                return numbers[i]*numbers[j]
    return None

from lib import load_file_to_list
numbers = load_file_to_list("numbers.txt")
answer = check_numbers(numbers)
if answer is not None:
    print("Numbers satisfying condition found. Product={}.".format(answer))
else:
    print("No numbers satisfying the condition found.")
