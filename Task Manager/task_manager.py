# Importing libraries
import datetime
import math

# Variables to user later for output
task = "Task:"
assigned = "Assigned to:"
date_assigned = "Date assigned:"
due_date = "Due date:"
complete = "Task Complete?"
description = "Task description"
users_temp = []
passwords_temp = []
input_username = input("Please enter your username: ").lower()
space_filler = ""
tasks_temp_list = []
new_assignee = ""
today_date = datetime.date.today().strftime('%d %b %Y')

# Define functions

# Registering a new user
def reg_user():
        with open("user.txt", "a+") as user_file:
            new_user = input("Please enter the new username to register: ")
            # Checking to make sure that username does not exist, if it does, looping until a new one is entered
            if new_user in users_temp:
                while True:
                    new_user = input("This username is already taken, please enter a new username to register: ").lower()
                    if new_user not in users_temp:
                        break
            # Get new password input from user
            new_password = input("Please enter the new password for this account: ")
            password_check = input("Please confirm the new password for this account: ")
            while True:
                #Comparing passwords, if they do not match, loop until they do
                if new_password != password_check:
                    while True:
                        new_password = input("Those passwords do not match, please enter the new password for this account: ")
                        password_check = input("And please confirm the new password for this account: ")
                        if new_password == password_check:
                            break
                elif new_password == password_check:
                    user_file.write(f"\n{new_user}, {new_password}")
                    users_temp.append(f"{new_user}")
                    print("User successfully entered")
                    break

# Adding a new task to the system
def add_task():
    with open("tasks.txt", "a+") as task_file:
            task_assignee = input("Please enter the username of the person that you would like to assign this task to: ").lower()
            # Check to make sure this user exists on file, loop until an existing user is entered if they are not on file
            while True:
                if task_assignee not in users_temp:
                    while True:
                        task_assignee = input("This user is not recognised, please enter a registered user: ")
                        if task_assignee in users_temp:
                            break
                elif task_assignee in users_temp:
                        break
            # Getting data to write to file
            task_title = input("Please enter the title of the task: ")
            task_description = input("Please enter a brief description of the task: ")
            task_due_date = input("Please enter the date this task must be completed by in the format Day Mon Year e.g. 17th of November 2022 would be: 17 Nov 2022: ")   
            # Writing data to file
            task_file.write(f"\n{task_assignee}, {task_title}, {task_description}, {today_date}, {task_due_date}, No")
            # Confirmation message
            print("The task has been successfully added")   
   
# View all tasks from file
def view_all():
    # Loop over each line and print the data out in a readable format (each line forms a list which can be indexed to get relevant information)
    with open("tasks.txt", "r+") as tasks_file:
        for task_line in tasks_file:
            print("\n" + "⸻" * 100)
            task_temp = task_line.split(", ")
            print(f"{task: <30} {task_temp[1]}")
            print(f"{assigned: <30} {task_temp[0]}")
            print(f"{date_assigned: <30} {task_temp[3]}")
            print(f"{due_date: <30} {task_temp[4]}")
            print(f"{complete: <30} {task_temp[5]}")
            print(f"{description:} \n   {task_temp[2]}")
            print("⸻" * 100 + "\n")

# Creating a backup list of the tasks, this will be used when user wants to edit a task, then written to the file after changes have been made, called immediately after defining
def task_temp_filler():
    with open("tasks.txt", "r+") as tasks_file:
        for task_line in tasks_file:
            tasks_temp_list.append(task_line)

task_temp_filler()

