# Library Management System using Abstraction and Encapsulation

class Library:

    def __init__(self):
        self.Books = ['Cengage-Physics', 'IE Irodov', 'N Avasthi', 'RD Sharma', 'HC Verma']
    
    def ShowBooks(self):
        self.num = len(self.Books)
        print("We have", self.num, "books which are:")
        for book in self.Books:
            print(book)
    
    def borrowBook(self, n):
        self.bookNum=n-1
        print("Thanks for taking", self.Books[self.bookNum])
        del self.Books[self.bookNum]
    
    def returnBook(self,name):
        print("Thanks for returning", name)
        self.Books.append(name)

customer = Library()
ch=0
while(ch!=5):
    print("1. Show Available Books")
    print("2. Borrow a Book")
    print("3. Return a Book")
    print("4. Exit")
    ch=int(input())
    if(ch==1):
        customer.ShowBooks()
    elif(ch==2):
        customer.ShowBooks()
        print("Select a number from above mentioned books to borrow that book")
        num=int(input())
        customer.borrowBook(num)
    elif(ch==3):
        print("Enter name of book you are returning")
        name=input()
        customer.returnBook(name)
    elif(ch==4):
        exit()
