#!/usr/bin/env python
import os
import sys


'''
This is a demonstration of a few of the standard sorting algorithms used in computer science applications and frequently, in interviews as well.

James Berger
July 21st, 2017
'''

def main_menu():
  os.system('clear')
  print '\nWelcome to the Ye Olde Sorting Algorithms Utility!\n\n'
  print 'Menu: '
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
      print 'Not implemented yet.'
      raw_input()
      os.system('clear')
      main_menu()
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
