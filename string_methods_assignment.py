# string_methods_assignment.py

# 1. Clean String
def clean_string(text):
    return text.strip().lower()


# 2. Extract Substring
def extract_substring(text, start_index):
    return text[start_index:]


# 3. Replace Vowels
def replace_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""

    for ch in text:
        if ch in vowels:
            result += "*"
        else:
            result += ch

    return result


# 4. Split String into Words
def split_words(text):
    return text.split()


# 5. Join List with Comma
def join_words(words):
    return ",".join(words)


# -------------------------
# Testing the Functions
# -------------------------

sample = "   Hello Python World   "

print("Original String:", sample)

print("Clean String:", clean_string(sample))

print("Extract Substring:", extract_substring(sample, 8))

print("Replace Vowels:", replace_vowels(sample))

word_list = split_words(sample)
print("Split Words:", word_list)

joined = join_words(word_list)
print("Joined String:", joined)