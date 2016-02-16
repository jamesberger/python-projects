#!/usr/bin/env python27

'''
 Sexy one liner:
 for i in range(1,101): print "FizzBuzz"[i*i%3*4:8--i**4%5] or i
'''

for number in range(1,101):
  result = ''
  if number % 3 == 0:
    result += 'Fizz'
  if number % 5 == 0:
    result += 'Buzz'
  print number, result

