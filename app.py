from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Global variables for Petfinder API credentials
CLIENT_ID = 'zLF6gyBE09GoJD8hNRAbxnn68jowasxJrZJQ00QOnDvSk68PtR'
CLIENT_SECRET = '06mdOGhm5auiLb6HXstq6GrvTs0ZjWkcktG2ItxU'


# CLIENT_ID = 'your-client-id'
# CLIENT_SECRET = 'your-client-secret'

def get_access_token(client_id, client_secret):
    """
    Requests access token from the Petfinder API.
    :param client_id (str): Petfinder API key
    :param client_secret (str): Petfinder API client secret
    :return: The access token as a string if the request was successful, string
    otherwise None.
    """
    token_url = "https://api.petfinder.com/v2/oauth2/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }

    try:
        response = requests.post(token_url, data=data)
        response.raise_for_status() #verify the request was successful

        response_data = response.json()
        access_token = response_data['access_token']

        return access_token

    except requests.RequestException as e:
        print(f"Error fetching access token: {e}")
        return None


@app.route('/pets', methods=['GET'])
def get_pets():
    """
    Endpoint to retrieve pet information from Petfinder API.
    Accepts query parameters (type, breed, etc.) to filter results.
    :return: JSON response that includes animal data from Petfinder API.
    """
    access_token = get_access_token(CLIENT_ID, CLIENT_SECRET)

    if access_token is not None:
        headers = {"Authorization": f"Bearer {access_token}"}
        api_url = "https://api.petfinder.com/v2/animals"

        # Include query parameters provided in the request
        query_params = request.args
        # This print statement was used to verify the parameters were being
        # fowarded correctly to the Petfinder API
        # print(f"Requesting {api_url} with parameters {query_params}")
        try:
            response = requests.get(api_url, headers=headers, params=query_params)
            response.raise_for_status()
            return jsonify(response.json())
        except requests.RequestException as e:
            print(f"API request error: {e}")
            return jsonify({"error": "Failed to fetch data from Petfinder API"}), 500

    else:
        return jsonify({"error": "Failed to obtain access token"}), 500


if __name__ == "__main__":
    app.run(debug=True)
