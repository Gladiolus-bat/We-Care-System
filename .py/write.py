# Importing datetime to get real time date and time
import datetime

def products(products_list):
    """

    A function that opens product.txt in write mode.
    It loops inside products_list, rewriting all the fields and storing it in a list called line.
    Line list is then written inside the file product.txt through product_file and then it is closed.
    Here product_id = str(product['id']) + " " * (3 - len(str(product['id']))),
    takes the string of value of key 'id' from product dictionary and then adds spaces subtracting the length of string.
    Basically, it is for the data inside file to have same spaces and positions as before.

    Parameters:
        products_list (list of dict): List of product dictionaries with keys:
            - 'id' (int): Product ID
            - 'name' (str): Product name
            - 'brand' (str): Product brand
            - 'volume' (str): Product volume
            - 'quantity' (int): Available quantity
            - 'cost_price' (float): Cost price
            - 'country' (str): Country of origin
            - 'mfg_date' (str): Manufacturing date
    Returns:
        None

    Raises:
        Exception: If there is an issue opening or writing the file.

    Example:
        >>>products([{"id": 1, "name": Vitamin C Serum, "brand": Garnier, "volume": 30ml, "quantity": 360, "cost_price": 1000.0, "country": France, "mfg_date": 2025-04-15}])

    """
    try:
        product_file = open("product.txt", "w")
            
        for product in products_list:
            product_id = str(product['id']) + " " * (3 - len(str(product['id'])))
            product_name = product['name'] + " " * (25 - len(product['name']))
            product_brand = product['brand'] + " " * (10 - len(product['brand']))
            product_volume = " " * (7 - len(product['volume'])) + product['volume']
            product_quantity = " " * (6 - len(str(product['quantity']))) + str(product['quantity']) + " "
            product_cost_price = " " * (7 - len(str(product['cost_price']))) + str(product['cost_price']) + " " 
            product_country = product['country'] + " " * (13 - len(product['country']))
            product_mfg_date = product['mfg_date']

            line = product_id + "," + product_name + "," + product_brand + "," + product_volume + "," + product_quantity + "," + product_cost_price + "," + product_country + "," + product_mfg_date
            product_file.write(line + "\n")
        product_file.close()
    except:
        print("Error opening or writing the file.")

def write_selling_invoice(customer_name, cart, total_free, products_list, seperator_function):
    """

    Generates and writes a selling invoice to a uniquely named file and displays it.

    Parameters:
        customer_name (str): Name of the customer.
        cart (list of dict): List of sold items with keys:
            - 'name' (str): Product name
            - 'brand' (str): Product brand
            - 'quantity_sold' (int): Quantity sold
            - 'free_items' (int): Free items given
            - 'selling_price' (float): Selling price per item unit
        total_free (int): Total number of free items.
        products_list (list of dict): Updated list of products after sale.
        seperator_function (function): Function that prints a visual separator.

    Returns:
        bool: If invoice was written successfully True, otherwise False.

    Raises:
        Exception: If the file cannot be created or written to.

    Example:
        >>> write_selling_invoice("Sabrina",[{"name": "Vitamin C Serum", "brand": "Garnier", "quantity_sold": 2, "free_items": 1, "selling_price": 1200.0}], 1, products_list, print_separator)

    """
    try:
        seperator_function()
        print("\n\t\t\t\t\tINVOICE")
        seperator_function()
            
        # Get current date and time as string components for invoice naming and display
        year = str(datetime.datetime.now().year)
        month = str(datetime.datetime.now().month)
        day = str(datetime.datetime.now().day)
        time = str(datetime.datetime.now().hour) + str(datetime.datetime.now().minute) + str(datetime.datetime.now().second)

        # Displays details of invoice
        print("Name:", customer_name, "\t\t\t\t\t\tDate:", year + "-" + month + "-" + day)
        seperator_function()
        print(" " + "_" * 87)
        print("| Name" + " " * 21 + "|" + " Brand" + " " * 5 + "|" + " Quantity | " + "Free Items | " + "Rate   | " + "Total Price   |")
        print("|" + "-" * 26 + "|" + "-" * 11 + "|" + "-" * 10 + "|" + "-" * 12 + "|" + "-" * 8 + "|" + "-" * 15 + "|")        

        # Generates a unique name for invoice file name
        invoice_name = customer_name + "_" + year + month + day + "-" + time
        invoice_file = open(invoice_name, "w")

        # Writing details in invoice file
        invoice_file.write("\n\n\t\t\t\t\tINVOICE\n")
        invoice_file.write("-" * 98)
        invoice_file.write("\nName: " + customer_name + "\t\t\t\t\t\tDate: " + year + "-" + month + "-" + day)
        invoice_file.write("\n" + "-" * 98)
        invoice_file.write("\n " + "_" * 87)
        invoice_file.write("\n| Name" + " " * 21 + "|" + " Brand" + " " * 5 + "|" + " Quantity | " + "Free Items | " + "Rate   | " + "Total Price   |")
        invoice_file.write("\n|" + "-" * 26 + "|" + "-" * 11 + "|" + "-" * 10 + "|" + "-" * 12 + "|" + "-" * 8 + "|" + "-" * 15 + "|")

        grand_total = 0
            
        # Loop through each item in the cart to compute line-wise totals and write to invoice
        for item in cart:
            # Formatting each field to match column widths
            total_free = total_free + item['free_items']
            name = item['name'] + " " * (25 - len(item['name']))
            brand = item['brand'] + " " * (11 - len(item['brand']))
            quantity = str(item['quantity_sold']) + " " * (9 - len(str(item['quantity_sold'])))
            free_items = str(item['free_items']) + " " * (11 - len(str(item['free_items'])))
            selling_price = str(item['selling_price']) + " " * ( 7 - len(str(item['selling_price'])))
            total_price = str(item['selling_price'] * item['quantity_sold']) + " " * ( 14 - len(str(item['selling_price'] * item['quantity_sold'])))

            grand_total = grand_total + (item['selling_price'] * item['quantity_sold'])

            # Preparing formatted line for both console and file
            invoice_line = "|" + name + "|" + brand + "| " + quantity + "| " + free_items + "| " + selling_price + "| " + total_price + "|"
            invoice_file.write("\n" + invoice_line)
            print(invoice_line)

        print(" " + "-" * 87, "\nFree items:", total_free, "\nGrand Total: Rs.", grand_total)
        invoice_file.write("\n " + "-" * 87 + "\nFree items: " + str(total_free) + "\nGrand Total: Rs. " + str(grand_total))
        invoice_file.close() # Closing the invoice file

        return True
    except:
            print("Error while generating or writing the file.")
            return False

