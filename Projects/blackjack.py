# Black Jack Game
import random as random
import time
def greetings():
    print("Welcome to BlackJack")
    
def play_game():
    while True:
        choice = input("Would you like to play? (y/n): ").lower()
        if choice in ['y', 'n']:
            return choice
        else:
            return input("Invalid input. Please enter 'y' or 'n'.")
    
def deck_list():
    cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    return random.choice(cards)

# Value of individual cards in a deck
def card_value(cards):
    if cards == 'A':
        return 11
    elif cards == 'J' or cards == 'Q' or cards == 'K':
        return 10
    else:
        return cards

cards = deck_list()
value = card_value(cards)    
# Check if values are matching 
# print(f'{cards} : {value}') 

def deal_another_card():
    while True:
        choice = input("Would you like another card? (y/n): ").lower()
        if choice in ['y', 'n']:
            return choice
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

#---------------------------------------------------------------#
def player_blackjack():
    return "Thats a Blackjack! Player wins!"

def player_busted():
    return "You bust! The house wins!"

def dealer_blackjack():
    return "Thats a Blackjack! Dealer wins!"

def dealer_busted():
    return "Dealer bust! Player wins!"
        
 # Function to calculate score       
def calculate_score(hand):
    hand_score = sum(card_value(card) for card in hand)
    if 'A' in hand and hand_score > 21:
        hand_score -= 10
    return hand_score
        
def display_score(hand):
    print(f'Your score: {calculate_score(hand)}')      

#---------------------------------------------------------------#

# function to deal cards to player and dealer
def deal_cards(dealer_hand, player_hand):
    dealer_hand = [deck_list()]
    time.sleep(0.5)
    player_hand = [deck_list(), deck_list()]
    time.sleep(0.5)
    return dealer_hand, player_hand
    # print(dealer_hand, player_hand)
def display_player_hands(player_hand):
    print("Player's hand: ", player_hand)
    
def display_dealer_hands(dealer_hand):
    print("Dealer's hand: ", dealer_hand)



def add_card_player_hand(player_hand):
    player_hand.append(deck_list())
    return player_hand
def add_card_dealer_hand(dealer_hand):
    dealer_hand.append(deck_list())
    return dealer_hand

def dealer_turn(dealer_hand):
    print("It is dealer's turn to draw a card")
    time.sleep(0.5)

    while True:    
        if calculate_score(dealer_hand) < 17:
            add_card_dealer_hand(dealer_hand)
            display_dealer_hands(dealer_hand)
            time.sleep(1)
        else:
            break

def tie():
    return "It's a tie!"

def player_wins():
    return "Player wins!"

def dealer_wins():
    return "Dealer wins!"

def who_wins(dealer_hand, player_hand):
    dealer_score = calculate_score(dealer_hand)
    player_score = calculate_score(player_hand)
    print(f"Dealer's score: {dealer_score}")
    print(f"Player's score: {player_score}")
    time.sleep(0.5)
    if dealer_score == 21:
        print(dealer_blackjack())
    elif player_score == 21:
        print(player_blackjack())
    elif dealer_score == player_score:
        print(tie())
    elif player_score > 21:
        print(player_busted())
    elif dealer_score > 21:
        print(dealer_busted())
    elif dealer_score > player_score and dealer_score < 22:
        print(dealer_wins())
    elif player_score > dealer_score and player_score < 22:
        print(player_wins())

def five_below_21(player_hand):
    if calculate_score(player_hand) <= 21 and len(player_hand) == 5:
        print(f"{player_wins()} That's 5 cards under!")

def main():
    greetings()
    time.sleep(1)
    player_choice = play_game()
    
    while player_choice == "y":
        player_blackjack_flag = False 
        dealer_hand, player_hand = deal_cards(dealer_hand=[], player_hand=[])
        display_dealer_hands(dealer_hand)
        display_player_hands(player_hand)
        display_score(player_hand)
        time.sleep(0.5)        
        
        if calculate_score(player_hand) == 21:
            print(player_blackjack())
            player_blackjack_flag = True
                       
        if player_blackjack_flag:
            player_choice = play_game()

        elif player_choice == 'y':
            while True:
                add_choice = deal_another_card()
                
                if add_choice == 'y':
                    player_below_5 = False
                    add_card_player_hand(player_hand)
                    display_dealer_hands(dealer_hand)
                    display_player_hands(player_hand)
                    display_score(player_hand)
                    time.sleep(0.5)
                    
                    if calculate_score(player_hand) == 21:
                        print(player_blackjack())
                        break
                    elif calculate_score(player_hand) > 21:
                        who_wins(dealer_hand, player_hand)
                        break
                    elif five_below_21(player_hand):
                        who_wins(dealer_hand, player_hand)
                        player_below_5 = True
                        break

                    # calculate_score(player_hand)
                elif add_choice == 'n':
                    print(f'Player current score: {calculate_score(player_hand)}')
                    dealer_turn(dealer_hand)
                    print("----------------------------------------------")
                    display_dealer_hands(dealer_hand)
                    display_player_hands(player_hand)
                    print("----------------------------------------------")  
                    time.sleep(0.5)    
                                       
                    who_wins(dealer_hand, player_hand)
                    # calculate_score(player_hand)
                    break     
        
                time.sleep(0.5)
            
        player_choice = play_game()                   
    else:
        print("Thank you for playing! Goodbye!")
    

if __name__ == "__main__":            
    main()
        

    