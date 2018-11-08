import config
import requests
import json

headers = {'Authorization' : 'Bearer ' + '%s' % config.API_KEY}

user_id = 15881

url = config.API_URL + 'api/v1/' + 'users/'+ str(user_id) + 'page_views'
print(url)
results = requests.get(url, headers = headers)
print(results.status_code)
response = results.text
print(response)
# users = json.loads(response)
# print(users)

# headers in case you need to deal with pagination
headers = results.headers
print(headers)