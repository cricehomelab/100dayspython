'''

Caesar cipher is essentially shifting the letters in a word by several letters of the alphabet

Standard alphabet
a b c d e f g h i j k l m n o p q r s t u v w x y z
alphabet shifted by 5
f g h i j k l m n o p q r s t u v w x y z a b c d e
alphabet shifted by 10
k l m n o p q r s t u v w x y z a b c d e f g h i j

message
hello
ciphered message
rovvy

How to shift the alphabet
1. Create a shifted_alphabet variable.
2. Add the letters to the alphabet according to the shift variable.
    A.

'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount
    # and print the encrypted text.
    # e.g.
    # plain_text = "hello"
    # shift = 5
    # cipher_text = "mjqqt"
    # print output: "The encoded text is mjqqt"
    end_result = ""
    for letter in text:
        # need to account for a space
        if letter != " ":
            # need to account for if the position of the shift is greater than the length of the list.
            if (alphabet.index(letter) + shift) > (len(alphabet) - 1):
                end_result += alphabet[abs((len(alphabet) - 1) - (alphabet.index(letter) + (shift-1)))]
            # this is the "standard case" ie the index position is in the index positions.
            else:
                end_result += alphabet[(alphabet.index(letter) + shift)]
        else:
            end_result += " "
    print(f"the encoded text is {end_result}")


    # HINT: How do you get the index of an item in a list:
    # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    # 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
    '''
    found that there was an index out of bounds error we were getting. Need to account for numbers that are larger than
    the index of the alphabet list. 
    Standard alphabet
    a b c d e f g h i j k l m n o p q r s t u v w x y z
    alphabet shifted by 5
    f g h i j k l m n o p q r s t u v w x y z a b c d e
    
    c i v i l i z a t i o n
    expected
    h n a n q n e f y n t s
    actual
    h n a n q n w f y n t s
    
    my 'z' encryption was not working correctly here. Originally i was using the output of 
    len(alphabet) - 1) - (alphabet.index(letter) + (shift-1)
    This came out to -4 which is a valid position tha came to 'w' not 'e' just not the one I wanted. 
    needed to take the absolute value of this to get the expected outcome. 
    the absolute function abs() was able to help with this. 
    abs((len(alphabet) - 1) - (alphabet.index(letter) + (shift-1)))
    tried a few other words
    zebra
    expected
    e j g w f
    actual
    e j g w f
    
    you
    expected
    d t z
    actual
    d t z
    
    '''

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
encrypt(text, shift)


'''
# Instructor answer
# for the 'civilization' bug issue the solution used by the instructor was to make a second alphabet after the first.
# the index() function only looks for the first occurrence of something. 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Don't change the code above 👆

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
  #TODO-2: Inside the encrypt function, shift each letter of the text forwards in the alphabet by the shift amount and print the encrypted text.  
  #e.g. 
  #plain_text = "hello"
  #shift = 5
  #cipher_text = "mjqqt"
  #print output: "The encoded text is mjqqt"
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"The encoded text is {cipher_text}")

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encrypt(plain_text=text, shift_amount=shift)
'''
