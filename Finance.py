from Clear import *
from ViewTable import *

def Finance():
    clear()     # Clearing screen before displaying further options
    
    # Displaying options to choose

    print(blue("--------------------------------------------------------------------------", 'bold'))
    print(red("\t\t     Choose onr from below to analyze", 'bold'))
    print(blue("--------------------------------------------------------------------------\n", 'bold'))
    
    print(green("--> 1.  Average monthly rent paid by the Franchise", 'bold'))
    print(green("--> 2.  Average cost of starters in Menu", 'bold'))
    print(green("--> 3.  Average cost of soups in Menu", 'bold'))
    print(green("--> 4.  Average cost of Table dips in Menu", 'bold'))
    print(green("--> 5.  Average cost of Salads in Menu", 'bold'))
    print(green("--> 6.  Average cost of Desserts in Menu", 'bold'))
    print(green("--> 7.  Average cost of Main-course in Menu", 'bold'))
    print(green("--> 8.  Average cost of Chaat in Menu", 'bold'))


    print("\n\n")

    financeOption = input(cyan("Your choice(1-8)? "))

    clear()

    if financeOption == '1':
        print(green("----- Analysis of Average monthly rent paid -----", 'bold'))
        query = "Select AVG(Monthly_Rent) AS 'Average Rent' From Owners;"
    elif financeOption == '2':
        print(green("----- Average cost of starters in menu -----", 'bold'))
        query = "SELECT AVG(Item_Cost) AS 'Average rate of Starters' FROM Menu WHERE Food_Type = 'Veg Starters' OR 'Non-veg Starters';"
    elif financeOption == '3':
        print(green("----- Average cost of soup in menu -----", 'bold'))
        query = "SELECT AVG(Item_Cost) AS 'Average rate of Soups' FROM Menu WHERE Food_Type = 'Soup';"
    elif financeOption == '4':
        print(green("----- Average cost of Table dips in menu -----", 'bold'))
        query = "SELECT AVG(Item_Cost) AS 'Average rate of table dips' FROM Menu WHERE Food_Type = 'Table Dips';"
    elif financeOption == '5':
        print(green("----- Average cost of Salads in menu -----", 'bold'))
        query = "SELECT AVG(Item_Cost) AS 'Average rate of soups' FROM Menu WHERE Food_Type = 'Salads';"
    elif financeOption == '6':
        print(green("----- Average cost of Desserts in menu -----", 'bold'))
        query = "SELECT AVG(Item_Cost) AS 'Average rate of soups' FROM Menu WHERE Food_Type = 'Dessets';"
    elif financeOption == '7':
        print(green("----- Average cost of main-course in menu -----", 'bold'))
        query = "SELECT AVG(Item_Cost) AS 'Average rate of main-course' FROM Menu WHERE Food_Type = 'Non-veg Main Course' OR 'Veg Main Course';"
    elif financeOption == '8':
        print(green("----- Average cost of chaat in menu -----", 'bold'))
        query = "SELECT AVG(Item_Cost) AS 'Average rate of chaat' FROM Menu WHERE Food_Type = 'Chaat';"

    try:
        no_of_rows = cur.execute(query)
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN !\n")
        return

    rows = cur.fetchall()
    viewTable(rows)
    con.commit()



#******************************************** Program starts here ************************************************************

while(1):
    tmp = sp.call('clear', shell=True)
    username = input(green("Username: ", 'bold'))
    password = input(green("Password: ", 'bold'))

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
            print(yellow("\t--> 1.  Display Options", 'bold'))
            print(yellow("\t--> 2.  Addition Options", 'bold'))
            print(yellow("\t--> 3.  Deletion Options", 'bold'))
            print(yellow("\t--> 4.  Modify/Update Options", 'bold'))
            print(yellow("\t--> 5.  Search Options", 'bold'))
            print(yellow("\t--> 6.  Finance Analysis Options", 'bold'))
            print(yellow("\t--> 7.  Quit", 'bold'))
            
            inp = input(cyan("\nCHOICE ? ", 'bold'))
            
            if(inp == '1'):
                Display()
            # elif(inp == '2'):
            #     addOptions()
            # elif(inp == '3'):
            #     deleteOptions()
            elif(inp == '4'):
                Update()
            elif(inp == '5'):
                Search()
            elif(inp == '6'):
                Finance()
            #         exitflag = 1
            #         print("Bye")
            #         break
            
            print("Press enter to continue ... ")
            x=input()

    if exitflag == 1:
        break
