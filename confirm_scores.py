import config
import requests
import csv
import json
import time
import ast

headers = {'Authorization' : 'Bearer ' + '%s' % config.API_KEY}

grades = {}

def getAssignmentID(course_id):
    url = config.API_URL + 'api/v1/' + 'courses/' + course_id + "/quizzes"
    print(url)
    try:
        results = requests.get(url, headers = headers)
        if results.status_code != 200:
            raise Exception()
    except:
        print("The course with id " + course_id + " does not exist...")
        return(None)
    
    response = results.text
    assignments = json.loads(response)

    for assignment in assignments:
        print(str(assignment['assignment_id']) + ": " + assignment['title'])
    
    assignment_id = input("Enter the assignment ID you would like to confirm: ")
    return(assignment_id)

def updateScores(assignment_id, course_id):
    url = config.API_URL + 'api/v1/' + 'courses/' + course_id + "/assignments/" + assignment_id + "/submissions"
    try:
        results = requests.get(url, headers = headers)
        if results.status_code != 200:
            raise Exception()
    except:
        print("The assignment with id " + assignment_id + " does not exist...")
        return(None)

    response = results.text
    # print(response)
    submissions = json.loads(response)

    for submission in submissions:
        if submission['body'] == None:
            None
        else:
            body = submission['body'].split(", ")
            user_score = body[2].split(": ")[1]
            print(float(user_score))
            # url = config.API_URL + 'api/v1/courses/' + course_id + "/assignments/" + assignment_id + "/submissions/" + str(submission['user_id'])
            # print(url)
            # print("grade: " + submission['grade'])
            # payload = {'submission[posted_grade]': submission['grade']}
            # results = requests.put(url, params = payload, headers = headers)

            # response = results.text
            # graded = json.loads(response)

            # print(graded)


    return False

def confirmSubmission(submission, course_id):
    # url = config.API_URL + 'api/v1/courses/' + str(course_id) + "/quizzes/" + str(submission['quiz_id']) + "/submissions/" + str(submission['id'])
    # print(url)
    # payload = {'quiz_submissions[][attempt]': submission['attempt'], 'quiz_submissions[][questions]': {"quiz_submissions": [{"attempt":submission['attempt'], "questions":}]}}

    # print(payload)

    # try:
    #     results = requests.put(url, params = payload, headers = headers)
    #     print(results.status_code)
    #     print(results)
    #     if results.status_code != 200:
    #         raise Exception()
    # except:
    #     print("The submission with id " + str(submission['id']) + " does not exist...")
    #     return(None)

    # response = results.text
    # # print(response)
    # submission = json.loads(response)

    for question in submission['quiz_submission_questions']:
        print(question['correct'])

def main():
    course_id = input("Enter the course's ID in Canvas: ")
    assignment_id = getAssignmentID(course_id)
    scores_updated = updateScores(assignment_id, course_id)

    if scores_updated:
        print("\n    All grades have been updated...")
    else:
        print("\n    No changes were made to the course...")

if __name__ == "__main__":
    main()