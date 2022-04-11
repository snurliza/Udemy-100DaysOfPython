# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_lower_case = name1.lower()
name2_lower_case = name2.lower()

t = name1_lower_case.count("t") + name2_lower_case.count("t")
r = name1_lower_case.count("r") + name2_lower_case.count("r")
u = name1_lower_case.count("u") + name2_lower_case.count("u")
e = name1_lower_case.count("e") + name2_lower_case.count("e")
l = name1_lower_case.count("l") + name2_lower_case.count("l")
o = name1_lower_case.count("o") + name2_lower_case.count("o")
v = name1_lower_case.count("v") + name2_lower_case.count("v")
e = name1_lower_case.count("e") + name2_lower_case.count("e")

total_true = t + r + u + e 
total_love = l + o + v + e
love_score = str(total_true) + str(total_love)

if int(love_score) <= 10 or int(love_score) >= 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif int(love_score) >= 40 and int(love_score) <=50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