def write_restock_invoice(buyer_name, cart, products_list, seperator):
    """

    Generates and writes an invoice for restocking based on added quantities and cost prices.

    Parameters:
        buyer_name (str): Name of the vendor.
        cart (list of dict): List of restocked items with keys:
            - 'name' (str): Product name
            - 'brand' (str): Product brand
            - 'quantity_bought' (int): Quantity purchased
            - 'cost_price' (float): Cost price per item unit
        products_list (list of dict): Updated inventory list.
        seperator (function): Function to print a separator for formatting.

    Returns:
        bool: If invoice was written successfully True, otherwise False.

    Raises:
        Exception: If the file cannot be written to or invoice fails.

    """
    try:
        seperator()
        print("\n\t\t\t\t\tINVOICE")
        seperator()

        # Get current date and time as string components for invoice naming and display
        year = str(datetime.datetime.now().year)
        month = str(datetime.datetime.now().month)
        day = str(datetime.datetime.now().day)
        time = str(datetime.datetime.now().hour) + str(datetime.datetime.now().minute) + str(datetime.datetime.now().second)

       # Displays details of invoice
        print("Name:", buyer_name, "\t\t\t\t\t\tDate:", year + "-" + month + "-" + day)
        seperator()
        print(" " + "_" * 74)
        print("| Name" + " " * 21 + "|" + " Brand" + " " * 5 + "|" + " Quantity | " + "Rate   | " + "Total Price   |")
        print("|" + "-" * 26 + "|" + "-" * 11 + "|" + "-" * 10 + "|" + "-" * 8 + "|" + "-" * 15 + "|")        

        # Generates a unique name for invoice file name
        invoice_name = buyer_name + "_" + year + month + day + "-" + time
        invoice_file = open(invoice_name, "w")# Opening a new file in write mode to save invoice

        # Writing details in invoice file
        invoice_file.write("\n\n\t\t\t\t\tINVOICE\n")
        invoice_file.write("-" * 98)
        invoice_file.write("\nName: " + buyer_name + "\t\t\t\t\t\tDate: " + year + "-" + month + "-" + day)
        invoice_file.write("\n" + "-" * 98)
        invoice_file.write("\n " + "_" * 74)
        invoice_file.write("\n| Name" + " " * 21 + "|" + " Brand" + " " * 5 + "|" + " Quantity | " + "Rate   | " + "Total Price   |")
        invoice_file.write("\n|" + "-" * 26 + "|" + "-" * 11 + "|" + "-" * 10 + "|" + "-" * 8 + "|" + "-" * 15 + "|")

        total = 0
        grand_total = 0

        # Loop through each item in the cart to compute line-wise totals and write to invoice
        for item in cart:
            # Formatting each field to match column widths
            name = item['name'] + " " * (25 - len(item['name']))
            brand = item['brand'] + " " * (11 - len(item['brand']))
            quantity = str(item['quantity_bought']) + " " * (9 - len(str(item['quantity_bought'])))
            cost_price = str(item['cost_price']) + " " * ( 7 - len(str(item['cost_price'])))
            total_price = str(item['cost_price'] * item['quantity_bought']) + " " * ( 14 - len(str(item['cost_price'] * item['quantity_bought'])))

            total = total + (item['cost_price'] * item['quantity_bought'])
            grand_total = total * 0.13 + total

            # Preparing formatted line for both console and file
            invoice_line = "|" + name + "|" + brand + "| " + quantity + "| " + cost_price + "| " + total_price + "|"
            invoice_file.write("\n" + invoice_line) # Writing the line to the invoice file
            print(invoice_line)

        print(" " + "-" * 74, "\nTotal: Rs.", total, "\nVat: 13%\nGrand Total: Rs.", grand_total)

        invoice_file.write("\n " + "-" * 74 + "\nTotal: Rs. " + str(total) + "\nVat: 13% " + "\nGrand Total: Rs. " + str(grand_total))
        invoice_file.close() # Closing the invoice file
        
        return True
    except:
        print("Error while generating or writing the file.")
        return False

