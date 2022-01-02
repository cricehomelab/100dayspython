'''

def my_function():
    result = 3 * 2
    return result

output = my_function()

In the above example it will output the result variable. and will be saved in the "output" variable.

'''

# functions with outputs

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    # print(f"{formated_f_name} {formated_l_name}")
    return f"{formated_f_name} {formated_l_name}"

formated_string = format_name("WILLY", "sMith")
print(formated_string)
print(format_name("Jeff", "SMITH"))