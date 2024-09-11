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

#Question 18 Write two Python programs, one using a loop and another using list comprehension, to achieve the same functionality of squaring all the elements in a list.
def same_loop(list):
    squared_list = []
    for num in list:
        squared_list.append(num ** 2)
    print(squared_list)
    newlist = [x**2 for x in list]
    print(newlist)
    
#Question 19 Write a Python program to find the second largest element in a list.
def second_largest(numbers):
    numbers.sort()
    return numbers[-2]

#Question 21: Write a Python program to implement a recursive function for calculating the factorial of a number.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
#Question 22 Write a Python program to implement a function for finding the GCD (Greatest Common Divisor) of two numbers.
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
#Question 23: Write a Python program to implement a function for checking if a string is a valid parenthesis expression.
def is_valid_parentheses(expression):
    stack = []
    opening_parentheses = ['(', '[', '{']
    closing_parentheses = [')', ']', '}']
    parentheses_mapping = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in opening_parentheses:
            stack.append(char)
        elif char in closing_parentheses:
            if not stack or parentheses_mapping[char]!= stack.pop():
                return False

    return not stack

#Question 24 Write a Python program to implement a function for finding the longest common substring in two strings.
def longest_common_substring(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0
    end_index = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i - 1

    return str1[end_index - max_length + 1: end_index + 1]

#Question 25 Write a Python program to implement a function for performing memoization on a function.
def memoize(func):
    cache = {}

    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]

    return wrapper
            
#Question 26 Write a Python program to implement a custom data structure like a binary search tree (BST).
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a new node with the given key
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.key:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        elif key > root.key:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    # Search for a node with a given key
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    # Inorder Traversal (left, root, right)
    def inorder(self):
        elements = []
        self._inorder(self.root, elements)
        return elements

    def _inorder(self, root, elements):
        if root:
            self._inorder(root.left, elements)
            elements.append(root.key)
            self._inorder(root.right, elements)

    # Preorder Traversal (root, left, right)
    def preorder(self):
        elements = []
        self._preorder(self.root, elements)
        return elements

    def _preorder(self, root, elements):
        if root:
            elements.append(root.key)
            self._preorder(root.left, elements)
            self._preorder(root.right, elements)

    # Postorder Traversal (left, right, root)
    def postorder(self):
        elements = []
        self._postorder(self.root, elements)
        return elements

    def _postorder(self, root, elements):
        if root:
            self._postorder(root.left, elements)
            self._postorder(root.right, elements)
            elements.append(root.key)

    # Find the minimum value in the BST
    def find_min(self):
        current = self.root
        while current and current.left is not None:
            current = current.left
        return current.key if current else None

    # Find the maximum value in the BST
    def find_max(self):
        current = self.root
        while current and current.right is not None:
            current = current.right
        return current.key if current else None

    # Delete a node from the BST
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            min_larger_node = self._find_min(root.right)
            root.key = min_larger_node.key
            root.right = self._delete(root.right, min_larger_node.key)

        return root

    def _find_min(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current
        