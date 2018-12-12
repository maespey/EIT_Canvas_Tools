import config
import requests
import csv
import json
import time

headers = {'Authorization' : 'Bearer ' + '%s' % config.API_KEY}
excluded_terms = []

def startReport():
    url = config.API_URL + 'api/v1/' + 'accounts/1/reports/unused_courses_csv'
    print(url)
    results = requests.post(url, headers = headers)
    #print("The call returned \"" + str(results.status_code) + "\"")

    response = results.text
    report = json.loads(response)
    print("\n****")
    print(report)
    print("****\n")

    while report['progress'] != 100:
        time.sleep(5)
        url = config.API_URL + 'api/v1/' + 'accounts/1/reports/unused_courses_csv/' + str(report['id'])
        results = requests.get(url, headers = headers)
        response = results.text
        report = json.loads(response)
        print("    Report is processing: "  + str(report['progress']) + "%\n")
    
    return(report['attachment']['url'], report['id'])

def getReport(report_url, report_id):
    print(report_url)
    csv_request = requests.get(report_url)

    file_name = "canvas_unused_courses_" + str(report_id) + ".csv"

    with open(file_name, 'wb') as report_file:
        report_file.write(csv_request.content)

    print("\n\nYour file " + file_name + " is ready...")

    return(file_name)

def filterCourses(file_name):
    filtered_course_list = []
    
    with open(file_name, 'r', newline='') as course_list:
        reader = csv.reader(course_list, delimiter=',')
        for row in reader:
            

    return filtered_course_list

# def deleteCourses(filtered_course_list):


#     return course_count

def main():
    start_time = time.time()

    report_url, report_id = startReport()
    file_name = getReport(report_url, report_id)

    filtered_course_list = filterCourses(file_name)

    # course_count = deleteCourses(filtered_course_list)

    end_time = time.time()
    print("\nIt took " + str(end_time-start_time) + " seconds to delete courses...")

    # print(str(course_id) + ": " + str(term_id))

    # payload = {'term_id[]': term_id}

    # url = config.API_URL + 'api/v1/' + 'courses/'+ str(course_id)
    # print(url)
    # results = requests.get(url, params = payload, headers = headers)
    # print("The call returned \"" + str(results.status_code) + "\"")

    # response = results.text
    # print(response)

if __name__ == "__main__":
    main()