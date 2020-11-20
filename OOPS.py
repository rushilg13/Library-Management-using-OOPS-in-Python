# OOPS Concept in Python.

# This is for class Attributes
class SJT303:
    Name='Raj'
    Hobby='Art'
    CGPA=9.0  

    def CheckCGPA(self):
        CGPA=self.CGPA
        if(CGPA>=9.0):
            print("9-Pointer")

Student1=SJT303()
Student2=SJT303()
print(Student1.Name)
print(Student2.Name)
# Both Gives same output -> Raj  Raj
# Class Attrubutes consists of those attributes that have same details for all its objects, (here students)
# To change value of class attributes ->

SJT303.Name='Binod'
print(Student1.Name)
print(Student2.Name)
# Both Gives same output -> Binod  Binod






# This is for instance Attributes
class SJT503:
    numberOfStudents = 50
Stud1 = SJT503()
Stud2 = SJT503()
print(Stud1.numberOfStudents) # Prints 50
Stud1.name='Rajkumar' # Although there is no attribute name in class SJT503
print(Stud1.name) # Prints Rajkumar
# But
# print(Stud2.name)  # AttributeError: 'SJT503' object has no attribute 'name'
# Now we will change NumberOfStudents for both Stud1 and Stud2
Stud1.numberOfStudents=40
print(Stud1.numberOfStudents) # Prints 40
print(Stud2.numberOfStudents) # Prints 50






# About Self Parameter
class ClassName:
    def test(self):
        print("This is func test")
        self.age=12
        print("Age is: ", self.age)
        dept='CSE'
        print("Dept is: ", dept)

    def trial(self):
        print("This is Trial Func")
        print("Age is (again): ", self.age)
        print("Dept is (again): ", dept)



name=ClassName()
name.test()
"""This is func test
Age is:  12
Dept is:  CSE"""
name.trial()  # NameError: name 'dept' is not defined

# This is because, Self keyword allows use of attribute throughout the lifetime of object but
# Here, We created self.age which was accessible in all methods but dept was not thus it was not usable in trial method





class Org:
    def orgName(self):
        self.name='Austin Park'
    
    @staticmethod
    def Welcome():
        print("Welcome to our Organization")

test1=Org()
test1.orgName()
print(test1.name) # Austin Park
test1.Welcome() # Welcome() takes 0 positional arguments but 1 was given

# But our method Welcome does not need self parameter because it has a simple greeting print message
# Thus we use static method
# Static method is used for those methods where we do not need the parameter
# We use @staticmethod for it. Check code.
# Output NOW ->
# Austin Park   Welcome to our Organization






# All about __init__
class Beach:
    def __init__(self, name):    # Initializes the attribute for all the methods
        self.name=name

    def BeachName(self):
        print("Name of beach is:", self.name)

test1=Beach("Marina Beach")
test1.BeachName()





# Library Management System using Abstraction and Encapsulation

class Library:

    def __init__(self):
        self.Books = ['Cengage-Physics', 'IE Irodov', 'N Avasthi', 'RD Sharma']
    
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







# Single inheritence
class Classroom:
    floor=5
    strength=60
    size='1200 sq ft'

    def since(self):
        print("Classroom Since {} with current strength of {} and size {} {}".format(2000, self.strength, self.size, self.capacity))
    
class Bench(Classroom):
    capacity=3

    def Details(self):
        print("This Bench is at {} floor and have a capacity of {}".format(self.floor, self.capacity))

test=Bench()
test.Details()
test.since()







# MultiClass Inheritance
class Bench:
    capacity=4

class Student:
    number=60

class School(Bench, Student):
    num_bench=15
    name="Pride School"
    def __init__(self):
        print("In {} there are {} students. There are {} benches and each have a capacity of {}".format(self.name, self.number, self.num_bench, self.capacity))

test = School()






# MultiLevel Inheritance
class Phones:
    style="Portable"

class Touch(Phones):
    size="5.5 inches"

class Samsung(Touch):
    brand="Samsung"
    def __init__(self):
        print("{} Phones are {} and {} in size".format(self.brand, self.style, self.size))

phone = Samsung()







# Access Specifiers - Public, Protected, Private
# For public -> memberName
# For Protected -> _memberName   # The '_' in the start
# For Private -> __memberName    # The '__' in the start

class Cricket:
    ThisIsPublic = "Public Text"
    _ThisIsProtected = "Protected Text"
    __ThisIsPrivate = "Private Text"

class ODI(Cricket):
    def __init__(self):
        print("Access Public: ",self.ThisIsPublic)          # Public attribute can be accessed by any class
        print("Access Protected: ",self._ThisIsProtected)   # Protected attribute can be accessed by derived class 
        # print("Access Private: ",self.__ThisIsPrivate)    # Error as Private attribute cannot be accessed outside base class

odi=ODI()   # Access Public:  Public Text   Access Protected:  Protected Text
cricket = Cricket()
print(cricket.ThisIsPublic)  # Public Text

