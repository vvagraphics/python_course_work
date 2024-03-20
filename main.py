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