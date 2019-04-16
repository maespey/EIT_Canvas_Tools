import config
import requests
import csv
import json
import re
import datetime

headers = {'Authorization' : 'Bearer ' + '%s' % config.API_KEY}

student_dict = {}

def getGroupMembership(group):
    group_members_url = config.API_URL + 'api/v1/' + '/groups/' + str(group['id']) + '/users'
    results = requests.get(group_members_url, headers = headers)

    members_lst = json.loads(results.text)

    for member in members_lst:
        # print("\nPerson: " + str(member['id']))
        # print("Group ID: " + str(group['id']))
        # print("Group Name: " + group['name'])

        try:
            student_dict[member['id']][2].append(group['name'])

        except:
            print("Student " + str(member['id']) + " is not in the course anymore.")

def getGroups(url):
    print("\n"+url)
    results = requests.get(url, headers = headers)
    print("The call returned \"" + str(results.status_code) + "\"")

    res_links = results.headers['Link']

    links = res_links.split(',')

    for link in links:
        nextRegEx = re.search("rel=\"next\"$",link)
        if nextRegEx:
            next_url = link[1:-13]
            break
        elif not nextRegEx:
            next_url = None

    return(json.loads(results.text), next_url)

def getStudents(url):
    print("/n"+url)
    results = requests.get(url, headers = headers)

    student_lst = json.loads(results.text)

    # {'id': 20397, 'name': 'Reinhard Beichel', 'created_at': '2016-03-25T10:38:42-05:00', 'sortable_name': 'Beichel, Reinhard', 'short_name': 'Reinhard Beichel', 'sis_user_id': '00611301', 'integration_id': None, 'sis_import_id': 10949, 'root_account': 'uiowa.instructure.com', 'login_id': 'rbeichel', 'email': 'reinhard-beichel@uiowa.edu'}

    for student in student_lst:
        student_dict[student['id']] = [student['sortable_name'], student['email'], []]
        print(student['id'])

    res_links = results.headers['Link']
    links = res_links.split(',')

    for link in links:
        nextRegEx = re.search("rel=\"next\"$",link)
        if nextRegEx:
            next_url = link[1:-13]
            break
        elif not nextRegEx:
            next_url = None

    return(next_url)

def main():
    course_id = input("Enter the Course ID in Canvas: ")
    filename = str(course_id)+"-group-export_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) +".csv"

    csv_file = open(filename, 'w')
    csv_file.write('student_last, student_first, student_email, group_affil\n')

    group_url = config.API_URL + 'api/v1/' + 'courses/'+ str(course_id) + '/groups'
    students_url = config.API_URL + 'api/v1/' + 'courses/'+ str(course_id) + '/users?enrollment_type%5B%5D=student'

    while students_url != None:
        students_url = getStudents(students_url)

    while group_url != None:
        groups, group_url = getGroups(group_url)

        for group in groups:
            getGroupMembership(group) # Checking the membership of groups against the student list

    for student in student_dict: # Outputting to the file created
        csv_file.write(student_dict[student][0] + ", " + student_dict[student][1] + ", " + str(student_dict[student][2]) + "\n")

if __name__ == "__main__":
    main()