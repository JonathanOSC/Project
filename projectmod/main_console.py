



from sale_subsystem import SaleFacade


SALES = SaleFacade()
MENU_OPTIONS = """
    0. Login 
    1. Create Sale
    2. Print Sale Check
    3. View Sales History 
    4. View inventory
    5. View tables
    6. Exit
"""

def login():
    username = input("Username: ")
    password = input("Password: ")
    if username == "admin" and password == "admin":
        print(f"Welcome {username}")    
        return username, password
    else:
        raise ValueError("Invalid credentials")
    
def main():
    """ This function is the main function of the program """
    user = None
    print(MENU_OPTIONS)
    
    while True:
        
        option = int(input("Select an option: "))
        
        if option == 0:
            print("================Login================")
            login()
        elif option == 1:
            print("================Create Sale================")
            product_id = int(input("Enter the product id: "))
            quantity = int(input("Enter the quantity: "))
            SALES.create_sale(product_id, quantity)
        elif option == 2:
            print("================Printing Sale Check================")
            SALES.print_sale_check()
        elif option == 3:
            print("================View Sales History================")
            SALES.view_sales_history()
        elif option == 4:
            print("================View Inventory================")
            SALES.view_inventory()
        elif option == 5:
            print("================View Tables================")
            SALES.view_tables()
        elif option == 6:
            print("================Exiting the system================")
            break
        else:
            print("Invalid option")
            
        print("\n"+ MENU_OPTIONS) + "\n\n" 
    
    
main()