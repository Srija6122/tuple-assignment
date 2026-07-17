# 1. Function to calculate the sum of all numbers in a list

def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

numbers = [10, 20, 30, 40, 50]
print("Sum:", sum_of_list(numbers))


# 2. Print each character of a string on a new line

text = input("Enter a string: ")
print("Characters:")
for ch in text:
    print(ch)


# 3. Print only the even numbers from a list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Even Numbers:")
for num in numbers:
    if num % 2 == 0:
        print(num)


# 4. Function to print the length of each word

def word_lengths(words):
    for word in words:
        print(word, ":", len(word))

words = ["Python", "Programming", "Loop", "Assignment"]
print("Word Lengths:")
word_lengths(words)


# 5. Calculate the average of numbers in a list

numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

average = total / len(numbers)
print("Average:", average)