import random #imports the library random, which allows us to generate a random number using their function randint()

random_num = random.randint(1,100) #generates a random number between 1 and 100, including both 1 and 100

#create a function to validate users input
#checks if input not within 1 and 100, if it isn't then it sets message to be a string explaining why the input is invalid
def validate_input(input_num):
    message = "" #initialise the variable message
    if input_num > 100 or input_num < 1:
        message = "Your guess needs to be within the range 1 to 100"
    return message

#create a function to check whether the guess is correct, lower, or higher than the random number
def check_success(n):
    message = "" #initialise the variable message
    if n < random_num:
        message = "Your guess is lower than the target number"
    elif n > random_num:
        message = "Your guess is higher than the target number"
    return message

success = False

while success == False: #continuously asks for input and runs through checks until success is no longer False
    guess = int(input("Please enter your guess: "))
    print(validate_input(guess))
    if guess == random_num:
        print("Correct!")
        success = True #set success to true so it ends the while loop that keeps asking for input
    print(check_success(guess))
    print()
