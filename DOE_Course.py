from canvasapi import Canvas
import config
import csv

def account_check(user_id):
    if user_id == 'DOE_A':
        accountID = '380'
    elif user_id == 'DOE_B':
        accountID = '381'
    elif user_id == 'DOE_D':
        accountID = '382'
    elif user_id == 'DOE_E':
        accountID = '383';
    elif user_id == 'DOE_G':
        accountID = '384';
    elif user_id == 'DOE_H':
        accountID = '385';
    elif user_id == 'DOE_L':
        accountID = '386';
    elif user_id == 'DOE_M':
        accountID = '387';
    elif user_id == 'DOE_N':
        accountID = '388';
    elif user_id == 'DOE_P':
        accountID = '389';
    elif user_id == 'DOE_R':
        accountID = '390';
    elif user_id == 'DOE_T':
        accountID = '391';
    else:
        accountID = '392';
    return(accountID)


canvas = Canvas(config.API_URL, config.API_KEY)

def main():
    with open('all_dce_courses.csv', 'r', newline='') as course_list:
        reader = csv.reader(course_list, delimiter=',')
        for row in reader:
            courseID = row[0]
            accountID = row[1]

            course = account_check(accountID)
            print(courseID + ": " + accountID + " -> " + course)

            # course = canvas.get_course(row[1], True)

if __name__ == "__main__":
    main()