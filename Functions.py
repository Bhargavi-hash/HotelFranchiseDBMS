import pymysql
import pymysql.cursors

from add import *
from Search import *

def addOptions(cur,con):
    print("Choose an item to add info!!")
    info=["Events","Order","Menu","Furniture","Staff","Raw_Materials"]
    
    for var in range(len(info)):
        print(var+1,". ",info[var],sep="")

    val = input("Enter your choice: ")

    if(val=='1'):
        Add_Events(cur,con)
    elif(val=='2'):
        Add_Order(cur,con)
    elif(val=='3'):
        Add_Menu(cur,con)
    elif(val=='4'):
        Add_Furniture(cur,con)
    elif(val=='5'):
        Add_Staff(cur,con)
    elif(val=='6'):
        Add_Raw_Materials(cur,con)
    else:
        print("Oops!! You Entered an invalid choice")
        print("Press enter to continue ....")
    return


def SearchOptions(cur,con):
    print("Choose an item to search info!!")
    info=["Orders","Offers","Menu","Furniture","Raw_Materials","Caterings","Owners"]
    
    for var in range(len(info)):
        print(var+1,". ",info[var],sep="")

    val = input("Enter your choice: ")

    if(val=='1'):
        Search_Order(cur,con)
    # elif(val=='2'):
    #     Search_Offer(cur,con)
    # elif(val=='3'):
    #     Search_Menu(cur,con)
    # elif(val=='4'):
    #     Search_Furniture(cur,con)
    # elif(val=='5'):
    #     Search_Raw_Materials(cur,con)
    # elif(val=='6'):
    #     Search_caterings(cur,con)
    # elif(val=='7'):
    #     Search_Owners(cur,con)
    else:
        print("Oops!! You Entered an invalid choice")
        print("Press enter to continue ....")
    return    