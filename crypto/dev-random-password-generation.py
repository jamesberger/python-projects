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
Last updated: Tuesday, May 31st 2016
'''

# General note: We should also keep track of how much entropy is available,
# traditionally done with 'cat /proc/sys/kernel/random/entropy_avail'. It'd be
# nice if we could display this in meter style graph for the end user.
# Maybe something that does the equivalent of
# 'watch -n2 cat /proc/sys/kernel/random/entropy_avail'.

# We'll use the struct library to help decode our binary data into something
# more usable
import struct

def randomData():
  # We'll implement some basic error handling here with a try / except block.
  try:
    # Opening it as read only, binary, as we won't be writing to it.
    truly_random_source = open("/dev/random", 'rb')
  except BufferError:
      print ('Buffer error on opening /dev/random, see randomData function.')
  except EnvironmentError:
      print ('Ran into an IO error or OS error, see randomData function.')
  # Currently not certain if the EOF exception will fire if we run out of
  # entropy in /dev/random, but we'll put it here for the time being.
  except EOFError:
      print ('Ran into an end-of-file condition, see randomData function.')
