import config
import requests
import json

headers = {'Authorization' : 'Bearer ' + '%s' % config.API_KEY}

pages_checked = {}
module_items_checked = {}

def getModules(course_id):
    payload = {'include': 'items'}
    url = config.API_URL + 'api/v1/courses/' + course_id + '/modules'
    results = requests.get(url, params=payload, headers = headers)

    response = results.text
    print(response)

def checkCourse(course_id):
    url = config.API_URL + 'api/v1/courses/' + course_id
    results = requests.get(url, headers = headers)

    if (results.status_code==404):
        print("    There are no courses with that ID...")
    else:
        response = results.text

        course = json.loads(response)
        return(course['name'])

def main():
    course_id = input("Enter the Course ID in Canvas: ")

    course_name = checkCourse(course_id)
    print("\n  Course Name: "+ course_name)

    getModules(course_id)

    # Building the request
    # payload = {'search_term': user_id}
    # url = config.API_URL + 'api/v1/courses/' + course_id
    # print(url)
    # results = requests.get(url, headers = headers)
    # print(results.status_code)

    # Sending/Recieving the response
    # results = requests.get(url, headers = headers)


if __name__ == "__main__":
    main()