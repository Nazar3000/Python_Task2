import re

def validator():
    password = input("Input your password")
    list_of_passwords =password.split(',')
    print(type(list_of_passwords))
    print(list_of_passwords)
    x = True
    for item in list_of_passwords:
        while x:

            if (len(item)<6 or len(item)>12):
                break
            elif not re.search("[a-z]", item):
                break
            elif not re.search("[0-9]", item):
                break
            elif not re.search("[A-Z]", item):
                break
            elif not re.search("[$#@]", item):
                break
            elif re.search("\s", item):
                break
            else:
                print("Valid Password")
                x=False
                continue

    if x:
        print("Not a Valid Password")

validator()