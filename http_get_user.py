import config
import requests
import json

headers = {'Authorization' : 'Bearer ' + '%s' % config.API_KEY}

user_id = input("Enter the user's UserID in Canvas:")

url = config.API_URL + 'api/v1/' + 'users/'+ str(user_id)
print(url)
results = requests.get(url, headers = headers)
print(results.status_code)
response = results.text
#print(response)
user = json.loads(response)
# print(user)
print("Name  : " + user['name'])
print("UserID: " + str(user['id']))
print("HawkID: " + str(user['login_id']))
print("Email : " + user['email'])

# headers in case you need to deal with pagination
headers = results.headers
# print(headers)