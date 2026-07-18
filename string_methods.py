# string_methods.py
# Demonstration of Python String Methods

try:
    # Read string from user
    text = input("Enter a string: ")

    # 1. upper()
    print("\nUppercase:", text.upper())

    # 2. lower()
    print("Lowercase:", text.lower())

    # 3. split()
    delimiter = input("Enter a delimiter to split the string: ")
    print("Split Result:", text.split(delimiter))

    # 4. replace()
    old = input("Enter the substring to replace: ")
    new = input("Enter the new substring: ")
    print("After Replace:", text.replace(old, new))

    # 5. find()
    search = input("Enter a character or substring to find: ")
    index = text.find(search)

    if index != -1:
        print(f"'{search}' found at index {index}")
    else:
        print(f"'{search}' not found in the string.")

    # Example use cases
    print("\n--- Example Methods ---")
    print("Upper Example:", "python".upper())
    print("Lower Example:", "PYTHON".lower())
    print("Split Example:", "apple,banana,mango".split(","))
    print("Replace Example:", "I like Java".replace("Java", "Python"))
    print("Find Example:", "Programming".find("gram"))

except Exception as e:
    print("Error:", e)