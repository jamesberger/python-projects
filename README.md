# A repo for various things I've written in Python

## algorithms
What was intended to be a series of implementing standard computer science algorithms in Python.
I started with sorting algorithms, but other higher priority work came along.
It'd be nice to finish this when I have some down time.

## boto3
This contains various example bits of Python code for working with the AWS boto3 library

### aws-secrets-manager.py
This contains everything you need to get started with the AWS Secrets Manager Service and boto3.
Notably, how to use boto3 to store a secret and retrieve a secret.

## cloudwatch-cli
### auth-test.py
Looking at this code years later, I vaguely recall plans to make a very simple front end for CloudWatch.
Apparently I started testing authentication but got sidetracked within minutes of starting.
It's almost like there's a bit of a theme here...

## crypto
### dev-random-password-generation.py
An obsessive attempt to avoid any potential pseudo-random data found in the difference between /dev/random and /dev/urandom
It's a terrible solution and I recommend you avoid implementing any part of it.

## fizzbuzz
### fizzbuzz.py
A very simple Python implementation of Fizz Buzz, which is a programming interview question equivalent of 'Please show us that you have the most rudimentary amount of programming ability'. You should only get this question during your first interview for your first real job.

## misc
### bar-graph.py
I was lamenting the fact that Python didn't have a good method for outputting bar graphs to the command line,
This was a quick and dirty example that was probably based on a Stack Overflow post somewhere.

## python-challenge
When I was working at AWS, I needed to come up with a way to get new hires to get their feet wet with Python.
I came up with a series of basic Python exercises, where I'd write some Python stub code that the new hires would elaborate on to solve a given problem.
Sadly, I only saved the code from Challenge \#4.

## s3-log-ship
Various Python bits that were written with the intention of shipping local error logs to a S3 bucket.
This was left unfinished and most likely will never be finished.
