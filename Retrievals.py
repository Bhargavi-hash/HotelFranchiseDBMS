import pymysql
import pymysql.cursors
from ViewTable import *


def Selection(cur, con):
    try:
        print("Choose an Option to get data")
        choices = ["Menu", "Staff", "Furniture"]

        for var in range(len(choices)):
            print(var+1, ". ", choices[var], sep="")

        val = int(input("Enter your choice: "))

        if(val == 1):
            Food_Type = input("Enter Food-Type: ")
            query = "SELECT * FROM Menu WHERE Food_Type='%s'" % (Food_Type)
            cur.execute(query)
            rows = cur.fetchall()
            viewTable(rows)

        elif(val == 2):
            Dept = input("Enter Department: ")
            Branch_ID = int(input("Enter Branch-ID: "))
            Name = (input("Enter Name: ")).split(" ")
            Name.append(" ")
            Name.append(" ")

            query = "SELECT * FROM Staff WHERE Department_Name='%s' AND Branch_ID='%d' AND First_Name='%s' AND Last_Name='%s'" % (
                Dept, Branch_ID, Name[0], Name[1])
            cur.execute(query)
            rows = cur.fetchall()
            viewTable(rows)

        elif(val == 3):
            Branch_ID = int(input("Enter Branch-ID: "))
            Furniture_Type = input("Enter Furniture Name: ")

            query = "SELECT * FROM Furniture WHERE Furniture_Name='%s' AND Branch_ID='%d'" % (
                Furniture_Type, Branch_ID)
            cur.execute(query)
            rows = cur.fetchall()
            viewTable(rows)
        else:
            print(yellow("Oops!! You Entered an invalid choice"))

    except Exception as e:
        print(e)
        print(red("Try with different data"))
        return

    print(green("Sucessfull Retrieval!!", 'bold'))
    return


def Projection(cur, con):
    try:
        print("Choose an Option to get data")
        choices = ["Owners", "Menu", "Raw-Material", "Staff"]

        for var in range(len(choices)):
            print(var+1, ". ", choices[var], sep="")

        val = int(input("Enter your choice: "))

        if(val == 1):

            Rent = int(input("Enter Monthly-rent: "))
            options = ["greater than ", "less than ", "equal to"]
            print("Do you want rent values ")
            for var in range(len(options)):
                print(var+1, ". ", options[var], sep="")

            option = int(input("Enter your choice: "))

            if(option == 1):
                query = "SELECT First_Name,Last_Name FROM Owners WHERE Monthly_Rent > ('%d')" % (
                    Rent)
                cur.execute(query)
                rows = cur.fetchall()
                viewTable(rows)
            elif(option == 2):
                query = "SELECT First_Name,Last_Name FROM Owners WHERE Monthly_Rent < ('%d')" % (
                    Rent)
                cur.execute(query)
                rows = cur.fetchall()
                viewTable(rows)
            elif(option == 3):
                query = "SELECT First_Name,Last_Name FROM Owners WHERE Monthly_Rent = ('%d')" % (
                    Rent)
                cur.execute(query)
                rows = cur.fetchall()
                viewTable(rows)
            else:
                print(yellow("Oops!! You Entered an invalid choice"))
                return

        elif(val == 2):

            Cost = int(input("Enter Cost of Food-Item: "))
            options = ["greater than ", "less than ", "equal to"]
            print("Do you want Cost of item value ")
            for var in range(len(options)):
                print(var+1, ". ", options[var], sep="")

            option = int(input("Enter your choice: "))

            if(option == 1):
                query = "SELECT Food_Item FROM Menu WHERE Item_Cost > ('%d')" % (
                    Cost)
                cur.execute(query)
                rows = cur.fetchall()
                viewTable(rows)
            elif(option == 2):
                query = "SELECT Food_Item FROM Menu WHERE Item_Cost < ('%d')" % (
                    Cost)
                cur.execute(query)
                rows = cur.fetchall()
                viewTable(rows)
            elif(option == 3):
                query = "SELECT Food_Item FROM Menu WHERE Item_Cost = ('%d')" % (
                    Cost)
                cur.execute(query)
                rows = cur.fetchall()
                viewTable(rows)
            else:
                print(yellow("Oops!! You Entered an invalid choice"))

        elif(val == 3):

            Branch_ID = int(input("Enter Branch-ID: "))
            Quantity = float(input("Enter Quantity: "))
            Raw = input("Choose a raw material type: ")
            choices = ["Poultry", "Vegetable_Shop", "Dairy"]

            for var in range(len(choices)):
                print(var+1, ". ", choices[var], sep="")

            val = int(input("Enter your choice: "))

            if(not(val > 0 and val < 4)):
                print("Invalid choice")
                return

            options = ["greater than ", "less than ", "equal to"]
            print("Do you want Quantity value ")

            for var in range(len(options)):
                print(var+1, ". ", options[var], sep="")

            option = int(input("Enter your choice: "))

            if(option == 1):
                query = "SELECT Day,month,year FROM (%s) WHERE Quantity > ('%f')" % (
                    choices[val-1], Quantity)
                cur.execute(query)
                rows = cur.fetchall()
                viewTable(rows)
            elif(option == 2):
                query = "SELECT Day,month,year FROM (%s) WHERE Quantity < ('%f')" % (
                    choices[val-1], Quantity)
                cur.execute(query)
                rows = cur.fetchall()
                viewTable(rows)
            elif(option == 3):
                query = "SELECT Day,month,year FROM (%s) WHERE Quantity = ('%f')" % (
                    choices[val-1], Quantity)
                cur.execute(query)
                rows = cur.fetchall()
                viewTable(rows)
            else:
                print(yellow("Oops!! You Entered an invalid choice"))

        elif(val == 4):

            age = int(input("Enter age: "))
            options = ["greater than ", "less than ", "equal to"]
            print("What comparision of age do you want? ")
            for var in range(len(options)):
                print(var+1, ". ", options[var], sep="")

            option = int(input("Enter your choice: "))

            if(option == 1):
                query = "SELECT Staff_ID,First_Name,Last_Name FROM Staff WHERE i_dunno_age > ('%d')" % (
                    age)
                cur.execute(query)
                rows = cur.fetchall()
                viewTable(rows)

            elif(option == 2):
                query = "SELECT Staff_ID,First_Name,Last_Name FROM Staff WHERE i_dunno_age > ('%d')" % (
                    age)
                cur.execute(query)
                rows = cur.fetchall()
                viewTable(rows)

            elif(option == 3):
                query = "SELECT Staff_ID,First_Name,Last_Name FROM Staff WHERE i_dunno_age > ('%d')" % (
                    age)
                cur.execute(query)
                rows = cur.fetchall()
                viewTable(rows)
            else:
                print(yellow("Oops!! You Entered an invalid choice"))

        else:
            print(yellow("Oops!! You Entered an invalid choice"))
            return

    except Exception as e:
        print(e)
        print(red("Try with different data"))
        return

    print(green("Sucessfull Retrieval!!", 'bold'))
    return