# View tasks assigned to a user, with capability to edit these tasks
def view_mine():
    with open("tasks.txt", "r+") as tasks_file:
        print(tasks_temp_list)
        task_number_counter = 0
        this_user_tasks = []
        for task_line in tasks_file:
            task_temp = task_line.split(", ")
            # Defining this here to improved readability in the next section
            def task_view():
                print(f"""
                \n{space_filler:-<80}
                \nTask number {task_number_counter + 1}:
                \n{task: <30} {task_temp[1]}
                \n{date_assigned: <30} {task_temp[3]}
                \n{due_date: <30} {task_temp[4]}
                \n{complete: <30} {task_temp[5]}
                \n{description: <30} 
                \n\t{task_temp[2]}
                \n{space_filler:-<80}\n
                """)
            if task_temp[0] == input_username:
                # Creating a list of all of this users tasks
                this_user_tasks.append(task_line)
                task_view()
                task_number_counter += 1
            else: 
                continue
        while True:
            task_number_selected = int(input("Please enter the number of the task you would like to select, or -1 to return to the previous menu: "))
            # Defining a variable we will use to break out of error loops
            break_these_loops = "n"
            # Loop in case a number is entered that is not one of the presented tasks
            if task_number_selected > task_number_counter or task_number_selected == 0:
                while True:
                    task_number_selected = int(input("That is not a valid option, please enter the number of the task you would like to edit, or -1 to go to the previous menu: "))
                    if task_number_selected <= task_number_counter:
                        break
            # Options for user to edit tasks
            if task_number_selected != -1:
                    # Define the index of this task in the list of all tasks, allowing us to access this value later when making changes to it
                    task_selected_index = tasks_temp_list.index(this_user_tasks[task_number_selected - 1])
                    # Define a variable for accessing this task from this users list of tasks
                    task_selected = this_user_tasks[task_number_selected - 1].split(", ")                    
                    with open("tasks.txt", "r+") as tasks_file:
                            # Take input from user
                            complete_or_edit_task = input("If you would like to mark the task as complete please enter 'Y'. If you would like to edit the task, please enter 'Edit': ").lower()
                            # Loop to catch errors
                            while True:
                                # Check user input for task
                                # User input has selected to complete task
                                if complete_or_edit_task == "y":
                                    # If user has selected to complete an already complete task, return to previous menu
                                    if task_selected[5].strip("\n") == "Yes":
                                        print("This task has been completed and cannot be edited")
                                        break
                                    # If task not complete, change to complete
                                    else:
                                        task_selected[5] = "Yes\n"
                                        tasks_temp_list[task_selected_index] = ", ".join(task_selected)
                                        print("Great, I have marked that task as complete")
                                        break_these_loops = "y"
                                        break
                                # User input has selected to edit task
                                elif complete_or_edit_task == "edit":
                                    # If user has selected to complete an already complete task, return to previous menu
                                    if task_selected[5].strip("\n") == "Yes":
                                        print("This task has been completed and cannot be edited")
                                        break
                                    # Get user input
                                    change_user_or_date = input("If you woud like to change the person assigned to this task, please enter 'Person'. If you would like to change the date, please enter 'Date': ").lower()
                                    # Loop in case incorrect input
                                    while True:
                                        # Change person assigned to task
                                        if change_user_or_date == "person":
                                            # Get input of person to change to
                                            new_assignee = input("Please enter the name of the person taking over this task: ").lower()
                                            # Loop in case of error
                                            while True:
                                                # If user inputs a name not on file loop until they do
                                                if new_assignee not in users_temp:
                                                    while True:                                                        
                                                        new_assignee = input("User not recognised. Please enter the name of the person taking over this task: ").lower()
                                                        if new_assignee in users_temp:
                                                            break
                                                elif new_assignee in users_temp:
                                                    # First item in task selected is the person assigned to the task, so change this to the new person
                                                    print(new_assignee)
                                                    task_selected[0] = new_assignee
                                                    # Create a string to write to the file
                                                    task_selected = ", ".join(task_selected)
                                                    # Update the list we will write to the file
                                                    tasks_temp_list[task_selected_index] = task_selected
                                                    # Break out of loops
                                                    break_these_loops = "y"
                                                    break
                                            if break_these_loops == "y":
                                                break      
                                        # Change date assigned to task
                                        elif change_user_or_date == "date":
                                            new_date = input("Please enter the new date this task must be completed by in the format Day Mon Year e.g. 17th of November 2022 would be: 17 Nov 2022: ")
                                            # Change date in the user list
                                            task_selected[4] = new_date
                                            # Convert this to a string
                                            task_selected = ", ".join(task_selected)
                                            # Update the list we will write to the file, with this string
                                            tasks_temp_list[task_selected_index] = task_selected
                                            # Break out of loops
                                            break_these_loops = "y"
                                            break   
                                        else:
                                            # Check for errors
                                            change_user_or_date = input("Unrecognised input, please enter either 'Person' or 'Date: ") 
                                    if break_these_loops == "y":
                                            break    
                                else:
                                    while True:
                                        complete_or_edit_task = input("Unrecognised input, please enter either 'Y' or 'Edit: ").lower()
                                        if complete_or_edit_task == "person" or "date":
                                            break
                            # Break out of loops
                            if break_these_loops == "y":
                                break                      
            elif task_number_selected == -1:
                        break
            if break_these_loops == "y":
                    break
    # Write the updated list of tasks to the file (not appending as we want to edit the data)
    with open("tasks.txt", "w+") as tasks_file:
        for item in tasks_temp_list:
            tasks_file.write(item)

