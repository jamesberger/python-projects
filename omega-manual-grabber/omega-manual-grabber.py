import requests
import wget
from datetime import datetime

'''
Problem: I need a copy of the manual for my 1980s Omega CT40 darkroom timer.
Omega has a large repository of PDF manuals for legacy equipment they no longer produce, 
but they do not list them on their website. Helpfully though, they seem to have numbered them in an easy to check sequence.
For example, https://assets.omega.com/manuals/M4988.pdf, https://assets.omega.com/manuals/M4989.pdf and so on.
However, not all numbers in a given sequence are valid - There may be a M4985.pdf, a M4986.pdf and a M4987.pdf, but no M4988.pdf
Also, the file names carry no indication of what equipment the manual is for.

Solution: So we need to get a list of every single valid URL. We can do this with the Python requests library and check a given 
list of URLs and see which ones return a HTTP 200 OK response. For the URLs that return a HTTP 200 OK, we can add them to a list 
of valid URLs. Then we can download the manual from each of those valid URLs and stick them all in a directory and grep through 
them to find the Omega CT40 darkroom timer manual.


Logic flow
1. Specify URL prefix - e.g., https://assets.omega.com/manuals/M
2. Specify URL postfix - e.g., .pdf
3. Specify a range - e.g., 1,000 to 9,999
4. Get a HTTP status code for each of those URLs, store the URL in a list of valid URLs if the status code is 200
5. For URL in list of valid URLs, download the PDF


Author: James Berger
Date: February 2022
'''

# Initial variables
attempted_urls = 0
download_directory = '/home/james/omega-manuals'
output_file = '/home/james/github/python-projects/omega-manual-grabber/valid-urls.txt'
url_prefix = 'https://assets.omega.com/manuals/M'
url_postfix = '.pdf'
url_digits = '0'
valid_urls = []

# To help distinguish the output when we have multiple runs of the script in a row during testing
# let's write a time stamp as the first line of our output to the log.
current_timestamp = datetime.now()
with open(output_file, 'a+') as f:
    f.write('\n\n%s\n' % current_timestamp)

for i in range(100,5000):
    url_digits = str(i)
    url_to_check = (url_prefix + url_digits + url_postfix)
    
    attempted_urls += 1

    try:
        site = requests.head(url_to_check)
        if site.status_code == 200:
            valid_urls.append(url_to_check)
            with open(output_file, 'a+') as f:
                f.write('%s\n' % url_to_check)

    except requests.ConnectionError:
        print('Failed to connect')


number_of_good_urls = len(valid_urls)

print(f'Checked {attempted_urls} urls, found {number_of_good_urls} good URLs.')

print(valid_urls)

for url in valid_urls:
    wget.download(url, out = download_directory)

