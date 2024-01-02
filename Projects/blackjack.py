# Black Jack Game
import random as random
import time
def greetings():
    print("Welcome to BlackJack")
    
def play_game():
    return input("Would you like to play? [y/n]: ").lower()
    
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
    return input("Would you like another card? (y/n): ").lower()

#---------------------------------------------------------------#
def player_blackjack():
    return "Thats a Blackjack! Player wins!"

def player_busted():
    return "You bust The house wins!"

def dealer_blackjack():
    return "Thats a Blackjack! Dealer wins!"

def dealer_busted():
    return "Dealer bust! Player wins!"
        
 # Function to calculate score       
def calculate_score(hand):
    hand_score = sum(card_value(card) for card in hand)
    if 'A' in hand and hand_score > 21:
        hand_score -= 10
    else:
        print(f"Score: {hand_score}")
    return hand_score
        
    # if player_score == 21:
    #     player_blackjack()
    # elif player_score > 21:
    #     player_busted()
    # return player_score
#---------------------------------------------------------------#

# function to deal cards to player and dealer
def deal_cards():
    dealer_hand = [deck_list()]
    player_hand = [deck_list(), deck_list()]
    return dealer_hand, player_hand
    # print(dealer_hand, player_hand)
def display_hands(dealer_hand, player_hand):
    print("Dealer's hand: ", dealer_hand)
    print("Player's hand: ", player_hand)


def add_card_player_hand(player_hand):
    player_hand.append(deck_list())
    return player_hand
def add_card_dealer_hand(dealer_hand):
    dealer_hand.append(deck_list())
    return dealer_hand

def dealer_turn(dealer_hand, player_hand):
    print("It is dealer's turn to draw a card")
    player_score = calculate_score(player_hand)
    
    # if player hand bust
    if player_score > 21:
        player_busted()
        
    elif calculate_score(dealer_hand) < 17:
        add_card_dealer_hand(dealer_hand)

    # if dealer_score > 21:
    #     dealer_busted()
    # elif dealer_score == 21:
    #     dealer_blackjack()
    # else:
    #     return f"The dealer's final score: {dealer_score}"
def tie():
    return "It's a tie!"

def player_wins():
    return "Player wins!"

def dealer_wins():
    return "Dealer wins!"

def who_wins(dealer_hand, player_hand):
    dealer_score = calculate_score(dealer_hand)
    player_score = calculate_score(player_hand)
    if dealer_score == 21:
        print(dealer_blackjack())
    elif player_score == 21:
        print(player_blackjack())
    elif dealer_score == player_score:
        print(tie())
    elif dealer_score > player_score:
        print(dealer_wins())
    elif player_score > dealer_score:
        print(player_wins())


def main():
    greetings()
    player_choice = play_game()
    
    while player_choice != "n":
        dealer_hand, player_hand = deal_cards()
        display_hands(dealer_hand, player_hand)
        
        if player_choice == 'y':
            while True:
                calculate_score(player_hand)
                add_choice = deal_another_card()
                
                if add_choice == 'y':
                    add_card_player_hand(player_hand)
                    display_hands(dealer_hand, player_hand)
                    
                    if calculate_score(player_hand) > 21:
                        who_wins(dealer_hand, player_hand)
                        break
                elif add_choice == 'n':
                    calculate_score(player_hand)      
                                       
                    dealer_turn(dealer_hand, player_hand)  
                    who_wins(dealer_hand, player_hand)
                    break     
        player_choice = play_game()
                    
                                
    else:
        print("Thank you for playing! Goodbye!")
    

if __name__ == "__main__":            
    main()
        

    