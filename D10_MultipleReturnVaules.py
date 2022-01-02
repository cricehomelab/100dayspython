def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    if f_name == "" or l_name == "":
        # this return will only run in the circumstance where there is no first name entered or no last name entered.
        # this will not compete with the other return but still only one return will happen.
        return "Incomplete first or last name"
    # this is the first return assuming first name and last name were entered. 
    return f"{formated_f_name} {formated_l_name}"
    # second return will never get executed if another return runs before it.
    return "This will never run."

print(format_name(input("What is your first name? "), input("What is your last name? ")))