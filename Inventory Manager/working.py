# Shoe class constructor
class Shoe:

    """Constructor to create shoe objects.
    Requires country, code, product, cost and quantity values for initialisation; has methods to return the cost of the shoe, the quantity in stock and a string representation of the object    
    """

    # Class variables
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Class methods
    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"


#=============Shoe list===========

# List for shoe objects
shoe_list = []

# Function to create the shoes list (including try, except to flag any errors in file)
def read_shoes_data():
    with open("inventory.txt", "r+") as inventory_file:
        for count, line in enumerate(inventory_file):
            if count != 0:
                try:
                    line = line.split(",")
                    country = line[0]
                    code = line[1]
                    product = line[2]
                    cost = line[3]
                    quantity = line[4]
                    shoe_list.append(Shoe(country, code, product, cost, quantity))
                except IndexError as error:
                    print(f"line {count + 1}")
                    print(error)

#==========Functions outside the class==============
'''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code. Also appending the object to inventory.txt to save it
    '''
# Capture user data about a shoe and use this data to create a shoe object appended to list and text file
def capture_shoes():
    country_input = input("Enter the country you are based in: ")
    code_input = input("Enter the product code: ")
    product_input = input("Enter the name of the product: ")
    cost_input = int(input("Enter the cost per item: "))
    quantity_input = int(input("Enter the quantity of items in storage: "))
    product_line = Shoe(country_input, code_input, product_input, cost_input, quantity_input)
    with open ("inventory.txt", "a+") as inventory_file:
        inventory_file.write(f"\n{product_line}")
    shoe_list.append(f"\n{product_line}")
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

def view_all():
    print()
    for shoe in shoe_list:
        print(shoe)
    print()
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

def re_stock():
    stock_list = []
    for shoe in shoe_list:
        stock_list.append(int(shoe.quantity.strip("\n")))
    stock_list.sort()
    lowest_stock_quantity = stock_list[0]

    #Making a list in case there's more than one object with the same low stock
    lowest_stocked_list =[]
    for shoe in shoe_list:
        if int(shoe.quantity.strip("\n")) == lowest_stock_quantity:
            lowest_stocked_list.append(shoe)
    user_update_stock_query = int(input(f"The lowest stocked shoe is {lowest_stocked_list[0]} Would you like to add to this quantity? If yes please enter an amount to get in stock: "))
    for item in lowest_stocked_list:
        item.quantity = f"{int(item.quantity) + user_update_stock_query}\n"
    with open("inventory.txt", "w+") as inventory_file:
        style_line = Shoe("Country","Code","Product","Cost","Quantity\n")
        shoe_list.insert(0, style_line)
        for shoe in shoe_list:
            inventory_file.write(f"{shoe}")
        del shoe_list[0]
    
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

def search_shoe(shoe_code):
    shoe_in_list = 0
    for shoe in shoe_list:
        if shoe.code == shoe_code:
            shoe_in_list += 1
            return shoe
    if shoe_in_list == 0:
            return "Unrecognized code, please try again"
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

def value_per_item():
    print()
    for shoe in shoe_list:
        print(f"{shoe.code} in {shoe.country}. Value is: {int(shoe.cost) * int(shoe.quantity)}")
    print()
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

def highest_qty():
    stock_list = []
    for shoe in shoe_list:
        stock_list.append(shoe)
    # Learnt about the sort function on w3schools, and how to define a function to sort by: https://www.w3schools.com/python/ref_list_sort.asp
    def myFunc(shoe):
        return(int(shoe.quantity))
    stock_list.sort(key=myFunc)
    highest_stock_quantity = stock_list[-1]
    print(f"\nFlash sale! Buy {highest_stock_quantity.product}. Was {int(highest_stock_quantity.cost) + 200}, now only {highest_stock_quantity.cost}\n") 
    # The line above may be the most cynical thing I have ever coded
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
user_choice = ""
read_shoes_data()

while user_choice != "q":
    user_choice = input("""Please enter a choice from the following menu: 
    input shoe - i
    view all stock - v
    restock - r
    search by product code, - s
    value of all items - u
    highest quantity - h
    quit - q
    """).lower()

    if user_choice == "i":
        capture_shoes()

    elif user_choice == "v":
        view_all()
    
    elif user_choice == "r":
        re_stock()

    elif user_choice == "s":
        while True:
            shoe_search_input = input("Please enter the product code: ")
            shoe_variable = search_shoe(shoe_search_input)
            if shoe_variable != "Unrecognized code, please try again":
                print(f"\nCountry: {shoe_variable.country} Product: {shoe_variable.product} Value per item: {shoe_variable.cost} Quantity in stock: {shoe_variable.quantity}")
                break
            else:
                print(shoe_variable)

    elif user_choice == "u":
        value_per_item()

    elif user_choice == "h":
        highest_qty()

    elif user_choice == "q":
        print("Goodbye")

    else:
        print("Oops - incorrect input")