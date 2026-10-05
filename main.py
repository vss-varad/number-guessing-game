import random 


def game():
    comp = random.randint(1,100)

    won = False 

    for i in range(7):
        try :
            user = int(input("Enter no. between 1 and 100 :"))
            if user < 1 or user > 100 :
                print("Please enter a number between 1 and 100")
                continue
        except ValueError :
            print("Please enter a valid number.")
            continue

        if user > comp :
            print("Your guess is too high")
            print("attempts left", 6-i)
        elif user < comp :
            print("Your guess is too low")
            print("attempts left", 6-i)
        else :
            print("You guessed it right") 
            won = True 
            break
    if not won :
        print("Your attempts are over\nYou lost the game\n")
        print("The number was", comp)


    ask = input("Do you want to play again? (y/n) :").lower()
    if ask == 'y' :
        game()
    elif ask == 'n' :
        print("Thanks for playing the game")        



game()
    