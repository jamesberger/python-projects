"""
A quick utility for rotating logs to S3

Written by James Berger

Last updated: October 23rd, 2015
"""

import boto
import os.path
from datetime import datetime


#Let's grab the date and time, very useful
the_current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#Let's check to see if our error log exists. If not, let's create it.
error_log_exists = os.path.isfile('s3-log-pusher-errors.log')

if error_log_exists is False:
  print("The error log file is missing. Attempting to create it.") 
  file = open('s3-log-pusher-errors.log', 'w+')
  file.write("Error log file - Last updated " + the_current_time + " \n")

  error_log_exists = os.path.isfile('s3-log-pusher-errors.log')
  print "Status of error log existence: ", error_log_exists

"""

from boto.s3.connection import S3Connection

conn = S3Connection('AKIAJ44SU64NZ7HNNKVA','lWQEXu1Q0noSDujRr78eNSK6jwxDTjAArjmpZwxH')

bucket = conn.create_bucket('mahbuckitlogshalp')

from boto.s3.key import Key

k = Key(bucket)

k.set_contents_from_string('Halp theyze stealin mah buckit')

"""
