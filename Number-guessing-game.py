import random
n = random.randint(1, 100)
guesses = 0

while True:
    guesses += 1
    a = int(input("Guess the number : "))
    if a == n:
        print(f"You guessed correct number in {guesses} attempts.")
        break
    
    elif a < n:
        print("Higher number....Please.")
    
    else:
        print("Lower number....Please.")

if guesses <= 10:
    print("You have done it in some attempts....this is incredible.")

elif 10 < guesses < 20:
    print("You are doing good....improve it more.")

else:
    print("Too much attempts .... try to lower the attempts count.")

# with open("Hi-score.txt", "w") as f:
#     f.write(str(guesses))

with open("Hi-score.txt","r") as f:
    content = f.read()
    if int(content) < (guesses):
        print("Try to make record...bro")
    elif int(content) > guesses:
        with open("Hi-score.txt", "w") as f:
            f.write(str(guesses))
            print(f"High score is {guesses}")
    else:
        print(f"High score is {content}")

# First make File of Hi-score.txt