# Generate reports for admin
def report_generator():
    with open("tasks.txt", "r+") as tasks_file:
        # Number of tasks generated and tracked (iterate by lines and add 1 for each line)
        number_of_tasks = 0
        for lines in tasks_file:
            number_of_tasks += 1
    with open("tasks.txt", "r+") as tasks_file:
        # Defining variables we will be adding to, to keep track of number of tasks
        completed_tasks = 0
        uncompleted_tasks = 0
        for lines in tasks_file:
            task_temp = lines.strip("\n").split(", ")
        # Number of completed tasks
            if "Yes" in task_temp:
                completed_tasks += 1
        # Number of uncompleted tasks
            elif "No" in task_temp:
                uncompleted_tasks += 1
    with open("tasks.txt", "r+") as tasks_file:
        # Define a variable for number of tasks that haven't been completed and that are overdue
        overdue_tasks = 0
        for lines in tasks_file:
            task_temp = lines.strip("\n").split(", ")
            # Access the due date from the file
            due_date_formatted = task_temp[4]
            # Compare the due date to todays date (both formatted in the same way), if in the past and not completed task is overdue
            if due_date_formatted < today_date and "No" in task_temp:
                overdue_tasks += 1
    # Writing task overview to file, using w+ to generate file if it does not exist
    with open("task_overview.txt", "w+") as task_overview:
        task_overview.write(f"""Total number of tasks registered: {number_of_tasks}\n
Total number of completed tasks: {completed_tasks}\n
Total number of uncompleted tasks: {uncompleted_tasks}\n
Total number of overdue tasks: {overdue_tasks}\n
Percentage of incomplete tasks: {math.ceil(uncompleted_tasks / number_of_tasks * 100)}\n
Percentage of overdue tasks: {(math.ceil(overdue_tasks / number_of_tasks * 100))}
                                """)
    # Reading user information from file
    with open("user.txt", "r+") as users_file:
        # Number of users registered (iterate line by line and add 1 each time)
        user_number = 0
        for line in users_file:
            user_number += 1
        # Writing total numbers to file
        with open("user_overview.txt", "w+") as user_overview:
            user_overview.write(f"Total number of tasks registered: {number_of_tasks}\n")
            user_overview.write(f"Total number of users registered: {user_number}\n")
    # Reading user information for each user from file
    with open("user.txt", "r+") as users_file:
            # Create variables for each user for data we will be gathering
            for user_line in users_file:
                user_number_of_tasks = 0
                user_tasks_completed = 0
                user_tasks_overdue = 0
                # Convert user string from file into a list so we can index easily
                user_temp = user_line.strip("\n").split(", ")
                # Open and close task file for every iteration, so that we get each individuals information, not the total numbers
                with open("tasks.txt", "r+") as tasks_file:
                    # Loop over every line
                    for tasks_line in tasks_file:
                        # Conver task string to list so we can index
                        tasks_temp = tasks_line.strip("\n").split(", ")
                        due_date_formatted = tasks_temp[4]
                        # Number of tasks assigned to that user
                        if user_temp[0] in tasks_line:
                            user_number_of_tasks += 1
                            # Number of tasks completed for each user
                            if tasks_temp[5] == "Yes":
                                user_tasks_completed += 1
                            # Percentage still to be completed and overdue
                            elif "No" in tasks_line and due_date_formatted < today_date:
                                user_tasks_overdue += 1
                # Write user information for each user, with different messages if user has no tasks assigned
                if user_number_of_tasks != 0:
                    with open("user_overview.txt", "a+") as user_overview:
                        user_tasks_pending = user_number_of_tasks - user_tasks_completed
                        # Write separator for readability
                        user_overview.write("-" * 25 + "\n")
                        # Write out all required information
                        user_overview.write(f"""{user_temp[0]}:
\tis assigned a total of {user_number_of_tasks} tasks.
\tis assigned {math.ceil(user_number_of_tasks / number_of_tasks * 100)}% of all tasks.
\thas completed {math.ceil(user_tasks_completed / user_number_of_tasks * 100)}% of their tasks.
\thas {math.ceil(user_tasks_pending / user_number_of_tasks * 100)}% of their tasks still to be completed.
\thas {math.ceil(user_tasks_overdue / user_number_of_tasks * 100)}% of their tasks overdue\n""")
                else:
                    # If user has no assigned tasks
                    with open("user_overview.txt", "a+") as user_overview:
                        user_overview.write("-" * 25 + "\n")
                        user_overview.write(f"{user_temp[0]}:\n\tHas no assigned tasks.\n")


