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
# import time
# # John_the_colossus object(name = John the Colossus, city = Sorros)
# # player_name object(name= ???, city=??)
# class Character:
#     def __init__(self, name, city):
#         self.name = name
#         self.city = city

# # Create a John the Colossus object
# john = Character("John the Colossus", "Sorros")

# Get player's information 
# player_name = input("What is your name?\n")
# player_city = input("Where are you from?\n")

# Create player object


# def display_dialog(speaker, line):
#     print(f"{speaker}: {line}")

# # print("Hello, Traveller!\n")
# # print("I am John the collosos from Sorros\n")
# # print("Are you alright? You were laying on the ground\n")
# # # add a delay? next font in italics?

# # time.sleep(2)

# # print("\033[3mYour vision is blurry and slowly comes to. \nYou feel an immense pain at the back of your head. \nYou try to remember how you got here but your mind is blank. \n")
# # print("What is your name?\n")

# display_dialog("John", "Hello, Traveller!")
# time.sleep(3)
# display_dialog("John", "I am John the Colossus from Sorros")
# time.sleep(1)
# display_dialog("John", "Are you alright? You were laying on the ground.")
# time.sleep(3)  # Pause for dramatic effect
# print("\n \033[3mYour vision is blurry as it slowly clears.")
# time.sleep(2)
# print(" \nYou feel an immense pain at the back of your head.")
# time.sleep(2)
# print("\nYou try to remember how you got here but your mind is blank.\033[0m \n")


# player_name = input("What is your name? (If you don't remember, type 'Unknown')"+"\n Enter Your Name >>> ").lower()
# # while True:
# #     print("\b_", end='', flush=True)  # Overwrite with an underscore
# #     time.sleep(0.5)
# #     print("\b ", end='', flush=True)
# player_name = player_name.title() 



# if player_name == "unknown":
#     display_dialog("John", "That's alright. The blow to your head must have rattled your memory.")
#     # You might store a flag like 'name_unknown = True' for later 
# else:
#     display_dialog("John", f"Well met, {player_name}. Do you remember anything at all?") 

# time.sleep(2)

# player_city = input("Where are you from? (If you don't remember, type 'Unknown') \n").lower()
# player_city = player_city.title() 
# if player_city == "Unknown":
#     display_dialog("John", "It seems the past is a fog. Perhaps it will return to you in time.")

# time.sleep(2)

# player = Character(player_name, player_city)






# DAY 2

# DATA TYPES
# String, Integer, Float, Boolean

# print(123 + 123)
# print("123" + "123")
# print(3.142)
# is_running = True
# print(is_running)
# z = 3 + 5j
# print(type(z))
# person = {"name": "Bob", "age": 30}
# print(type(person))

# # Converting Data Types
# num_str = "15"
# num_int = int(num_str)  # num_int will be 15 (integer)

# price = "39.95"
# price_float = float(price)  # price_float will be 39.95 (float)

# real_part = 2
# imag_part = 5
# complex_num = complex(real_part, imag_part)  # complex_num will be (2+5j) 
# print(type(complex_num))
# print(complex_num)

# number = 58
# number_str = str(number)  # number_str will be "58" (string)

# my_tuple = (1, "hello", 3.14)
# my_list = list(my_tuple)  # my_list will be [1, "hello", 3.14]

# my_list = [5, 6, 7]
# my_tuple = tuple(my_list)  # my_tuple will be (5, 6, 7)

# two_digit_number = 35

# a = str(two_digit_number)[0]
# b = str(two_digit_number)[1]
# print(int(a) + int(b)) //my initial solution after error in vscode

# a = int(two_digit_number[0])
# b = int(two_digit_number[1])
# c = a + b
# print(c)  //error in vscode

# PEMDAS Parenthese Exponents Multiplication Division Addition Subtraction
# 3 + 5
# 7 - 4
# 3 * 2
# #  (gives float)
# 6 / 3
# 2 ** 3
# multiply and divide goes in order of left most

# height = 1.75
# weight = 80

# bmi = weight/(height ** 2)
# print(bmi)//mysolution

# weight_int = int(weight)
# height_float = float(height)
# bmi = weight_int/(height_float ** 2)
# print(bmi)//solution

# # Rounding
# print(round(8 / 3))
# print(round(8 / 3, 2))

