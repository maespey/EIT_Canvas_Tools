from canvasapi import Canvas
import config
import csv

canvas = Canvas(config.API_URL, config.API_KEY)

accountIDs = [6,7,8,9,10,11,12,13,14,15,16,17,18]

filename = "DOE_Admin.csv"

csv = open(filename, "w")
csv.write("username,role,role_id,subaccount\n")

def build_admin_lst(account, mode):

    print("\n_______________________\n" + "Admin's for: " + str(account))
    root_admins = account.get_admins()
    print("*****Root Admins*****\n")

    for admin in root_admins: # Grabs all root level Admin Users
        user = admin.user
        role = admin.role
        print("Name: " + user['login_id'] + " -> Role: " + role)

        csv.write(str(user['login_id'])+","+role+","+str(admin.id)+","+str(account)+"\n")


    if mode == "all":
        subaccounts = account.get_subaccounts(True) # Get all subaccounts in an account
        for subaccount in subaccounts:
            #print("     " + str(subaccount))
            admins = subaccount.get_admins() # Get all Admin Users
            tmp = []
            for admin in admins:
                user = admin.user
                role = admin.role
                # print("      Name: " + user['name'] + " -> Role: " + role)

    else:
        return None


for ID in accountIDs:
    current_account = canvas.get_account(ID)

    build_admin_lst(current_account, "root") # Account, Mode("root" or "all")

print("Your .CSV is done...")