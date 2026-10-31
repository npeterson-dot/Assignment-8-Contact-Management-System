
class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"


class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''

    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        new_contact = Contact(key, value)

        # If the index is empty, add the first node.
        if self.data[index] is None:
            self.data[index] = Node(key, new_contact)
            return

        # Search the linked list for duplicates or its last node.
        current = self.data[index]

        while current is not None:
            if current.key == key:
                current.value.number = value
                return

            if current.next is None:
                break

            current = current.next

        # A collision occurred, so add another linked list node.
        current.next = Node(key, new_contact)

    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]

        while current is not None:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def print_table(self):
        for index in range(self.size):
            current = self.data[index]

            if current is None:
                print(f"Index {index}: Empty")
            else:
                contacts = []

                while current is not None:
                    contacts.append(str(current.value))
                    current = current.next

                print(f"Index {index}: - " + " - ".join(contacts))


# Test your hash table implementation here.
if __name__ == "__main__":
    table = HashTable(10)

    print("Testing an empty hash table:")
    table.print_table()

    print("\nAdding contacts:")
    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")
    table.print_table()

    print("\nSearching for John:")
    print("Search result:", table.search("John"))

    print("\nTesting hash collisions:")
    # Amy and May have the same character total, so they collide.
    table.insert("Amy", "111-222-3333")
    table.insert("May", "222-333-1111")
    table.print_table()

    print("\nTesting duplicate contact updates:")
    table.insert("Rebecca", "999-444-9999")
    print("Updated contact:", table.search("Rebecca"))
    table.print_table()

    print("\nSearching for a missing contact:")
    print("Search result:", table.search("Chris"))

    print("\nTesting Contact and Node classes:")
    contact_1 = Contact("Riley", "123-456-7890")
    node_1 = Node(contact_1.name, contact_1)
    print("Contact:", contact_1)
    print("Node key:", node_1.key)
    print("Node value:", node_1.value)
    print("Node next:", node_1.next)