# # Floor
# print(8 // 3)

# Previous value 
# score = 0
# score += 1
# score /= 1

# f-String
# f"This is an f-string with {expression}." //so like jquery ish

# name = "Alice"
# age = 30

# greeting = f"Hello, my name is {name} and I am {age} years old."
# print(greeting)  # Output: Hello, my name is Alice and I am 30 years old.

# Years Left Challenge
# age = 15
# x=(90*52)-(52*int(age))

# print(f"You have {x} weeks left.")//my solution

# age = 15
# # Your code below this line 👇
# years = 90 - int(age)
# weeks = years * 52

# print(f"You have {weeks} weeks left.")//solution


# Tip Calculator

# print("Welcome to the tip calculator!")
# bill_Total = float(input("What was the total bill? $ "))
# tip_Amount = float(input("How much tip would you like to give? 10, 12, or 15? "))
# split_Amount = int(input("How many people to split the bill? "))

# calc = float(bill_Total + (bill_Total * (tip_Amount/100))) / int(split_Amount)

# print(f"Each person should pay: {calc}")//my solution


# other solution
# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# people = int(input("How many people to split the bill?"))

# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)


# # FAQ: How to round to 2 decimal places?

# # Find the answer in the Q&A here: https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048


# print(f"Each person should pay: ${final_amount}")




# DAY 3
# CONDITIONAL STATEMENTS
# If Else, 

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height > 120:
#     print("You can ride the rollercoaster")
# else:
#     print("Sorry, you hve to grow taller before you can ride.")

# Comparison Operators
# >,<,>=,<=
    
# EXERCISE
# Which number do you want to check?
# number = int(input())
# number = 8
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# if number % 2 == 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")

# Exercise bmi 2.0
# height = 1.75
# weight = 80
# bmi = weight / (height ** 2)

# if bmi < 18.5:
#   print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#   print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#   print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#   print(f"Your BMI is {bmi}, you are obese.")
# else:
#   print(f"Your BMI is {bmi}, you are clinically obese.")

# Leap Year Exercise
# use flow charts to help with if else

# year = 1900

# if year % 4 == 0:
#   if year % 100 == 0: 
#     if year % 400 == 0: 
#       print("Leap year")
#     else:
#       print("Not leap year")
#   else:
#     print("Leap year")
# else:
#   print("Not leap year")

# rollercoaster
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#   print("You can ride the rollercoaster!")
#   age = int(input("What is your age? "))
#   if age < 12:
#     bill = 5
#     print("Child tickets are $5.")
#   elif age <= 18:
#     bill = 7
#     print("Youth tickets are $7.")
#   else:
#     bill = 12
#     print("Adult tickets are $12.")
  
#   wants_photo = input("Do you want a photo taken? Y or N. ")
#   if wants_photo == "Y":
#     bill += 3
  
#   print(f"Your final bill is ${bill}")

# else:
#   print("Sorry, you have to grow taller before you can ride.")


# Pizza 
# print("Thank you for choosing Python Pizza Deliveries!")
# size = input() # What size pizza do you want? S, M, or L
# add_pepperoni = input() # Do you want pepperoni? Y or N
# extra_cheese = input() # Do you want extra cheese? Y or N
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# bill = 0
# # What size pizza do you want? S, M, or L 
# if size == "S": 
#   bill = 15
#   if add_pepperoni == "Y":
#     bill += 2
# elif size == "M":
#   bill = 20
#   if add_pepperoni == "Y":
#     bill += 3
# elif size == "L":
#   bill = 25
#   if add_pepperoni == "Y":
#     bill += 3
# # Do you want pepperoni? Y or N
# # if add_pepperoni == "Y":
#   # if size == "S":
#   #   bill += 2
#   #   else:
#   #     bill += 3
# # Do you want extra cheese? Y or N
# if extra_cheese == "Y":
#   bill += 1
# print(f"Your final bill is: ${bill}.")

# Logical operators
# A and B
# C or D
# Not


# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#   print("You can ride the rollercoaster!")
#   age = int(input("What is your age? "))
#   if age < 12:
#     bill = 5
#     print("Child tickets are $5.")
#   elif age <= 18:
#     bill = 7
#     print("Youth tickets are $7.")
#   elif age >= 45 and age <= 55:
#     print("Everything is going to be ok. Have a free ride on us!")  
#   else:
#     bill = 12
#     print("Adult tickets are $12.")
  
