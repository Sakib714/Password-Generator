import random


print('Welcome to password generator:') # WElcome Note


# Random Character
charecters = 'qweryuioplkjhdsaazxcvbnmQWERTYUIOPLKJHGFAAZXXCCVBNM123456789@#$%&*'


# User Input
how_many = int(input('How many password do you want to generate: '))
length = int(input("Enter the length of your password: "))

# Password Generation Process
for i in range(how_many):

    password = ''

    for i in range(length):
        
        password += random.choice(charecters)
        i+=1

    print(password)
