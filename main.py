name = "bro code"

# if(name[0]).islower():
#     name = name.capitalize()


first_name = name[:3].upper()
last_name = name[4:]
last_character = name[-1]
print(first_name)
print(last_name)
print(last_character)

def hello(name1, name2):
   # print("hello " + name)
    print("Hello " + name1 + " " + name2)
    print("have a nice day")

hello("bro", "code")

def customersDetails(age, address, gender,typeofphone):
    print("The customers age is ", str(age))
    print("The customers address is ", address)
    print("The customers gender is ", gender)
    print("The customers typeofphone is ", typeofphone)

customersDetails(32, "Lagos Nigeria", "male", "Iphone")


def multiply(number1, number2):
    return number1 * number2
print(multiply(3,2))


# nested function calls

print(round(abs(float(input("Enter a whole positive number")))))



# scope = the region that a variable is recognized.
# a variable is only available from inside the region it is created

name = "bro"
def displayName():
    name = "code"
    print(name)

displayName()
print(name)



# **kwargs = parameter that will pack all arguments into a dictionary

def hello(**kwargs):
    print("Hello", end= " ")
    for key,value in kwargs.items():
        print(value,end=" ")

hello(Title = "Mr.", first = "Bro", middle = "Dude", last = "code")




# str.format() = optional method that gives users more control
# when displaying output


# {} format field... they act as a placeholder
animal = "cow"
item = "moon"
name = "bro"
#print("The " + animal + " jumped over the " + item)

print("The {} jumped over the {}".format(animal, item))

print("Hello, my name is {:<10}. Nice to meet you".format(name))
print("Hello, my name is {:>10}. Nice to meet you".format(name))
print("Hello, my name is {:^10}. Nice to meet you".format(name))


#formating numbers
#number = 3.14159 # print first two digits after the decimal point
number = 10000


print("The number is {:.2f}".format(number))
print("The number  is {:,}".format(number)) # add comma to the print out
print("The number is {:b}".format(number)) # binary rep of number
print("The number is {:o}".format(number))   # print out as octal number
print("The number is {:X}".format(number))  # print out in hexadecimal



# importing random method

import random
x = random.randint(1,6) # random numbers between 1 and 6
y = random.random()   # random numbers between 0 and 1

myList = ['rock', 'papers', 'scissors']
z = random.choice(myList)

cards = [1,2,3,4,5,6,7,8,9,"J", "K", "K","A"]
random.shuffle(cards)


print(cards)
print(z)
print(y)
print(x)



# exception = events detected during execution that
# interrupt the flow of a program
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator


except ZeroDivisionError as e:
    print(e)
    print("You tried to divide by Zero which is not allowed")

except ValueError as e:
    print(e)
    print("You tried to divide with an invalid literal")

except Exception as e: # this catches any other error in a program
    print(e)
    print("Something went wrong")

else:
    print(result)

finally:   # irrespective of the error, this will always execute
    print("This will always execute")


# File detection = check if file exist or not and location if it exists

import os;

path = "C:\\Users\\HP\\Downloads\\test.txt"

if os.path.exists(path):
    print("That locations exists")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")

else:
    print("That location doesnt exist")


# reading content of a file using python
try:
    with open('C:\\Users\\HP\\Downloads\\test.txt') as file:
        print(file.read())

except FileNotFoundError as e:
    print(e)
    print("You tried looking in the wrong directory")

# writing files in python
text = 'Have  a nice day'

with open('test.txt', 'w') as file:
    file.write(text)


# copying files in python
# copyfile() = copies content of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile('test.txt', 'copy.txt') # (source, destination)


# moving file using python

import os

source = "test.txt"
destination = "C:\\Users\\HP\\desktop"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")

except FileNotFoundError:
    print(source + " was not found")


# deleting files using python

import os

path = 'test.txt'
try:
    os.remove(path)

except FileNotFoundError:
    print("That file was not found")



# rock paper and scissors


import random

while True:
    choices = ['rock', 'papers', 'scissors']

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Rock, papers, or scissors").lower()

    if player == computer:
        print("computer: ", computer)
        print("Player: ", player)
        print("Tie!")

    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("Player: ", player)
            print("You lose!")
        elif computer == "scissors":
            print("computer: ", computer)
            print("Player: ", player)
            print("You win!")

    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("Player: ", player)
            print("You lose!")
        elif computer == "scissors":
            print("computer: ", computer)
            print("Player: ", player)
            print("You lose!")

    play_again = input("Do you want to play again: (Yes/No)").lower()

    if play_again != "Yes":
        break

print("Bye!")
