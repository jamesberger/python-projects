#!/usr/bin/env python
import os
import sys

'''
This is a demonstration of a few of the standard sorting algorithms used in
computer science applications and frequently, in interviews as well.

While written with the beginner CS student in mind, it's also a handy review
guide for anyone.

This is designed to run on a Linux box or on a Mac using a command line based
menu system. It's a little more verbose for it, but it's a nice way for new
students to learn.

James Berger
July 21st, 2017
'''
# A few global variables
prompt = '> '
user_array_items_list = []

def bubble_sort_my_list(user_array_items_list):
  # Traditionally and in most languages, you need a temporary spot to store
  # a value when swapping it, but Python has this nice functionality where you
  # can swap two items simultaneously.

  # In plain English, our implementation of the bubble sort algorithm performs
  # the following steps:
  # 1. Shortens the name of the user's array to keep this from getting too messy
  # 2. Gets the length of the user's array and stores it as a variable
  # 3. For each element in the list, do the following
  # 3. For each element in the list, but one position back, do the following
  # 4. If the first item in the list is less than the second item
  # 5. Then swap the pairs of values, putting the second item in the first
  #    item's place and vice-versa.
  # 6. Keep doing this until no item is greater than the one after it in the list.
  array = user_array_items_list
  array_length = len(array)
  for value_a in range(array_length):
    for value_b in range(array_length-1):
        if (array[value_a] < array[value_b]):
          array[value_a], array[value_b] = array[value_b], array[value_a]

  return user_array_items_list

def main_menu():
  os.system('clear')
  print '\nWelcome to the Ye Olde Sorting Algorithms Utility!\n\n'
  print 'Menu:'
  print ' 1. Create your array'
  print ' 2. View the contents of your array'
  print ' 3. Wipe the contents of your array'
  print ' 4. Sort your array with Bubble Sort (for the depraved only)'
  print ' 5. Sort your array with Selection sort'
  print ' 6. Sort your array with Merge sort'
  print ' 7. Sort your array with Quick sort'
  print ' 8. Sort your array with Radix sort'
  print ' 9. Stats - see how each of your attempts performed'
  print ' 10. Tell me why I shouldn\'t use Bubble sort'
  print ' 11. Tell me about Selection sort'
  print ' 12. Tell me about Merge sort'
  print ' 13. Tell me about Quick sort'
  print ' 14. Tell me about Radix sort'
  print ' 15. Exit'
  print '\n\n'

  try:
    #Get the user's menu choice
    main_menu_choice = raw_input('Enter a selection [1-8]: ')

    if main_menu_choice == '1':
      os.system('clear')
      print 'Please enter the items you\'d like in the array, one item per line.'
      print 'To exit when you\'re done, hit enter on a blank line.'
      while True:
        user_array_input = raw_input(prompt)
        if user_array_input == "":
            break
        user_array_items_list.append(user_array_input)
      main_menu()
    elif main_menu_choice == '2':
      os.system('clear')
      print 'Below is a list of the items stored in the array:\n'
      for item in user_array_items_list:
          print item
      raw_input()
      main_menu()
    elif main_menu_choice == '3':
      os.system('clear')
      print 'Wiping contents of array...\n'
      del user_array_items_list[:]
      print 'Contents of array are now as listed below:\n'
      for item in user_array_items_list:
          print item
      raw_input()
      main_menu()
    elif main_menu_choice == '4':
      os.system('clear')
      bubble_sort_my_list(user_array_items_list)
      print 'List sorted with bubble sort.'
      raw_input()
      main_menu()
    elif main_menu_choice == '5':
      print 'Not implemented yet.'
      raw_input()
      os.system('clear')
      main_menu()
    elif main_menu_choice == '6':
      print 'Not implemented yet.'
      raw_input()
      os.system('clear')
      main_menu()
    elif main_menu_choice == '10':
      os.system('clear')
      print bubble_sort_description
      raw_input()
      main_menu()
    elif main_menu_choice == '15':
      os.system('clear')
      print 'Goodbye!'
      sys.exit()
    else:
      print'That was something other than a number from 1 to 15. Hit enter to back out to the main menu.'
      raw_input()
      os.system('clear')
      main_menu()


  except Exception, error_content:
    print "\nError:\n", error_content, "\n"

bubble_sort_description = """
We assume you're using this algorithm as a joke, but if you must...

A short summary of how the bubble sort algorithm works:
Bubble sort starts at the beginning of a list, and compares the first item to
the next item in the list.

If the first item is greater (however you define that) than the second item,
it will swap the two items with each other. It then proceeds to the next two
items in the list and performs the same operation.

This is one of the slowest and most computationally intensive ways to sort a list
and years ago, my own programming professor once swore to personally come after
any student that used bubble sort in a production setting.

Yes, it inspires that much rage, and with a worst-case performance of O(n^2),
it should inspire rage in you as well.
"""


if __name__ == "__main__":
  main_menu()
