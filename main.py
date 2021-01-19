import game

# creating a bank instance
test_bank = game.Bank()

# creating a player instance
# and assigning the player  name + displaying the balance
dealer1 = game.Player('d')
player1 = game.Player('p')
player1.player_name()

# creating a bet instance and saving to the variable
# and assigning the bet to the bank
bet1 = player1.place_bet()
test_bank.add_to_bank(bet1)
player1_balance = player1.show_player_balance()

# dealer bet
bet2 = dealer1.place_bet()
test_bank.add_to_bank(bet2)
dealer1_balance = dealer1.show_player_balance()

# displaying the balance of the bank
print(test_bank)

new_deck = game.Deck()
new_deck.shuffle()

# setting the actions
player1_actions = game.Game(player1)
dealer1_actions = game.Game(dealer1)

# assigning cards to the player and dealer
player1.add_cards(new_deck.deal_two())
dealer1.add_cards(new_deck.deal_two())

while True:

    player1_card_values = player1_actions.define_values()
    dealer1_card_values = dealer1_actions.define_values()

    player1_choice = player1_actions.hit_or_stay()

    if player1_choice == 'H':

        player1.add_card(new_deck.deal_one())

        player1_card_values = player1_actions.define_values()

        winner = player1_actions.main_logic(player1_card_values, dealer1_card_values)

        if winner:

            break

        else:

            continue


    elif player1_choice == 'S':

        if not player1_card_values and not dealer1_card_values:

            player1_card_values = player1_actions.define_values()

            dealer1_card_values = dealer1_actions.define_values()

        elif not dealer1_card_values:

            player1_card_values = player1_actions.define_values()

        winner = player1_actions.main_logic(player1_card_values, dealer1_card_values)

        if not winner and (player1_card_values < 21) and (dealer1_card_values < 21):

            dealer1.add_card(new_deck.deal_one())

            dealer1_card_values = dealer1_actions.define_values()

        else:

            break

        dealer1.add_card(new_deck.deal_one())

        dealer1_card_values = dealer1_actions.define_values()

        winner = player1_actions.main_logic(player1_card_values, dealer1_card_values)

        break

if winner == 'p':
    winner_gain = test_bank.withdraw(player1)
    print(f'Player card values: {player1_card_values}')
    print(f'Dealer card values: {dealer1_card_values}\n')
    print(f'Your gain: {winner_gain}')


elif winner == 'd':
    winner_gain = test_bank.withdraw(dealer1)
    print(f'Player card values: {player1_card_values}')
    print(f'Dealer card values: {dealer1_card_values}\n')
    print(f'Your gain: {winner_gain}')
