import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
url = input("enter url: ")  # Replace with the URL of the website you want to scrape

# Initialize an HTTP session and set browser user-agent
session = requests.Session()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
}
session.headers.update(headers)

# Send a GET request to the website
response = session.get(url)

# Check if the request was successful
if response.status_code == 200:
    html = response.text
else:
    print("Failed to retrieve the web page.")
    exit()

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html, 'html.parser')  # You can choose another parser like 'lxml' if preferred

# Find all the forms in the parsed HTML
forms = soup.find_all('form')

# Process the forms as needed
print(f"[+] Detected {len(forms)} forms on {url}.")
print("Form html")
for form in forms:
    print(form)
    print()

for form in forms:
    print("Form Name:", form.get('name', 'No Name'))
    print("Form Method:", form.get('method', 'No Method'))
    print("Form Action:", form.get('action', 'No Action'))
    print()
 # Find and print input fields within the form
input_fields = form.find_all('input')
if input_fields:
    for form in forms:
        print("Input Fields Found: ")
        for input_field in input_fields:
            input_name = input_field.get('name', 'No Name')
            input_type = input_field.get('type', 'No Type')
            input_value = input_field.get('value', 'No Value')
            print(f"Input Name: {input_name}, Input Type: {input_type}, Input Value: {input_value}")
    print("****************************************************************")
else:
    print("No Input Fields Found")


# Close the session when done
session.close()