#   wants_photo = input("Do you want a photo taken? Y or N. ")
#   if wants_photo == "Y":
#     bill += 3
  
#   print(f"Your final bill is ${bill}")

# else:
#   print("Sorry, you have to grow taller before you can ride.")


# Love Calc Exer
# print("The Love Calculator is calculating your score...")
# name1 = "Angela Yu" # What is your name?
# name2 = "Jack Bauer" # What is their name?
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# combo = name1 + name2
# combo_lower = combo.lower()
# t = combo_lower.count("t")
# r = combo_lower.count("r")
# u = combo_lower.count("u")
# e = combo_lower.count("e")

# l = combo_lower.count("l")
# o = combo_lower.count("o")
# v = combo_lower.count("v")
# e = combo_lower.count("e")

# first_digit = t + r + u + e
# last_digit = l + o + v + e

# score = int(str(first_digit) + str(last_digit))
# if (score < 10) or (score > 90):
#   print(f"Your score is {score}, you go together like coke and mentos.")
# elif (score >= 40) and (score <= 50):
#   print(f"Your score is {score}, you are alright together.")
# else:
#   print(f"Your score is {score}.")


# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.") 

# #https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# #Write your code below this line 👇
# choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
# if choice1 == "left":
#   choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
#   if choice2 == "wait":
#     choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
#     if choice3 == "red":
#       print("It's a room full of fire. Game Over.")
#     elif choice3 == "yellow":
#       print("You found the treasure! You Win!")
#     elif choice3 == "blue":
#       print("You enter a room of beasts. Game Over.")
#     else:
#       print("You chose a door that doesn't exist. Game Over.")
#   else:
#     print("You get attacked by an angry trout. Game Over.")
# else:
#   print("You fell into a hole. Game Over.")






# DAY 4
# RANDOM

# import random

# random_int = random.randint(1, 10)
# print(random_int)

# random_float = random.random()
# print(random_float)


# LIST
# data structure

#  banker roulette
# import random
# names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]


# a = random.randint(0, len(names)-1)
# x= names[a]
# print(f"{x} is going to buy the meal today!")


# exercise treasure map
# line1 = ["⬜️", "️⬜️", "️⬜️"]
# line2 = ["⬜️", "⬜️", "️⬜️"]
# line3 = ["⬜️️", "⬜️️", "⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input()  # Where do you want to put the treasure?

# A = [line1[0], line2[0], line3[0]]
# B = [line1[1], line1[1], line1[1]]
# C = [line1[2], line2[2], line3[2]]

# # Process the user's input
# column_letter = position[0].upper()
# row_number = int(position[1]) - 1

# # Determine the correct list to modify
# if column_letter == 'A':
#     map[row_number][0] = 'X'
# elif column_letter == 'B':
#     map[row_number][1] = 'X'
# elif column_letter == 'C':
#     map[row_number][2] = 'X'

# # Print the updated map 
# print(f"{line1}\n{line2}\n{line3}")

# Rock, Paper, Scissors

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

#Write your code below this line 👇
# import random
# computer_choice = [rock, paper, scissors]

# if computer == rock and player == rock print("It is a draw")
#     if computer == rock and player == scissors print("You lose")
# else 
#     print("You win!")


# if computer == paper and player == rock 
#     if computer == rock and player == scissors 
# else 
    


# if computer == scissors and player == rock
#     if computer == rock and player == scissors 
# else 
    

# import random

# def get_computer_choice():
#     choices = ["rock", "paper", "scissors"]
#     return random.choice(choices)

# def get_player_choice():
#     while True:  # Get valid input
#         player_input = input("Choose Rock, Paper, or Scissors: ").lower()
#         if player_input in ["rock", "paper", "scissors"]:
#             return player_input
#         else:
#             print("Invalid input. Please try again.")

# def determine_winner(computer, player):
#     if computer == player:
#         print("It's a draw!")
#     elif (computer == "rock" and player == "scissors") or \
#          (computer == "paper" and player == "rock") or \
#          (computer == "scissors" and player == "paper"):
#         print("You lose!")
#     else:
#         print("You win!")

