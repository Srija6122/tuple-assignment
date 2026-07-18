# while_loop_assignment.py

# Program 1: Print numbers from 1 to 10 using a while loop

print("Numbers from 1 to 10:")
count = 1

while count <= 10:
    print(count)
    count += 1

# Program 2: Print numbers from 1 to user input with input validation

try:
    number = int(input("\nEnter a positive integer: "))

    if number <= 0:
        print("Error: Please enter a positive integer.")
    else:
        print(f"Numbers from 1 to {number}:")
        count = 1
        while count <= number:
            print(count)
            count += 1

except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")