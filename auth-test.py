# Tests AWS CloudWatch authentication

"""
Tests CloudWatch authentication
"""

import base64
import boto
import boto.auth_handler
import boto.exception
import boto.plugin
import boto.utils
import copy
import datetime
from email.utils import formatdate
import hmac
import os
import sys
import time
import urllib
import urlparse
import posixpath

from boto.auth_handler import AuthHandler
from boto.exception import BotoClientError

class auth_test_io_error(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return repr(self.value)



try:
  f = open('file.txt', 'r')
except auth_test_io_error:
  raise Exception()


try:
  print 'Hi there!'
except auth_test_io_error:
  raise Exception()
