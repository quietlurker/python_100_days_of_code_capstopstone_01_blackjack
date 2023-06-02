import random


def deal_card(card_nb, current_hand):
    """Adds cards to hand
    inputs:
    nb of cards to draw
    deck from which to draw
    hand to which to add drawn cards
    output:
    hand with new cards"""
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    for _ in range(card_nb):
        current_hand.append(random.choice(deck))
    return current_hand


def calc_hand_value(hand):
    """calculates current value of hand
    input: hand
    output: hand value"""
    # hand_value = 0
    # for card in hand:
    #     hand_value += card
    # return hand_value
    return sum(hand)


def check_if_end_game(player_hand, dealer_hand, first_draw):

    """checks end conditions
    inputs:
    player score
    dealer score
    first draw to check for natural win
    output: key of the results dictionary
    """
    player_score = calc_hand_value(player_hand)
    dealer_score = calc_hand_value(dealer_hand)
    if player_score == 21:
        if dealer_score == 21:
            return "Draw"
        else:
            return "Player natural win"
    elif player_score > 21:
        return "Player bust"
    elif dealer_score > 21:
        return "Dealer bust"
    elif not first_draw:
        if 21 - dealer_score > 21 - player_score:
            return "Player wins"
        elif dealer_score == player_score:
            return "Draw"
        else:
            return "Dealer wins"
    else:
        return "Not over"


def resolve_dealers_hand(dealer_hand):
    """draw cards to dealers hand till they get to 16
    input: dealer's hand
    output: updated dealer's hand"""
    dealer_score = calc_hand_value(dealer_hand)
    while dealer_score < 17:
        dealer_hand = deal_card(1, dealer_hand)
        # print(dealer_hand) # for tests
        dealer_score = calc_hand_value(dealer_hand)
        if dealer_score >= 17 and dealer_hand[-1] == 11:
            dealer_score -= 10
            dealer_hand[-1] = 1
    return dealer_hand
