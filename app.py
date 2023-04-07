import requests
import base64

# Replace YOUR_APP_ID and YOUR_APP_SECRET with your API credentials
APP_ID = '138684d8df5aab7f3df9aef8a5039c79'
APP_SECRET = '	042f74f247b70865d6d8a09c96517b504b57424ee70ba51d2eb43f1beb3d36be'

# Set the API endpoint and search query
url = 'https://api.myanimelist.net/v2/anime'
query = 'Naruto'

# Set the request headers with the API credentials
headers = {
    'Authorization': f'Basic {base64.b64encode((f"{APP_ID}:{APP_SECRET}").encode()).decode()}',
    'Content-Type': 'application/x-www-form-urlencoded'
}

# Set the request parameters with the search query
params = {
    'q': query,
}

# Send the request to the API
response = requests.get(url, headers=headers, params=params)

# Parse the response JSON
data = response.json()

print(data)

# Print the search results
for result in data['data']:
    print(result['node']['title'])