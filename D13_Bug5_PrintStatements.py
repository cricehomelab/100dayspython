# #Print is Your Friend
'''
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

# The above example will print out 0

# using print statements to narrow down the issue
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
print(pages)
word_per_page == int(input("Number of words per page: "))
print(word_per_page)
total_words = pages * word_per_page
print(total_words)
'''

# from the above example after we ask for words per page it always prints out "0" as the answer.

# Fixed code
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
# our fix is to make "words_per_page =" it was previously "words_per_page =="
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)