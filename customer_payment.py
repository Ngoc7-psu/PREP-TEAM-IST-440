#Need to install requests package for python
#easy_install requests
import requests
total = []
methods = ["3", "4", "5", "6"]

# Set the request parameters
url = 'https://emplkasperpsu1.service-now.com/api/now/table/x_snc_beer_brewing_ingredients'

# Eg. User name="admin", Password="admin" for this code sample.
user = str(input("Enter username: "))
pwd = str(input("Enter password: "))

# Set proper headers
headers = {"Content-Type": "application/json", "Accept": "application/json"}

# Do the HTTP request
response = requests.post(url, auth=(user, pwd), headers=headers, data="{\"price\":\"\"}")

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
total = data.lower()
total.append(total)

def payment():
    print("Total = " + data)
    method = str(input("Enter payment method: "))
    isPaymentValid(method)

payment()

def isPaymentValid(method):
    counter = 0
    while counter < methods.length():
        if method[0] == methods[counter]:
            print("Your order was placed")
            url = 'https://emplkasperpsu1.service-now.com/api/now/table/sc_ordered_item_link'
            user = user
            pwd = pwd
            headers = {"Content-Type": "application/json", "Accept": "application/json"}
            response = requests.post(url, auth=(user, pwd), headers=headers,
                                     data="{\"name\":\"\",\"sys_created_by\":\"\"}")

        else:
            print("The payment method you entered is invalid")

