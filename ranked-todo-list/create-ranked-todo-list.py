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



def get_todo_item():
  # Get a todo item from user input
  item = input("Enter something you need to do: ")
  print("\n")
 

  # Pass it to the add_item function
  add_item(item)


def rank_items():
    compared_pairs = set()
    for item1 in todo_items:
        for item2 in todo_items:
            if item1 != item2 and (item1, item2) not in compared_pairs and (item2, item1) not in compared_pairs:
                print(f"Comparing '{item1}' to  '{item2}':")
                response = input("which one is a higher priority? Enter '1' if it's the first, or '2' if it's the second: ")
                if response == '1':
                    todo_items[item1] += 1
                elif response == '2':
                    todo_items[item2] += 1
                compared_pairs.add((item1, item2))


if __name__ == "__main__":
   # Clear the screen a bit
   print('\n' * 5)

   # Tell the user what this is
   print("Creating a ranked to-do list:")
   print('-' * 40 + '\n' * 2)

   # Get a todo item from the user
   get_todo_item()
   print('\n')

   add_another_item = input("Would you like to add another item? If so, type 'y': ")
   print('\n')

   while add_another_item == "y":
     
     get_todo_item()

     add_another_item = input("Would you like to add another item? If so, type 'y': ")
     print('\n')

   else:
      pass
   
   print("Now to rank the items: ")

   rank_items()

   print("Here are the to-do items ranked by importance: ")

   # Sort the todo_items dictionary by values (rankings)
   ranked_items = sorted(todo_items.items(), key=lambda x: x[1], reverse=True)
    
   # Print the ranked items
   print("Here is a ranked list of your to-do items: ")
   for rank, (item, _) in enumerate(ranked_items, start=1):
       print(f"{rank}. {item}")
   
   print("\nGoodbye!\n\n")