def Aggregate(cur, con):
    try:
        print("Choose an Option to get data")
        choices = ["Owners", "Staff"]

        for var in range(len(choices)):
            print(var+1, ". ", choices[var], sep="")

        val = int(input("Enter your choice: "))

        if(val == 1):
            options = ["Maximum", "Miniumum", "Average"]
            print("What value of rent do you want? ")
            for var in range(len(options)):
                print(var+1, ". ", options[var], sep="")

            option = int(input("Enter your choice: "))

            if(option == 1):
                query = "SELECT MAX(Monthly_Rent) AS Max_Rent FROM Owners"
                cur.execute(query)
                rows = cur.fetchall()
                viewTable(rows)

            elif(option == 2):
                query = "SELECT MIN(Monthly_Rent) AS Min_Rent FROM Owners"
                cur.execute(query)
                rows = cur.fetchall()
                viewTable(rows)

            elif(option == 3):
                query = "SELECT AVG(Monthly_Rent) AS Avg_Rent FROM Owners"
                cur.execute(query)
                rows = cur.fetchall()
                viewTable(rows)
            else:
                print(yellow("Oops!! You Entered an invalid choice"))
                return

        elif(val == 2):
            Dept = input("Enter Department: ")
            Branch_ID = int(input("Enter Branch-ID: "))
            options = ["Maximum", "Miniumum", "Average"]
            print("What value of salary do you want? ")
            for var in range(len(options)):
                print(var+1, ". ", options[var], sep="")

            option = int(input("Enter your choice: "))

            if(option == 1):
                query = "SELECT MAX(Salary) AS Max_Salary FROM Staff WHERE Department_Name='%s' AND Branch_ID='%d'" % (
                    Dept, Branch_ID)
                cur.execute(query)
                rows = cur.fetchall()
                viewTable(rows)

            elif(option == 2):
                query = "SELECT MIN(Salary) AS Min_Salary FROM Staff WHERE Department_Name='%s' AND Branch_ID='%d'" % (
                    Dept, Branch_ID)
                cur.execute(query)
                rows = cur.fetchall()
                viewTable(rows)

            elif(option == 3):
                query = "SELECT AVG(Salary) AS Avg_Salary FROM Staff WHERE Department_Name='%s' AND Branch_ID='%d'" % (
                    Dept, Branch_ID)
                cur.execute(query)
                rows = cur.fetchall()
                viewTable(rows)
            else:
                print(yellow("Oops!! You Entered an invalid choice"))
                return

        else:
            print(yellow("Oops!! You Entered an invalid choice"))
            return

    except Exception as e:
        print(e)
        print(red("Try with different data"))
        return

    print(green("Sucessfull Retrieval!!", 'bold'))
    return



def Search(cur, con):
    try:
        print("Choose an Option to get data")
        choices = ["Owners", "Staff"]

        for var in range(len(choices)):
            print(var+1, ". ", choices[var], sep="")

        val = int(input("Enter your choice: "))

        if(val == 1):
            Name=input("Enter part of Owner Name to be matched")                    
            query = "SELECT * FROM Owners WHERE FirstName LIKE CONCAT('%','%s','%') OR Last_Name LIKE CONCAT('%','%s','%')" % (Name,Name)
            cur.execute(query)
            rows = cur.fetchall()
            viewTable(rows)


        elif(val == 2):
            No=9999999999                  
            No=input("Enter part of Staff Mobile Number to be matched")                    
            query = "SELECT * FROM Staff_Mobile_Number WHERE Phone_Number LIKE CONCAT('%','%d','%')" % (No)
            cur.execute(query)
            rows = cur.fetchall()
            viewTable(rows)            

        else:
            print(yellow("Oops!! You Entered an invalid choice"))
            return

    except Exception as e:
        print(e)
        print(red("Try with different data"))
        return

    print(green("Sucessfull Retrieval!!",'bold'))
    return


def Analysis(cur, con):
    try:
        print("Choose an Option to get data")
        choices = ["Owners", "Menu", "Order"]

        for var in range(len(choices)):
            print(var+1, ". ", choices[var], sep="")

        val = int(input("Enter your choice: "))

        if(val == 1):
            print("")
    except Exception as e:
        print(e)
        print(red("Try with different data"))
        return

    print(green("Sucessfull Retrieval!!", 'bold'))
    return
