#main.py
# main.py
import random, time, pygame, os

pygame.init()

os.system('cls')

WIDTH, HEIGHT = 900, 700
window = pygame.display.set_mode((WIDTH, HEIGHT))

TITLE_FONT = pygame.font.SysFont('elephant', 80)
SUBTITLE_FONT = pygame.font.SysFont('elephant', 40)

#FUNCTION TO ADD VALUE OF CARDS
def add_card_total(hand):
    total = 0

    for nums in hand:
        if nums in faceCards:
            total = total + faceCards[nums]
        elif nums in range(1, 11):
            total = total + int(nums)
            
    #If it is an ace, before, it added all the other "cards" so if the number is above 10, it will add 1 but if the number is below 10 it will add eleven
    for nums in hand:
        if nums == str("Ace"):
            if total < 10:
                total += 11
            else:
                total += 1
    
    return total


instructions =  """Welcome to the game of Blackjack! In this game, you will be dealt two cards to start. Your goal is to get as close to 21 as possible without going over - or busting! In this game, Jack, Queen, and King are each worth 10 and the Ace is worth 1 or 11.
                The dealer will first ask your to hit (take another card) or stay. As long as you don't bust, once you decide to stay, the dealer will then play his hand. THe dealer always has to hit until his hand is at least 17. Whoever has the better hand at the end wins!"""

#Make the list and the dictionary which puts all the varibles in a list and puts numbers as meanings for the face cards
faceCards = {"Queen":10, "King": 10, "Jack":10}
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

background_color = (255, 255, 255)

user_stickers = []

#IMAGES
sticker_imgs = [pygame.image.load("images\dice_chips_sticker.png")]

cards_imgs = {'Ace': pygame.image.load("cards/ace.png"), 2: pygame.image.load("cards/2.png"), 3: pygame.image.load("cards/3.png"), 4: pygame.image.load("cards/4.png"), 5: pygame.image.load("cards/5.png"), 6: pygame.image.load("cards/6.png"), 7: pygame.image.load("cards/7.png"), 8: pygame.image.load("cards/8.png"), 9: pygame.image.load("cards/9.png"), 10: pygame.image.load("cards/10.png"), 'Jack': pygame.image.load("cards/jack.png"), 'Queen': pygame.image.load("cards/queen.png"), 'King': pygame.image.load("cards/king.png"),}

game_over = False
dealer_run = True

run = True
while run:
    game_over = False

    dealer_total = 0
    player_total = 0
    
    playerHand = []
    dealerHand = []

    #GET ORIGINAL PLAYER HAND
    # card_x = 0
    # for i in range(2):
    #     num = random.randint(0, 12)
    #     playerHand.append(cards[num])
    #     window.blit(cards_imgs[cards[num]], (card_x, 0))
    #     card_x += 50
    
    playerHand.append(cards[2])
    playerHand.append(cards[3])


    pygame.display.flip()
    #Make a second loop which asks to hit or stay
    while True:
        window.fill(background_color)
        mouse_pos = [-1,-1]

        #DISPLAY HIT/STAY TEXT
        hit_text = SUBTITLE_FONT.render("HIT", 5, (0,0,0))
        hit_text_box = window.blit(hit_text, (WIDTH/4 - hit_text.get_width()/2, 650))

        stay_text = SUBTITLE_FONT.render("STAY", 5, (0,0,0))
        stay_text_box = window.blit(stay_text, (WIDTH/4*3 - hit_text.get_width()/2, 650))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                mouse_pos = event.pos

        #DISPLAY CARDS FOR PLAYER
        card_x = 0
        for i in playerHand:
            window.blit(cards_imgs[i], (card_x, 0))
            card_x += 200

        #If the person hits, add another random number to the hand
        if hit_text_box.collidepoint(mouse_pos):
            player_total = 0
            num = random.randint(0, 12)
            playerHand.append(cards[num])


            player_total = add_card_total(playerHand)

            #if the sum of the hand is greater than 21, say that the player busted and end the second loop
            if player_total > 21:
                player_busted_text = TITLE_FONT.render("You Busted!", 5, (0,0,0))
                game_over = True
                pygame.display.quit()
                break

        #if they stay add two random numbers to the dealers hand then print it
        elif stay_text_box.collidepoint(mouse_pos):
            dealer_total = 0

            dealerHand.append(cards[2])
            dealerHand.append(cards[3])
            # card_x = 0
            # for m in range(2):
            #     num = random.randint(0, 12)
            #     dealerHand.append(cards[num])
            #     window.blit(cards_imgs[cards[num]], (card_x, 350))
            #     card_x += 200

            pygame.display.flip()

            #Start a third loop that adds to the dealers hand until it is greater than 17
            while dealer_run:
                print('test')
                window.fill(background_color)
                mouse_pos = [-1,-1]
                dealer_total = add_card_total(dealerHand)

                #If the number is less than seventeen add a random number
                if dealer_total <= 17:
                    print('less than 17')
                    num = random.randint(0, 12)
                    dealerHand.append(cards[num])
                    # time.sleep(.5)
                    card_x = 0
                    for i in dealerHand:
                        window.blit(cards_imgs[i], (card_x, 350))
                        card_x += 200

                    print(dealer_total, dealerHand)
                    dealer_total = add_card_total(dealerHand)

                
                #If the number is greater than seventeen but less than twenty one say that the dealer has finalized his hand
                elif dealer_total > 17 and dealer_total < 22:
                    print("17-21")
                    print(dealer_total, dealerHand)
                    card_x = 0
                    for i in dealerHand:
                        window.blit(cards_imgs[i], (card_x, 350))
                        card_x += 200
                    dealer_run = False

                #If the number is greater than twentyone say that the dealer busted
                elif dealer_total > 21:
                    # win_lose_text = TITLE_FONT.render("Dealer Busted!", 5, (0,0,0))
                    print('gameover')
                    dealer_run = False
                    game_over = False
                    # user_stickers.append(random.choice(sticker_imgs))

        card_x = 0
        for i in dealerHand:
            window.blit(cards_imgs[i], (card_x, 350))
            card_x += 200

            # #If the dealers hand is greater than the player's and is less than 21 say that the dealer won
            # if dealer_total > player_total and dealer_total < 21:
            #     win_lose_text = TITLE_FONT.render("Dealer Won", 5, (0,0,0))
            #     game_over = False
            #     break

            # #If The players hand is greater than the dealers, say that the play won
            # elif player_total > dealer_total:
            #     win_lose_text = TITLE_FONT.render("You Win!", 5, (0,0,0))
            #     game_over = False
            #     user_stickers.append(random.choice(sticker_imgs))
            #     break

            # #if the player's hand and the dealrs hand is the same, say that it is a tie
            # elif int(player_total) == int(dealer_total):
            #     win_lose_text = TITLE_FONT.render("Tie!", 5, (0,0,0))
            #     game_over = False
            #     break

            # #if it is an else, like the dealer busted just break the loop
            # else:
            #     game_over = False
            #     break

        # if game_over == True:
            # window.blit(win_lose_text, (WIDTH/2 - player_busted_text.get_width()/2, HEIGHT/2 - player_busted_text.get_height()/2))


        pygame.display.flip()
    
    pygame.display.flip()

pygame.quit()



# NOTES:
# ADD TEXT FOR "DEALERS HAND" AND "PLAYERS HAND"

