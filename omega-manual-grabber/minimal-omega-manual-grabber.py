import requests
import wget

# Initial variables
download_directory = '/home/james/omega-manuals'
url_prefix = 'https://assets.omega.com/manuals/M'
url_postfix = '.pdf'
url_digits = '0'
valid_urls = []

# Checking for valid URLs and adding them to a list
for i in range(5000,9000):
    url_digits = str(i)
    url_to_check = (url_prefix + url_digits + url_postfix)

    try:
        site = requests.head(url_to_check)
        if site.status_code == 200:
            valid_urls.append(url_to_check)

    except requests.ConnectionError:
        print('Failed to connect')

# Download the PDF manual found at each valid URL
for url in valid_urls:
    wget.download(url, out = download_directory)


