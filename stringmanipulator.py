class StringManipulator:
    def __init__(self, string):
        self.string = string

    # 1. Reverse the string
    def reverse_string(self):
        return self.string[::-1]

    # 2. Convert the string to uppercase
    def to_uppercase(self):
        return self.string.upper()

    # 3. Convert the string to lowercase
    def to_lowercase(self):
        return self.string.lower()

    # 4. Convert the string to title case
    def to_titlecase(self):
        return self.string.title()

    # 5. Split the string into a list of words
    def split_string(self, delimiter=" "):
        return self.string.split(delimiter)

    # 6. Join a list of words into a single string
    def join_string(self, words_list, delimiter=" "):
        return delimiter.join(words_list)

    # 7. Check if a substring exists within the string
    def contains_substring(self, substring):
        return substring in self.string

    # 8. Replace a substring with another substring
    def replace_substring(self, old, new):
        return self.string.replace(old, new)

    # 9. Remove leading and trailing whitespace from the string
    def trim_whitespace(self):
        return self.string.strip()

# Example usage:
string_manipulator = StringManipulator("Hello Python")

# Reverse string
print("Reversed String:", string_manipulator.reverse_string())

# Convert to uppercase
print("Uppercase String:", string_manipulator.to_uppercase())

# Convert to lowercase
print("Lowercase String:", string_manipulator.to_lowercase())

# Convert to title case
print("Titlecase String:", string_manipulator.to_titlecase())

# Split string into words
split_words = string_manipulator.split_string()
print("Split String:", split_words)

# Join words into a string
print("Joined String:", string_manipulator.join_string(split_words, "-"))

# Check if a substring exists
print("Contains 'Python':", string_manipulator.contains_substring("Python"))

# Replace substring
print("Replace 'Python' with 'World':", string_manipulator.replace_substring("Python", "World"))

# Trim whitespace
string_with_spaces = StringManipulator("  Hello World  ")
print("Trimmed String:", string_with_spaces.trim_whitespace())
