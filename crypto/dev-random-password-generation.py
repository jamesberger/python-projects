#!/usr/bin/env python
'''
We need random data for some given cryptographic task. With Linux, we have two
primary sources of entropy, /dev/random and /dev/urandom. Both of the two sources
have good and bad aspects to them.

The upside of /dev/random is that the data within is as truly random as you'll
get without a hardware RNG.

The downside of /dev/random is when it runs out of entropy, your IO is blocked
until the entropy pool starts to fill up again. If you're in the middle of
gathering data, your application will stop until that pool fills, which can be
less than ideal in most real-world situations.

The upside of /dev/urandom is that there's never any IO blocking.

The downside of /dev/urandom is that while it's decent for most purposes, it
does have one small issue. When it runs out of entropy, it starts generating
pseudo-random data. This isn't the end of the world, as the Linux CSPRNG
(Cryptographically secure pseudorandom number generator) is fairly solid.

But why bother taking any risk at all if blocking IO isn't a major problem?

Python has a number of great libraries and functions for handling things that
need random data, but they're all based on using /dev/urandom. Using the
/dev/random pool instead is a little more painful, but definitely possible.

This is intended to provide basic functionality that can be extended or adapted
as needed. That said, this has not been audited by any professional
cryptographers and is not indended for anything other than recreational use.

Fair warning:
A "I'll roll my own crypto solution!" fool and his data are soon parted.

Written by: James Berger
Last updated: Tuesday, June 7th 2016
'''

# General note: We should also keep track of how much entropy is available,
# traditionally done with 'cat /proc/sys/kernel/random/entropy_avail'. It'd be
# nice if we could display this in meter style graph for the end user.
# Maybe something that does the equivalent of
# 'watch -n2 cat /proc/sys/kernel/random/entropy_avail'.

# We should also do some sort of estimate of how quickly the entropy pool fills
# up, as we don't want to have the end user trying to generate a 200 character
# long random string if the entropy pool only fills up 100 characters every 10
# minutes or so.

# We'll use the struct library to help decode our binary data into something
# more usable
import struct, sys

def randomData():
  # We'll implement some basic error handling here with a try / except block.
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


def translateRandomToAlpha():
  # Users may want purely alphanumeric content, or they might want the extended
  # character set, so we'll let them switch between the two by changing the
  # variable alpha_contents. We need to improve this though, rather than having
  # them manually change a variable.
  alphabet_extended = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
  alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  alpha_contents = alphabet

  random_string_length = 80
  random_string = ''

  try:
    for item in range(random_string_length):
      temp_string = alpha_contents[struct.unpack('I', randomData())[0] % len(alpha_contents)]
      random_string += temp_string
    print random_string

  # Need to go through list of all possible exceptions to verify that we have an
  # exception for everything that could possibly generate an exception.
  except EnvironmentError:
      print ('Ran into an IO error or OS error, see translateRandomToAlpha function.')
  # Currently not certain if the EOF exception will fire if we run out of
  # entropy in /dev/random, but we'll put it here for the time being.
  except EOFError:
      print ('Ran into an end-of-file condition, see translateRandomToAlpha function.')


#def entropyMeter():
    # Build entropy meter functionality here

#def entropyPoolFillRate():
    # Build entropy pool fill rate calculation functionality here

if __name__ == "__main__":
    translateRandomToAlpha()
    sys.exit()
