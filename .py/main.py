"""

Presents a menu to the user and allows them to choose various functions of the WeCare system. (viewing products, buying products, restocking products and adding new products)

"""

# Importing operations.py and read.py files
import operations
import read
# Importing datetime to get real time date and time
import datetime 

print("\n\n\t\t\t\t\t   Welcome to WeCare!!!")

# Initializing continue_
continue_ = True

# Runs while continue_ is True
while continue_ == True:
    
    # Get products data from read.py
    products_list, line = read.read_file()

    # Calls menu() and stores its return value in user_choice.
    # According to that choice other functions are called.
    user_choice = operations.menu()
        
    if user_choice == 1:
        operations.display_products(line)
        
    if user_choice == 2:
        operations.selling_products(products_list, line)
        
    if user_choice == 3:
        operations.restock_products(products_list, line)

    if user_choice == 4:
        operations.adding_products(products_list, line)
        
    if user_choice == 5:
        print("\nThank you for using WeCare! See you again.")
        break   

    operations.seperator()

    # Asks the user if they want to continue running the program.
    # If 'y' yes then the while continue_ == True loop keeps on running otherwise, displays an exit message and ends the program.
    continue_choice = input("\nDo you want to continue? (y/n) ").lower()

    if continue_choice != 'y':
        print("\nThank you for using WeCare! See you again.")
        continue_ = False
