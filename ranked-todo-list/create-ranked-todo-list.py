"""
Creating a ranked todo list:

Step 1: Enter list of todo items as a dictionary
Step 2: Assign an initial rank of 0 for the value for each item in the dictionary.
Step 3: Perform a comparison of each todo item against every other item in the dictionary.
Step 4: For each item that is compared, increment the rank value of that item by 1 if it's more important than the current item. Otherwise, increase the rank of the current item.
Step 5: Print a ranked list of the todo items. Also maybe provide an option to export the ranked items into a CSV?
"""

def add_item(item):
    # Check to see if todo_items dictionary exists
    if 'todo_items' not in globals():
        globals()['todo_items'] = {}

    # Assign the item to our dictionary with an initial rank of zero
    todo_items[item] = 0



    