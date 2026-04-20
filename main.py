import random

target = random.randint(1, 100)
userChoice = -1
guesses = 0
print("\n*****Welcome to the NO. Guessing Game*****")
print("------------------------------------------\n")
print("Guess a number between 1 and 100")

while True:
    userChoice = input("Enter your guess (or type exit)🙂: ")

    if userChoice == "exit":
        print("Game ended.")
        break

    if not userChoice.isdigit():
        print("❌Please enter a valid number!")
        continue

    userChoice = int(userChoice)
    guesses += 1

    if  (userChoice == target):
        print(f"🎉Success : You have gussed the number {target} correctly in {guesses} attempts !!")
        break
    elif (userChoice <  target):
        print("📈 Your number was too small. Take a bigger guess..")
    else:
        print("📉Your number was too big. Take a smaller guess..")

    # little hint system
    if abs(userChoice - target) <= 3:
        print("🔥You are very close!")
print("------------GAME OVER-------------")