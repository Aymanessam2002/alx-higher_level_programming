# Alx School - 0x10-python-network_1
This project involved learning how to use the `urllib` and `requests` Python libraries to send and receive HTTP messages to URL's. I practiced sending `GET` and `POST` requests, fetching JSON resources, and interacting with API's (the Star Wars API, GitHub API, and Twitter API).

## Project Description
Learn how to fetch internet resources with the Python package `urllib`.
How to decode `urllib` body response.
How to use the Python package `requests` #requestsiswaysimplerthanurllib.
How to make HTTP `GET` request.
How to make HTTP `POST`/`PUT`/etc. request.
How to fetch JSON resources.
How to manipulate data from an external service.

## New commands / functions used:
``urllib``, ``requests``

## Helpful Links
* [HOWTO Fetch Internet Resources Using urllib Package](https://docs.python.org/3/howto/urllib2.html "HOWTO Fetch Internet Resources Using urllib Package")
* [Quickstart with Requests package](https://requests.readthedocs.io/en/latest/ "Quickstart with Requests package")
* [Requests package](https://pypi.org/project/requests/ "Requests package")
* [Python 3 Programming Tutorial - urllib module](https://youtu.be/5GzVNi0oTxQ?si=gl0uQEtz60J5bNDd)
* [Requests Library in Python - Beginner Crash Course](https://youtu.be/Xi1F2ZMAZ7Q?si=ue2entI2poRvz-RY)

##  Requirements

### Python Scripts
*   Allowed editors: `vi`, `vim`, `emacs`.
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS.
*   All your files should end with a new line.
*   The `main.py` files are used to test your functions, but you don’t have to push them to your repo.
*   The first line of all your python files should be exactly `#!/usr/bin/python3`.
*   Your code should use the pycodestyle (version `2.8.*`).
*   All your files must be executable.
*   The length of your files will be tested using `wc`.
*   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).
*   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified).
*   Your code should not be executed when imported (by using if `__name__ == "__main__":`).

* [**0. What's my status? #0**](0-hbtn_status.py) - Write a Python script that fetches `https://alx-intranet.hbtn.io/status`. - `0-hbtn_status.py`.
* [**1. Response header value #0**](./1-hbtn_header.py) - Write a Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response. - `1-hbtn_header.py`.
* [**2. POST an email #0**](./2-post_email.py) - Write a Python script that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`). - `2-post_email.py`.
* [**3. Error code #0**](./3-error_code.py) - Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`). - `3-error_code.py`.
* [**4. What's my status? #1**](./4-hbtn_status.py) - Write a Python script that fetches `https://alx-intranet.hbtn.io/status`. - `4-hbtn_status.py`.
* [**5. Response header value #1**](./5-post_params.sh) - Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header. - `5-post_params.sh`.
* [**6. POST an email #1**](./6-post_email.py) - Write a Python script that takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response. - `6-post_email.py`.
* [**7. Error code #1**](./7-error_code.py) - Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response. - `7-error_code.py`.
* [**8. Search API**](./8-json_api.py) - Write a Python script that takes in a letter and sends a `POST` request to `http://0.0.0.0:5000/search_user` with the letter as a parameter. - `8-json_api.py`.
* [**9. Catch me if you can!**](./10-my_github.py) - Write a Python script that takes your GitHub credentials (username and password) and uses the [GitHub API](https://docs.github.com/en/rest/users?apiVersion=2022-11-28) to display your id. - `10-my_github.py`.
