'''
Moo Joon Park
Encryption non-PKE
Homework 2
Encoding a message

This program will encode a user-defined message using a reverse alphabetical algorithm. It will find the index value of the letter in the message and match it to the index of the reverse alphabetical list, then print that letter.

The program runs, but there is an issue with encoding special characters and punctuations. It will correctly insert spaces in between words, but it will not return any punctuations or special characters are entered. I would've debugged it if there was more time.
'''

# User defined input for the message to be decoded
message = input("Enter a message to encode: ")
message = message.upper()
print(message)

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ahpla = "ZYXWVUTSRQPONMLKJIHGFEDCBA" # reverse alpha

result = ""

# loop to extract the index values of the original message
# and match them to the letters in the reverse alpha list
for letter in message:
  if letter in alpha:
    letter_index = alpha.find(letter)
    print(ahpla[letter_index], end="")
  else:
    print(" ", end="")
    