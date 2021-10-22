import pymysql
import pymysql.cursors
from ViewTable import *


def Search_Order(cur, con):
    print("Choose one of the following options to get order information")
    choices = ["Customer-ID", "Food-Item", "Branch-ID"]

    for var in range(len(choices)):
        print(var+1, ". ", choices[var], sep="")

    val = input("Enter your choice:")

    try:
        if(val == '1'):
            Customer_ID=int(input("Enter Customer-ID: "))
            query = "SELECT Table_ID,Branch_ID FROM Customer WHERE Customer_ID='%d'" % (Customer_ID)
            cur.execute(query)
            x=cur.fetchone()
            print("Details of Customer with ID:",Customer_ID)
            print("Table-ID:",x["Table_ID"])
            print("Branch-ID:",x["Branch_ID"])

            query="SELECT Food_Item_ID,Quantity FROM _Order WHERE Customer_ID='%d'" % (Customer_ID)            
            cur.execute(query)
            rows=cur.fetchall()
            print("Food Item Ordered and Quantity: ")
            for row in rows:
                Food_ID=row["Food_Item_ID"]
                query="SELECT Food_Item FROM Menu WHERE Food_Item_ID='%d'" % (Food_ID)
                cur.execute(query)
                x=cur.fetchone()
                print(x["Food_Item"],row["Quantity"])

        # elif(val == '2'):
        #     Food_Item=input("Enter Food-Item Name: ")
            
        #     query = "SELECT Food_Item_ID FROM _Order WHERE Food_Item_ID='%d'" % (
        #         2)
        # elif(val == '3'):
        #     query = "SELECT Food_Item_ID FROM _Order WHERE Customer_ID='%d'" % (
        #         2)
        # else:
        #     print(yellow("Oops!! You Entered an invalid choice"))
        # cur.execute(query)
        # rows = cur.fetchall()
        # viewTable(rows)

    except Exception as e:
        print(e)
