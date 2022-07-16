def guessingGame():
    import random
    r = random.randrange(0, 101)
    winStatus = 0
    while winStatus == 0:
        s = input("Pick a number between 0 and 100 including 0 and 100: ")
        if s.isdigit():
            s = int(s)

            if s > 100:
                print("Please guess a number between 0 and 100 including 0 and 100")

            elif s < r:
                print("Too low, try again.")
                
            elif s > r:
                print("Too high, try again")

            elif s == r:
                winStatus += 1
                return "You have correctly guessed the number!. Congratulations!"
                
        else:
            print("Please guess a number between 0 and 100 including 0 and 100")

print(guessingGame())

hi = True
while hi == True:
    play_again = input("Play again? ")
    print(play_again)
    
    if play_again.lower() == "yes":
        print(guessingGame())
    else:
        hi = False
