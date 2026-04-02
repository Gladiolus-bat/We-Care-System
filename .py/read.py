def read_file():
    """

    Opening .txt file and storing it in file to read it (denoted by "r").
    Storing the file content in a list named line and splitting the contents of lists by a new line.
    Closing the product_file.
    Initializing an empty list called products_list.

    Parameters:
        None

    Returns:
        tuple: Contains two elements:
            - products_list (list of dict): List of product dictionaries with keys:
                - 'id' (int): Product ID
                - 'name' (str): Product name
                - 'brand' (str): Product brand
                - 'volume' (str): Product volume
                - 'quantity' (int): Available quantity
                - 'cost_price' (float): Cost price
                - 'country' (str): Country of origin
                - 'mfg_date' (str): Manufacturing date
            - line (list of str): Raw lines read from the file
            
    Raises:
        Exception: If 'product.txt' does not exist.
        ValueError: If the data in the file is improperly formatted (e.g., missing fields).

    Example:
        >>> products, lines = read_file()

    """
    try:
        product_file = open("product.txt", "r")
        line = product_file.read().split('\n')
        product_file.close()
        products_list = []

        ''' Loops inside the list line.
            Separates the fields accorning to ','.
            Checks if the fields are greater than or equals to 8. If yes then, a dictionary product with key and values is made and appended in products_list.''' 
        for i in line:
            fields = i.split(',')
            if len(fields) >= 8:
                product = {'id': int(fields[0]), 'name': fields[1], 'brand': fields[2], 'volume': fields[3], 'quantity': int(fields[4]), 'cost_price': float(fields[5]), 'country': fields[6], 'mfg_date': fields[7]}
                products_list.append(product)
        return products_list, line
    except:
        print("File not found.")
        return [], []
