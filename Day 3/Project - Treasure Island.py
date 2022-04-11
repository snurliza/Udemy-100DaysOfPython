name = input("What is your name? ")
print("Hello, " + name + "! Let's start our adventure.")

a = input("You are standing outside of your house. You see a man running towards you and asking for urgent shelter. Will you provide shelter for him?\n").lower()

if a == "yes":
    
    b = input("After two minutes, the police came to your house and ask you that whether the thief is in your house or not. Will you say 'Yes' or 'No'?\n").lower()
    if b == "yes":
        print("You are an honest person. He was a thief and you won the game.")
    else:
        print("You helped the thief. Go to jail. Game over.")

elif a == "no":
    c = input("Now he is trying to kill you. Will you knock him do?\n").lower()
    if c == "yes":
        print("Congrats! He was a thief and you helped the police to catch him with your bravery.").lower()
    else:
        print("Sorry, you are dead. He was a thief and he killed you. Game Over")
else:
    print("Invalid. Game over")