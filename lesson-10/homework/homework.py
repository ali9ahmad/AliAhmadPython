# Homework 1. ToDo List Application

# 1.
from datetime import datetime

class Task:
    """Class representing a task."""
    def __init__(self, title, description, due_date):
        self.title = title 
        self.description = description 
        self.due_date = self.set_due_date(due_date) 
        self.status = "Pending" 
    def set_due_date(self, due_date):
        """Set the due date, ensuring it's a valid date."""
        try:
            return datetime.strptime(due_date, "%Y-%m-%d")  
        except ValueError:
            print("Invalid date format. Please use 'YYYY-MM-DD'.")
            return None

    def mark_completed(self):
        """Mark the task as completed."""
        self.status = "Completed"
        print(f"Task '{self.title}' marked as completed.")

    def __str__(self):
        """Return a string representation of the task."""
        return (f"Task: {self.title}\n"
                f"Description: {self.description}\n"
                f"Due Date: {self.due_date.strftime('%Y-%m-%d') if self.due_date else 'N/A'}\n"
                f"Status: {self.status}")
#2.
class Task:
    """Class representing a task."""
    def __init__(self, title, description, due_date):
        self.title = title 
        self.description = description  
        self.due_date = due_date
        self.status = "Pending"  

    def mark_completed(self):
        """Mark the task as completed."""
        self.status = "Completed"

    def __str__(self):
        """Return a string representation of the task."""
        return (f"Task: {self.title}\n"
                f"Description: {self.description}\n"
                f"Due Date: {self.due_date}\n"
                f"Status: {self.status}")


class ToDoList:
    """Class representing a to-do list."""
    def __init__(self):
        self.tasks = []  

    def add_task(self, title, description, due_date):
        """Add a new task to the to-do list."""
        new_task = Task(title, description, due_date)
        self.tasks.append(new_task)
        print(f"Added task: '{title}'.")

    def mark_task_complete(self, title):
        """Mark a task as complete by title."""
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()
                print(f"Task '{title}' marked as completed.")
                return
        print(f"Task '{title}' not found.")

    def list_all_tasks(self):
        """List all tasks in the to-do list."""
        if not self.tasks:
            print("No tasks in the to-do list.")
            return
        print("All Tasks:")
        for task in self.tasks:
            print(task)
            print("-" * 20)

    def display_incomplete_tasks(self):
        """Display all incomplete tasks."""
        incomplete_tasks = [task for task in self.tasks if task.status == "Pending"]
        if not incomplete_tasks:
            print("No incomplete tasks.")
            return
        print("Incomplete Tasks:")
        for task in incomplete_tasks:
            print(task)
            print("-" * 20)

# 3.
class Task:
    """Class representing a task."""
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "Pending"

    def mark_completed(self):
        """Mark the task as completed."""
        self.status = "Completed"

    def __str__(self):
        return (f"Task: {self.title}\n"
                f"Description: {self.description}\n"
                f"Due Date: {self.due_date}\n"
                f"Status: {self.status}")

    
class ToDoList:
    """Class representing a to-do list."""
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date):
        new_task = Task(title, description, due_date)
        self.tasks.append(new_task)
        print(f"Added task: '{title}'.")

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()
                print(f"Task '{title}' marked as completed.")
                return
        print(f"Task '{title}' not found.")

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
            return
        print("All Tasks:")
        for task in self.tasks:
            print(task)
            print("-" * 20)

    def display_incomplete_tasks(self):
        incomplete_tasks = [task for task in self.tasks if task.status == "Pending"]
        if not incomplete_tasks:
            print("No incomplete tasks.")
            return
        print("Incomplete Tasks:")
        for task in incomplete_tasks:
            print(task)
            print("-" * 20)


def main():
    todo_list = ToDoList()

    while True:
        print("\nToDo List CLI")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. Display Incomplete Tasks")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            todo_list.add_task(title, description, due_date)

        elif choice == "2":
            title = input("Enter the title of the task to mark as complete: ")
            todo_list.mark_task_complete(title)

        elif choice == "3":
            todo_list.list_all_tasks()

        elif choice == "4":
            todo_list.display_incomplete_tasks()

        elif choice == "5":
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please choose a number between 1 and 5.")


if __name__ == "__main__":
    main()

# Homework 2. Simple Blog System

