"""
Jasmine Carrion
jasmine.carrion73@myhunter.cuny.edu
(personal project) 4/28/26
"""

import time

reserved = ["admin", "root", "guest"]

while True:
    user = input("Username: ").strip()
    if len(user) < 4:
        print("invalid: Username must be more than 4 characters long.")
    elif user in reserved:
        print("This username is reserved. Please try another.")
    elif not user.isalnum():
        print("invalid: Only letters and numbers allowed.")
    else:
        print(f"Username {user} accepted!", flush=True)
        time.sleep(3)
        print(f"Welcome {user}!")
        break
