import pymysql
import pymysql.cursors

from add import *
from Retrievals import *
from Clear import *
from datetime import date

def addOptions(cur, con):
    try:
        print("Choose an item to add info!!")
        info = ["Events", "Order", "Menu",
                "Furniture", "Staff", "Raw_Materials"]

        for var in range(len(info)):
            print(var+1, ". ", info[var], sep="")

        val = int(input("Enter your choice: "))

        if(val == 1):
            Add_Events(cur, con)
        elif(val == 2):
            Add_Order(cur, con)
        elif(val == 3):
            Add_Menu(cur, con)
        elif(val == 4):
            Add_Furniture(cur, con)
        elif(val == 5):
            Add_Staff(cur, con)
        elif(val == 6):
            Add_Raw_Materials(cur, con)
        else:
            print("Oops!! You Entered an invalid choice")
            print("Press enter to continue ....")
        return

    except Exception as e:
        print(e)
        print(red("Try again!!"), 'bold')
        return


def Retrievals(cur, con):
    try:
        clear()
        print("Choose a Query type to Search information!!")
        info = ["Select a row specific to some data", "Search by a particular attribute",
                "Get information from entire columns", "Search by text", "Analysis on order"]

        for var in range(len(info)):
            print(var+1, ". ", info[var], sep="")

        val = int(input("Enter your choice: "))
        clear()
        if(val == 1):
            Selection(cur, con)
        elif(val == 2):
            Projection(cur, con)
        elif(val == 3):
            Aggregate(cur, con)
        elif(val == 4):
            Search(cur, con)
        elif(val == 5):
            Analysis(cur, con)
        else:
            print("Oops!! You Entered an invalid choice")
        return

    except Exception as e:
        print(e)
        print(red("Try again!!"), 'bold')
        return

    
# *************************************** AGE *********************************************************
def AgeSearch(con, cur):
    clear()
    
    todays_date = date.today()

    age = int(input("Enter age: "))
    options = ["greater than ", "less than ", "equal to"]
    print("What comparision of age do you want? ")
    for var in range(len(options)):
        print(var+1, ". ", options[var], sep="")
    option = int(input("Enter your choice: "))

    # def calculateAge(birthDate):
    #     today = date.today()
    #     age = today.year - birthDate.year -
    #          ((today.month, today.day) <
    #          (birthDate.month, birthDate.day))
    #  
    #     return age

    today = date.today() 

    if(option == 1):
        query = "SELECT Staff_ID, First_Name, Last_Name FROM Staff WHERE (%d - Year_date - IF(%d < Month_date, 0, IF(%d < Day_date, 0, 1)))> %d;" % (today.year, today.month, today.day, age)
        cur.execute(query)
        rows = cur.fetchall()
        viewTable(rows)
    elif(option == 2):
        query = "SELECT Staff_ID, First_Name, Last_Name FROM Staff WHERE (%d - Year_date - IF(%d < Month_date, 0, IF(%d < Day_date, 0, 1)))< %d;" % (today.year, today.month, today.day, age)
            age)
        cur.execute(query)
        rows = cur.fetchall()
        viewTable(rows)
    elif(option == 3):
        query = "SELECT Staff_ID, First_Name, Last_Name FROM Staff WHERE (%d - Year_date - IF(%d < Month_date, 0, IF(%d < Day_date, 0, 1)))= %d;" % (today.year, today.month, today.day, age)
            comp_Year)
        cur.execute(query)
        rows = cur.fetchall()
        viewTable(rows)
    else:
        print(yellow("Oops!! You Entered an invalid choice"))



