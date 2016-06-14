#!/usr/bin/env python
'''
We need random (as-is-possible with our source) data for some given task.
With Linux, we have two primary sources of entropy, /dev/random and
/dev/urandom. Both of the two sources have good and bad aspects to them, and
both are backed by the same CSPRNG.

The upside of /dev/random is that the data within is as truly random as you'll
get without a hardware RNG.

The downside of /dev/random is when it runs out of entropy, your IO is blocked
until the entropy pool starts to fill up again. If you're in the middle of
gathering data, your application will stop until that pool fills, which can be
less than ideal in real-world situations.

The massive upside of /dev/urandom is that there's never any IO blocking. If our
system is secure, an attacker cannot differentiate the output of the CSPRNG from
true randomness if the initial seed is actually random.

The downside of /dev/urandom is that while it's perfect for all real-world
purposes, it does have one small issue - when it runs out of entropy, it starts
generating pseudo-random data.

This isn't the end of the world, as the Linux CSPRNG (Cryptographically secure
pseudorandom number generator) is solid.

An attacker would need perfect knowledge of the internal state of the CSPRNG to
differentiate the output from actual randomness. In the real world, this is a
non-issue - if an attacker could actually have  perfect knowledge of the
internal state of the CSPRNG, the quality of randomness would be the least of
your concerns.

An imperfect analogy would be a person that is concerned about the quality of
the locks on their house when the attackers are already inside the house.

But why bother taking any risk at all if blocking IO isn't a major problem?

Python has a number of great libraries and functions for handling things that
need random data, but they're all based on using /dev/urandom. Using the
/dev/random pool instead is a little more painful, but definitely possible.

This is intended to provide basic functionality that can be extended or adapted
as needed. That said, this should never be used for anything other than
recreational use. It would be stupid to use it for any real-world thing.

Fair warning:
A "I'll roll my own crypto solution!" fool and his data are soon parted.

Written by: James Berger
Last updated: Tuesday, June 14th 2016
'''

# We'll use the struct library to help decode our binary data into something
# more usable
import struct, sys, os
from stat import *


def randomData():
  # We'll implement some basic error handling here with a try / except block.

  # We should make sure that the things we need for this to work actually exist
  try:
    # We'll stat the device and get the device number
    dev_random_device_number = os.stat("/dev/random").st_rdev
    # Now we need to make sure it's a character device
    if S_ISCHR(dev_random_device_number):
      dev_random_device_exists = True

      if dev_random_device_exists is True:
        try:
          # Opening it as read only, binary, as we won't be writing to it.
          truly_random_source = open("/dev/random", 'rb')
          # Struct requires a minimum length of 4 characters, so we'll use 4 here.
          random_data_contents = truly_random_source.read(4)
          return random_data_contents

        except BufferError:
          print ('Buffer error on opening /dev/random, see randomData function.')
        except EnvironmentError:
          print ('Ran into an IO error or OS error, see randomData function.')
        # Currently not certain if the EOF exception will fire if we run out of
        # entropy in /dev/random, but we'll put it here for the time being.
        except EOFError:
          print ('Ran into an end-of-file condition, see randomData function.')
      else:
        print ('I\'m unable to find /dev/random, is this running on something other than a Linux box?')

    # If it's anything other than a character device, it doesn't exist for us
    else:
      dev_random_device_exists = False

  except:
    print ('I\'m unable to find /dev/random, is this running on something other than a Linux box?')


def userDefinedVariables():
  alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  alphabet_extended = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
  desired_alphabet_type = alphabet
  random_string_length = 8

  return alphabet, alphabet_extended, desired_alphabet_type, random_string_length

def entropyMeter():
  # Note - this does not work on a Mac

  # General note: We should also keep track of how much entropy is available,
  # traditionally done with 'cat /proc/sys/kernel/random/entropy_avail'. It'd be
  # nice if we could display this in meter style graph for the end user.
  # Maybe something that does the equivalent of
  # 'watch -n2 cat /proc/sys/kernel/random/entropy_avail'.
  # Note: We will need the value to be 64 or greater to read without blocking IO.
  try:
    available_entropy_value = open("/proc/sys/kernel/random/entropy_avail", "r")
    available_entropy = available_entropy_value.read()
    return available_entropy

  except IOError:
    print ('\n\nWARNING: IOError - Entropy meter function can\'t run. \nREASON: I wasn\'t able to read from /proc/sys/kernel/random/entropy_avail, are you running this on something other than a Linux box?')


#def entropyPoolFillRate():

  # We should also do some sort of estimate of how quickly the entropy pool fills
  # up, as we don't want to have the end user trying to generate a 200 character
  # long random string if the entropy pool only fills up 100 characters every 10
  # minutes or so.

  # Build entropy pool fill rate calculation functionality here


def translateRandomToAlpha():
  random_alpha_string = ''

  try:
    # string_length = 80
    string_length = userDefinedVariables()[3]
    alpha_contents = userDefinedVariables()[2]

    for item in range(string_length):
      temp_string = alpha_contents[struct.unpack('I', randomData())[0] % len(alpha_contents)]
      random_alpha_string += temp_string
    print ('\nYour random string is:\n\n'), random_alpha_string, ('\n')
    return random_alpha_string

  # Need to go through list of all possible exceptions to verify that we have an
  # exception for everything that could possibly generate an exception.
  except EnvironmentError:
    print ('Ran into an IO error or OS error, see translateRandomToAlpha function.')
  # Currently not certain if the EOF exception will fire if we run out of
  # entropy in /dev/random, but we'll put it here for the time being.
  except EOFError:
    print ('Ran into an end-of-file condition, see translateRandomToAlpha function.')


if __name__ == "__main__":

  print('\n\nWelcome to the (truly) Random Password Generator\n')
  print('The current amount of available entropy is: '), entropyMeter()
  print('\nIf the available amount of entropy is less than 100, it may take quite a while to generate random data.')

  yes_answer = ['yes','y']
  no_answer = ['no', 'n']
  run_generator_choice = ''

  while not run_generator_choice in yes_answer or no_answer:
    run_generator_choice = raw_input('Do you want to proceed? (y/n) ').lower()

    if run_generator_choice in yes_answer:
      translateRandomToAlpha()
      break
    elif run_generator_choice in no_answer:
      print('Exiting...\n')
      sys.exit()
    else:
      print('Please enter "y" or "n".')

  sys.exit()
