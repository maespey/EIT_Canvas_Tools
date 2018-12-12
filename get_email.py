import config
import requests
import json
import csv

filename = "Canvas_Email_AdminID.csv"

csv_file = open(filename, 'w')
csv_file.write('canvas_id,login_id,email\n')

headers = {'Authorization' : 'Bearer ' + '%s' % config.API_KEY}


def build_line(canvas_id):
    #print(courseID)
    try:
        url = config.API_URL + 'api/v1/users/' + canvas_id
        results = requests.get(url, headers = headers)
        response = results.text
        user = json.loads(response)

        email = user['email']
        hawk_id = user['login_id']

        line = canvas_id
        line += ',' + hawk_id
        line += ',' + email + '\n'

        return line
    except:
        print("Email Not Found: " + str(canvas_id))
        return None

def build_file():
    with open('adminID.csv', 'r', newline='') as user_list:
        reader = csv.reader(user_list, delimiter=',')
        for row in reader:
            canvas_id = row[0]

            line = build_line(canvas_id)

            if line != None:
                csv_file.write(line)
    print("done processing lines...")

def main():
    build_file()

if __name__ == "__main__":
    main()