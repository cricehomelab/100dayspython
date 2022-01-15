# #Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
# Debugger URL
# https://pythontutor.com/visualize.html#mode=display
# If you run this through the list only ends up appending the final item in the original list it goes through which is
# why it only will ever output [26] which is the last number going through new_item = new_item * 2 (IE 13 * 2 = 26)

# fixed code

def mutate_fixed(a_list):
    b_list = []
    for item in a_list:
        new_item_fixed = item * 2
        b_list.append(new_item_fixed)
    print(b_list)


mutate_fixed([1, 2, 3, 5, 8, 13])
