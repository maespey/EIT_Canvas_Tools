from canvasapi import Canvas
import config
import csv


canvas = Canvas(config.API_URL, config.API_KEY)

def getLocalUser(user_id):
    if user_id == None:
        local_user = canvas.get_user(\
            input("Enter the Local UserID from Canvas:")
            )
        print("Here is the user you selected: " + str(local_user))

    else:
        local_user = canvas.get_user(user_id)
    return local_user

def getHawkIDUser(user_id):
    if user_id == None:
        guest_user = canvas.get_user(\
            input("Enter the new Guest HawkID's UserID in Canvas:"))
        print("Here is the user you selected: " + str(guest_user))

    else:
        guest_user = canvas.get_user(user_id)
    return guest_user


##___________________________________________________________________________##

def main():
    if (input("Would like to read from users.csv? (Y/N)  ")\
            in ["Y", "y", "yes", "Yes"]):
        with open('users.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            merge_count = 0
            for row in csv_reader:
                if merge_count == 0:
                    print("\n\nMerging users from users.csv...")
                    merge_count += 1

                else:
                    local_user = getLocalUser(row[0])
                    guest_user = getHawkIDUser(row[1])
                    print(f'  -> merging {local_user} into {guest_user}')
                    local_user.merge_into(guest_user)
                    merge_count += 1

            print(f'{merge_count-1} accounts have been merged on {config.domain}.')


    else:
        more_users = True
        merge_count = 0
        while more_users:
            local_user = getLocalUser()
            guest_user = getHawkIDUser()

            new_user = local_user.merge_into(guest_user)
            print("You have successfully merged the accounts."\
                "\n  -> The merged user is: " + str(new_user)
                )

            if (input("Do you have more to merge? (Y/N)  ")\
                    in ["Y", "y", "yes", "Yes"]):
                more_users = True
            else: more_users = False
            merge_count += 1
            print("")

        print(f"{merge_count} users have been merged\n\n")

if __name__ == "__main__":
    main()