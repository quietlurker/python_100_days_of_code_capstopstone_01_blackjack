# rules:
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
import emoji as emoji

import bj_art as art
import bj_functions as functions
import emoji


def blackjack():
    continue_play = True
    player_hand = []
    dealer_hand = []

    # first draw
    player_hand = functions.deal_card(2, player_hand)
    dealer_hand = functions.deal_card(2, dealer_hand)
    first_draw = True # this is needed for some stupid blackjack rules about natural wins

    while continue_play:
        if not first_draw:
            player_hand = functions.deal_card(1, player_hand)

        print(f"Your cards: {player_hand}")
        print(f"Dealer's first card: {dealer_hand[0]}")

        # print(f"Your score is {player_hand_value}") # for tests
        # print(f"Dealer's score is {dealer_hand_value}")  # for tests

        # check if someone won after first draw
        # TODO score condition in check_if_end_game() to be redone based on simplified rules
        verdict = functions.check_if_end_game(player_hand, dealer_hand, first_draw=True)
        if verdict != "Not over":
            # do all this if game is over after first draw
            print(f"Your hand is {player_hand}")
            print(f"Dealer's hand is {dealer_hand}")
            print(results[verdict])
            continue_play = False

            # Play again?
            if input("Do you want to play again? Y/N: ").upper() == "Y":
                blackjack()
            else:
                print("OK bye")
        else:
            # noone won after the draw
            first_draw = False
            if input("Do you want to draw another card? Y/N: ").upper() == "N":
                # stop dealing cards to player and calculate final score
                continue_play = False

                # resolve dealer's hand (deal till they get 17)
                functions.resolve_dealers_hand(dealer_hand)

                # check who won
                verdict = functions.check_if_end_game(player_hand, dealer_hand, first_draw=False)
                print(f"Your hand is {player_hand}")
                print(f"Dealer's hand is {dealer_hand}")
                print(results[verdict])

                # Play again?
                if input("Do you want to play again? Y/N: ").upper() == "Y":
                    blackjack()
                else:
                    print("OK bye")


results = {
    "Draw": emoji.emojize(":yellow_square: It's a draw :yellow_square:"),
    "Player natural win": emoji.emojize(":green_square: You win you have 21 in first draw :green_square:"),
    "Dealer bust": emoji.emojize(":green_square: You win because dealer's hand is bigger than 21 :green_square:"),
    "Player wins": emoji.emojize(":green_square: You win because your hand is closer to 21 :green_square:"),
    "Dealer wins": emoji.emojize(":red_square: You lose because dealer's hand is closer to 21 :red_square:"),
    "Player bust": emoji.emojize(":red_square: You lose because your hand is bigger that 21 :red_square:"),
}
print(art.logo)
if input("Do you want to play a game of Blackjack? Y/N: ").upper() == "Y":
    blackjack()
else:
    print("OK bye")
