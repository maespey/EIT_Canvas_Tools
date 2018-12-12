import config
import requests
import csv

headers = {'Authorization' : 'Bearer ' + '%s' % config.API_KEY}

def main():
    term_id = 95

    print(str(course_id) + ": " + str(term_id))

    payload = {'enrollment_term_id[]': term_id}

    url = config.API_URL + 'api/v1/' + 'courses/'+ str(course_id)
    print(url)
    results = requests.put(url, params=payload, headers = headers)
    print("The call returned \"" + str(results.status_code) + "\"")

    response = results.text
    print(response)

if __name__ == "__main__":
    main()