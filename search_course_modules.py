import config
import requests
import json

headers = {'Authorization' : 'Bearer ' + '%s' % config.API_KEY}

def main():
    user_id = input("Enter the user's UserID in Canvas: ")

    # Building the request
    # payload = {'search_term': user_id}
    url = config.API_URL + 'api/v1/users/' + user_id
    print(url)

    # Sending/Recieving the response
    results = requests.get(url, headers = headers)

    # Using the response
    print(results.status_code)
    response = results.text

    users = json.loads(response)
    print(users)

    if users == []:
        print("    There are no users with that username...")

    print("\nlogin ID: "+ users['login_id'])


if __name__ == "__main__":
    main()