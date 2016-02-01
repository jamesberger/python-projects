#!/usr/bin/env python27
import sys
import os
from collections import Counter, defaultdict

''' 
A quick utility for gathering stats for writers from text input.

The utility will take text from the command line or from a file.

Once it has text to work with, it will give the following stats:
1. Word count
2. Top ten most common words
3. Frequency count for a user-specified word

By: James Berger
Last updated: February 1st 2016
'''

# A function to print out a menu
def main_menu():
  os.system('clear')
  print '\nWelcome to the writing stats utility, enjoy!\n'
  print 30 * '-'
  print 'Menu: '
  print '1. Analyze text in a file'
  print '2. Analyze text pasted in'
  print '3. Exit'
  print 30 * '-'
 
  #Get user input for main menu choice
  main_menu_choice = raw_input('Enter a selection [1-3]: ')
  
  #Convert choice to a string and error out on  non-integer values
  try:
    main_menu_choice = int(main_menu_choice)
  except:
   print'That wasn\'t an integer! Please choose 1, 2, or 3.'
   raw_input()
   os.system('clear')
   main_menu()

  #Do stuff based on the choice
  if main_menu_choice == 1:
    file_text() 
  elif main_menu_choice == 2:
    pasted_text()  
  elif main_menu_choice == 3:
    os.system('clear')
    print ('\n"EOL" -Master Control Program\n')
    sys.exit()
  else:
    # We'll call raw_input here so we can pause long enough for the user to read the error message
    # It doesn't matter what they enter, but it will wait until something is entered before continuing
    raw_input('That was something other than 1, 2 or 3. Please select one of those options.')
    # Now let's clear the screen and bring up the menu again
    os.system('clear')
    main_menu()

def writing_stats(content):
  os.system('clear')
  # Convert content into a list for ease of use.
  content_list = content.split()
  # Get a length based on the list
  wordCount = len(content_list)
  # Get the top ten words by frequency using the Python 2.7 Counter library
  topWords = Counter(content_list)
  topTen = topWords.most_common(10)
  # Print out our stats
  print 'Here\'s a few stats on the supplied text: '
  print '\nNumber of words: %s' % (wordCount)
  print '\nTop ten most commonly used words and how often they appear in the text: '
  rank = 1
  for item in topTen:
     # Printing nicely formatted tuples without the parens is painful
     # So we'll use str.format() here
     print '#{0}: \'{1}\''.format(rank, *item)
     rank += 1
  # Let's see if they want to find how frequently a specific word shows up
  specificWordCheckDesired = raw_input('\nWould you like to check how frequently a specific word appears in the text? (y/n)  ')
  try:
    if specificWordCheckDesired == 'y':
      specificWordCheck(content_list)
    elif specificWordCheckDesired == 'n':
      pass  
  except:
   print('Bob That wasn\'t a \'y\' or a \'n\'. Please choose \'y\' or a \'n\'.')
   raw_input()
   os.system('clear')
   writing_stats(content) 
  pass

def specificWordCheck(content_list):
  os.system('clear')
  text_to_check = content_list
  word_to_check = raw_input('Which word would you like to get a frequency count for?\n')
  print '\nChecking for %s...' % (word_to_check)
  word_count = 0
  #word_count = defaultdict(list)
  #for word_to_check in text_to_check:
  #  word_count[word_to_check] += 1

  # The variable word_to_check is a string, so we'll use %s, but word_count is an int, so we'll use %d string formatting operator here
  print '\nThe word %s was found %d times in the supplied text' % (word_to_check, word_count)
  raw_input('\nPress any key to return to the main menu.')
  main_menu()
  pass

def pasted_text():
  os.system('clear')
  # Getting user input (note this is Python 2.x specific)
  pasted_text_content = raw_input('The text god demands text! Enter it below: \n')
  os.system('clear')
  writing_stats(pasted_text_content)
  pass

def file_text():
  os.system('clear')
  file_path = raw_input('\nEnter the path for your filename, like /home/bob/my-story.txt: ')
  if os.path.isfile(file_path):
    print('\nFile found.')
    user_file = open(file_path, 'r')
    file_contents = user_file.read();
    print('\nReading...')
    raw_input('\nPress any key to proess the file.')
    user_file.close()
    writing_stats(file_contents)
  else:
    file_text_menu_choice = raw_input('\nFile not found. \n\nPress \'r\' to re-try or \'e\' to exit to the main menu.\n')
    if file_text_menu_choice == 'r':
      file_text()
    elif file_text_menu_choice == 'e':
      main_menu()
    else:
      raw_input('That was something other than \'r\' or \'e\'. Exiting to main menu.')
      os.system('clear')
      main_menu()
  pass

# Let's give them a menu
main_menu()

# If we exit a sub menu, we should bring up the main menu again
main_menu()

# Otherwise? Let's exit then
print '\n"EOL" -Master Control Program'
sys.exit()

