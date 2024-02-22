import requests

# localhost/url where app is running
url = 'http://127.0.0.1:5000/pets'

# Include query parameters if you want to specify
# what you're interested in or set limits to the results
params = {
    "type": "Cat",
    "limit": 1
}

# GET request to /pets endpoint of service. Use this one if you want to add parameters
response = requests.get(url, params=params)

# GET request to /pets endpoint. Comment out 'params' and use this one if you
# don't want to add any query parameters.
#response = requests.get(url)
print(response.status_code)
print(response.text)




#  NOTES -- Use cURL request to get new access token (manually, if needed)
#
# curl -d "grant_type=client_credentials&client_id=zLF6gyBE09GoJD8hNRAbxnn68jowasxJrZJQ00QOnDvSk68PtR&client_secret
# =06mdOGhm5auiLb6HXstq6GrvTs0ZjWkcktG2ItxU" https://api.petfinder.com/v2/oauth2/token


# cURL request to directly call API
# curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" "https://api.petfinder.com/v2/animals?type=cat"


