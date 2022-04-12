import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
length_names = len(names)
random_names = random.randint(0, length_names - 1)

Going_to_pay = names[random_names] 

print(Going_to_pay + "is going to buy the meal today!")





