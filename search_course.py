import config
import requests
import json

headers = {'Authorization' : 'Bearer ' + '%s' % config.API_KEY}

pages = {}
module_items = {} # { (Module Item ID) : [ (Item Type), (Has the item been checked) ] }
discussions = {}
assignments = {}
quiz = {}
announcements = {}

##### PAGES #####
def checkPage(module_id):
    None

##### DISCUSSIONS #####
def checkDisc(module_id):
    None

##### ASSIGNMENTS #####
def checkAssignments(module_id):
    None

##### QUIZZES #####
def checkQuiz(module_id):
    None

##### ANNOUNCEMENTS #####
def checkAnnouncement(module_id):
    None

##### MODULES #####
def checkExternalURL(module_id):
    None

def getModules(course_id):
    payload = {'include': 'items'}
    url = config.API_URL + 'api/v1/courses/' + course_id + '/modules'
    results = requests.get(url, params=payload, headers = headers)

    response = results.text

    course = json.loads(response)
    for module in course:        
        for item in module['items']:
            if item['type'] == 'ExternalTool':
                module_items[item['id']] = [item['type'], False]
            
##### CONFIRM COURSE #####
def checkCourse(course_id):
    url = config.API_URL + 'api/v1/courses/' + course_id
    results = requests.get(url, headers = headers)

    if (results.status_code==404):
        print("    There are no courses with that ID...")
    else:
        response = results.text
        course = json.loads(response)
        
        print(course['name'])
        if input("...is that the correct user? (Y/N)  ")\
            in ["Y", "y", "yes", "Yes", "YES", "YAS"]:
            return(course['name'])
        else:
            print("Cancel...")
            return False

        

def main():
    course_id = input("Enter the Course ID in Canvas: ")

    course_name = checkCourse(course_id)
    if course_name == False:
        return
    print("\nCourse Name: " + course_name)

    getModules(course_id)

    print(module_items)

if __name__ == "__main__":
    main()