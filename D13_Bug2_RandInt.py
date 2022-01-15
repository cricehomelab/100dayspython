# # Reproduce the Bug
'''
Reproduced error:
Traceback (most recent call last):
  File "C:/Users/charl/PycharmProjects/Day13Python/D13_Bug2_RandInt.py", line 8, in <module>
    print(dice_imgs[dice_num])
IndexError: list index out of range

Does not happen all the time.

ISSUE: Lists start at 0 and count up so in this case the "1" image will never print because it is at position 0 and
if 6 is chosen it will be out of range. Need to change the randint range
'''

'''
# Original code: commented out because it will fail sometimes...
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])
'''

#fixed code
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])
