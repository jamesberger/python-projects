#!/usr/bin/env python3

import boto3
import botocore.exceptions
import logging
import os
import sys

# This utility is designed to backup photos to the AWS S3 service either automatically as a cron job or scheduled task, or manually as desired.
#
# You will most likely need to install the Python 3 exif library for automatic folder generation and photo sorting to work. 
# If you have Pip installed, the command is 'pip3 install exif' minus the quotes.
# Without the exif library, the script will just replicate the folder and file structure of the target directory you specify in the S3 bucket path you've selected.

# Set your photo directory, S3 bucket path and path to your AWS credentials file here
# Linux example:
# target_directory = '/home/myuser/photos'
# target_s3_bucket = 's3://mybucketname/myphotos'
# target_credentials_file = '/home/myuser/.aws/credentials'
target_directory = '/home/james'
target_s3_bucket = ''
target_credentials_file = '/home/blah/credentials'

# Set up logger
#logging.basicConfig(level=logging.WARN)
#logger = logging.getLogger()

# Check to see if the target locations exist:
try:
    if os.path.exists(target_directory) == False:
        sys.exit('BPS3: Could not find target directory ' + target_directory + ', exiting.')
except Exception as e:
    sys.exit(e)


# Check to see if the AWS credentials are valid
try: 
    client = boto3.client('sts')
    client.get_caller_identity()
except botocore.exceptions.NoCredentialsError:
    sys.exit('BPS3: Could not validate credentials via boto3.client.get_caller_identity(), exiting.')
else:
    aws_credentials_valid = True

# Check to see if S3 bucket exists if our AWS credential check succeeds
if aws_credentials_valid = True:
    response = client.head_bucket(
        Bucket = target_s3_bucket,
    )