#!/usr/bin/env python
import os
import sys

'''
This is a demonstration of a few of the standard sorting algorithms used in computer science applications and frequently, in interviews as well.

James Berger
July 21st, 2017
'''
# A few global variables
prompt = '> '
user_array_items_list = []


def user_array_menu():
  os.system('clear')
  print 'Create Your array!\n\n'
  # Technically, Python doesn't natively implement an array, but we'll use
  # a list and call it an array.
  print 'Menu:'
  print '1. Add items to the array'
  print '2. View items currently in the array'
  print '3. Wipe the contents of the array'
  print '4. Exit back to main menu'
  try:
    #Get the user's array menu choice
    array_menu_choice = raw_input('Enter a selection [1-4]: ')
    if array_menu_choice == '1':
      # We'll let users append items to the list here
      # Note where we break for a blank line - we want to exit and not append
      # a blank line to the list if the user is exiting.
      os.system('clear')
      print 'Please enter the items you\'d like in the array, one item per line.'
      print 'To exit when you\'re done, hit enter on a blank line.'
      while True:
        user_array_input = raw_input(prompt)
        if user_array_input == "":
            break
        user_array_items_list.append(user_array_input)
      user_array_menu()
    elif array_menu_choice == '2':
      os.system('clear')
      print 'Below is a list of the items stored in the array:\n'
      for item in user_array_items_list:
          print item
      print '\nTo exit to the array menu, press enter.'
      raw_input()
      user_array_menu()
    elif array_menu_choice == '3':
      os.system('clear')
      print 'Wiping contents of array...\n'
      del user_array_items_list[:]
      print 'Contents of array are now as listed below:\n'
      for item in user_array_items_list:
          print item
      print ''
      raw_input('\nTo exit to the array menu, press enter.')
      user_array_menu()
    elif array_menu_choice == '4':
      os.system('clear')
      main_menu()
    else:
      print'That was something other than a number from 1 to 4. Hit enter to go back to the array creation menu.'
      raw_input()
      os.system('clear')
      user_array_menu()
  except Exception, error_content:
    print "\nError:\n", error_content, "\n"


def main_menu():
  os.system('clear')
  print '\nWelcome to the Ye Olde Sorting Algorithms Utility!\n\n'
  print 'Menu:'
  print ' 1. Create array of items to be sorted'
  print ' 2. Sort your array with Bubble Sort (for the depraved only)'
  print ' 3. Sort your array with Selection Sort'
  print ' 4. Sort your array with Merge Sort'
  print ' 5. Sort your array with Quick Sort'
  print ' 6. Sort your array with Radix Sort'
  print ' 7. Stats - see how each of your attempts performed'
  print ' 8. Exit'
  print '\n\n'

  try:
    #Get the user's menu choice
    main_menu_choice = raw_input('Enter a selection [1-8]: ')

    if main_menu_choice == '1':
      user_array_menu()
    elif main_menu_choice == '2':
      print 'Still not implemented yet.'
      raw_input()
      os.system('clear')
      main_menu()
    elif main_menu_choice == '3':
      print 'Not implemented either.'
      raw_input()
      os.system('clear')
      main_menu()
    elif main_menu_choice == '4':
      print 'Not implemented yet.'
      raw_input()
      os.system('clear')
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
    elif main_menu_choice == '7':
      print 'Not implemented yet.'
      raw_input()
      os.system('clear')
      main_menu()
    elif main_menu_choice == '8':
      os.system('clear')
      print 'Goodbye!'
      sys.exit()
    else:
      print'That was something other than a number from 1 to 8. Hit enter to back out to the main menu.'
      raw_input()
      os.system('clear')
      main_menu()


  except Exception, error_content:
    print "\nError:\n", error_content, "\n"

if __name__ == "__main__":
  main_menu()
