#!/usr/bin/env python

# A simple method to print out a dynamically updated
# progress bar to the command line. Using a unicode
# character so it prints out as a nice looking solid
# bar instead of hash marks or anything like that. 

import time,sys

for i in range(100+1):
    time.sleep(0.01)
    sys.stdout.write((u'\u2588'*i)+(''*(100-i))+("\r [ %d"%i+"% ] "))
    sys.stdout.flush()
