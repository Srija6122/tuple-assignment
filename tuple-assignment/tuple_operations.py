# Tuple of 5 cities
cities = ("Hyderabad", "Chennai", "Bangalore", "Delhi", "Mumbai")
print("Cities:", cities)

# First and last element
def first_last(t):
    return t[0], t[-1]

print("First and Last:", first_last(cities))

# Tuple of students
students = (
    ("John", 85),
    ("Alice", 92),
    ("Bob", 78)
)

# Sort student names
def sort_students(data):
    names = sorted([student[0] for student in data])
    return tuple(names)

print("Sorted Names:", sort_students(students))

# Tuple unpacking
def unpack(values):
    a, b, c = values
    print(a)
    print(b)
    print(c)

numbers = (10, 20, 30)
unpack(numbers)