# # loop
# while True:
#     computer_choice = get_computer_choice()
#     player_choice = get_player_choice()
#     determine_winner(computer_choice, player_choice)

#     play_again = input("Play again? (y/n): ").lower()
#     if play_again != 'y':
#         break


# import random

# def get_computer_choice():
#     choices = ["rock", "paper", "scissors"]
#     return random.choice(choices)

# def get_player_choice():
#     while True:  # Get valid input
#         player_input = input("Choose Rock, Paper, or Scissors: ").lower()
#         if player_input in ["rock", "paper", "scissors"]:
#             return player_input
#         else:
#             print("Invalid input. Please try again.")

# def determine_winner(computer, player):
#     print("Computer chose:", computer)
#     print("You chose:", player)

#     if computer == player:
#         print("It's a draw!")
#     elif (computer == "rock" and player == "scissors") or \
#          (computer == "paper" and player == "rock") or \
#          (computer == "scissors" and player == "paper"):
#         print("You lose!")
#     else:
#         print("You win!")

# # Main game loop
# while True:
#     computer_choice = get_computer_choice()
#     player_choice = get_player_choice()
#     determine_winner(computer_choice, player_choice)

#     play_again = input("Play again? (y/n): ").lower()
#     if play_again != 'y':
#         break




# import random

# rock = '''
#     _______
# ---'   ____)
#        (_____)
#        (_____)
#        (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#        _______)
#        _______)
#        _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#        _______)
#        __________)
#        (____)
# ---.__(___)
# '''

# def get_computer_choice():
#     choices = ["rock", "paper", "scissors"]
#     return random.choice(choices)

# def get_player_choice():
#     while True:
#         player_input = input("Choose Rock, Paper, or Scissors: ").lower()
#         if player_input in ["rock", "paper", "scissors"]:
#             return player_input
#         else:
#             print("Invalid input. Please try again.")

# def determine_winner(computer_choice, player_choice):
#     print("Computer chose:")
#     display_choice(computer_choice)
#     print("You chose:")
#     display_choice(player_choice)

#     if computer_choice == player_choice:
#         print("It's a draw!")
#     # ... rest of the logic to determine the winner

# def display_choice(choice):
#     if choice == "rock":
#         print(rock)
#     elif choice == "paper":
#         print(paper)
#     else:
#         print(scissors)

# # Main game loop
# while True:
#     computer_choice = get_computer_choice()
#     player_choice = get_player_choice()
#     determine_winner(computer_choice, player_choice)

#     play_again = input("Play again? (y/n): ").lower()
#     if play_again != 'y':
#         break

# Day 5
# Loops

# Input a Python list of student heights
# student_heights = input().split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆
  
# # Write your code below this row 👇
# y = 0
# for x(each loop thru) in student_heights:
#   y +=(add = to y) (capture)x
# print(y)

# exercise

# Input a Python list of student heights
# student_heights = input().split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆
  
# # Write your code below this row 👇
# total_height = 0
# for height in student_heights:
#   total_height += height
# print(f"total height = {total_height}")

# number_of_students = 0
# for student in student_heights:
#   number_of_students += 1
# print(f"number of students = {number_of_students}")

# average = round(total_height / number_of_students)
# print(f"average height = {average}")

# Even Sum exer
# target = int(input()) # Enter a number between 0 and 1000
# # 🚨 Do not change the code above ☝️

# # Write your code here 👇

# even_sum = 0
# for numba in range(2,target + 1, 2):
#   even_sum += numba
# print(even_sum)

# # or
# e_sum = 0
# for num in range(1, target + 1):
#   if num % 2 == 0:
#     e_sum += num
# print(e_sum)

# Write your code here 👇
# for num in range(1, 101):
#   if num % 3 == 0 and num % 5 != 0:
#     print ("Fizz")
#   elif num % 5 == 0 and num % 3 != 0:
#     print ("Buzz")
#   elif num % 3 == 0 and num % 5 == 0:
#     print("FizzBuzz")
#   else:
#     print(num)  my solution. have to put fizz buzz first

# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0:
#      print("FizzBuzz")
#     elif num % 3 == 0 and num % 5 != 0:
#      print ("Fizz")
#     elif num % 5 == 0 and num % 3 != 0:
#      print ("Buzz")
#     else:
#      print(num)


#Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# password_letters = random.choice(letters) * nr_letters
# password_symbols = random.choice(symbols) * nr_symbols
# password_numbers = random.choice(numbers) * nr_numbers

# password = password_letters + password_symbols + password_numbers
# print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# password_list = []
# for char in range(nr_letters):
#     password_list.append(random.choice(letters))
# for char in range(nr_symbols):
#     password_list.append(random.choice(symbols))
# for char in range(nr_numbers):
#     password_list.append(random.choice(numbers))

# random.shuffle(password_list)

# password = "".join(password_list)
# print(password)


# Day 6
# loops

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# while not at_goal():
#     if front_is_clear():
#         move()
#     elif right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()

# Day 7
# HangMan

#Step 1 
# import random

# word_list = ["aardvark", "baboon", "camel"]

# #TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# chosen_word = word_list[random.randint(0,2)]
# print(chosen_word)
# # chosen_word = random.choice(word_list) sollution
# #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# guess = input("Guess a letter >>>").lower()
# #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# # for letter in chosen_word: solution
# for letter in chosen_word:
#     if guess in chosen_word:
#         print("right")
#     else:
#         print("wrong")


# import random
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)

# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# #Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"

# #TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
# end_of_game = False

# while not end_of_game:
#     guess = input("Guess a letter: ").lower()

#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter

#     print(display)

#     #Check if there are no more "_" left in 'display'. Then all letters have been guessed.
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")


# import random

# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']

# end_of_game = False
# word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)

# #TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
# #Set 'lives' to equal 6.
# lives = 6

# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# #Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"

# while not end_of_game:
#     guess = input("Guess a letter: ").lower()

#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter

#     #TODO-2: - If guess is not a letter in the chosen_word,
#     #Then reduce 'lives' by 1. 
#     #If lives goes down to 0 then the game should stop and it should print "You lose."
#     if guess not in chosen_word:
#         lives -= 1
#         if lives == 0:
#             end_of_game = True
#             print("You lose.")

#     #Join all the elements in the list and turn it into a String.
#     print(f"{' '.join(display)}")

#     #Check if user has got all letters.
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")

#     #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
#     print(stages[lives])

#     # add a if already guessed variable that prints already guessed.



#Step 5

# import random

# #TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# #Delete this line: word_list = ["ardvark", "baboon", "camel"]
# from hangman_words import word_list

# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)

# end_of_game = False
# lives = 6

# #TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
# from hangman_art import logo
# print(logo)

# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# #Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"

# while not end_of_game:
#     guess = input("Guess a letter: ").lower()

#     #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
#     if guess in display:
#         print(f"You've already guessed {guess}")

#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter

#     #Check if user is wrong.
#     if guess not in chosen_word:
#         #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
#         print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
#         lives -= 1
#         if lives == 0:
#             end_of_game = True
#             print("You lose.")

#     #Join all the elements in the list and turn it into a String.
#     print(f"{' '.join(display)}")

#     #Check if user has got all letters.
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")

#     #TODO-2: - Import the stages from hangman_art.py and make this error go away.
#     from hangman_art import stages
#     print(stages[lives])

#     # addition. just show already guessed and letter and solution no art





# DAY 8
# def greeting (name, location):
#     print(f"Hello {name}")
#     print(f"what is it like in {location}")

# greeting("john", "usa")
# # note always check indentation when debug


# # Write your code below this line 👇
# import math
# def paint_calc(height, width, cover):
#   number_of_cans = (height * width) / cover
#   round_up = math.ceil(number_of_cans)
#   print(f"You'll need {round_up} cans of paint.")



# # Write your code above this line 👆
# # Define a function called paint_calc() so the code below works.   

# # 🚨 Don't change the code below 👇
# test_h = int(input()) # Height of wall (m)
# test_w = int(input()) # Width of wall (m)
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

# Write your code below this line 👇
# def prime_checker(number):
#   if number <= 1:
#     print("It's not a prime number.")
#   elif number == 2:
#     print("It's a prime number.")
#   else:
#     for i in range(2, int(number** 0.5)+1):
#       if number % i == 0:
#         print("It's not a prime number.")
#         return
#     print("It's a prime number.")


