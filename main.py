import random

str_inp = "Hello, from Python"
names = str_inp.split(",")

print(names)

names_string = input("Give me everybody's names, separated by a comma. \n")
names_list = names_string.split(", ")

number = random.randint(0, len(names_list) - 1)                 #need the -1 because list's start at 0 and the len starts at 1
print(names_list)
print(f"The name chosen at random was {names_list[number]}")

random_name = random.choice(names_list)                         #easier way to get random value from name_list
print(random_name)
