# strs

# firstName = "Ethan"
# lastName = "Scott"
# fullName = firstName + " " +lastName
# print("Hello" + " " + fullName)

# ints and converting to strs

# age = 14
# age += 2
# print("To be able to drive I must be over the age of " + str(age))

# floats

# height = 130.5
# print(height)
# print(type(height))
# print("To ride the rollercoaster you must be " + str(height) + "cm")

# boolean

# human = True
# print(type(human))
# print("Are you a human? " + str(human))

# grouping variables

# name, age, attractive = "Ethan", 14, True
# print(name)
# print(age)
# print(attractive)

# str methods

# name = "Ethan"
# print(len(name))
# print(name.find("n"))
# print(name.upper())
# print(name.isdigit())
# print(name.isalpha()) [!a space is not alpha]
# print(name.count("E"))
# print(name.replace("E", "e"))
# print(name*3)

# type casting = convert one data type to another type

# x = 3
# y = 1.5
# z = "2"
# y = int(y)
# print(str(x)*3)
# print(int(y))
# print(float(z)*3)
# print("The value of y is "+str(y))

# user input

# print("This program will find your age in 1 year!")
# name = input("What is your name: ")
# age = int(input("What is your age: "))
# age += 1
# print("Hello " + name + ", nice to meet you. In one year you will be " + str(age) + " years old")

# math functions

# import math
# pi = 3.14
# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi,2))
# print(int(math.sqrt(9)))
# x=1
# y=2
# z=3
# print(max(x,y,z))
# print(min(x,y,z))

# str slicing() and indexing[]
# [start:stop:step], start is inclusive, stop is exclusive, if start is blank python will assume 0, if stop is blank python will assume the end

# name = "Ethan Scott"
# firstName = name[0:5]
# lastName = name[6:]
# reversedName = name[::-1]
# print(firstName)
# print(lastName)
# print(reversedName)
# website = "https://www.google.com/"
# slice = slice(8,-1)
# print(website[slice])

# if statements

# age = int(input("How old are you: "))
# if age >= 16:
# import time
# print("You can drive.")
# elif age <= 0:
# print("You haven't been born yet.")
# else:
# print("You cannot drive.")

# logical operators
# you can use not() to make a statement false

# temp = int(input("What is the temperature outside in fahrenheit: "))
# if temp >= 32 and temp <= 85:
# print("That's some great weather. Go outside!")
# elif temp < 32 or temp > 85:
# print("Stay inside that's bad weather.")

# while loop

# while 1 == 1:
# print("This is an infinite loop!")
# name = ""
# while name == "":
# name = input("Enter your name: ")
# print("Hello " + name)

# another way to write

# name = None
# while not(name):
# name = input("Enter your name: ")
# print("Hello " + name)

# for loops = statement that will execute its code a limited amount of time

# for i in range(10):
# print(i+1)
# for i in range(50, 101):
# print(i)
# for i in range(50, 101, 2):
# print("This counts by 2s: " + str(i))
# for name in "Ethan Scott":
# print(name)
# for seconds in range(10, -1, -1):
# print(seconds)
# time.sleep(1)
# print("Happy New Year!")

# nested loops = a loop within a loop

# rows = int(input("How many rows: "))
# columns = int(input("How many columns: "))
# sym = input("Enter a symbol to use: ")
# for i in range(rows):
# for j in range(columns):
# print(sym, end="")
# print()

# loop control statements = change a loops execution from its normal sequence
# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder

# while True:
# name = input("Input your name: ")
# if name != "":
# break
# phoneNumber = "404-323-3246"
# for i in phoneNumber:
# if i == "-":
# continue
# print(i, end="")
# for i in range(1,21):
# if i == 13:
# pass
# else:
# print(str(i) + " ", end="")

# list = used to store multiple items in a single variable

# food = ["pizza", "hamburger", "pasta", "sushi"]
# food[0] = "pudding"
# print(food[0])
# for x in food:
# print(x)
# food.append("icecream")
# food.remove("hamburger")
# food.pop()
# food.insert(0,"cake")
# food.sort()
# food.clear()

# 2D lists = a lists of lists

# drinks = ["soda", "milk", "coffee"]
# dinner = ["hotdog", "steak"]
# dessert = ["icecream", "cake", "pie", "flan"]
# food = [drinks, dinner, dessert]
# print(food)
# print(food[0])
# print(food[1][1])

# tuples = collection which is ordered and unchangeable, used to group related data

# student = ("male", 14, "Ethan Scott")
# print(student.count("male"))
# print(student.index("Ethan Scott"))
# for i in student:
# print(i)
# if 14 in student:
# print("The student's name is Ethan Scott")

# set = collection which is unordered(always random order), unindexed. No duplicate values

# utensils = {"spoon", "fork", "knife"}
# dishes = {"plate", "bowl", "cup", "knife"}
# utensils.add("napkin")
# utensils.remove("spoon")
# utensils.update(dishes)
# dinnerTable = utensils.union(dishes)
# utensils.clear()
# print(utensils.difference(dishes))
# print(utensils.intersection(dishes))
# if not("spoon" in utensils):
# print("We have no spoons sir.")
# for i in utensils:
# print(i)
# for i in dinnerTable:
# print(i)

