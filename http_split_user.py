import config
import requests
import json

headers = {'Authorization' : 'Bearer ' + '%s' % config.API_KEY}

def check_user(user_id):
    url = config.API_URL + 'api/v1/' + 'users/'+ str(user_id)

    results = requests.get(url, headers = headers)
    response = results.text
    user = json.loads(response)

    print("\n*** The user that has been requested ***")
    print("       Name  : " + user['name'])
    print("       UserID: " + str(user['id']))
    print("       HawkID: " + str(user['login_id']))
    print("       Email : " + user['email'] + "\n")

    if input("...is that the correct user? (Y/N)  ")\
            in ["Y", "y", "yes", "Yes", "YES", "YAS"]:
        return True
    else:
        print("Cancel...")
        return False



def main():
    user_id = input("Enter the user's UserID in Canvas: ")

    if check_user(user_id):
        url = config.API_URL + 'api/v1/' + 'users/'+ str(user_id) + "/split"
        print(url)
        results = requests.post(url, headers = headers)
        print("The call returned \"" + str(results.status_code) + "\"")

        response = results.text
        print(response)

        
    else:
        return

if __name__ == "__main__":
    main()