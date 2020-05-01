import os
import requests 

os.system("cls") # Hack to clear the terminal

def request_exception(request):
    # Useful info about the request
    request_type = request.request
    url = request.url
    status = request.status_code
    reason = request.reason
    
    # Build error message with the useful info
    error_message = 'request to {0} failed:'.format(url)
    error_message += '\n    request:....{0}'.format(request_type)
    error_message += '\n    status:.....{0}'.format(status)
    error_message += '\n    reason:.....{0}'.format(reason)

    return Exception(error_message)


def simple_request():
    # Send a get request to the website
    r = requests.get('https://httpbin.org/')
    # if status code 200
    if r.ok: 
        # access header
        print('content-type', r.headers['content-type'], '\n')
        # access html
        print('HTML response: \n', r.text[0:50], '\n  ... \n ', r.text[-50:])
    else:
        raise request_exception(r)

def image_request():
    url = 'https://httpbin.org/image'
    # Accepted return type must be specified in the header fo the request
    headers =  {'accept': 'image/png'}        
    r = requests.get(url, headers=headers)

    if r.ok:
        # Write the image to file in downloads folder
        with open('./downloads/simple-image-request.png', 'wb') as f:
            f.write(r._content)
    else:
        raise request_exception(r)


simple_request()
image_request()