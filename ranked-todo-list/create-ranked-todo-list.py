"""
Creating a ranked to-do list:

Step 1: Enter list of to-do items as a dictionary
Step 2: Assign an initial rank of 0 for the value for each item in the dictionary.
Step 3: Perform a comparison of each to-do item against every other item in the dictionary.
Step 4: For each item that is compared, increment the rank value of that item by 1 if it's more important than the current item. Otherwise, increase the rank of the current item.
Step 5: Print a ranked list of the to-do items. 

Stretch goal: Add functionality to import a list of to-do items from a .csv and export the re-ranked version to that same .csv or another

Written by James Berger, last major update on 4/15/2024
"""

import csv
import os
import re

# A regex to allow us to validate that a file name only contains alphanumeric characters (a-z, A-Z, 0-9), underscores and dashes
valid_filename_chars = re.compile('^[a-zA-Z0-9_-]+$')

# Set the file extension and path
file_extension = '.csv'

# Create an empty dictionary for our data
todo_items = {}

# Default value for selected CSV file
selected_csv_file = None


def csv_append(selected_csv_file):
    if selected_csv_file is None:
        print("No CSV file has been selected.")
        return

    # Load data from the selected CSV file if it exists
    try:
        with open(selected_csv_file, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            rows = list(csv_reader)
    except FileNotFoundError:
        rows = []

    while True:
        # Get the item to append from the user
        new_item = input("Enter the item to append to the CSV layout or 'exit' to finish: ")
        if new_item.lower() == 'exit':
            break

        # Append the new item with a default value of 0 to each row
        rows.append([new_item, '0'])

        # Write the updated rows back to the CSV file
        with open(selected_csv_file, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerows(rows)

        print(f"Item '{new_item}' appended to the CSV layout in '{selected_csv_file}'.")
        input("Press any key to continue.")

        # Ask the user if they want to append another item
        choice = input("Do you want to append another item? (yes/no): ")
        if choice.lower() != 'yes':
            break


def csv_create (filename):
    # Create the CSV file with the specified filename and write the header
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Task'] + ['Rank'])
    print(f"CSV file '{filename}' created successfully.")
    selected_csv_file = filename
    csv_menu(selected_csv_file)


def csv_menu(selected_csv_file):
    while True:
        print('\n\nCREATE CSV MENU:')
        print('Currently selected CSV file: ', selected_csv_file)
        print('\nSelect from the following:')
        print('1. Create a new list')
        print('2. Select and load an existing list')
        print('3. Print contents of selected list')
        print('4. Re-rank items in currently selected list')
        print('5. Wipe all items in currently selected list, add new items and rank them')
        print('6. Append items to currently selected list')
        print('7. Exit to the main menu')
        csv_menu_option = input('\n> ')

        if csv_menu_option == '1':
            raw_filename = input("\n\nWhat would you like to name your list?\n\nNotes:\n       Valid characters are 'A-Z', 'a-z', '0-9', '-', and '_'.\n       All files are saved with a .csv extension, no need to add it.\n> ")
            result = valid_filename_chars.match(raw_filename)
            if result  == None:
                print("\n\nAn invalid character was present in the filename, please try again.")
            else:
                filename = raw_filename + file_extension
                csv_create(filename)
        elif csv_menu_option == '2':
            selected_csv_file = csv_select_file()
        elif csv_menu_option == '3':
            csv_print(selected_csv_file)
        elif csv_menu_option == '4':
            csv_rank(selected_csv_file)
        elif csv_menu_option == '6':
            csv_append(selected_csv_file)
        elif csv_menu_option == '7':
            main_menu()
        else:
            print("\nPlease enter '1', '2', '3', '4', '5', '6', or '7'.")


def csv_print(selected_csv_file):
    # Read data from the CSV file and print it
    with open(selected_csv_file, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)

        print(f"Contents of {selected_csv_file}:")
        for row in csv_reader:
            # Print the contents of an entire row on a single line
            print(', '.join(row))
        input('Press any key to return to the CSV menu...\n')
        csv_menu(selected_csv_file)
    

def csv_rank(selected_csv_file):
    if selected_csv_file is None:
        input("No CSV file has been selected. Press any key to return to the menu.")
        return

    # Load data from the selected CSV file
    with open(selected_csv_file, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        
        # Check if the CSV file has only one row (excluding the header)
        num_rows = sum(1 for _ in csv_reader)
        if num_rows <= 1:
            input("The CSV file has no data aside from the header row. Please select a different CSV file. Press any key to continue.")
            return

        # Reset the file pointer to the beginning
        csvfile.seek(0)

        # Skip the header row
        next(csv_reader)
        
        # Extract todo items from each row
        todo_items = {row[0].strip(): 0 for row in csv_reader}

    # Rank todo items
    rank_items(todo_items)


def csv_select_file ():
    # Get a list of all CSV files in the current directory
    csv_files = [file for file in os.listdir() if file.endswith('.csv')]

    # Check for condition where there are no .csv files
    if not csv_files:
        print("No .csv files found in the current directory.")
        return None

    # Present the list of .csv files to the user
    print("Here are the .csv files in the current directory:")
    for i, file in enumerate(csv_files, start=1):
        print(f"{i}. {file}")

    # Ask the user to select a .csv file
    while True:
        try:
            choice = int(input("Enter the number of the .csv file you want to open:\n> "))
            if 1 <= choice <= len(csv_files):
                return csv_files[choice - 1]
            else:
                print("Invalid choice. Please enter a number within the range.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def csv_write (filename, data):
    # Append data to the .csv file
    with open(filename, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in data:
            csv_writer.writerow(row)
    print("Data written to CSV file.")


def get_todo_items():
    while True:
        task = input("\nEnter something you need to do:\n> ")
        todo_items[task] = 0

        while True:
            another = input("Do you want to add another item? (y/n):\n> ").lower()
            if another == 'y':
                break
            elif another == 'n':
                return todo_items
            else:
                print("Please enter 'y' or 'n'.")

def main_menu():
   # Clear the screen a bit and tell the user what this is
   print('\n' * 5)
   print('Welcome!\n\nThis will ask you for items on your to-do list, then ask you to rank each of those items vs all the other items.')
   print('Once it has that, it will print a ranked list for you!')
   print('-' * 115 + '\n')

   while True:
     print('MAIN MENU:\n\nWhich would you like to make:')
     print('1. A quick, one-time use ranked to-do list')
     print('2. A multiple use ranked to-do list that will be saved to a .csv')
     print('3. Exit')

     main_menu_option = input("\n> ")
     
     if main_menu_option == '1':
       # Get a list of to-do items from the user
       get_todo_items()
       print("\n\nNow that we have all your to-do items, let's rank them: \n" + '-' * 55)
       rank_items(todo_items)
       print('\nGoodbye!\n')
       break
     
     elif main_menu_option == '2':
        csv_menu(selected_csv_file)

     elif main_menu_option == '3':
        print("Goodbye!")
        exit()
     
     else:
       print("\nPlease enter '1', '2' or '3'.\n\n")

def rank_items(todo_items):
    compared_pairs = set()
    for item1 in todo_items:
        for item2 in todo_items:
            if item1 != item2 and (item1, item2) not in compared_pairs and (item2, item1) not in compared_pairs:
                print(f"\nComparing '{item1}' to  '{item2}', which one is a higher priority?")
                response = input("Enter '1' if it's the first, or '2' if it's the second:\n> ")
                if response == '1':
                    todo_items[item1] += 1
                elif response == '2':
                    todo_items[item2] += 1
                compared_pairs.add((item1, item2))
                compared_pairs.add((item2, item1))
    
    # Sort the todo_items dictionary by values (rankings)
    print("\n\nSorting the list of items...")
    ranked_items = sorted(todo_items.items(), key=lambda x: x[1], reverse=True)
    
    # Print the ranked items
    print("\nHere is a ranked list of your to-do items: \n" + 40 * '_')
    for rank, (item, _) in enumerate(ranked_items, start=1):
       print(f"{rank}. {item}")


if __name__ == "__main__":
  main_menu()


   
   




