# 1.
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius  

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius

if __name__ == "__main__":
    radius = float(input("Enter the radius of the circle: "))  
    circle = Circle(radius)  

    print(f"Area of the circle: {circle.area():.2f}")
    print(f"Perimeter of the circle: {circle.perimeter():.2f}")  

# 2.
from datetime import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name  
        self.country = country  
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d") 

    def age(self):
        """Calculate the person's age."""
        today = datetime.today()  
        age = today.year - self.date_of_birth.year  
        
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age

if __name__ == "__main__":
    name = input("Enter the person's name: ")
    country = input("Enter the person's country: ")
    date_of_birth = input("Enter the date of birth (YYYY-MM-DD): ") 

    person = Person(name, country, date_of_birth)  
    print(f"{person.name} is {person.age()} years old and lives in {person.country}.")  

# 3.
class Calculator:
    def add(self, a, b):
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the difference of a and b."""
        return a - b

    def multiply(self, a, b):
        """Return the product of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the quotient of a and b."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

if __name__ == "__main__":
    calculator = Calculator()  
    
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    operation = input("Enter the operation (1/2/3/4): ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operation == '1':
        result = calculator.add(num1, num2)
        print(f"The result is: {result}")
    elif operation == '2':
        result = calculator.subtract(num1, num2)
        print(f"The result is: {result}")
    elif operation == '3':
        result = calculator.multiply(num1, num2)
        print(f"The result is: {result}")
    elif operation == '4':
        try:
            result = calculator.divide(num1, num2)
            print(f"The result is: {result}")
        except ValueError as e:
            print(e)
    else:
        print("Invalid operation selected.")

  # 4.
import math

class Shape:
    """Base class for different shapes."""
    def area(self):
        """Calculate the area of the shape."""
        raise NotImplementedError("This method should be overridden in subclasses.")

    def perimeter(self):
        """Calculate the perimeter of the shape."""
        raise NotImplementedError("This method should be overridden in subclasses.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, base, height, side_a, side_b, side_c):
        self.base = base
        self.height = height
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return 4 * self.side_length

if __name__ == "__main__":

    circle = Circle(radius=5)
    triangle = Triangle(base=6, height=4, side_a=5, side_b=5, side_c=6)
    square = Square(side_length=4)

    print(f"Circle: Area = {circle.area():.2f}, Perimeter = {circle.perimeter():.2f}")
    print(f"Triangle: Area = {triangle.area():.2f}, Perimeter = {triangle.perimeter():.2f}")
    print(f"Square: Area = {square.area():.2f}, Perimeter = {square.perimeter():.2f}")

# 5.
class TreeNode:
    """Class representing a node in the binary search tree."""
    def __init__(self, key):
        self.left = None  
        self.right = None 
        self.val = key  
      
class BinarySearchTree:
    """Class representing the binary search tree."""
    def __init__(self):
        self.root = None  

    def insert(self, key):
        """Insert a new key into the BST."""
        if self.root is None:
            self.root = TreeNode(key)  
        else:
            self._insert_recursively(self.root, key)

    def _insert_recursively(self, node, key):
        """Helper method to insert keys recursively."""
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)  
            else:
                self._insert_recursively(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)  
            else:
                self._insert_recursively(node.right, key)

    def search(self, key):
        """Search for a key in the BST."""
        return self._search_recursively(self.root, key)

    def _search_recursively(self, node, key):
        """Helper method to search for keys recursively."""
        if node is None or node.val == key:
            return node is not None  
        elif key < node.val:
            return self._search_recursively(node.left, key)
        else:
            return self._search_recursively(node.right, key)

if __name__ == "__main__":
    bst = BinarySearchTree()  

  
    elements = [7, 3, 9, 1, 5, 8, 10]
    for elem in elements:
        bst.insert(elem)

    search_keys = [5, 11]
    for key in search_keys:
        result = bst.search(key)
        print(f"Element {key} {'found' if result else 'not found'} in the BST.")

  # 6.
class Stack:
    """Class representing a stack data structure."""
    def __init__(self):
        self.items = []  

    def push(self, item):
        """Push an item onto the stack."""
        self.items.append(item)
        print(f"Pushed {item} onto the stack.")

    def pop(self):
        """Pop an item off the stack."""
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        item = self.items.pop() 
        print(f"Popped {item} from the stack.")
        return item

    def peek(self):
        """Return the top item of the stack without removing it."""
        if self.is_empty():
            print("Stack is empty. Cannot peek.")
            return None
        return self.items[-1]  

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0  

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)  

if __name__ == "__main__":
    stack = Stack()  
    
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    print(f"Top element is: {stack.peek()}")
    
    stack.pop()
    stack.pop()
    
    print(f"Current stack size: {stack.size()}")
   
    stack.pop()
  
    stack.pop()

# 7.
class Node:
    """Class representing a node in a linked list."""
    def __init__(self, data):
        self.data = data  
        self.next = None  

class LinkedList:
    """Class representing the linked list."""
    def __init__(self):
        self.head = None  

    def insert(self, data):
        """Insert a new node at the end of the linked list."""
        new_node = Node(data)  
        if self.head is None:
            self.head = new_node 
            return
        last = self.head
        while last.next:  
            last = last.next
        last.next = new_node 

    def delete(self, key):
        """Delete the first node with the specified key."""
        current = self.head
        previous = None

        if current is None:
            print("List is empty. Cannot delete.")
            return

        if current is not None and current.data == key:
            self.head = current.next  
            return

        while current is not None and current.data != key:
            previous = current
            current = current.next

        if current is None:
            print(f"Node with data {key} not found.")
            return

        previous.next = current.next

    def display(self):
        """Display the linked list."""
        current = self.head
        if current is None:
            print("Linked list is empty.")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  
      
