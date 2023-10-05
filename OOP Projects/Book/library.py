class Book:
    def __init__(self, id, name, quantity) -> None:
        self.id = id
        self.name = name
        self.quantity = quantity
    
class User:
    def __init__(self, id, name, password) -> None:
        self.id = id
        self.name = name
        self.password = password
        self.borrowedBooks = []
        self.returnedBooks = []

class Library:
    def __init__(self, name) -> None:
        self.name = name
        self.users = []
        self.books = []

    def addBook(self, id, name, quantity):
        book = Book(id, name, quantity)
        self.books.append(book)
        print(f'{book.name} added successfully!')
        
    def addUser(self, id, name, password):
        user = User(id, name, password)
        self.users.append(user)
        return user
    
    def borrowBook(self, user, token):
        for book in self.books:
            if book.name == token:
                if book in user.borrowedBooks:
                    print("Already Borrowed!\n")
                    return
                elif book.quantity == 0:
                    print("No copies available!\n")
                    return
                else:
                    user.borrowedBooks.append(book)
                    book.quantity -= 1
                    print("Borrowed book successfully!\n")
                    return
        print(f"Not found any book with name {token}!\n")
    
    def returnBook(self, user, token):
        for book in self.books:
            if book.name == token:
                if book in user.borrowedBooks:
                    book.quantity += 1
                    user.returnedBooks.append(book)
                    user.borrowedBooks.remove(book)
                    print("Returned book successfully!\n")
                    return
                elif book.quantity == 0:
                    print("No copies available!\n")
                    return
                else:
                    user.borrowedBooks.append(book)
                    book.quantity -= 1
                    return
        print(f"Not found any book with name {token}!\n")

bsk = Library('sonar bangla')
admin = bsk.addUser(1000, 'admin', 'admin')
alo = bsk.addUser(17, 'ala uddin', 'hello123')
cpBook = bsk.addBook(121, 'CP Book', 2)
pythonBook = bsk.addBook(131, 'Python', 3)
oopBook = bsk.addBook(141, 'C++', 5)

currentUser = admin

while True:
    try:
        if currentUser is None:
            print("No Logged in user\n")
            
            option = input("Login or Registration (L/R): ")
            if option == 'L':
                id = int(input('Enter Id: '))
                password = input("Enter password: ")
                match = False
                for user in bsk.users:
                    if user.id == id and user.password == password:
                        currentUser = user
                        match = True
                        break
                    
                if not match:
                    print("No user found!\n")
            elif option == 'R':
                id = int(input('Enter Id: '))
                name = input("Enter your Name: ")
                password = input("Enter password: ")
                
                for user in bsk.users: 
                    if user.id == id:
                        print("User already exists!\n")
                        break
                else:
                    user = bsk.addUser(id, name, password)
                    currentUser = user
        else:
            print(f'Welcome Back {currentUser.name}!\n')
            if currentUser.name == 'admin':
                print("Options: \n")
                print("1: Add Book")
                print("2: Add User")
                print("3: Show all Books")
                print("4: Logout")
                
                ch = int(input("Enter option: "))
                if ch == 1:
                    id = int(input('Enter id: '))
                    name = input("Enter your Book name: ")
                    quantity = int(input("Enter your book quantity: "))
                    
                    bsk.addBook(id, name, quantity)
                elif ch == 2:
                    id = int(input('Enter Id: '))
                    name = input("Enter your Name: ")
                    password = input("Enter password: ")
                    
                    bsk.addUser(id, name, password)
                elif ch == 3:
                    for book in bsk.books:
                        print(f'{book.id}\t{book.name}\t{book.quantity}')
                    print('\n')
                elif ch == 4:
                    currentUser = None
                else:
                    print("Invalid option!")
            else:
                print("Options: ")
                print("1: Borrow Book")
                print("2: Return Book")
                print("3: Show all Borrowed Books")
                print("4: Show all History")
                print("5: Logout")
                
                ch = int(input("Enter option: "))
                if ch == 1:
                    name = input("Enter your Book name: ")
                    bsk.borrowBook(currentUser, name)
                elif ch == 2:
                    name = input("Enter your Book name: ")
                    bsk.returnBook(currentUser, name)
                elif ch == 3:
                    print('Borrowed Books: \n')
                    for book in currentUser.borrowedBooks:
                        print(book)
                        print(f'{book.id}\t{book.name}\t{book.quantity}')
                    print('\n')
                elif ch == 4:
                    print('\nHistory\n')
                    for book in currentUser.returnedBooks:
                        print(f'{book.id}\t{book.name}\t{book.quantity}')
                    print('\n')
                elif ch == 5:
                    currentUser = None
                else:
                    print("Invalid option!")
                    
    except ValueError:
        print("Invalid input. Please enter a valid number.")
