# 1. Check if string contains only alphabets
def is_alphabets(s):
    return s.isalpha()


# 2. Check if string contains only digits
def is_digits(s):
    return s.isdigit()


# 3. Check if string is alphanumeric
def is_alphanumeric(s):
    return s.isalnum()


# 4. Capitalize first letter of every word
def capitalize_words(sentence):
    return sentence.title()


# 5. Count number of words
def count_words(sentence):
    return len(sentence.split())


# 6. Remove all vowels
def remove_vowels(s):
    vowels = "aeiouAEIOU"
    result = ""
    for ch in s:
        if ch not in vowels:
            result += ch
    return result


# 7. Check palindrome
def is_palindrome(s):
    text = s.replace(" ", "").lower()
    return text == text[::-1]


# 8. Replace multiple spaces with a single space
def remove_extra_spaces(s):
    return " ".join(s.split())


# 9. Convert sentence to camelCase
def to_camel_case(sentence):
    words = sentence.lower().split()
    if not words:
        return ""
    return words[0] + "".join(word.capitalize() for word in words[1:])


# 10. Convert sentence to snake_case
def to_snake_case(sentence):
    return "_".join(sentence.lower().split())


# ----------------------------
# Test Examples
# ----------------------------

print("1.", is_alphabets("Python"))
print("2.", is_digits("12345"))
print("3.", is_alphanumeric("Python123"))
print("4.", capitalize_words("welcome to python"))
print("5.", count_words("Welcome to Python Programming"))
print("6.", remove_vowels("Programming"))
print("7.", is_palindrome("madam"))
print("8.", remove_extra_spaces("Hello     World    Python"))
print("9.", to_camel_case("welcome to python programming"))
print("10.", to_snake_case("Welcome To Python Programming"))