# Code to login
with open("user.txt", "r+") as user_file:
    # Retrieve user and password from file, add this to list of each to check later
    for line in user_file:
        line_temp = line.strip("\n").split(", ")
        users_temp.append(line_temp[0])
        passwords_temp.append(line_temp[1])        
    while True:
        # Variable to break out of loops
        break_all_loops = "n"
        # If a username that is not in the file is entered throw error until a recognised username is input
        if input_username not in users_temp:
            while True:
                input_username = input("Username not recognised. Please enter your username or contact admin to create a new account: ").lower()
                # Break on recognised input
                if input_username in users_temp:
                    break
        else:
            # Check the position of the username in the list and get its index (as the password and username are from the same line in the file they will have been assigned the same index in their respective lists)
            username_index = users_temp.index(input_username)
            # Get user password
            input_password = input("Please enter your password: ")
            
            # If password is not present, will throw an error message, check for this to prevent crash
            # Loop until password is correct
            if input_password not in passwords_temp:
                while True: 
                    input_password = input("Password incorrect. Please enter your password: ")
                    if input_password in passwords_temp:
                        password_index = passwords_temp.index(input_password)
                        if password_index == username_index:
                            print("\nYou are logged in\n")
                            break_all_loops = "y"
                            break
            else:
                # Create password index to compare against username
                password_index = passwords_temp.index(input_password) 
                # If password is in password list but index does not match username index create an error loop until correct password entered  
                if password_index != username_index:
                        while True:
                            input_password = input("Password incorrect. Please enter your password: ")
                            password_index = passwords_temp.index(input_password)      
                            if password_index == username_index:
                                print("\nYou are logged in\n")
                                break_all_loops ="y"
                                break
                else:
                        print("\nYou are logged in\n")
                        break_all_loops = "y"
                        break
        # Break otu of loops
        if break_all_loops == "y":
            break

while True:
    # Present the menu to the user and make sure input is lowercase
    if input_username == "admin":
        menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    gr - generate reports
    ds - display statistics
    e - Exit
    : ''').lower()
    else :
        menu = input('''Select one of the following Options below:
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit
    : ''').lower()
    # Add new user (only allowed for admin)
    if menu == 'r' and input_username == "admin":
        reg_user()
    # Assign task to user (included check to make sure user already exists)
    elif menu == 'a':
        add_task()
    # View all tasks
    elif menu == 'va':
        view_all()
    # Display tasks for current user (omitted assigned to as it seems superfluous in this case)
    elif menu == 'vm':
        view_mine()
    # Generate reports (only for admin)
    elif menu == "gr" and input_username == "admin":
        report_generator()
    # Display statistics (only for admin)
    elif menu == "ds" and input_username == "admin":
        report_generator()
        with open("task_overview.txt", "r+") as task_overview:
            print()
            for line in task_overview:
                print(line.strip("\n"))
        with open("user_overview.txt", "r+") as user_overview:
            for line in user_overview:
                print(line)  
    # Error in case input from previous task entered 
    elif menu == "d" and input_username == "admin":
        print("Did you mean to enter 'ds' for display statistics?")
    # Exit code
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    else:
        print("You have made a wrong choice, Please Try again")

#I found this website when researching formatting for this task https://docs.python.org/3/tutorial/inputoutput.html I was unsure how to format in the way specified, I've used variables for the strings to output, then given them a specific width but was wondering if there's a more most elegant solution, if you have any pointers about formatting they'd be much appreciated

# Trying to use more comments to improve readability, let me know if I've gone overboard