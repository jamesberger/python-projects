#!/usr/bin/env python27
# Note, we need to use Python 2.7 or later for the argparse module

'''
A quick utility for logging information
to a log file.

Features to add:
1. Append a line to the log with the current date / time stamp.
2. Log the system uptime followed by 'as of' with the current time / date stamp.

Optional but nice features to add:
3. Log information on how much system memory is available 
   out of how much system memory total.
'''

import os, sys,  argparse

def main():

  # Add a command line argument to allow the user to select a log file
  # The 'help' and 'metavar' show up when the help option is called to provide more info on how the argument works
  parser = argparse.ArgumentParser()
  parser.add_argument("-f", "--file", dest="userSuppliedFileName", help="Supply an input file.", metavar="myLogFile.txt")
  args = parser.parse_args()

  logFile = args.userSuppliedFileName

  # Let's make sure that the user specified a file that actually exists
  try:
    if os.path.exists(logFile):
      print 'file exists.'
      editLogFile(logFile)
    else:
      print 'Couldn\'t find that file, exiting...'
  except:
    print 'Encountered an error opening the file, exiting...'
    sys.exit(2)


def editLogFile(logFile):

  # Open our file in append mode
  workingFile = open(logFile, 'a')
  
  # Write some sample text to the file with a few \n line breaks
  workingFile.write('\nHello world! Isn\'t Python awesome?\n')

  # Close our file
  workingFile.close()


if __name__ == "__main__":
  main()
 
