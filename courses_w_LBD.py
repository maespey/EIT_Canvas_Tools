import config
import requests
import csv
import json
import time

headers = {'Authorization' : 'Bearer ' + '%s' % config.API_KEY}

def main():
    course_id = 107389

    payload = {'indlude[]': "external"}

    url = config.API_URL + 'api/v1/courses/'+ str(course_id) + "/tabs"
    print(url)
    results = requests.get(url, params = payload, headers = headers)
    print("The call returned \"" + str(results.status_code) + "\"")

    response = results.text
    # print(response)

    enabled_lti = json.loads(response)
    for lti in enabled_lti:
        print(lti)


if __name__ == "__main__":
    main()