#main.py
# main.py
import random
import time
#Print the first two things
print("Welcome to the game of Blackjack! In this game, you will be dealt two cards to start. Your goal is to get as close to 21 as possible without going over - or busting! In this game, Jack, Queen, and King are each worth 10 and the Ace is worth 1 or 11.")
print("\nThe dealer will first ask your to hit (take another card) or stay. As long as you don't bust, once you decide to stay, the dealer will then play his hand. THe dealer always has to hit until his hand is at least 17. Whoever has the better hand at the end wins!")
#Make the list and the dictionary which puts all the varibles in a list and puts numbers as meanings for the face cards
faceCards = {"Queen":10, "King": 10, "Jack":10}
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
enter = input("\nPress Enter to start playing: ")
while True:
    y = 0
    x = 0
    playerHand = []
    dealerHand = []
    for i in range(2):
        num = random.randint(0, 12)
        playerHand.append(cards[num])
    print("\nHere is your hand: ")
    print(playerHand)
    #Make a second loop which asks to hit or stay
    while True:
        hitorstay = input("Type in H to hit or S to stay: ")
        #If the person hits, add another random number to the hand
        if hitorstay == str("H"):
            x = 0
            num = random.randint(0, 12)
            playerHand.append(cards[num])
            print("\nHere is your hand: ")
            print(playerHand)
            #add all the numbers together to see if they are greater than 21
            for nums in playerHand:
                #A loop for if the number is in face cards or if it is a number then adding it
                if nums in faceCards:
                    x = x + faceCards[nums]
                elif nums == 1 or nums == 2 or nums == 3 or nums == 4 or nums == 5 or nums == 6 or nums == 7 or nums == 8 or nums == 9 or nums == 10:
                    x = x + int(nums)
                #If it is an ace, before, it added all the other "cards" so if the number is above 10, it will add 1 but if the number is below 10 it will add eleven
            for nums in playerHand:
                if nums == str("Ace"):
                    if x < 10:
                        x = x + 11
                    elif x > 10:
                        x = x + 1
            print(x)
            #if the sum of the hand is greater than 21, say that the player busted and end the second loop
            if x > 21:
                print("You busted (ಥ﹏ಥ)")
                enter = input("\nPress Enter to play again! ")
                break
            #if they stay add two random nmbers to the dealers hand then print it
        elif hitorstay == str("S"):
            x = 0
            for nums in playerHand:
                #A loop for if the number is in face cards or if it is a number then adding it
                if nums in faceCards:
                    x = x + faceCards[nums]
                elif nums == 1 or nums == 2 or nums == 3 or nums == 4 or nums == 5 or nums == 6 or nums == 7 or nums == 8 or nums == 9 or nums == 10:
                    x = x + int(nums)
                    #If it is an ace, before, it added all the other "cards" so if the number is above 10, it will add 1 but if the number is below 10 it will add eleven
            for nums in playerHand:
                if nums == str("Ace"):
                    if x < 10:
                        x = x + 11
                    elif x > 10:
                        x = x + 1
            y = 0
            print("Dealer's turn")
            print("\nHere is the dealer's hand: ")
            for m in range(2):
                num = random.randint(0, 12)
                dealerHand.append(cards[num])
            print(dealerHand)
            #Start a third loop that adds to the dealers hand until it is greater than 17
            while True:
                y = 0
                for nums in dealerHand:
                #A loop for if the number is in face cards or if it is a number then adding it
                    if nums in faceCards:
                        y = y + faceCards[nums]
                    elif nums == 1 or nums == 2 or nums == 3 or nums == 4 or nums == 5 or nums == 6 or nums == 7 or nums == 8 or nums == 9 or nums == 10:
                        y = y + int(nums)
                    #If it is an ace, before, it added all the other "cards" so if the number is above 10, it will add 1 but if the number is below 10 it will add eleven
                for nums in dealerHand:
                    if nums == str("Ace"):
                        if y < 10:
                            y = y + 11
                        elif x > 10:
                            y = y + 1
                #If the number is less than seventeen add a random number
                if y < 17:
                    y = 0
                    num = random.randint(0, 12)
                    dealerHand.append(cards[num])
                    time.sleep(2)
                    print("\nThe dealer hit. Here is the dealer's new hand: ")
                    print(dealerHand)
                    y = 0
                    for nums in dealerHand:
                        #A loop for if the number is in face cards or if it is a number then adding it
                        if nums in faceCards:
                            y = y + faceCards[nums]
                        elif nums == 1 or nums == 2 or nums == 3 or nums == 4 or nums == 5 or nums == 6 or nums == 7 or nums == 8 or nums == 9 or nums == 10:
                            y = y + int(nums)
                        #If it is an ace, before, it added all the other "cards" so if the number is above 10, it will add 1 but if the number is below 10 it will add eleven
                    for nums in dealerHand:
                        if nums == str("Ace"):
                            if y < 10:
                                y = y + 11
                            elif x > 10:
                                y = y + 1
                    print(y)
                
                #If the number is greater than seventeen but less than twenty one say that the dealer has finalized his hand
                if y > 17 and y < 22:
                    time.sleep(2)
                    print("The dealer has finalized his hand.")
                    break
                #If the number is greater than twentyone say that the dealer busted
                elif y > 21:
                    print("The dealer busted! ♪~ ᕕ(ᐛ)ᕗ")
                    print(y)
                    enter = input("\nPress Enter to play again! ")
                    break
            #If the dealers hand is greater than the player's and is less than 21 say that the dealer won
            if y > x and y < 21:
                print("The dealer won. (ಥ﹏ಥ)")
                enter = input("\nPress Enter to play again! ")
                break
            #If The players hand is greater than the dealers, say that the play won
            elif x > y:
                print("You win! ♪~ ᕕ(ᐛ)ᕗ")
                enter = input("\nPress Enter to play again! ")
                break
            #if the player's hand and the dealrs hand is the same, say that it is a tie
            elif int(x) == int(y):
                print("It's a tie!")
                enter = input("\nPress Enter to play again! ")
                break
            #if it is an else, like the dealer busted just break the loop
            else:
                break
            #If the input of an H or an S was not an H or an S just write invalid Input
        else:
            x = 0
            print("Invalid Input")