#1.
class Post:
    """Class representing a blog post."""
    def __init__(self, title, content, author):
        self.title = title  
        self.content = content  
        self.author = author  

    def __str__(self):
        """Return a string representation of the post."""
        return (f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Content:\n{self.content}\n")

# 2.
class Post:
    """Class representing a blog post."""
    def __init__(self, title, content, author):
        self.title = title  
        self.content = content  
        self.author = author  

    def __str__(self):
        """Return a string representation of the post."""
        return (f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Content:\n{self.content}\n")


class Blog:
    """Class representing a blog that manages a list of posts."""
    def __init__(self):
        self.posts = [] 
      
    def add_post(self, title, content, author):
        """Add a new post to the blog."""
        new_post = Post(title, content, author)
        self.posts.append(new_post)
        print(f"Added post: '{title}' by {author}.")

    def list_posts(self):
        """List all posts in the blog."""
        if not self.posts:
            print("No posts available in the blog.")
            return
        print("All Posts:")
        for post in self.posts:
            print(post)
            print("-" * 20)

    def display_posts_by_author(self, author):
        """Display all posts by a specific author."""
        author_posts = [post for post in self.posts if post.author == author]
        if not author_posts:
            print(f"No posts found by author '{author}'.")
            return
        print(f"Posts by {author}:")
        for post in author_posts:
            print(post)
            print("-" * 20)


# 3.
class Post:
    """Class representing a blog post."""
    def __init__(self, title, content, author):
        self.title = title 
        self.content = content  
        self.author = author  

    def __str__(self):
        """Return a string representation of the post."""
        return (f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Content:\n{self.content}\n")


class Blog:
    """Class representing a blog that manages a list of posts."""
    def __init__(self):
        self.posts = []  

    def add_post(self, title, content, author):
        """Add a new post to the blog."""
        new_post = Post(title, content, author)
        self.posts.append(new_post)
        print(f"Added post: '{title}' by {author}.")

    def list_posts(self):
        """List all posts in the blog."""
        if not self.posts:
            print("No posts available in the blog.")
            return
        print("All Posts:")
        for post in self.posts:
            print(post)
            print("-" * 20)

    def display_posts_by_author(self, author):
        """Display all posts by a specific author."""
        author_posts = [post for post in self.posts if post.author == author]
        if not author_posts:
            print(f"No posts found by author '{author}'.")
            return
        print(f"Posts by {author}:")
        for post in author_posts:
            print(post)
            print("-" * 20)


def main():
    blog = Blog()  

    while True:
        print("\nBlog CLI")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Display Posts by Author")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            blog.add_post(title, content, author)

        elif choice == "2":
            blog.list_posts()

        elif choice == "3":
            author = input("Enter the author's name: ")
            blog.display_posts_by_author(author)

        elif choice == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please choose a number between 1 and 4.")


if __name__ == "__main__":
    main()

# 4.
class Post:
    """Class representing a blog post."""
    def __init__(self, title, content, author):
        self.title = title 
        self.content = content  
        self.author = author  

    def __str__(self):
        """Return a string representation of the post."""
        return (f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Content:\n{self.content}\n")


class Blog:
    """Class representing a blog that manages a list of posts."""
    def __init__(self):
        self.posts = []  

    def add_post(self, title, content, author):
        """Add a new post to the blog."""
        new_post = Post(title, content, author)
        self.posts.append(new_post)
        print(f"Added post: '{title}' by {author}.")

    def list_posts(self):
        """List all posts in the blog."""
        if not self.posts:
            print("No posts available in the blog.")
            return
        print("All Posts:")
        for post in self.posts:
            print(post)
            print("-" * 20)

    def display_posts_by_author(self, author):
        """Display all posts by a specific author."""
        author_posts = [post for post in self.posts if post.author == author]
        if not author_posts:
            print(f"No posts found by author '{author}'.")
            return
        print(f"Posts by {author}:")
        for post in author_posts:
            print(post)
            print("-" * 20)

    def delete_post(self, title):
        """Delete a post by title."""
        for i, post in enumerate(self.posts):
            if post.title == title:
                del self.posts[i]
                print(f"Deleted post: '{title}'.")
                return
        print(f"Post '{title}' not found.")

    def edit_post(self, title, new_title=None, new_content=None):
        """Edit an existing post by title."""
        for post in self.posts:
            if post.title == title:
                if new_title:
                    post.title = new_title
                if new_content:
                    post.content = new_content
                print(f"Updated post: '{title}'.")
                return
        print(f"Post '{title}' not found.")

    def display_latest_posts(self, count=5):
        """Display the latest posts (up to the specified count)."""
        if not self.posts:
            print("No posts available in the blog.")
            return
        print(f"Latest {count} Posts:")
        for post in self.posts[-count:]:
            print(post)
            print("-" * 20)


def main():
    blog = Blog()  

    while True:
        print("\nBlog CLI")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Display Posts by Author")
        print("4. Delete Post")
        print("5. Edit Post")
        print("6. Display Latest Posts")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            blog.add_post(title, content, author)

        elif choice == "2":
            blog.list_posts()

        elif choice == "3":
            author = input("Enter the author's name: ")
            blog.display_posts_by_author(author)

        elif choice == "4":
            title = input("Enter the title of the post to delete: ")
            blog.delete_post(title)

        elif choice == "5":
            title = input("Enter the title of the post to edit: ")
            new_title = input("Enter new title (leave blank to keep current): ")
            new_content = input("Enter new content (leave blank to keep current): ")
            blog.edit_post(title, new_title if new_title else None, new_content if new_content else None)

        elif choice == "6":
            count = int(input("Enter the number of latest posts to display: "))
            blog.display_latest_posts(count)

        elif choice == "7":
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please choose a number between 1 and 7.")


if __name__ == "__main__":
    main()

# Homework 3. Simple Banking System

# 1.
class Account:
    """Class representing a bank account."""
    def __init__(self, account_number, account_holder_name, balance=0.0):
        self.account_number = account_number  
        self.account_holder_name = account_holder_name 
        self.balance = balance 

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}.")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance.")

    def __str__(self):
        """Return a string representation of the account."""
        return (f"Account Number: {self.account_number}\n"
                f"Account Holder: {self.account_holder_name}\n"
                f"Balance: ${self.balance:.2f}")

#2.
class Account:
    """Class representing a bank account."""
    def __init__(self, account_number, account_holder_name, balance=0.0):
        self.account_number = account_number 
        self.account_holder_name = account_holder_name 
        self.balance = balance  

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}."
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}."
        else:
            return "Withdrawal amount must be positive and less than or equal to the balance."

    def get_balance(self):
        """Return the current balance."""
        return self.balance

    def __str__(self):
        """Return a string representation of the account."""
        return (f"Account Number: {self.account_number}\n"
                f"Account Holder: {self.account_holder_name}\n"
                f"Balance: ${self.balance:.2f}")


