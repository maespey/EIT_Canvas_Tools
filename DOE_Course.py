from canvasapi import Canvas
import config
import csv

# def account_check(id):
#     if id == 'DOE_A':
#         accountID = '380'
#     elif id == 'DOE_B':

#     switch(id) {
#         case 'DOE_A': accountID = '380';
#         case 'DOE_B': accountID = '381';
#         case 'DOE_D': accountID = '382';
#         case 'DOE_E': accountID = '383';
#         case 'DOE_G': accountID = '384';
#         case 'DOE_H': accountID = '385';
#         case 'DOE_L': accountID = '386';
#         case 'DOE_M': accountID = '387';
#         case 'DOE_N': accountID = '388';
#         case 'DOE_P': accountID = '389';
#         case 'DOE_R': accountID = '390';
#         case 'DOE_T': accountID = '391';
#         case 'DOE_DCE': accountID = '392';
#     }
#     return(accountID)


canvas = Canvas(config.API_URL, config.API_KEY)

# with open('all_dce_courses.csv', 'r', newline='') as course_list:
#     reader = csv.reader(course_list, delimiter=',')
#     for row in reader:
#         courseID = row[0]
#         accountID = row[1]

#         course = account_check(accountID)
#         print(courseID + ": " + accountID + " -> " + course)

        #course = canvas.get_course(row[1], True)

course = canvas.get_course("DCE1_CLSL2002_0EXW_20148", True)
old = [course]

# course.update(course= {"account_id": "380"})

# course = canvas.get_course("DCE1_CLSL2002_0EXW_20148", True)
# new = [course]

print(old)
# print()
# print(new)