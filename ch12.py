#!/usr/bin/python 3

# Python Library
# Stanley L. Ferguson III
# 30 Mar 2023
# create a script that prompts the user to perform an HTTP method

# shout out to the youtube page Learn Coding that recently finished a python series.

import requests
# Prompt user to enter a destination URL
url = input("Enter the URL: ")
# Prompt user to select HTTP method
method = input("Select HTTP method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ")
# Print the entire request that will be sent
print(f"Sending {method} request to {url}")
# Confirm with user before proceeding
confirm = input("Do you want to proceed? (y/n): ")
if confirm.lower() == 'y':
    # Make the request using requests library
    response = requests.request(method, url)
    # Print the status code and reason phrase
    print(f"Status Code: {response.status_code} - {response.reason}")
    # Translate code to plain text
    if response.status_code == 200:
        status_text = "OK"
    elif response.status_code == 201:
        status_text = "Created"
    elif response.status_code == 204:
        status_text = "No Content"
    elif response.status_code == 304:
        status_text = "Unmonified"
    elif response.status_code == 400:
        status_text = "Bad Request"
    elif response.status_code == 401:
        status_text = "Unauthorized"
    elif response.status_code == 403:
        status_text = "Forbidden"
    elif response.status_code == 404:
        status_text = "Not Found"
    elif response.status_code == 409:
        status_text = "Request Conflict"
    elif response.status_code == 410:
        status_text = "URI doesnt exist"
    elif response.status_code == 500:
        status_text = "Server Error"
    else:
        status_text = "Unknown Error"
    print(f"Status: {status_text}")
    # Print the response headers
    print("\nResponse Headers:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")
else:
    print("Request cancelled.")
