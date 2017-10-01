def general_validator(text):

    error = 0

    if text == "":
        error = 'You forgot to put your information'
    elif len(text) < 3 or len(text) > 20:
        error = 'Must be between 3-20 characters'
    elif " " in text:
        error = "Can't include spaces"

    return error


def verify_pw_validator(password, verify_password):

    error = 0

    if verify_password != password:
        error = "Password doesn't match"

    return error


def email_validator(email):

    error = 0

    if email == "":
        return error

    if len(email) < 3 or len(email) > 20:
        error = 'Email must be between 3-20 characters'
        return error 

    sp_counter = 0
    at_counter = 0
    pd_counter = 0

    for ch in email:
        if ch == " ":
            sp_counter += 1
        if ch == "@":
            at_counter += 1
        if ch == ".":
            pd_counter += 1

    if sp_counter != 0 or at_counter != 1 or pd_counter != 1:
        error = "Email address must contain one '@', one '.', and no spaces"

    return error