# # Angela's solution
# def prime_checker(number):
#   is_prime = True
#   for i  in range(2, number):
#     if number % i == 0:
#       is_prime = False
#   if is_prime:
#     print("It's a prime number.")
#   elif:
#     print("It's not a prime number.")


# # Write your code above this line 👆
    
# #Do NOT change any of the code below👇
# n = int(input()) # Check this number
# prime_checker(number=n)

# Final Project
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# # direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# # text = input("Type your message:\n").lower()
# # shift = int(input("Type the shift number:\n"))

# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(text, shift):
#     #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
#     #e.g. 
#     #plain_text = "hello"
#     #shift = 5
#     #cipher_text = "mjqqt"
#     #print output: "The encoded text is mjqqt"
#     # plain_text = "hello"
#     for i in range(0, len(alphabet)):
#       shift = alphabet[i+shift]
#       cipher_text = f"{text}"
#       print("The encoded text is {text}")
    
    

#     ##HINT: How do you get the index of an item in a list:
#     #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

#     ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
# encrypt("hello", 5)

# solution
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# solution to bug of shifting pass z
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# # my solution
# # if new_position >= len(alphabet):
# #   new_position -= len(alphabet)

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   #  cycle thru and store as x
#   for x in plain_text:
#       position = alphabet.index(x)
#       new_position = position + shift_amount
#       new_letter = alphabet[new_position]
#       cipher_text += new_letter
#   print(f"The encoded text is {cipher_text}")
   

#     #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
#     #e.g. 
#     #plain_text = "hello"
#     #shift = 5
#     #cipher_text = "mjqqt"
#     #print output: "The encoded text is mjqqt"

#     ##HINT: How do you get the index of an item in a list:
#     #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

#     ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# # #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
# # encrypt(plain_text=text, shift_amount=shift)
  
#   # decrypt
# #TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# def decrypt(cipher_text, shift_amount):
#   plain_text = ""
#   for letter in cipher_text:
#     position = alphabet.index(letter)
#     new_position = position - shift_amount
#     plain_text += alphabet[new_position]
#   print(f"The decoded text is {plain_text}")

#   #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
#   #e.g. 
#   #cipher_text = "mjqqt"
#   #shift = 5
#   #plain_text = "hello"
#   #print output: "The decoded text is hello"


# #TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
# if direction == "encode":
#   encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#   decrypt(cipher_text=text, shift_amount=shift)

# Combining all to one function
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))


# def caesar(start_text, shift_amount, cipher_directions):
#   end_text = ""
#   if cipher_directions == "decode":
#           shift_amount *= -1
#   for letter in start_text:
#       position = alphabet.index(letter)
#       # bug make sure if inside for loop doesnt have bugs
#       # if cipher_directions == "decode":
#       #     shift_amount *= -1
#       new_position = position + (shift_amount)
#       end_text += alphabet[new_position]
#   print(f"The {cipher_directions}d text is {end_text}")

# caesar(start_text=text, shift_amount=shift, cipher_directions=direction)



# Final Final caesar maybe
# from art import logo

# print(logo)
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode":
#     shift_amount *= -1
#   for char in start_text:
#     if char in alphabet:
#       position = alphabet.index(char)
#       new_position = position + shift_amount
#       end_text += alphabet[new_position]
#     else:
#       end_text += char
#     #TODO-3: What happens if the user enters a number/symbol/space?
#     #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
#     #e.g. start_text = "meet me at 3"
#     #end_text = "•••• •• •• 3"
#     position = alphabet.index(char)
#     new_position = position + shift_amount
#     end_text += alphabet[new_position]
    
#   print(f"Here's the {cipher_direction}d result: {end_text}")

# #TODO-1: Import and print the logo from art.py when the program starts.

# #TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# #e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# #If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# #Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
# should_continue = True
# while should_continue:
#   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#   text = input("Type your message:\n").lower()
#   shift = int(input("Type the shift number:\n"))

#   #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#   #Try running the program and entering a shift number of 45.
#   #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#   #Hint: Think about how you can use the modulus (%).
#   shift = shift % 26
#   caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
#   result = input("Continue type 'yes' otherwise type 'no'. \n")
#   if result == "no":
#     should_continue = False
#     print("Goodbye")
# input yes > caesar
# input no = bye









# Day 9
# Python Dictionary
programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])