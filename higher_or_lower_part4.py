#Asks the user to input a number
print("Please enter a number between 0 and 10.")
player_number = input()

#Generates a random number between 1 and 10
from random import randrange
computer_number = randrange(1,10,1)

#The function prints out the two numbers, compares them, and tells the user if they won the game
def higher_or_lower(x, y):

    print("Your number was: ", x)
    print("The computer's number was: ", y)

    if(x>y):
        print("Sorry, your number was too big.")
    elif(x<y):
        print("Sorry, your number was too small.")
    else:
        print("Congratulations, you win! :)")

higher_or_lower(int(player_number), computer_number)

#Asks the user to play again if they were wrong
while (player_number != computer_number):
    play_again = input("Would you like to try again? Enter y/n")
    if (play_again == "y" or play_again == "Y"):
        player_number = input("Enter your new number")
        computer_number = randrange(1,10,1)
        higher_or_lower(int(player_number), computer_number)
    else:
        print("Ok, have a nice day!")
        player_number = computer_number