def write_add_invoice(buyer_name, cart, products_list, seperator):
    """

    Generates and writes an invoice for newly added products to the inventory.

    Parameters:
        buyer_name (str): Name of the vendor.
        cart (list of dict): Items added with keys:
            - 'name' (str): Product name
            - 'brand' (str): Product brand
            - 'quantity_bought' (int): Quantity purchased
            - 'cost_price' (float): Cost price per item unit
        products_list (list of dict): Updated product list including the new items.
        seperator (function): Function that prints a visual separator.

    Returns:
        bool: If invoice was written successfully True, otherwise False.

    Raises:
        Exception: If the file cannot be written to or invoice fails.

    """
    try:
        seperator()
        print("\n\t\t\t\t\tINVOICE")
        seperator()

        # Get current date and time as string components for invoice naming and display
        year = str(datetime.datetime.now().year)
        month = str(datetime.datetime.now().month)
        day = str(datetime.datetime.now().day)
        time = str(datetime.datetime.now().hour) + str(datetime.datetime.now().minute) + str(datetime.datetime.now().second)

        # Displays details of invoice
        print("Name:", buyer_name, "\t\t\t\t\t\tDate:", year + "-" + month + "-" + day)
        seperator()
        print(" " + "_" * 74)
        print("| Name" + " " * 21 + "|" + " Brand" + " " * 5 + "|" + " Quantity | " + "Rate   | " + "Total Price   |")
        print("|" + "-" * 26 + "|" + "-" * 11 + "|" + "-" * 10 + "|" + "-" * 8 + "|" + "-" * 15 + "|")        

        # Generates a unique name for invoice file name
        invoice_name = buyer_name + "_" + year + month + day + "-" + time
        invoice_file = open(invoice_name, "w") # Opening a new file in write mode to save invoice

        # Writing details in invoice file
        invoice_file.write("\n\n\t\t\t\t\tINVOICE\n")
        invoice_file.write("-" * 98)
        invoice_file.write("\nName: " + buyer_name + "\t\t\t\t\t\tDate: " + year + "-" + month + "-" + day)
        invoice_file.write("\n" + "-" * 98)
        invoice_file.write("\n " + "_" * 74)
        invoice_file.write("\n| Name" + " " * 21 + "|" + " Brand" + " " * 5 + "|" + " Quantity | " + "Rate   | " + "Total Price   |")
        invoice_file.write("\n|" + "-" * 26 + "|" + "-" * 11 + "|" + "-" * 10 + "|" + "-" * 8 + "|" + "-" * 15 + "|")

        total = 0
        grand_total = 0

        # Loop through each item in the cart to compute line-wise totals and write to invoice
        for item in cart:
            # Formatting each field to match column widths
            name = item['name'] + " " * (25 - len(item['name']))
            brand = item['brand'] + " " * (10 - len(item['brand']))
            quantity = str(item['quantity_bought']) + " " * (9 - len(str(item['quantity_bought'])))
            cost_price = str(item['cost_price']) + " " * ( 7 - len(str(item['cost_price'])))
            total_price = str(item['cost_price'] * item['quantity_bought']) + " " * ( 14 - len(str(item['cost_price'] * item['quantity_bought'])))

            total = total + (item['cost_price'] * item['quantity_bought'])
            grand_total = total * 0.13 + total

            # Preparing formatted line for both console and file
            invoice_line = "|" + name + " |" + brand + " | " + quantity + "| " + cost_price + "| " + total_price + "|"
            invoice_file.write("\n" + invoice_line)
            print(invoice_line)

        print(" " + "-" * 74, "\nTotal: Rs.", total, "\nVat: 13%\nGrand Total: Rs.", grand_total)

        invoice_file.write("\n " + "-" * 74 + "\nTotal: Rs. " + str(total) + "\nVat: 13% " + "\nGrand Total: Rs. " + str(grand_total))
        invoice_file.close()

        return True

    except:
        print("Error while generating or writing the file.")
        return False
