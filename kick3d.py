import requests
import json
import sys
from types import SimpleNamespace

option = input("Do you want to check a username or userlist? ")

def check_user(uid):
    target = f"https://ws2.kik.com/user/{uid}"
    r = requests.get(target)
    if r.status_code == 200:
        return r.json()

if option == "username":
    uid = input("Enter the uid: ")
    user = check_user(uid)
    if user:
        print(user)
    else:
        print("user not found")
elif option == "userlist":
    userlist = input("Enter a userlist: ")
    output = "valid.txt"
    with open(userlist, 'r') as f:
        for line in f:
            uid = line.strip()
            user = check_user(uid)
            if user:
                with open(output, "a") as v:
                    v.write(f"{user}\n")
    print(f"valid users were written to {output}")
else:
    print ("Invalid option")
