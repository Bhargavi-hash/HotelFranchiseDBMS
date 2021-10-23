import pymysql
import pymysql.cursors
from ViewTable import *


def Search_Order(cur, con):
    print("Choose one of the following options to get order information")
    choices = ["Customer-ID", "Food-Item", "Branch-ID"]

    for var in range(len(choices)):
        print(var+1, ". ", choices[var], sep="")

    val = int(input("Enter your choice:"))

    try:
        if(val == 1):

            Customer_ID=int(input("Enter Customer-ID: "))
            query = "SELECT Table_ID,Branch_ID FROM Customer WHERE Customer_ID='%d'" % (Customer_ID)
            cur.execute(query)
            x=cur.fetchone()

            if(not(bool(x))):
                print("You entered an invalid Customer-ID")
                con.rollback()
                return

            print("Details of Customer with ID:",Customer_ID)
            print("Table-ID:",x["Table_ID"])
            print("Branch-ID:",x["Branch_ID"])

            query="SELECT Food_Item_ID,Quantity FROM _Order WHERE Customer_ID='%d'" % (Customer_ID)            
            cur.execute(query)
            rows=cur.fetchall()
            if(len(rows)):
                print(magenta("\nFood Item Ordered and Quantity: "))
            else:
                print(magenta("No orders by the Customer"))
                return 

            for row in rows:
                Food_ID=int(row["Food_Item_ID"])
                query="SELECT Food_Item FROM Menu WHERE Food_Item_ID='%d'" % (Food_ID)
                cur.execute(query)
                x=cur.fetchone()
                print("Food-Item:",x["Food_Item"])
                print("Quantity:",row["Quantity"])

        elif(val == 2):

            Food_Item=input("Enter Food-Item Name: ")
            query="SELECT Food_Item_ID,Food_Type,Item_Cost FROM Menu WHERE Food_Item='%s'" % (Food_Item)
            cur.execute(query)
            x=cur.fetchone()

            if(not(bool(x))):
                print("You entered an invalid food item name")
                con.rollback()
                return

            print("\nInformation of Food-Item:",Food_Item)
            print("Food-Type:",x["Food_Type"])
            print("Item cost:",x["Item_Cost"])

            query="SELECT Customer_ID,Quantity FROM _Order WHERE Food_Item_ID='%d'" % (int(x["Food_Item_ID"]))            
            cur.execute(query)
            rows=cur.fetchall()
            if(len(rows)):
               print(magenta("Current orders by Customers and quantity:"))
            else:
                print(magenta("No orders on this item currently available"))
                return   
            
            for row in rows:      
                print("Customer-ID:",row["Customer_ID"])
                print("Quantity:",row["Quantity"])
                
        elif(val == 3):

            Branch_ID=int(input("Enter the Branch-ID to get information: "))                       
            query = "SELECT Food_Item_ID,Customer_ID FROM _Orders WHERE Branch_ID='%d'" % (Branch_ID)
            
            if not(Branch_ID > 0 and Branch_ID < 6):
                print("You entered a Invalid Branch-ID")
                return

            cur.execute(query)
            rows=cur.fetchall()

            if(len(rows)):
               print(magenta("Current orders by Customers and quantity: "))
            else:
                print(magenta("No orders on this item currently available"))
                return   
            
            for row in rows:      
                Food_ID=int(row["Food_Item_ID"])
                query="SELECT Food_Item FROM Menu WHERE Food_Item_ID='%d'" % (Food_ID)
                cur.execute(query)
                x=cur.fetchone()

                if(not(bool(x))):
                    continue

                print("Customer-ID:",row["Customer_ID"])
                print("Food-Item:",x["Food_Item"])
                
        else:
            print(yellow("Oops!! You Entered an invalid choice"))

        return

    except Exception as e:
        print(e)



def Search_Staff(cur,con):
    print("Choose one of the following options to get Offer information")
    choices = ["Customer-ID", "Food-Item"]

    for var in range(len(choices)):
        print(var+1, ". ", choices[var], sep="")

    val = int(input("Enter your choice:"))

    try:
        if(val == 1):
           print()
        elif(val==2):
            print()
        else:
            print(yellow("Oops!! You Entered an invalid choice"))

        return

    except Exception as e:
        print(e)


def Search_Menu(cur,con):
    print("Choose one of the following options to get Offer information")
    choices = ["Min-Cost", "Max-Cost","Food-Type"]

    for var in range(len(choices)):
        print(var+1, ". ", choices[var], sep="")

    val = int(input("Enter your choice:"))

    try:
        if(val == 1):
            Customer_ID=int(input("Enter Customer-ID: "))

           
        elif(val==2):
            print()
        else:
            print(yellow("Oops!! You Entered an invalid choice"))

        return

    except Exception as e:
        print(e)


def Search_Furniture(cur,con):
    print("Choose one of the following options to get Offer information")
    choices = ["", "Food-Item"]

    for var in range(len(choices)):
        print(var+1, ". ", choices[var], sep="")

    val = int(input("Enter your choice:"))

    try:
        if(val == 1):
           print()
        elif(val==2):
            print()
        else:
            print(yellow("Oops!! You Entered an invalid choice"))

        return

    except Exception as e:
        print(e)

def Search_Raw_Materials(cur,con):
    print("Choose one of the following options to get Offer information")
    choices = ["Customer-ID", "Food-Item"]

    for var in range(len(choices)):
        print(var+1, ". ", choices[var], sep="")

    val = int(input("Enter your choice:"))

    try:
        if(val == 1):
           print()
        elif(val==2):
            print()
        else:
            print(yellow("Oops!! You Entered an invalid choice"))

        return

    except Exception as e:
        print(e)


def Search_caterings(cur,con):
    print("Choose one of the following options to get Offer information")
    choices = ["Customer-ID", "Food-Item"]

    for var in range(len(choices)):
        print(var+1, ". ", choices[var], sep="")

    val = int(input("Enter your choice:"))

    try:
        if(val == 1):
           print()
        elif(val==2):
            print()
        else:
            print(yellow("Oops!! You Entered an invalid choice"))

        return

    except Exception as e:
        print(e)        


def Search_Owners(cur,con):
    print("Choose one of the following options to get Offer information")
    choices = ["Owners", "Rent"]

    for var in range(len(choices)):
        print(var+1, ". ", choices[var], sep="")

    val = int(input("Enter your choice:"))

    try:
        if(val == 1):
           print()
        elif(val==2):
            print()
        else:
            print(yellow("Oops!! You Entered an invalid choice"))

        return

    except Exception as e:
        print(e)        