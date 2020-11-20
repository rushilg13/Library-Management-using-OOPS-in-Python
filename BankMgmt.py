# Banking System Using OOPS Concepts
import random
class Table:
    Account_Numbers_list=[23001, 45002]
    Account_Name_list=[['Austin Moon',1000], ['Matthew George',2000]]
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
            print("Invalid Credentials")
    def display(self):
        print(self.Account_zip)
          


ch=0
while(ch!=100):
    print("1. Create new savings Account\n2. Access existing savings Account\n3. Show Existing Account Details\n4. Exit")
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
        user=exist()
        user.display()
    elif(ch==4):
        exit()