# print(cricket.__ThisIsPrivate)  # Error
# To overcome the accessing of private attribute error, we need to know how private attributes are saved internally
# We do it by Name Wangling
# the way its saved is -> _ClassName__AttributeName
# So in our case it will be, _Cricket__ThisIsPrivate
print(cricket._Cricket__ThisIsPrivate)









# Overriding
class Colour:
    def define(self):
        self.Colour1="Red"

    def disp(self):
        print("The Colour is:", self.Colour1)

class rang(Colour):
    def define(self):
        self.Colour1="Black"

    def reset(self):
        super().define()    # super() method gives access back to parent/base class ie Resets

colour=Colour()
colour.define()
colour.disp()

colours=rang()
colours.define()
colours.disp()

colours.reset()
colours.disp()

"""The Colour is: Red
   The Colour is: Black
   The Colour is: Red"""






# Diamond Inheritance
class A:
    def of(self):
        print("This Belongs to Class A")

class B(A):
    def of(self):
        print("This Belongs to Class B")

class C(A):
    def of(self):
        print("This Belongs to Class C")

class D(B,C):
    pass

c = C()
c.of() # CASE of Overridding.       Output -> This Belongs to Class C

d = D()
d.of() # This Belongs to Class B
# Method Resolution Order - in class D, we inherit class B and then Class C (Check order in D(B,c)) 
# thus method overriding happens in B and not C
# Incase we do class D(C,B) and run same code, we get -> This Belongs to Class C




  

# Overloading
class Square:
    def __init__(self,side):
        self.side=side
    
    def __add__(SquareOne,SquareTwo):             # We overloaded '+' operator, which is defined as __add__ in py
        return (SquareOne.side*4 + SquareTwo.side*4)

SquareOne=Square(5)  # 4*5=20
SquareTwo=Square(10) # 4*10=40
print(SquareOne+SquareTwo) # 60 (40+20)             # We can overload any operator we want in py we want to just need hoe its defined in py









# Abstract Classes
from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta):   # Abstract classes are base classes which contain abstract methods that should be implemented in its base class
    @abstractmethod
    def area(self):
        return 0

class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        print("Area of square is", self.side**2)

class Rectangle(Shape):
    def __init__(self,len, wid):
        self.len=len
        self.wid=wid
    def area(self):
        print("Area of Rectangle is", self.len*self.wid)

square=Square(4)
square.area()

rectangle=Rectangle(2,3)
rectangle.area()

#Area of square is 16   Area of Rectangle is 6













# Banking System Using OOPS Concepts
import random
class Table:
    Account_Numbers_list=[23001, 45002]
    Account_Name_list=[['Austin',1000], ['Matthew',2000]]
    Account_zip=zip(Account_Numbers_list,Account_Name_list)
    Account_zip=dict(Account_zip)
    Account_Name_list=Account_Name_list
    Account_Numbers_list=Account_Numbers_list


class new(Table):

    def User_name(self):
        print("Enter Your Full Name:")
        name=str(input())
        self.name=name
        self.Account_Name_list.append(self.name)
    def ini_depo(self):
        print("Enter your Initial Deposit:")
        depo=int(input())
        self.depo=depo
    def newAccno(self):
        acc_no=random.randint(10000,99999)
        self.acc_no=acc_no
        print("Your new Account Number is:", acc_no)
        self.Account_Numbers_list.append(self.acc_no)
        newEntry={acc_no:[self.name, self.depo]}
        self.Account_zip |= newEntry
        print(dict(self.Account_zip))


class exist(new):
    def User_name(self):
        print("Enter Your Full Name:")
        name=str(input())
        self.name=name
    def Accno(self):
        print("Enter your Account Number")
        acc_no=int(input())
        self.acc_no=acc_no
    def validate(self):
        if(self.acc_no in self.Account_zip and self.Account_zip.get(self.acc_no)[0]==self.name):
            print("Valid User!")
            print("1. Do you want to Deposit?\n2. Do you want to Withdraw?")
            z=int(input())
            if(z==2):
                print("Enter Amount to Withdraw:")
                amt=int(input())
                if(amt>self.Account_zip.get(self.acc_no)[1]):
                    print("Insufficient Balance")
                else:
                    self.Account_zip.get(self.acc_no)[1]=self.Account_zip.get(self.acc_no)[1]-amt
                    print("You have withdrawn $", amt)
                    print("Total Amount in Account now is: $", self.Account_zip.get(self.acc_no)[1])
            elif(z==1):
                print("Enter Amount to Deposit:")
                amt=int(input())
                self.Account_zip.get(self.acc_no)[1]=self.Account_zip.get(self.acc_no)[1]+amt
                print("You have deposited $", amt)
                print("Total amount in account now is: $", self.Account_zip.get(self.acc_no)[1])
        else:
            print(self.Account_zip)
          


ch=0
while(ch!=100):
    print("1. Create new savings Account\n2. Access existing savings Account\n3. Exit")
    ch=int(input())
    if(ch==1):
        newUser=new()
        newUser.User_name()
        newUser.ini_depo()
        newUser.newAccno()
    elif(ch==2):
        olduser=exist()
        olduser.User_name()
        olduser.Accno()
        olduser.validate()
    elif(ch==3):
        exit()
