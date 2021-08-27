import random                               #to create random objects

random_integer = random.randint(1, 10)      #setting random number in a specific range
print(random_integer)                       #printing it off

random_float = random.random()              #creating random float between 0.0 and 0.9999999999
print(random_float)                         #printing the value

love_score = random.randint(1,100)          #Based on previous lesson
print(f"You're love score is {love_score}") #print out