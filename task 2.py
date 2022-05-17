import random

random_num = random.randint(1,100) #between 1 and 100, including both 1 and 100

#create a function to validate users input
def validate_input(input_num):
    message = ""
    if input_num > 100 or input_num < 1:
        message = "Your guess needs to be within the range 1 to 100"
    return message
    
def check_success(n):
    message = ""
    if n == random_num:
        message = "Correct!"
        success = True
    elif n < random_num:
        message = "Your guess is lower than the target number"
    elif n > random_num:
        message = "Your guess is higher than the target number"
    return message

success = False

while success == False:
    guess = int(input("Please enter your guess: "))
    print(validate_input(guess))
    print(check_success(guess))
    print()