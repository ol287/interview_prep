#Question 1 Write a Python program to check if a number is even or odd.
def check_number(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

#Question 2 Write a Python program to find the factorial of a number.
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)
    
#Question 3: Write a Python program to find the largest number in a list.
def find_largest(numbers):
    return max(numbers)

#Question 4: Write a Python program to convert a string to uppercase and lowercase.
def convert_case(string):
    return string.upper(), string.lower()

#Question 5: Write a Python program to find the sum and average of elements in a list.
def calculate_sum_average(numbers):
    return sum(numbers), sum(numbers) / len(numbers)

#Question 6: Write a Python program to check if a string contains a specific substring.
def check_substring(string, substring):
    return substring in string

#Question 7:  Write a Python program to print the elements of a list in reverse order.
def reverse(numbers):
    return numbers[::-1]

#Question 9: Write a Python program to check if a character is a vowel or consonant.
def is_vowel(char):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return char.lower() in vowels

#Question 10: Write a Python program to find the length of a string.
def length_of_string(string):
    return len(string)

#Question 11: Find the minimum and maximum elements in a list:
def min_max_elements(list):
    return min(list), max(list)

# Question 12: Write a Python program to find the sum of all prime numbers in a given range.
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

#Question 13: Create a dictionary from a list of key-value pairs:
def create_dictionary(pairs):
    return {key: value for key, value in pairs}

#Question 14:Write a Python program to sort a list in ascending or descending order.
def sort_list(numbers, ascending=True):
    return sorted(numbers, reverse=not ascending)

#Question 15 Write a function to calcuate the area of a rectangle
def calc_rect(width, height):
    return width * height

#Question 16 Question 17: Write a Python program to implement a simple text-based menu using loops and conditional statements.
def menu():
    while True:
        print("1. Add numbers")
        print("2. Subtract numbers")
        print("3. Multiply numbers")
        print("4. Divide numbers")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 + num2
            print(f"The sum is: {result}")
        elif choice == "2":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 - num2
            print(f"The difference is: {result}")
        elif choice == "3":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 * num2
            print(f"The product is: {result}")
        elif choice == "4":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 / num2
            print(f"The product is: {result}")
        else:
            break
        
#Question 17 Write a Python program to check if a string is a palindrome.A palindrome is a word or phrase that reads the same backward as forward (e.g., "racecar", "madam").
def is_palindrome(string):
    return string == string[::-1]

            
    
        