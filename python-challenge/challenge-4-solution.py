#!/usr/bin/env python27
# Note, we need to use Python 2.7 or later for the argparse module

'''
A quick utility for logging information
to a log file.

Features to add:
1. Append a line to the log with the current date / time stamp.
2. Log the system uptime followed by 'as of' with the current time / date stamp.

Optional but nice features to add:
3. Log information on how much system memory is available out of how much system memory total.
   If we're classy, we'll format this in human readable sizes (megabytes or gigabytes, but not bytes)
'''

import os, sys, argparse, datetime, subprocess

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
      print 'File found, editing file.'
      editLogFile(logFile)
    else:
      print 'Couldn\'t find that file, exiting...'
  except:
    print 'Encountered an error opening the file, exiting...'
    sys.exit(2)


def editLogFile(logFile):
  try:
    # Compute the current time and format it as a string
    currentTime = str(datetime.datetime.now())
 
    # Get the system uptime
    uptime = subprocess.check_output('uptime')

    # Get the system memory stats, pass in the -m flag to display it in megabytes
    memoryStats = subprocess.check_output(['free','-m'])

    # Open our file in append mode
    workingFile = open(logFile, 'a')
  
    # Write some sample text to the file with a few \n line breaks
    workingFile.write('\n'+ currentTime + ' - Current uptime is:'  + uptime + '\nCurrent memory usage is:\n' + memoryStats)

    # Close our file
    workingFile.close()
  
  except:
    print 'Encountered an error while editing the log file.'
    sys.exit(1)


if __name__ == "__main__":
  main()
 
