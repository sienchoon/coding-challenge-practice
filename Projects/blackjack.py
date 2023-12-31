# Black Jack Game
import random as random

def deck_list():
    cards = ['A',2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
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

#---------------------------------------------------------------#
def blackjack():
    print("Thats a blackjack!")

def busted():
    print("Thats a bust!")
        
 # Function to calculate score       
def calculate_score(player_hand):
    player_score = sum(card_value(card) for card in player_hand)
    if 'A' in player_hand and player_score >21:
        player_score -= 10
        
    if player_score == 21:
        blackjack()
    elif player_score > 21:
        busted()
    return player_score
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
    player_score = calculate_score(player_hand)
    
    # if player hand bust
    if player_score > 21:
        print("Player bust! Dealer doesn't have to take more cards")
        
    while calculate_score(dealer_hand) < 17:
        add_card_dealer_hand(dealer_hand)
        print("Dealer takes another card.")
        
    display_hands(dealer_hand, player_hand)
    
    dealer_score = calculate_score(dealer_hand)
    
    if dealer_score > 21:
        busted()
        print("The dealer lost, player win!")
    elif dealer_score == 21:
        blackjack()
    else:
        print(f"The dealer's final score: {dealer_score}")

def who_wins(dealer_hand, player_hand):
    dealer_score = calculate_score(dealer_hand)
    player_score = calculate_score(player_hand)
    if dealer_score > 21:
        print("Dealer busts. You win!")
    elif player_score > 21:
        print("You bust. The house wins!")
    elif dealer_score == player_score:
        print("It's a tie! No winner!")
    elif dealer_score > player_score:
        print("The house wins!")
    else:
        print("You win!")

def main():
    print("Welcome to BlackJack Game!")
    print("Would you like to play? [y/n]: ")
    player_choice = " "
    dealer_hand, player_hand = deal_cards()
    while player_choice != "n":
        player_choice = input()
        if player_choice == 'y':
            display_hands(dealer_hand, player_hand)
            calculate_score(player_hand)
            while True:
                print("Would you like another card? (y/n)")
                choice = input()
                if choice == 'y':
                    add_card_player_hand(player_hand)
                    display_hands(dealer_hand, player_hand)
                    if calculate_score(player_hand) > 21:
                        break
                elif choice == 'n':
                    current_score = calculate_score(player_hand)
                    print(f"Current score is: {current_score}")
                    break     
            
            dealer_turn(dealer_hand, player_hand)
            display_hands(dealer_hand, player_hand)
            calculate_score(dealer_hand)  
            who_wins(dealer_hand, player_hand)          
            
                                
        else:
            print("Thank you for playing! Goodbye!")
            break


if __name__ == "__main__":            
    main()
        

    