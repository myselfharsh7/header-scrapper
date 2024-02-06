import requests

# Define the URL to make a GET request to
url = input("enter your url : ")

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the User-Agent header
    user_agent = response.request.headers.get('User-Agent')
    
    # Get all headers as a dictionary
    all_headers = response.headers
    
    # Print the User-Agent and all headers
    print(f"User-Agent: {user_agent}\n")
    print("All Headers:")
    for key, value in all_headers.items():
        print(f"{key}: {value}")
else:
    print(f"Failed to retrieve headers. Status code: {response.status_code}")
