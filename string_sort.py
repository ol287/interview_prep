

"""Problem:

You are given a string containing alphanumeric characters. Sort the string with the following rules:

All lowercase letters come before uppercase letters.
All uppercase letters come before digits.
Odd digits come before even digits.
Input:
A single string of alphanumeric characters.

Output:
Output the sorted string based on the above rules."""

def sort_key(x):
    if x.isdigit():
        if int(x) % 2 == 1:
            return (2, x)  # Odd digits come first
        else:
            return (3, x)  # Even digits come after odd digits
    elif x.isupper():
        return (1, x)  # Uppercase letters come after lowercase letters
    else:
        return (0, x)  # Lowercase letters come first

def custom_sort(s):
    return ''.join(sorted(s, key=sort_key))

# Example usage
s = input()
print(custom_sort(s))