# dictionary = A changeable, unordered collection of unique key:value pairs, fast because they use hashing, allow us to access a value quickly

#capitals = {"USA": "D.C.", "India": "New Deli", "China": "Beijing", "Russia": "Moscow"}
#capitals.update({"Germany":"Berlin"})
#capitals.update({"USA":"L.A."})
#capitals.pop("China")
#capitals.clear()
#print(capitals["Russia"])
#print(capitals.get("Germany"))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())
#for key, value in capitals.items():
    #print(key, value)

#index operator [] = gives access to a sequence's element (str,list, tuples)

#name = "ethan scott"
#if(name[0].islower()):
    #name = name.capitalize()
#print(name)
#firstName = name[:5]
#lastName = name[6:]
#print(lastName)

# function = a block of code which is executed only when it is called

#def name():
#    print('Ethan')
#name()

#import os

#source = "text.txt"
#destination = "//Users//ashleyscott//Desktop//Coding//Python//Learning-Python//#destination//text.txt"

#try:
#    if os.path.exists(destination):
#        print('There is already a file in the destination.')
#    else: 
#        os.replace(source, destination)
#        print(source + ' was moved.')
#except FileNotFoundError:
#        print(source+" was not found.")

# Modules = others work that can be imported to be used or improve code
# see the document 'message.py' for more information
#from message import *
#Hello()
#Bye()
#help("modules")

# rock paper scissors game
#import random
#choices = [
#    'Rock',
#    'Paper',
#    'Scissors'
#]
#
#print('''|Welcome to the rock paper scissors game|''')
#while True:
#    print('Please select your choice of "rock" "paper" or "scissors"')
#    choice = input('--> ')
#    c = random.randint(0,2)
#    choices[c]
#    if choice == 'rock' and c == 0:
#        print('The bot chose rock so, you tied, try again!')
#        continue
#    if choice== 'rock' and c==1:
#        print('The bot chose paper so, you lost, try again!')
#        continue
#    if choice == 'rock' and c == 2:
#        print('The bot chose scissors so, you won, great job!')
#        break
#    if choice == 'paper' and c == 0:
#        print('The bot chose rock so, you won, great job!')
#        break
#    if choice == 'paper' and c == 1:
#        print('The bot chose paper so, you Tied, try again!')
#        continue
#    if choice == 'paper' and c == 2:
#        print('The bot chose scissors so, you lost, try again!')
#        continue
#    if choice == 'scissors' and c == 0:
#        print('The bot chose rock so, you lost, try again!')
#        continue
#    if choice == 'scissors' and c == 1:
#        print('The bot chose paper so, you won, great job!')
#        break
#    if choice == 'scissors' and c == 2:
#        print('The bot chose scissors so, you tied, try again!')
#        continue
#    if choice != 'scissors' or 'paper' or 'rock':
#        print('That choice is invalid, try again!')

# quiz game

#print('Welcome to the quiz game about Ethan Scott!')
#print('In this game you will answer four questions about Ethan Scott. The amount you get right will #influence how much Ethan loves you. Hint: answer with letters.')
#q1 = input('''Question 1:
#    What is Ethan's favorite game?
#        A. Fortnite
#        B. Minecraft
#        C. Valorant
#        D. Call of Duty
#        --> ''').lower()
#q2 = input('''Question 2:
#    What is Ethan's favorite fruit?
#        A. Strawberries
#        B. Grapes
#        C. Cherries
#        D. Watermelon
#        --> ''').lower()
#q3 = input('''Question 3:
#    What is Ethan's favorite snack?
#        A. Ruffles
#        B. Lays classic
#        C. Doritos
#        D. He does not snack
#        --> ''').lower()
#q4 = input('''Question 4:
#    Who is Ethan's favorite person?
#        A. Himself
#        B. He doesn't have a favorite person
#        C. His mom
#        D. His dad
#        --> ''').lower()
#correct_questions = 0
#if q1 == 'c':
#    correct_questions = correct_questions + 1
#if q2 == 'a':
#    correct_questions = correct_questions + 1
#if q3 == 'c':
#    correct_questions = correct_questions + 1
#if q4 == 'b':
#    correct_questions = correct_questions + 1
#print(f'You got {correct_questions}/4 questions right.')
#if correct_questions != 4:
#    print('The correct answers were: C A C B or Valorant, Strawberries, Doritos, and He doesn\'t have a #favorite person')
#if correct_questions == 0:
#    print('Forget about Ethan\'s love')
#elif correct_questions == 1:
#    print('Ethan can tolerate your presence.')
#elif correct_questions == 2:
#    print('You are somewhat liked by Ethan.')
#elif correct_questions == 3:
#    print('Ethan may often show appreciation towards you.')
#elif correct_questions == 4:
#    print('Ethan loves you very much.')

# Object oriented programming

