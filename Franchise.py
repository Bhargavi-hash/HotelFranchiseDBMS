import subprocess as sp
import pymysql
import pymysql.cursors
import sys
from colorama import Fore, Style
from simple_colors import *
from tabulate import tabulate
from os import system, name
from time import sleep


def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def viewTable(rows):

    a = []
    try:
        a.append(list(rows[0].keys()))
    except:
        print("\n-----------------\nEMPTY TABLE\n-----------------\n")   
        return
    for row in rows:
        b = []
        for k in row.keys():
            b.append(row[k])
        a.append(b)
    print(tabulate(a, tablefmt="psql", headers="firstrow"))
    print()
    return

def Display():
    clear()
    
    print(blue("--------------------------------------------------------------------------"))
    print(red("\t\t   Choose what you want to view", 'bold'))
    print(blue("--------------------------------------------------------------------------\n"))
    
    print(green("--> 1.  Hotel branches", 'bold'))
    print(green("--> 2.  Staff details", 'bold'))
    print(green("--> 3.  Customer details", 'bold'))
    print(green("--> 4.  Departments", 'bold'))
    print(green("--> 5.  Land lords", 'bold'))
    print(green("--> 6.  Menu", 'bold'))
    print(green("--> 7.  Discounts", 'bold'))
    print(green("--> 8.  Furniture present", 'bold'))
    print(green("--> 9.  Raw material source", 'bold'))
    
    print("\n\n")

    viewOption = input(magenta("Your choice(1 - 10) ? ", 'bold'))

    clear()

    if viewOption == '1':
        query = "SELECT * FROM Hotel;"
    elif viewOption == '2':
        clear()
        print(magenta("------------- Select one from below -------------\n", 'bold'))
        print(yellow("--> 1. Branch-1 Staff details"))
        print(yellow("--> 2. Branch-2 Staff details"))
        print(yellow("--> 3. Branch-3 Staff details"))
        print(yellow("--> 4. Branch-4 Staff details"))
        print(yellow("--> 5. Staff details of all branches\n"))

        staffOption = input(magenta("Your choice(1 - 5) ? ", 'bold'))

        if staffOption == '1':
            query = "SELECT * FROM Staff WHERE Branch_ID = 1;"
        elif staffOption == '2':
            query = "SELECT * FROM Staff WHERE Branch_ID = 2;"
        elif staffOption == '3':
            query = "SELECT * FROM Staff WHERE Branch_ID = 3;"
        elif staffOption == '4':
            query = "SELECT * FROM Staff WHERE Branch_ID = 4;"
        elif staffOption == '5':
            query = "SELECT * FROM Staff;"
        
        try:
            no_of_rows = cur.execute(query)
        except Exception as e:
            print(e)
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
            return

    elif viewOption == '3':
        clear()
        print(magenta("------------- Select one from below -------------\n", 'bold'))
        print(yellow("--> 1. Branch-1 Customer details"))
        print(yellow("--> 2. Branch-2 Customer details"))
        print(yellow("--> 3. Branch-3 Customer details"))
        print(yellow("--> 4. Branch-4 Customer details"))
        print(yellow("--> 5. Customer details of all branches\n"))

        customerOption = input(magenta("Your choice(1 - 5) ? ", 'bold'))

        if customerOption == '1':
            query = "SELECT * FROM Customer WHERE Branch_ID = 1;"
        elif customerOption == '2':
            query = "SELECT * FROM Customer WHERE Branch_ID = 2;"
        elif customerOption == '3':
            query = "SELECT * FROM Customer WHERE Branch_ID = 3;"
        elif customerOption == '4':
            query = "SELECT * FROM Customer WHERE Branch_ID = 4;"
        elif customerOption == '5':
            query = "SELECT * FROM Customer;"
        
        try:
            no_of_rows = cur.execute(query)
        except Exception as e:
            print(e)
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
            return


    elif viewOption == '4':
        query = "SELECT * FROM Department;"
    elif viewOption == '5':
        query = "SELECT * From Owners;"
    elif viewOption == '6':
        query = "SELECT * From Menu;"
    elif viewOption == '7':
        query = "SELECT * From Discount;"
    elif viewOption == '8':
        query = "SELECT * From Furniture;"
    elif viewOption == '9':
        query = "SELECT * From Raw_Materials;"

    try:
        no_of_rows = cur.execute(query)
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return

    rows = cur.fetchall()
    viewTable(rows)
    con.commit()

while(1):
    tmp = sp.call('clear', shell=True)
    username = input("Username: ")
    password = input("Password: ")

    try:
        con = pymysql.connect(host='localhost',
                              user=username,
                              password=password,
                              db='Franchise',
                              cursorclass=pymysql.cursors.DictCursor)
    except Exception as e:
        print(e)
        tmp = sp.call('clear', shell=True)
        print(red('Connection Failed:', 'bold'))
        print(Fore.RED + "Credentials entered are incorrect or user doesn't have access to database")
        tmp = input(Fore.GREEN + "Enter any key to CONTINUE > ")
        print(Style.RESET_ALL)
        continue

    with con:
        cur = con.cursor()
        exitflag = 0
        while(1):
            tmp = sp.call('clear', shell=True)
            # refreshDatabase()
            print(blue("----------- CHOOSE AN OPTION -----------\n", 'bold'))
            print(yellow("\t--> 1.Display Options", 'bold'))
            print(yellow("\t--> 2.Addition Options", 'bold'))
            print(yellow("\t--> 3.Deletion Options", 'bold'))
            print(yellow("\t--> 4.Modify Options", 'bold'))
            print(yellow("\t--> 5.Quit", 'bold'))
            
            inp = input(cyan("\nCHOICE ? ", 'bold'))
            
            if(inp == '1'):
                Display()
            # elif(inp == '2'):
            #     addOptions()
            # elif(inp == '3'):
            #     deleteOptions()
            # elif(inp == '4'):
            #     updateOptions()
            # elif(inp == '5'):
            #         exitflag = 1
            #         print("Bye")
            #         break
            
            print("Press enter to continue ... ")
            x=input()

    if exitflag == 1:
        break