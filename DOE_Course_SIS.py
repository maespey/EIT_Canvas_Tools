from canvasapi import Canvas
import config
import csv

canvas = Canvas(config.API_URL, config.API_KEY)

filename = "DOE_Account_Import.csv"

csv_file = open(filename, 'w')
csv_file.write('course_id,short_name,long_name,account_id,status\n')

line_count = 0

def buildLine(courseID, accountID):
    #print(courseID)
    try:
        course = canvas.get_course(courseID, True)
        line = courseID
        line += ',' + course.course_code
        line += ',' + course.name
        line += ',' + accountID
        line += ',active\n'

        return line
    except:
        print("Course Not Found: " + str(courseID))


with open('all_dce_courses.csv', 'r', newline='') as course_list:
    reader = csv.reader(course_list, delimiter=',')
    for row in reader:
        line_count += 1
        if (line_count % 100) == 0:
            print(line_count)

        courseID = row[0]
        accountID = row[1]

        if courseID == "course_id":
            print(courseID)
        else:
            line = buildLine(courseID, accountID)
            # print(line)
            if line != None:
                csv_file.write(line)