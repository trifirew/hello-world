import random
import string

print("Guess Number")
print("By: trifirew")


print()
minn = int(input("What is the minimum number for you to guess? "))
maxn = int(input("What is the maximum number for you to guess? "))
print()
print("You will be guessing a number between " + str(minn) + " and " + str(maxn))
print("START!")
rightn = random.randrange(minn, maxn)
time = 0
#print(rightn)

while True:
    print()
    guessn = int(input("Guess the number: "))
    time += 1
    print("You have tried for " + str(time) + " times")
    if guessn < rightn:
        print("The number you guess is too SMALL! Try a LARGER number!")
    elif guessn > rightn:
        print("The number you guess is too LARGE! Try a SMALLER number!")
    else:
        print("YOU ARE RIGHT! THE NUMBER IS " + str(rightn))
        break

print("Game over")
