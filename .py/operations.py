# Importing datetime to get real time date and time
import datetime
# Importing write.py file
import write

continue_ = True

def seperator():
    """

    Prints dashes 98 times.
    A function used to display dashes to make the output look beautiful.

    Parameters:
        None

    Returns:
        None

    Example:
        >>>seperator()
        --------------------------------------------------------------------------------------------------

    """    
    print("-" * 98)

def menu():
    """

    Displays the main menu and validates user input for menu selection.
    
    Parameters:
        None
    
    Returns:
        int: User's validated menu choice (1-5)
    
    Raises:
        ValueError: If input cannot be converted to integer
        
    Example:
        >>> choice = menu()
        ----------------------------------
        What would you like to do?
        1. View Products       2. Buy Products
        3. Restock Products    4. Add New Products
        5. Exit
        ----------------------------------
        Enter a number (1-5): 2
        >>> print(choice)
        2
    
    """
    # Loop runs till continue_ is true
    while continue_ == True:
        seperator()
        print("\nWhat would you like to do?\n1. View Products\t\t2. Buy Products\n3. Restock Products\t\t4. Add New Products\n5. Exit")
        seperator()

        ''' Exception handling.
            Tries the try block. Only if the number entered is an integer number continues without error otherwise gives a ValueError exception.
            Check if choice is more than or equals to 1 and less than or equals to 4 otherwise, the else condition is displayed.'''
        try:
            choice = int(input("\nEnter a number (1-5): "))
            
            if 1 <= choice <= 5:
                return choice
            else:
                print("Invalid choice! Please enter a number from 1-5.")
        except ValueError:
            print("Enter a valid number. (Integer)")

def display_products(line):
    """

    A function that upon called displays the product details.

    Parameters:
        line(list of str): Product data lines from the file.

    Returns:
        None

    Raises:
        ValueError: If product price cannot be converted to float.
        Error: If product line is missing fields.

    Example:
        >>> display_products(["1  , Vitamin C Serum          , Garnier   ,   30ml ,   360 , 1000.0 , France       , 2025-04-15"])

    """
    # Making the output look beautiful by displaying it in a table format
    print("\n\n\t\t\t\t\t   PRODUCT DETAILS")
    print("\n " + "_" * 96)
    print("| ID | Name\t\t\t| Brand     | Volume | Stock | Price | Country\t    | Mfg. Date  |")
    print("|----|--------------------------|-----------|--------|-------|-------|--------------|------------|")

    ''' For each loop.
        Loop starts from line = 0 and goes on till the items inside the list.
        Takes each line and separates it according to ',' and stores it in the fields list.'''
    for i in line:
        try:
            fields = i.split(',')

            # Checks if the length of fields is greater than 5. There are 8 fields.
            if len(fields) > 5:
                ''' Sometimes there might be empty lines and error might occur.
                    So, to prevent that, exception handling is used.
                    Multiplies the cost price(the price in product.txt) by 2, converts the price into string and stores it in the respective fields.'''
                try:
                    price = float(fields[5]) * 2 
                    fields[5] = str(price) 
                    fields[5] = " " * (7 - len(fields[5])) + fields[5]
                    formatted_line = '|'.join(fields)
                    print("|", formatted_line, "|")
                except ValueError:
                    print("Skipping line due to invalid price format.")
        except:
            print("Error!!")

