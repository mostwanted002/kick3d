import requests
import json
import sys

target = "https://ws2.kik.com/user/{check}"
option = input("Do you want to check a username or userlist? ")


if option == "username":
    check = input("Enter the uid: ")
    r = requests.get(target)
    if r.????contains("firstName:"):
       print(r.json())
    else:
        print("User not found")
elif option == "wordlist":
    wordlist = input("Enter a wordlist: ")
    with open(wordlist, 'r') as f:
        for line in f:
            check = line.strip()
            r = requests.get(target)
            if r.status_code == 200:
                print(r.json())
else:
    print ("Invalid option")
