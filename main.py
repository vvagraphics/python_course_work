# Day 1

# There are two variables, a and b
# a = input("Bond")
# b = input("James")
# # Create a third variable to help switch the values
# c = a
# a = b
# b = c

# print("a: " + a)
# print("b: " + b)

# There are two variables, a and b
# a = "Bond"
# b = "James"
# # Create a third variable to help switch the values
# c = a
# a = b
# b = c

# # print("a: " + a)
# # print("b: " + b)
# print("a: " + a, "b: " + b)
# print(a + "," + b + " - shaken not stirred")


# # BAND GENERATOR
# #1. Create a greeting for your program.
# print("Welcome to the Band Name Generator.")
# #2. Ask the user for the city that they grew up in.
# city = input("What's the name of the city you grew up in?\n")
# #3. Ask the user for the name of a pet.
# pet = input("What's your pet's name? \n")
# #4. Combine the name of their city and pet and show them their band name.
# print("Your band name could be " + city +" "+ pet)
# #5. Make sure the input cursor shows on a new line:

# Solution: https://replit.com/@appbrewery/band-name-generator-end

# MY Version mix
import time
# John_the_colossus object(name = John the Colossus, city = Sorros)
# player_name object(name= ???, city=??)
class Character:
    def __init__(self, name, city):
        self.name = name
        self.city = city

# Create a John the Colossus object
john = Character("John the Colossus", "Sorros")

# Get player's information 
# player_name = input("What is your name?\n")
# player_city = input("Where are you from?\n")

# Create player object


def display_dialog(speaker, line):
    print(f"{speaker}: {line}")

# print("Hello, Traveller!\n")
# print("I am John the collosos from Sorros\n")
# print("Are you alright? You were laying on the ground\n")
# # add a delay? next font in italics?

# time.sleep(2)

# print("\033[3mYour vision is blurry and slowly comes to. \nYou feel an immense pain at the back of your head. \nYou try to remember how you got here but your mind is blank. \n")
# print("What is your name?\n")

display_dialog("John", "Hello, Traveller!")
time.sleep(3)
display_dialog("John", "I am John the Colossus from Sorros")
time.sleep(1)
display_dialog("John", "Are you alright? You were laying on the ground.")
time.sleep(3)  # Pause for dramatic effect
print("\n \033[3mYour vision is blurry as it slowly clears.")
time.sleep(2)
print(" \nYou feel an immense pain at the back of your head.")
time.sleep(2)
print("\nYou try to remember how you got here but your mind is blank.\033[0m \n")


player_name = input("What is your name? (If you don't remember, type 'Unknown')"+"\n Enter Your Name >>> ").lower()
# while True:
#     print("\b_", end='', flush=True)  # Overwrite with an underscore
#     time.sleep(0.5)
#     print("\b ", end='', flush=True)
player_name = player_name.title() 



if player_name == "unknown":
    display_dialog("John", "That's alright. The blow to your head must have rattled your memory.")
    # You might store a flag like 'name_unknown = True' for later 
else:
    display_dialog("John", f"Well met, {player_name}. Do you remember anything at all?") 

time.sleep(2)

player_city = input("Where are you from? (If you don't remember, type 'Unknown') \n").lower()
player_city = player_city.title() 
if player_city == "Unknown":
    display_dialog("John", "It seems the past is a fog. Perhaps it will return to you in time.")

time.sleep(2)

player = Character(player_name, player_city)