if __name__ == "__main__":
    linked_list = LinkedList()  

    linked_list.insert(10)
    linked_list.insert(20)
    linked_list.insert(30)

    print("Current linked list:")
    linked_list.display()

    linked_list.delete(20)
    print("Linked list after deleting 20:")
    linked_list.display()

    linked_list.delete(40)

    linked_list.display()

# 8.
class ShoppingCart:
    """Class representing a shopping cart."""
    def __init__(self):
        self.items = {} 

    def add_item(self, item_name, price, quantity=1):
        """Add an item to the shopping cart."""
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity  
        else:
            self.items[item_name] = {'price': price, 'quantity': quantity} 
        print(f"Added {quantity} of {item_name} at ${price:.2f} each.")

    def remove_item(self, item_name, quantity=1):
        """Remove an item or quantity from the shopping cart."""
        if item_name in self.items:
            if self.items[item_name]['quantity'] <= quantity:
                del self.items[item_name]  
                print(f"Removed all of {item_name} from the cart.")
            else:
                self.items[item_name]['quantity'] -= quantity  
                print(f"Removed {quantity} of {item_name} from the cart.")
        else:
            print(f"{item_name} not found in the cart.")

    def calculate_total(self):
        """Calculate the total price of items in the cart."""
        total = sum(item['price'] * item['quantity'] for item in self.items.values())
        return total

    def display_cart(self):
        """Display the items in the shopping cart."""
        if not self.items:
            print("Shopping cart is empty.")
            return
        print("Shopping Cart Items:")
        for item, details in self.items.items():
            print(f"{item}: {details['quantity']} @ ${details['price']:.2f} each")

if __name__ == "__main__":
    cart = ShoppingCart()  
    
    cart.add_item("Apple", 0.99, 3)
    cart.add_item("Banana", 0.50, 5)
    cart.add_item("Milk", 1.50, 2)

    cart.display_cart()

    total_price = cart.calculate_total()
    print(f"Total price: ${total_price:.2f}")

    cart.remove_item("Banana", 2)
    cart.display_cart()

    total_price = cart.calculate_total()
    print(f"Total price after removal: ${total_price:.2f}")

# 9.
class Stack:
    """Class representing a stack data structure."""
    def __init__(self):
        self.items = []  

    def push(self, item):
        """Push an item onto the stack."""
        self.items.append(item) 
        print(f"Pushed {item} onto the stack.")

    def pop(self):
        """Pop an item off the stack."""
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        item = self.items.pop() 
        print(f"Popped {item} from the stack.")
        return item

    def peek(self):
        """Return the top item of the stack without removing it."""
        if self.is_empty():
            print("Stack is empty. Cannot peek.")
            return None
        return self.items[-1]  

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0 

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items) 

    def display(self):
        """Display the elements of the stack."""
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Current stack elements (top to bottom):")
            for item in reversed(self.items):
                print(item)

if __name__ == "__main__":
    stack = Stack() 

    stack.push(10)
    stack.push(20)
    stack.push(30)

    stack.display()

    print(f"Top element is: {stack.peek()}")

    stack.pop()
    stack.display()

    stack.pop()
    stack.pop()

    stack.pop()

    stack.display()

# 10.
class Queue:
    """Class representing a queue data structure."""
    def __init__(self):
        self.items = [] 
    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)  
        print(f"Enqueued {item} to the queue.")

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        item = self.items.pop(0) 
        print(f"Dequeued {item} from the queue.")
        return item

    def peek(self):
        """Return the front item of the queue without removing it."""
        if self.is_empty():
            print("Queue is empty. Cannot peek.")
            return None
        return self.items[0]  

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0  

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items) 

    def display(self):
        """Display the elements of the queue."""
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Current queue elements (front to back):")
            for item in self.items:
                print(item)

if __name__ == "__main__":
    queue = Queue()  

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    queue.display()

    print(f"Front element is: {queue.peek()}")

    queue.dequeue()
    queue.display()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.display()

# 11.
class Customer:
    """Class representing a customer account."""
    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number
        self.balance = 0.0
      
    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f} to {self.name}'s account.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > self.balance:
            print("Insufficient funds for withdrawal.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} from {self.name}'s account.")

    def get_balance(self):
        """Return the current balance."""
        return self.balance


class Bank:
    """Class representing the bank."""
    def __init__(self):
        self.customers = {} 

    def add_customer(self, name, account_number):
        """Add a new customer account."""
        if account_number not in self.customers:
            self.customers[account_number] = Customer(name, account_number)
            print(f"Added customer: {name} with account number: {account_number}.")
        else:
            print("Account number already exists.")

    def deposit(self, account_number, amount):
        """Deposit money into a customer's account."""
        if account_number in self.customers:
            self.customers[account_number].deposit(amount)
        else:
            print("Account number not found.")

    def withdraw(self, account_number, amount):
        """Withdraw money from a customer's account."""
        if account_number in self.customers:
            self.customers[account_number].withdraw(amount)
        else:
            print("Account number not found.")

    def get_balance(self, account_number):
        """Get the balance of a customer's account."""
        if account_number in self.customers:
            balance = self.customers[account_number].get_balance()
            print(f"Balance for account {account_number}: ${balance:.2f}")
            return balance
        else:
            print("Account number not found.")
            return None
