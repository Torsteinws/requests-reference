import os
import requests 

os.system("cls") # Hack to clear the terminal

# Send a get request to the website
r = requests.get('https://httpbin.org/')
# If no error encountered (status code == 200)
if r.ok:

    # The items in the header is accessible
    print('content-type', r.headers['content-type'], '\n')

    print('HTML response: ')
    print(r.text[0:50], '\n  ... \n ', r.text[-50:])
 

# print(r.json())
