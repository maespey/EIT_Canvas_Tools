import config
import requests
import json

headers = {'Authorization' : 'Bearer ' + '%s' % config.API_KEY}

user_id = 58

url = config.API_URL + 'api/v1/' + 'users/'+ str(user_id) + "/split"
print(url)
results = requests.post(url, headers = headers)
print("The call returned \"" + str(results.status_code) + "\"")

response = results.text
print(response)
# users = json.loads(response)
# print(users)