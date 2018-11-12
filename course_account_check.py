from canvasapi import Canvas
import config
import csv

canvas = Canvas(config.API_URL, config.API_KEY)

account_id_lst = []

write_file = input("What would you like to name your file? ")

csv_w_file = open(write_file, 'w')
csv_w_file.write('course_id,short_name,long_name\n')

line_count = 0

def get_subaccounts(account):
    subaccounts = account.get_subaccounts(True) # Get all subaccounts in an account
    for subaccount in subaccounts:
        account_id_lst.append(subaccount.id)

def buildLine(course, account):
    try:
        line = str(course.id)
        line += ',' + str(course.course_code)
        line += ',' + str(course.name)
        line += '\n'

        return line
    except:
        print("Course Not Found: " + str(courseID))

def main():
    account_id = input("Enter the root account ID: ")
    account = canvas.get_account(account_id)
    account_id_lst.append(account.id)

    get_subaccounts(account)

    print(account_id_lst)
    print("\nAccount list has been built...\n")

    with open('Proctorio_Courses.csv', 'r', newline='') as course_list:
        reader = csv.reader(course_list, delimiter=',')
        line_count = 0
        for row in reader:
            line_count += 1
            if (line_count % 10) == 0:
                print("Lines Processed: " + str(line_count))
            course_id = row[1]
            if course_id == "context_id":
                print("***********************")
            else:
                #print(course_id)
                course = canvas.get_course(course_id)

                course_account_id = course.account_id
                account = canvas.get_account(course_account_id)

                print(account)

                if course.account_id in account_id_lst:
                    None
                else:
                    line = buildLine(course, account)
                    # print(line)
                    if line != None:
                        csv_w_file.write(line)

if __name__ == "__main__":
    main()