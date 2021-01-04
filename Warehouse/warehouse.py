#imports
from menu import print_menu, print_header, clear, print_line, print_product
from homework import calculate_age, calculate_tip
from product import Product

#global vars
catalog = []
next_id = 1



#functions





def register_product():
    global next_id
    try:
        # title, category, stock, price
        print_header(" Register a new Product")
        title = input("Please provide the Title ")
        category = input("Please provide the Category: ")
        stock = int(input("Please provide the Stock: "))
        price = float(input("Please provide the Price: "))

        # create object
        the_product = Product(next_id, title, category, stock, price)
        next_id = next_id +1
        



        #add obj to a list
        catalog.append(the_product)

        print_line()
        print("** Product Registered!!")

    except:
        print_line()
        print("** Error: verify values and try again!")


def print_catalog():
    print_header(" Current Catalog ")

    for prod in catalog: 
        print_product(prod)


def out_of_stock():
    print_header("Currently Out of Stock")

    for prod in catalog:
        if(prod.stock == 0):
            print_product(prod)


def total_stock():
    print_header(" Total Stock Value ")
    total=0

    for prod in catalog:
        total = total + (prod.stock * prod.price)

    print(total)


def cheapest_product():
    print_header("Cheapest price")

    prices = []
    for prod in catalog:
        prices.append(prod.price)

    cheapest = min(prices)
    print ("The cheapest is " + str(cheapest))

def cheapest_product_adv():
    print_header(" Cheapest price advance")

    if(len(catalog) < 1):
        print("** Error, empty catalog. Register prods first.")
        return

    cheapest = catalog[0]
    #check if prod is cheaper than cheapest, if it is, then prod is my new cheapest
    for prod in catalog:
        if(prod.price < cheapest.price):
            cheapest = prod
    
    print_product(cheapest)

    """
    1- show the catalog to the user
    2- ask the user to choose an id
    2.5- create flag (found=False)
    3- travel the list
    4- if the prod id is equal to the id provided by the user
    5- if it is , then remove that product
    



    """


def delete_product():
    print_header(" Delete a product")

    print_catalog()
    
    id = input("Choose an id:")

    found = False

    for prod in catalog:
        if(str(prod.id) == id):
            found = True
            catalog.remove(prod)

    if(found):
        print("** Product removed!")
    else:
        print(" ** Error: Invalid ID")

def update_price():
    print_header(" Update product price")

    print_catalog()
    
    id = input("Choose an id:")

    found = False
    for prod in catalog:
        if(str(prod.id) == id):
            found = True
            newPrice= float(input("What is the new price? "))
            prod.price = newPrice

        # parse the price to a float
        # set the price in the object (prod.price = price)

    if(found):
        print("** Product price updated!")
    else:
        print(" ** Error: Invalid ID")

def update_stock():
    print_header("Update product stock")

    print_catalog()

    id = input("Choose and id to update: ")
    found = False
    for prod in catalog:
        if(str(prod.id) == id):
            found=True

            newStock= int(input("What is the new stock? "))
            prod.stock = newStock


    if(found):
        print("** Product stock updated!")
    else:
        print("** Error: Invalid ID")



    
        
    


    

    







#instructions

opc = ''
while(opc != 'x'):
    clear()
    print_menu()
    opc = input("PLease choose an option: ")

    if(opc == '1'):
        register_product()

    elif(opc == '2'):
        print_catalog()

    elif(opc == '3'):
        out_of_stock()

    elif(opc == '4'):
        total_stock()

    elif(opc == '5'):
        cheapest_product_adv()

    elif(opc == '6'):
        delete_product()

    elif(opc == '7'):
        update_price()

    elif(opc == '8'):
        update_stock()


    

    elif(opc =='a'):
        calculate_age()
    elif(opc =='b'):
        calculate_tip()

    input("Press Enter to continue...")



print("Good bye!!")
