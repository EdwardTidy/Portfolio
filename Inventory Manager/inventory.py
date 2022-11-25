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

# Function to create the shoes list from inventory file (including try, except to flag any errors in file)
def read_shoes_data():
    with open("inventory.txt", "r+") as inventory_file:
        
        # Using enumerate to skip the first line
        for count, line in enumerate(inventory_file):
            if count != 0:

                # Receive the values from each line to be used to create the shoe object
                try:
                    line = line.split(",")
                    country = line[0]
                    code = line[1]
                    product = line[2]
                    cost = line[3]
                    quantity = line[4]
                    shoe_list.append(Shoe(country, code, product, cost, quantity))
                
                # Formatting errors leading to gaps in the file will flag an error with the line number to check
                except IndexError as error:
                    print(f"line {count + 1}")
                    print(error)

#==========Functions outside the class==============

# Capture user data about a shoe and use this data to create a shoe object appended to list and text file
def capture_shoes():

    # Creating a loop to get user input and make sure it is correct before adding the shoe to the file
    while True:
        loop_breaker = "n"

        # Get user input, while Loops to make sure integers are added for cost and quantity, plus error messages if not
        country_input = input("Enter the country you are based in: ")
        code_input = input("Enter the product code: ")
        product_input = input("Enter the name of the product: ")
        while True:
            try:
                cost_input = int(input("Enter the cost per item: "))
                break
            except ValueError:
                print("This must be an integer, please try again")
        while True:
            try:
                quantity_input = int(input("Enter the quantity of items in stock: "))
                break
            except ValueError:
                print("This must be an integer, please try again")

        # Summarise user information to make sure they're happy
        print(f"""You have entered:
        Country: {country_input}
        Product code: {code_input}
        Product name: {product_input}
        Cost per item: {cost_input}
        Quantity in stock: {quantity_input}""")
        user_input_correct = input("Is this correct? y/n: ").lower()

        # Make sure user input either y or n, y also breaks out of larger loop
        while True:
            if user_input_correct =="y":
                print("Shoe added")
                loop_breaker = "y"
                break
            elif user_input_correct == "n":
                print("Let's take that information again")
                break
            else:
                user_input_correct = input("Unrecognised input, please enter y/n: ")
        if loop_breaker == "y":
            break

    # Once user input finalised, create shoe object with this information  
    product_line = Shoe(country_input, code_input, product_input, cost_input, quantity_input)

    # Write shoe to file and append shoe to list
    with open ("inventory.txt", "a+") as inventory_file:
        inventory_file.write(f"\n{product_line}")

    # Added this casting to allow me to strip the \n later on
    product_line.quantity = str(product_line.quantity)
    shoe_list.append(product_line)

# Iterate over shoes list and print details of the shoes
def view_all():
    print()
    for shoe in shoe_list:
        # Formatting bug where objects I add myself don't have a line between them, stripping \n from all shoes and then adding it to all of them to get around this
        shoe.quantity = shoe.quantity.strip("\n")
        shoe.quantity = shoe.quantity + "\n"
        print(shoe)

#Find shoe object with lowest quantity
def re_stock():

    # Create a list of just the quanity of each object, so we can user sort() on it (strip \n as it's the last value on each line)
    stock_list = []
    for shoe in shoe_list:
        stock_list.append(int(shoe.quantity.strip("\n")))

    # Sort from low to high, lowest item will be at index 0
    stock_list.sort()
    lowest_stock_item = stock_list[0]

    #Making a list to hold this item for ease of access
    lowest_stocked_list =[]
    for shoe in shoe_list:
        if int(shoe.quantity.strip("\n")) == lowest_stock_item:
            lowest_stocked_list.append(shoe)
    
    # Stripping the \n to make the next section easier to format
    lowest_stocked_list[0].quantity = lowest_stocked_list[0].quantity.strip("\n")

    # Tell user number in stock, check if they would like to update it (loop to make sure correct input)
    user_update_stock_query = ""
    while True:
        user_update_stock_query = input(f"""The lowest stocked shoe is {lowest_stocked_list[0].code} ({lowest_stocked_list[0].product}) in {lowest_stocked_list[0].country}.
There are currently {lowest_stocked_list[0].quantity} in stock. Would you like to add to this quantity? y/n: """).lower()
        if user_update_stock_query == "y" or user_update_stock_query == "n":
            break
        else:
            print("Unrecognised input, please try again")
    
    # If user wants to update stock then get input for number to increase stock by, while loop to catch errors, if n then finish this function and go to main loop
    if user_update_stock_query == "y":
        while True:
            try:
                user_update_stock_query = int(input("Please enter the amount you would like to increase the stock by: "))
                break
            except ValueError:
                print("Please enter an integer")

        # Increase quantity of item and format it as before then write to file and append list
        for item in lowest_stocked_list:
            item.quantity = f"{int(item.quantity) + user_update_stock_query}\n"
        with open("inventory.txt", "w+") as inventory_file:
            style_line = Shoe("Country","Code","Product","Cost","Quantity\n")
            shoe_list.insert(0, style_line)
            for shoe in shoe_list:
                inventory_file.write(f"{shoe}")
            
            # Delete item at shoe_list 0 as this will be the placeholder showing the style of object variables from the file, not necessary in the list
            del shoe_list[0]

# Search for shoe from the list using shoe code, if the shoe code does not return any results throw an error
def search_shoe(shoe_code):
    while True:
        shoe_in_list = 0
        for shoe in shoe_list:
            if shoe.code == shoe_code:
                shoe_in_list += 1
                return shoe
        if shoe_in_list == 0:
                return "Unrecognized code, please try again"

# Calculate the total value for each item and print them out (with whitespace for user readability)
def value_per_item():
    print()
    for shoe in shoe_list:
        print(f"{shoe.code} in {shoe.country}. Value is: {int(shoe.cost) * int(shoe.quantity)}")
    print()

# Determine the product with the highest quantity then print as being for sale
def highest_qty():
    stock_list = []
    for shoe in shoe_list:
        stock_list.append(shoe)

    # Learnt about using a function to sort by: https://www.w3schools.com/python/ref_list_sort.asp
    def myFunc(shoe):
        return(int(shoe.quantity))
    stock_list.sort(key=myFunc)
    highest_stock_quantity = stock_list[-1]

    # This may be the most cynical thing I have ever coded
    print(f"\nFlash sale! Buy {highest_stock_quantity.product}. Was {int(highest_stock_quantity.cost) + 200}, now only {highest_stock_quantity.cost}\n") 


#==========Main Menu=============

# Empty string to start the loop and function to create shoes list
user_choice = ""
read_shoes_data()

# Loop for menu with error if unrecognised input
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
        # Loop to make sure a recognised shoe code is input, otherwise we'll get an error
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