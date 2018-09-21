from canvasapi import Canvas
import config
import csv

canvas = Canvas(config.API_URL, config.API_KEY)

accountIDs = [6,7,8,9,10,11,12,13,14,15,16,17,18]

file_name = "DOE_Admin.csv"

csv = open(file_name, "w")
csv.write("username,role,role_id,subaccount\n")

def build_admin_lst(account, mode):

    print("\n_______________________\n" + "Admin's for: " + str(account))
    root_admins = account.get_admins()
    print("*****Root Admins*****\n")

    for admin in root_admins: # Grabs all root level Admin Objects from Canvas
        print("Name: " + admin.user['login_id'] + " -> Role: " + admin.role) #shows attribs of Admin Object

        csv.write(str(user['login_id'])+","+role+","+str(admin.id)+","+str(account)+"\n")


    if mode == "all": ###  Not currently used   ###
        subaccounts = account.get_subaccounts(True) # Get all subaccounts in an account
        for subaccount in subaccounts:
            #print("     " + str(subaccount))
            admins = subaccount.get_admins() # Get all Admin Objects
            tmp = []
            for admin in admins:
                user = admin.user
                role = admin.role
                # print("      Name: " + user['name'] + " -> Role: " + role)

    else:
        return None

def main():
    for ID in accountIDs:
        current_account = canvas.get_account(ID)

        build_admin_lst(current_account, "root") # Account, Mode("root" or "all")

    print("Your .CSV is done...")

if __name__ == "__main__":
    main()