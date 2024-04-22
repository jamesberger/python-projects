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
selected_csv_file = 'None'

def csv_create (filename):
    # Create the CSV file with the specified filename and write the header
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Task'] + ['Rank'])
    print(f"CSV file '{filename}' created successfully.")


def csv_menu(selected_csv_file):
    while True:
        print('\n\nCREATE CSV MENU:')
        print('Currently selected CSV file: ', selected_csv_file)
        csv_menu_option = input("\n\nSelect from the following:\n1. Create a new list\n2. Load an existing list\n3. Exit to the main menu\n> ")
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
            csv_print(selected_csv_file)
        elif csv_menu_option == '3':
            break
        else:
            print("\nPlease enter '1', '2' or '3'.")


def csv_print(filename):
    # Read data from the CSV file and print it
    with open(filename, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)

        print(f"Contents of {filename}:")
        for row in csv_reader:
            # Print the contents of an entire row on a single line
            print(', '.join(row))


# def csv_read (filename):
#     # Read data from the CSV file and return it
#     with open(filename, 'r') as csvfile:
#         csv_reader = csv.reader(csvfile)

#         # Do we need to actually do this?
#         # Maybe just return csv_reader
#         file_contents = csv_reader

#         # DEBUG: Get type of csv_reader to verify 
#         # whether or not it's something we can safely return`   `
#         print("The type of the variable csv_reader is:", type(csv_reader))

#     return file_contents


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
       rank_items()
       print('\nGoodbye!\n')
       break
     
     elif main_menu_option == '2':
        csv_menu(selected_csv_file)

     elif main_menu_option == '3':
        print("Goodbye!")
        exit()
     
     else:
       print("\nPlease enter '1', '2' or '3'.\n\n")

def rank_items():
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


   
   




