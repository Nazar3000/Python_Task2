import re


def input_password():
    """A function that accepts a comma separated list of passwords
    from console input.
    :return: password: Password string"""

    password = input("Input your passwords: ")
    password_validator(password)

    return password


def password_validator(password):
    """A function that accepts a string of passwords.
    Validates a string of passwords and splits them into two lists
    that have passed validation and are not valid.
    :param password:"password1, passwor2"
    :return: (valid_output_list, false_output_list), password lists"""

    list_of_passwords = password.split(',')

    valid_output_list = []
    false_output_list = []
    for item in list_of_passwords:
        x = True
        while x:

            if (len(item) < 4 or len(item) > 6):
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
            elif not re.search("[*#+@]", item):
                false_output_list.append(item)
                break
            elif re.search("\s", item):
                false_output_list.append(item)
                break
            else:

                valid_output_list.append(item)

                x = False
                break

    output_print(valid_output_list, false_output_list)
    return valid_output_list, false_output_list


def output_print(valid_output_list, false_output_list):
    """A function that turns a list into a string with a delimiter ",".
    Prints lists to the console.
    :param valid_output_list: ['password1', 'passwor2']
    :param false_output_list: ['password1', 'passwor2']
    :return:(password1, passwor2) password strings"""

    valid_output_list = ",".join(valid_output_list)
    if false_output_list:
        false_output_list = ",".join(false_output_list)
    if valid_output_list:
        print(f"List of Valid Passwords: {valid_output_list}")
    if false_output_list:
        print(f"List of Not Valid Passwords: {false_output_list}")
    return valid_output_list, false_output_list


input_password()
