import re

def validator():
    password = input("Input your password")
    list_of_passwords =password.split(',')


    output_list=[]
    false_output_list = []
    for item in list_of_passwords:
        x = True
        while x:

            if (len(item)<6 or len(item)>20):
                false_output_list.append(item)
                break
            elif not re.search("[a-z]", item):
                false_output_list.append(item)
                break
            elif not re.search("[0-9]", item):
                false_output_list.append(item)
                break
            elif not re.search("[A-Z]", item):
                false_output_list.append(item)
                break
            elif not re.search("[$#@!]", item):
                false_output_list.append(item)
                break
            elif re.search("\s", item):
                false_output_list.append(item)
                break
            else:

                output_list.append(item)

                x=False
                break
    print(output_list)
    print(false_output_list)
    return output_list, false_output_list






validator()