class Bank:
    """Class representing a bank that manages a list of accounts."""
    def __init__(self):
        self.accounts = [] 

    def add_account(self, account_number, account_holder_name, initial_balance=0.0):
        """Add a new account to the bank."""
        new_account = Account(account_number, account_holder_name, initial_balance)
        self.accounts.append(new_account)
        print(f"Added account for {account_holder_name} with account number {account_number}.")

    def check_balance(self, account_number):
        """Check the balance of a specific account."""
        for account in self.accounts:
            if account.account_number == account_number:
                return f"Balance for account {account_number}: ${account.get_balance():.2f}"
        return "Account not found."

    def deposit_money(self, account_number, amount):
        """Deposit money into a specific account."""
        for account in self.accounts:
            if account.account_number == account_number:
                return account.deposit(amount)
        return "Account not found."

    def withdraw_money(self, account_number, amount):
        """Withdraw money from a specific account."""
        for account in self.accounts:
            if account.account_number == account_number:
                return account.withdraw(amount)
        return "Account not found."

    def list_accounts(self):
        """List all accounts in the bank."""
        if not self.accounts:
            return "No accounts available in the bank."
        account_list = "Accounts:\n"
        for account in self.accounts:
            account_list += str(account) + "\n" + "-" * 20 + "\n"
        return account_list

#3.
class Account:
    """Class representing a bank account."""
    def __init__(self, account_number, account_holder_name, balance=0.0):
        self.account_number = account_number  
        self.account_holder_name = account_holder_name  
        self.balance = balance  

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}."
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}."
        else:
            return "Withdrawal amount must be positive and less than or equal to the balance."

    def get_balance(self):
        """Return the current balance."""
        return self.balance

    def __str__(self):
        """Return a string representation of the account."""
        return (f"Account Number: {self.account_number}\n"
                f"Account Holder: {self.account_holder_name}\n"
                f"Balance: ${self.balance:.2f}")


class Bank:
    """Class representing a bank that manages a list of accounts."""
    def __init__(self):
        self.accounts = []  

    def add_account(self, account_number, account_holder_name, initial_balance=0.0):
        """Add a new account to the bank."""
        new_account = Account(account_number, account_holder_name, initial_balance)
        self.accounts.append(new_account)
        print(f"Added account for {account_holder_name} with account number {account_number}.")

    def check_balance(self, account_number):
        """Check the balance of a specific account."""
        for account in self.accounts:
            if account.account_number == account_number:
                return f"Balance for account {account_number}: ${account.get_balance():.2f}"
        return "Account not found."

    def deposit_money(self, account_number, amount):
        """Deposit money into a specific account."""
        for account in self.accounts:
            if account.account_number == account_number:
                return account.deposit(amount)
        return "Account not found."

    def withdraw_money(self, account_number, amount):
        """Withdraw money from a specific account."""
        for account in self.accounts:
            if account.account_number == account_number:
                return account.withdraw(amount)
        return "Account not found."

    def list_accounts(self):
        """List all accounts in the bank."""
        if not self.accounts:
            return "No accounts available in the bank."
        account_list = "Accounts:\n"
        for account in self.accounts:
            account_list += str(account) + "\n" + "-" * 20 + "\n"
        return account_list


