#!/usr/bin/env python27

'''
Notes on FizzBuzz as implemented in Python
James Berger
February 16th, 2016

Sexy one liner found via Google:
for i in range(1,101): print "FizzBuzz"[i*i%3*4:8--i**4%5] or i

Terrible Python, but the fact that it's on one line is strangely appealing.
'''

# A more comprehensible solution to FizzBuzz in Python
# AKA "Do you know how to divide a number in Python?"
# While we're at it, why did people go with 'modulus' instead of good 'ol 'division' and 'remainder'?

for number in range(1,101):
  result = ''
  if number % 3 == 0:
    result += 'Fizz'
  if number % 5 == 0:
    result += 'Buzz'
  print number, result

