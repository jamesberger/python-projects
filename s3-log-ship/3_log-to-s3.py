"""
A quick utility for rotating logs to S3

Written by James Berger

Last updated: October 25th, 2015
"""

import boto
from boto.s3.connection import S3Connection
from boto.s3.key import Key
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


#Now let's set up our connection to S3.
#Right now, we're storing the creds for our IAM user right in the file.
#This is not secure or ideal, so we'll change how that's done once we have this working.

conn = S3Connection('myKeyNameGoesHere','myKeyGoesHere')

#Next, let's test the bucket we'll be pushing our logs to.
#We'll create a bucket, a file in the bucket and write some text in it.

#Set our bucket
bucket = conn.create_bucket('mahbuckitlogshalp_v3')

#Set our file name
k = Key(bucket)
k.key = "Test-text-file.txt"

#Set the contents of our file
k.set_contents_from_string('Halp theyze stealin mah buckit_v3')


