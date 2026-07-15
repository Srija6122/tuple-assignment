# List with duplicate numbers
numbers = [1, 2, 3, 4, 2, 5, 6, 3]

# Convert list to set
num_set = set(numbers)
print("Original Set:", num_set)

# Add new element
num_set.add(10)
print("After Adding:", num_set)

# Remove an element
num_set.remove(2)
print("After Removing:", num_set)

# Another set
set2 = {4, 5, 6, 7, 8}

# Union
print("Union:", num_set.union(set2))

# Intersection
print("Intersection:", num_set.intersection(set2))

# Difference
print("Difference:", num_set.difference(set2))




library = {
    "Python Basics": {
        "author": "John",
        "year": 2022,
        "genre": "Programming"
    },
    "Data Science": {
        "author": "Alice",
        "year": 2021,
        "genre": "Education"
    }
}

# Add Book
library["AI Basics"] = {
    "author": "David",
    "year": 2023,
    "genre": "Technology"
}

# Remove Book
library.pop("Data Science")

# Search Book
search = "Python Basics"

if search in library:
    print(search, "Found")
    print(library[search])
else:
    print("Book Not Found")

# Display Books
print("\nLibrary Books:")
for book in sorted(library):
    print(book, ":", library[book])