alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
'''
This was my original attempt at this which does work, but as I watched the solution it looks like there is a different 
approach to reorganization that is being looked at. 

def caesar(direction, message, shift_amount):
    plain_text = ""
    cipher_text = ""
    if direction == "encode":
        plain_text = message
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            cipher_text += alphabet[new_position]
        print(f"The encoded text is {cipher_text}")
    elif direction == "decode":
        cipher_text = message
        for letter in cipher_text:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            plain_text += alphabet[new_position]
        print(f"The decoded text is {plain_text}")


# second attempt after watching to about 3:00 in the video.
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction == "encode":
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        elif cipher_direction == "decode":
            new_position = position - shift_amount
            end_text += alphabet[new_position]
    print(f"The decoded text is {end_text}")
'''

# my solution is 10 lines of code, the instructor solution is 9 lines.

# instructor solution

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
      shift_amount *= -1
  for letter in start_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    end_text += alphabet[new_position]
  print(f"Here's the {direction}d result: {end_text}")



#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
# caesar(direction=direction, message=text, shift_amount=shift)
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