def main():
    bank = Bank()  

    while True:
        print("\nBanking CLI")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. List Accounts")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            account_number = input("Enter account number: ")
            account_holder_name = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance (default is 0.0): ") or 0.0)
            bank.add_account(account_number, account_holder_name, initial_balance)

        elif choice == "2":
            account_number = input("Enter account number to check balance: ")
            print(bank.check_balance(account_number))

        elif choice == "3":
            account_number = input("Enter account number to deposit money: ")
            amount = float(input("Enter amount to deposit: "))
            print(bank.deposit_money(account_number, amount))

        elif choice == "4":
            account_number = input("Enter account number to withdraw money: ")
            amount = float(input("Enter amount to withdraw: "))
            print(bank.withdraw_money(account_number, amount))

        elif choice == "5":
            print(bank.list_accounts())

        elif choice == "6":
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please choose a number between 1 and 6.")


if __name__ == "__main__":
    main()

# 4.
class Account:
    """Class representing a bank account."""
    def __init__(self, account_number, account_holder_name, balance=0.0):
        self.account_number = account_number  # Account number
        self.account_holder_name = account_holder_name  # Account holder's name
        self.balance = balance  # Initial balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}."
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}."
        elif amount > self.balance:
            return "Insufficient funds. Overdraft not allowed."
        else:
            return "Withdrawal amount must be positive."

    def transfer(self, amount, target_account):
        """Transfer money to another account."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            target_account.deposit(amount)
            return f"Transferred ${amount:.2f} to account {target_account.account_number}."
        elif amount > self.balance:
            return "Insufficient funds. Overdraft not allowed."
        else:
            return "Transfer amount must be positive."

    def get_balance(self):
        """Return the current balance."""
        return self.balance

    def __str__(self):
        """Return a string representation of the account."""
        return (f"Account Number: {self.account_number}\n"
                f"Account Holder: {self.account_holder_name}\n"
                f"Balance: ${self.balance:.2f}")


class Bank:
    """Class representing a bank that manages a list of accounts."""
    def __init__(self):
        self.accounts = []  # Initialize an empty list to hold accounts

    def add_account(self, account_number, account_holder_name, initial_balance=0.0):
        """Add a new account to the bank."""
        new_account = Account(account_number, account_holder_name, initial_balance)
        self.accounts.append(new_account)
        print(f"Added account for {account_holder_name} with account number {account_number}.")

    def find_account(self, account_number):
        """Find an account by its account number."""
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def check_balance(self, account_number):
        """Check the balance of a specific account."""
        account = self.find_account(account_number)
        if account:
            return f"Balance for account {account_number}: ${account.get_balance():.2f}"
        return "Account not found."

    def deposit_money(self, account_number, amount):
        """Deposit money into a specific account."""
        account = self.find_account(account_number)
        if account:
            return account.deposit(amount)
        return "Account not found."

    def withdraw_money(self, account_number, amount):
        """Withdraw money from a specific account."""
        account = self.find_account(account_number)
        if account:
            return account.withdraw(amount)
        return "Account not found."

    def transfer_money(self, from_account_number, to_account_number, amount):
        """Transfer money from one account to another."""
        from_account = self.find_account(from_account_number)
        to_account = self.find_account(to_account_number)
        if from_account and to_account:
            return from_account.transfer(amount, to_account)
        return "One or both accounts not found."

    def list_accounts(self):
        """List all accounts in the bank."""
        if not self.accounts:
            return "No accounts available in the bank."
        account_list = "Accounts:\n"
        for account in self.accounts:
            account_list += str(account) + "\n" + "-" * 20 + "\n"
        return account_list


def main():
    bank = Bank()  # Create a Bank object

    while True:
        print("\nBanking CLI")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. List Accounts")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            account_number = input("Enter account number: ")
            account_holder_name = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance (default is 0.0): ") or 0.0)
            bank.add_account(account_number, account_holder_name, initial_balance)

        elif choice == "2":
            account_number = input("Enter account number to check balance: ")
            print(bank.check_balance(account_number))

        elif choice == "3":
            account_number = input("Enter account number to deposit money: ")
            amount = float(input("Enter amount to deposit: "))
            print(bank.deposit_money(account_number, amount))

        elif choice == "4":
            account_number = input("Enter account number to withdraw money: ")
            amount = float(input("Enter amount to withdraw: "))
            print(bank.withdraw_money(account_number, amount))

        elif choice == "5":
            from_account_number = input("Enter your account number: ")
            to_account_number = input("Enter the target account number: ")
            amount = float(input("Enter amount to transfer: "))
            print(bank.transfer_money(from_account_number, to_account_number, amount))

        elif choice == "6":
            print(bank.list_accounts())

        elif choice == "7":
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please choose a number between 1 and 7.")


if __name__ == "__main__":
    main()
