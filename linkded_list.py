# Define a Node class to represent an element in the linked list
class Node:
    def __init__(self, data):
        # Initialize the node with data and set the next node to None
        self.data = data  # Data field to store the value
        self.next = None  # Next field to store the reference to the next node


# Define a LinkedList class to represent the linked list itself
class LinkedList:
    def __init__(self):
        # Initialize the linked list with a head node set to None (empty list)
        self.head = None

    # Method to insert a new node at the end of the list
    def append(self, data):
        # Create a new node with the given data
        new_node = Node(data)

        # If the list is empty, set the head to the new node
        if self.head is None:
            self.head = new_node
            return

        # Traverse the list to find the last node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        # Set the next reference of the last node to the new node
        last_node.next = new_node

    # Method to print the entire linked list
    def print_list(self):
        # Start from the head of the list
        current_node = self.head

        # Traverse the list and print each node's data
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")  # End of the list

    # Method to insert a new node at the beginning of the list
    def prepend(self, data):
        # Create a new node
        new_node = Node(data)

        # Set the new node's next reference to the current head
        new_node.next = self.head

        # Update the head to the new node
        self.head = new_node

    # Method to delete a node with a specific value from the list
    def delete_node(self, key):
        # Start with the head of the list
        current_node = self.head

        # If the head node itself holds the key, update the head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        # Otherwise, search for the key in the list
        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next

        # If the key was not found, return
        if current_node is None:
            return

        # Unlink the node to be deleted by updating the previous node's next reference
        prev.next = current_node.next
        current_node = None

    # Method to reverse the linked list
    def reverse(self):
        # Initialize previous, current, and next pointers
        prev = None
        current = self.head

        # Traverse the list and reverse the next pointers
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # After reversal, the previous node will be the new head
        self.head = prev


# Example usage of the LinkedList class
if __name__ == "__main__":
    # Create an empty linked list
    ll = LinkedList()

    # Append elements to the list
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)

    # Print the current list
    print("Initial linked list:")
    ll.print_list()

    # Prepend an element to the list
    ll.prepend(0)
    print("\nAfter prepending 0:")
    ll.print_list()

    # Delete a node with value 2
    ll.delete_node(2)
    print("\nAfter deleting node with value 2:")
    ll.print_list()

    # Reverse the linked list
    ll.reverse()
    print("\nAfter reversing the linked list:")
    ll.print_list()
