import random

user_cards = []
comp_cards = []
is_game_over = False

def deal_card():
    """"returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """takes a list of cards and calculates the score of them"""
    if len(cards) == 2 and sum(cards) ==21:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score , comp_score):
    if user_score > 21 and comp_score > 21:
        return "you went over, you lose."
    elif user_score == comp_score:
        return "draw!"
    elif comp_score == 0 :
        return "you lose, computer has blackjack."
    elif user_score == 0 :
        return "win with a blackjack."
    elif user_score > 21:
        return "You went over. You lose."
    elif comp_score > 21:
        return "Opponent went over. You win."
    elif user_score > comp_score:
        return "You win."
    else:
        return "You lose."
def play_game():
    for i in range(0,2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())
    is_game_over = False
    while not is_game_over:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)
        print(f"    your cards are: {user_cards} and your current score is: {user_score}" )
        print(f"    first card of computer is: {comp_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True

        #while game isnt over ask the user if they want to hit a card or stand
        user_should_deal =input("type 'H' to hit another card and type 'S' to stand: ").lower()
        if user_should_deal == "h":
            user_cards.append(deal_card())
        elif user_score < 17:
            print("your score is less than 17.you'd have to draw a card")
            user_cards.append(deal_card())
        else:
            is_game_over = True

    #when user is done computer should keep playing until the score is over 17.
    while comp_score!=0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = calculate_score(comp_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {comp_cards}, final score: {comp_score}")
    print(compare(user_score, comp_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  play_game()