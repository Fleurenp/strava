import requests
import json
import datetime


#Constants
CLIENT_ID = ''
CLIENT_SECRET = ''
REFRESH_TOKEN = ''
TOKEN_URL = 'https://www.strava.com/oauth/token'
ACTIVITIES_URL = 'https://www.strava.com/api/v3/athlete/activities'

def get_access_token(client_id, client_secret, refresh_token):
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token': refresh_token,
        'grant_type': 'refresh_token'
    }
    response = requests.post(TOKEN_URL, data=payload)
    response_data = response.json()
    return response_data['access_token']

def get_activities(access_token, per_page=30, page=1):
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    params = {
        'per_page': per_page,
        'page': page
    }
    response = requests.get(ACTIVITIES_URL, headers=headers, params=params)
    return response.json()

def main():
    access_token = get_access_token(CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN)
    activities = get_activities(access_token)
    
    # Print activities
    for activity in activities:
        print(f"Name: {activity['name']}, Distance: {activity['distance']}, Date: {activity['start_date']}")

if __name__ == "__main__":
    main()