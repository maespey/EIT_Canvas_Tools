# This would create a tool on the account with configuration pulled from an external URL
# curl -X POST 'https://<canvas>/api/v1/accounts/<account_id>/external_tools' \
#      -H "Authorization: Bearer <token>" \
#      -F 'name=LTI Example' \
#      -F 'consumer_key=asdfg' \
#      -F 'shared_secret=lkjh' \
#      -F 'config_type=by_url' \
#      -F 'config_url=https://example.com/ims/lti/tool_config.xml'

import config
import requests
import json

headers = {'Authorization' : 'Bearer ' + '%s' % config.API_KEY}

def add_LTI(course_id):
    payload = {'name': config.proctorio_name, 'consumer_key': config.proctorio_key,\
               'shared_secret': config.proctorio_secret, 'config_type': 'by_url',\
               'config_url': config.proctorio_url}

    url = config.API_URL + 'api/v1/courses/'+ str(course_id) + "/external_tools"
    print(url)

    results = requests.post(url, params = payload, headers = headers)
    print("The call returned \"" + str(results.status_code) + "\"")

    if results.status_code == 200:
        return True
    else:
        return False

def main():
    course_id = input("Enter the user's UserID in Canvas: ")

    url = config.API_URL + 'api/v1/courses/' + course_id + '/external_tools'
    payload = {'search_term': config.proctorio_name, 'include_parents': False}

    results = requests.get(url, params = payload, headers = headers)
    print("The call returned \"" + str(results.status_code) + "\"")
    external_tools = json.loads(results.text)

    if external_tools == []:
        if add_LTI(course_id):
            print("Proctorio added to " + course_id)
            return
            
        else:
            print("Couldn't add to " + course_id)
            return
    else:
        print("Proctorio is already in " + course_id)
        return

if __name__ == "__main__":
    main()