def selling_products(products_list, line):
    """
    A function used to sell products to the customers taking inputs like customer_name, product id and quantity.

    Parameters:
        products_list (list of dict): Product inventory.
        line (list of str): Product data lines from the file for display

    Returns:
        None

    Raises:
        ValueError: If user enters invalid product ID or quantity.
    Example:
        >>> selling_products(products_list, lines)
        Enter customer name: John Doe
        Enter product ID: 1
        Enter quantity: 5
        Do you want to add more products? (y/n): n
        [Invoice generated]
    """
    display_products(line)
    seperator()
    customer_name = input("\nEnter customer name: ")
    cart = []
    item = {}
    total_free = 0

    while continue_ == True:
        try:
            seperator()
            product_id = int(input("Enter the product ID: "))
            
            ''' Loops till it reads every line in products_list; is completed.
            Checks if user entered product id exists.
            Takes quantity from user and stores in quantity.
            Checks if quantity is in negative or zero.
            Checks if there is enough stock.
            Calculates the free items.
            Stores every details needed in item dictionary and appends it to cart.'''
            found = False
            for product in products_list:
                if product['id'] == product_id:
                    found = True
                    try:
                        seperator()
                        quantity = int(input("Enter the quantity: "))
                            
                        if quantity <= 0:
                            print("Quantity must be greater than zero.")
                            break

                        if quantity > product['quantity']:
                            print("Not enough stock!!")
                            break

                        free = (quantity // 3)

                        if quantity != 3:
                            quantity = quantity - free
                            
                        total_quantity = quantity + free 
                        product['quantity'] = product['quantity'] - total_quantity

                        ''' Checks if item already exists in the cart, if it does and the user adds the same product, it merges the quantity and calculates free items
                            otherwise, just normal calculation.'''
                        item_exists = False
                        for item in cart:
                            if (item['name'] == product['name'] and item['brand'] == product['brand']):
                                existing_total_quantity = item['quantity_sold'] + item['free_items'] # Calculates total quantity that is already in the cart
                                new_total_quantity = quantity + free
                                combined_total_quantity = existing_total_quantity + new_total_quantity # Combining old and new quantities
                                new_free_items = combined_total_quantity // 3 # Calculating the free items for new quantity

                                if new_total_quantity != 3:
                                    combined_total_quantity = combined_total_quantity - new_free_items 

                                new_sold = combined_total_quantity - new_free_items # Calculaing the new quantity sold

                                # Updating existing item in the cart
                                item['quantity_sold'] = new_sold
                                item['free_items'] = new_free_items
                                
                                item_exists = True
                                break
                            
                        # If there is no products in the cart, it creates a new item dictonary and adds it to the list cart
                        if item_exists == False: 
                            item = {"name": product['name'], "brand": product['brand'], "quantity_sold": quantity, "free_items": free, "selling_price": product['cost_price'] * 2}
                            cart.append(item)
                        
                    except ValueError:
                        print("Invalid quantity. Must be an integer.")
                    break
            if found == False:
                print("Product ID not found.")
        except ValueError:
            print("Invalid input. Please enter a valid product ID.(Integer)")

        seperator()
        continue_choice = input("\nDo you want to add more products? (y/n): ").lower() # Asks user if they want to add more products
        if continue_choice != 'y':
            break
        
    # Checks if cart is empty
    if cart:
        write_invoice = write.write_selling_invoice(customer_name, cart, total_free, products_list, seperator)
        if write_invoice:
            write.products(products_list) # Calling the function to update product details in the product.txt file.
        else:
            print("Failed to generate invoice.")
    else:
        seperator()
        print("\nYour cart is empty.\n")

def restock_products(products_list, line):
    """
    A function used to restock products taking inputs like buyer_name, product id and quantity.
    Calls display_products() function to display the details of products.
    Initializes an empty list named cart.

    Parameter:
        products_list (list of dict): Product inventory.
        line (list of str): Product data lines for display.

    Returns:
        None

    Raises:
        ValueError: If invalid product ID or quantity is entered.

    Example:
        >>> restock_products(products_list, lines)
        Enter vendor name: Gladiolus
        Enter product ID to restock: 1
        Enter quantity to add: 100
        Do you want to restock more products? (y/n): n
        [Restock invoice generated] 

    """
    display_products(line)
    seperator()
    buyer_name = input("\nEnter vendor name: ")
    cart = []

    while continue_ == True:
        try:
            seperator()
            product_id = int(input("Enter product ID to restock: "))

            ''' Loops till it reads every line in products_list; is completed.
            Checks if user inputed product id exists.
            Takes quantity from user and stores in add_quantity.
            Checks if add_quantity is in negative or zero. Stores every details needed in item dictionary and appends it to cart.'''
            found = False
            for product in products_list:
                if product['id'] == product_id:
                    found = True
                    try:
                        seperator()
                        add_quantity = int(input("Enter quantity to add: "))
                        
                        if add_quantity <= 0:
                            print("Quantity must be greater than zero.")
                            break
                        
                        product['quantity'] = product['quantity'] + add_quantity

                        # Check if product already exists in cart
                        item_exists = False
                        for item in cart:
                            if item['name'] == product['name'] and item['brand'] == product['brand']:
                                item['quantity_bought'] += add_quantity
                                item_exists = True
                                break

                        if item_exists == False:
                            item = {"name": product['name'], "brand": product['brand'], "quantity_bought": add_quantity, "cost_price": product['cost_price']}
                            cart.append(item)
                    except ValueError:
                        print("Invalid quantity. Must be an integer.")
                    break
            if found == False:
                print("Product ID not found.")
        except ValueError:
            print("Invalid input. Please enter a valid product ID.(Integer)")

        seperator()
        # Asks user if they want to add more products
        continue_choice = input("\nDo you want to restock more products? (y/n): ").lower() 
        if continue_choice != 'y':
            break

    # Checks if cart is empty
    if cart:
        write_invoice = write.write_restock_invoice(buyer_name, cart, products_list, seperator)
        if write_invoice:
            write.products(products_list) # Calling the function to update product details in the product.txt file.
        else:
            print("Failed to generate invoice.")
    else:
        seperator()
        print("\nYour cart is empty.\n")

def adding_products(products_list, line):
    """

    A function used to add new products taking inputs like buyer_name, product id, name, brand, volume, quantity, cost price, country of origin and manufacture date.
    Calls display_products() function to display the details of products.
    Initializes an empty list named cart.

    Parameters:
        products_list (list of dict): Product inventory.
        line (list of str): Product data lines for display.

    Returns:
        None

    Raises:
        ValueError: If inputs are invalid.

    Example:
        >>> Enter vendor name: sabrina
        ----------------------------------------------------------------
        Enter new product ID: 1
        Product ID already exists. Please enter a unique ID.
        ----------------------------------------------------------------
        Enter new product ID:
        
    """
    display_products(line)
    seperator()
    buyer_name = input("\nEnter vendor name: ")
    cart = []
    conti_ = True

    while continue_ == True:
        try:
            seperator()
            while conti_ == True:
                product_id = int(input("Enter new product ID: "))
                exists = False
                for product in products_list:
                    if product['id'] == product_id:
                        exists = True
                        break
                if exists == True:
                    print("Product ID already exists. Please enter a unique ID.")
                    seperator()
                else:
                    break
            
            product_name = input("Enter product name: ")
            brand = input("Enter product brand: ")
            volume = input("Enter product volume (e.g., 500ml): ")
            while conti_ == True:
                quantity = int(input("Enter quantity: "))          
                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                    seperator()
                else:
                    break
                    
            while conti_ == True:              
                cost_price = float(input("Enter cost price: "))     
                if cost_price <= 0:
                    print("Cost price must be greater than zero.")
                    seperator()
                else:
                    break

            origin = input("Enter country of origin: ")
            manufacture_date = input("Enter manufacture date (YYYY-MM-DD): ")
            
            item = {"id": product_id, "name": product_name, "brand": brand, "volume": volume, "quantity": quantity, "cost_price": cost_price, "country": origin, "mfg_date": manufacture_date}

            products_list.append(item)

            cart.append({"name": product_name, "brand": brand, "quantity_bought": quantity, "cost_price": cost_price})

        except ValueError:
            print("Invalid input. Please enter correct data types.")

        seperator()
        continue_choice = input("\nDo you want to add more products? (y/n): ").lower()
        if continue_choice != 'y':
            break

    # Checks if cart is empty
    if cart:
        write_invoice = write.write_add_invoice(buyer_name, cart, products_list, seperator)
        if write_invoice:
            write.products(products_list) # Calling the function to update product details in the product.txt file.
        else:
            print("Failed to generate invoice.")
    else:
        seperator()
        print("\nYour cart is empty.\n")
