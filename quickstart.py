import os
import requests 

class color:
    YELLOW = '\033[33m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    END = '\033[m'

def clear_terminal():
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
        print(color.YELLOW, 'content-type:', color.END, r.headers['content-type'])
        # access html
        print(color.YELLOW, 'HTML response:', color.END)
        print(r.text[0:50])
        print(color.YELLOW, '...', color.END)
        print(r.text[-50:])
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

def build_simple_url():
    params = {'book-id': '1337', 'page': '69'}
    r = requests.get('https://httpbin.org/', params=params)

    print(color.YELLOW, '\n Built url: ', color.END, r.url)

def simple_post():
    # Sends a payload as formdata
    payload = {'username': 'Thanos', 'password': 'password - as all things should be'}
    r = requests.post('https://httpbin.org/post', data=payload)
    
    # Converts the response from json to a dictionary
    r_dict = r.json() 
    
    print('\n')
    print(color.YELLOW, 'Form:     ', color.END, r_dict['form'])
    print(color.YELLOW, 'Data:     ', color.END, r_dict['data'])
    print(color.YELLOW, 'Files:    ', color.END, r_dict['files'])
    print(color.YELLOW, 'Headers:  ', color.END, r_dict['headers'])


def simple_timeout():
    timeout = 2 # seconds
    response_delay = 3
    url = 'http://httpbin.org/delay/' + str(response_delay) # The url will wait the response_delay before responding

    try:
        r = requests.get(url, timeout=timeout)
        if r.ok:
            print('\n')
            print(color.GREEN, 'Connection did not time out', color.END)
    
    except requests.exceptions.Timeout as e:
        print('\n')
        print(color.RED, 'Connection timed out', color.END)
        print(color.RED, 'Exception:', color.END, e)

# Authentication using the basic access authentication method:
#   Format of header field: Authorization: Basic <credentials in base64>
def basic_auth():
    username = 'thanos'
    correct_password = 'password' # as all things should be
    wrong_password = 'wrong password'
    url = 'http://httpbin.org/basic-auth/thanos/password'

    r_correct = requests.get(url, auth=(username, correct_password))
    r_wrong = requests.get(url, auth=(username, wrong_password))

    print('\n')
    print(color.GREEN, 'Correct credentials: ...', r_correct, color.END)
    print(color.RED,   'Wrong credentials: .....', r_wrong,   color.END)

def bearer_auth():
    url = 'http://httpbin.org/bearer'
    headers = {"Authorization": "Bearer MY-JSON-WEB-TOKEN"}
    r = requests.get(url, headers=headers)

    print('\n')
    print(color.YELLOW, 'Bearer autnetication status:    ', color.END, r.status_code, r.reason)
    print(color.YELLOW, 'Bearer authentication response: ', color.END, r.text)


if __name__ == "__main__":
    clear_terminal()
    simple_request()
    image_request()
    build_simple_url()
    simple_post()
    simple_timeout()
    basic_auth()
    bearer_auth()