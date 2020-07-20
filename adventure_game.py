import time
import random

# list for places playes will visit
places = ["field", "cave", "house"]

# lise of weapons player can use
weapons = ["trusty (but not very effective) dagger.", "magic potion", "rock"]

# list of enemies
enemy = ["wicked_fairie", "wolf", "bear"]


# function to ask to reaped the game or not
def repeat():
    time.sleep(1)
    print("the game has ended and will reset")


# fight function
def fight():
    attack = input("will you fight them? (y/n)")
    if attack == "y":
        print("you have won!")
        repeat()
    elif attack == "n":
        print("they have chased you and you lost!")
        repeat()
    else:
        print("please etnter a valid answer")


# function for the feild
def field():
    print(
        "You find yourself standing in an open field, ",
        "filled with grass and, yellow wildflowers."
        )
    time.sleep(2)
    print(
        "Rumor has it that a wicked fairie is somewhere around here, and has",
        "been terrifying the nearby village."
    )
    time.sleep(2)
    print("In front of you is a house.")
    time.sleep(2)
    print("To your right is a dark cave.")
    time.sleep(2)
    print("In your hand you have your " + random.choice(weapons))
    time.sleep(2)
    where_to_go = input(
            "Enter 1 to knock on the door of the house." +
            "\nEnter 2 to peer into the cave"
        )
    if where_to_go == "1":
        house()
    elif where_to_go == "2":
        cave()
    else:
        print("please choose either 1 or 2!")


# function for the house
def house():
    print("no one answers, so you walk inside the house, and look around")
    time.sleep(2)
    print(
        "once you entered the living room, ",
        "you heard a noise coming from the kitchen"
        )
    time.sleep(2)
    print(
        "you followed the noise to findout there is a ",
        random.choice(enemy) + " inside"
        )
    fight()


# function for the cave
def cave():
    print("when you peeked into the cave, u found 2 paths ahead of you")
    choice = input("would you go in? (y/n) ")
    if choice.lower().strip() == "y":
        Choose_path = input(" will you go right or left?")
        if Choose_path == "right":
            print("you walked right into an edge then fell and died")
            time.sleep(1)
            repeat()

        elif Choose_path == "left":
            print("OMG! infront of you is the cave's " + random.choice(enemy))
            fight()
        else:
            print("please enter a valid answer (left/right)")
            left_or_right()

    elif choice.lower().strip() == "n":
        print("u are back at the begining")
        field()


# function to repeat the quetsion if no valid answer were given
def left_or_right():
    Choose_path = input(" will you go right or left?")
    if Choose_path == "right":
        print("you walked right into an edge then fell and died")
        time.sleep(1)
        print("now the game will reset")

    elif Choose_path == "left":
        print("OMG! infront of you is the cave's " + random.choice(enemy))
        fight()
    else:
        print("please enter a valid answer (left/right)")
        left_or_right()


while True:
    answer = input("Would you like to play? (y/n) ")
    if answer.lower().strip() == "y":
        name = input("Please enter your name: ")
        print(
            f"Greetings {name}! welcome to our adventure game, ",
            "you will face several situations, ",
            "where you will need to make a choice!",
            " \n choose wisley so you can win!"
            )
        time.sleep(2)
        field()
    elif answer == "n":
        print("That is too bad !")
        break

    else:
        print("please enter a valid answer")
