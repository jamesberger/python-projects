# A repo for various things I've written in Python

## algorithms
### ye-olde-standard-sorting-algorithms.py
What was intended to be a series of implementing standard computer science algorithms in Python.
I started with sorting algorithms, but other higher priority work came along.
It'd be nice to finish this when I have some down time.

## backup photos to S3
### backup-photos-to-s3.py
A utility that scans photo EXIF time stamps to put them in chronological order and upload and organize them in that order to a S3 bucket

## boto3
### aws-secrets-manager.py
This contains everything you need to get started with the AWS Secrets Manager Service and boto3.
Notably, how to use boto3 to store a secret and retrieve a secret.
This also shows how to use JSON to store a secret in key / value pairs, which was something that was not as well documented as I'd have liked.
This is the solution to the 'The secret value can't be converted to key name and value pairs' error you may run into initially.

## coin-toss
### coint-toss.py
A very quick and dirty utility that simulates tossing a coin with a reasonable degree of accuracy.

## crypto
### dev-random-password-generation.py
An obsessive attempt to avoid any potential pseudo-random data found in the difference between /dev/random and /dev/urandom
It's a terrible solution and I recommend you avoid implementing any part of it.

## fizzbuzz
### fizzbuzz.py
A very simple Python implementation of Fizz Buzz, which is a programming interview question equivalent of 'Please show us that you have the most rudimentary amount of programming ability'. You should only get this question during your first interview for your first real job.

## Omega Manual Grabber
### minimal-omega-manual-grabber.py
### omega-manual-grabber.py
I have a 1984 Omega CT-40 Darkroom Timer. While Omega the company is still in business, their website no longer lists the manuals for their legacy hardware products.
However, they do have an ordered, unsorted collection of what appears to be digitized manuals for every product they've ever made. There's no index page for these manuals,
so this is a script to check through them and grab copies of the ones that exist so we can find the correct one for the darkroom timer.

## misc
### bar-graph.py
I was lamenting the fact that Python didn't have a good method for outputting bar graphs to the command line,
This was a quick and dirty example that was probably based on a Stack Overflow post somewhere.

## python-challenge
When I was working at AWS, I needed to come up with a way to get new hires to get their feet wet with Python.
I came up with a series of basic Python exercises, where I'd write some Python stub code that the new hires would elaborate on to solve a given problem.
Sadly, I only saved the code from Challenge \#4.

## Ranked to-do list
### create-ranked-todo-list.py
A helpful utility I wrote to take any number of to-do items and rank them by comparing each one to all the other ones. Very good for analysis paralysis and related issues.

## s3-log-ship
### 3_log-to-s3.py
### log-to-s3.py
### s3-log-pusher-errors.log
### v2_log-to-s3.py
Various Python bits that were written with the intention of shipping local error logs to a S3 bucket.
This was left unfinished and most likely will never be finished.
