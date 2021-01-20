import random

board = []
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 0}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Bank:

    def __init__(self):
        self.amount = 0
        self.bank_balance = 0

    def add_to_bank(self, amount):
        self.bank_balance += amount
        return self.bank_balance

    def __str__(self):
        return f"The bank amount: {self.bank_balance} \n"

    def withdraw(self, winner):
        gain = self.bank_balance
        winner.player_balance = gain
        return winner.player_balance


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


# CLASS DECK
class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)

                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

        # to start the game

    def deal_two(self):

        dealed_cards = [self.all_cards.pop(), self.all_cards.pop(0)]

        return dealed_cards

    # to continue hitting
    def deal_one(self):

        dealed_card = [self.all_cards.pop()]

        return dealed_card


class Player:

    def __init__(self, player_type):

        self.player_type = player_type
        self.player_choice = ''
        player_balance = 15000
        self.player_balance = player_balance
        self.all_cards = []

    def player_name(self):
        self.name = ''
        self.name = input('Enter player name: \n')
        return self.name

    def show_player_balance(self):
        if self.player_type == 'p':
            print(f'Player score is {self.player_balance} \n')
            return self.player_balance
        elif self.player_type == 'd':
            # print(f'Dealer score is {self.player_balance} \n')
            return self.player_balance

    def place_bet(self):
        value = 0

        if self.player_type == 'p':
            while True:
                try:
                    value = int(input('Enter your bet please: \n'))
                except ValueError:
                    print('You have entered the wrong value! Please try again\n')
                    continue
                else:
                    self.player_balance = self.player_balance - value
                    print(f'Your bet {value} is accepted!')
                    break

        elif self.player_type == 'd':
            value = random.randint(100, 15000)
            self.player_balance -= value
            print(f'Dealer bet {value}!')
        return value

    def add_cards(self, new_cards):
        self.new_cards = new_cards

        for card in self.new_cards:
            self.all_cards.append(card)

        if self.player_type == 'p':
            print(f"Your cards : '{self.all_cards[0]}', '{self.all_cards[1]}'")
        elif self.player_type == 'd':
            print(f"Dealer cards : '{self.all_cards[0]}', '{self.all_cards[1]}'")

    def add_card(self, new_card):
        self.new_card = new_card

        for card in self.new_card:
            self.all_cards.append(card)

        if self.player_type == 'p':
            print(f'\nPlayer taken the card: {card}\n')
        elif self.player_type == 'd':
            print(f'\nDealer taken the card: {card}\n')

    def show_player_cards(self):
        card_number = 0
        if self.player_type == 'p':
            print('Your cards are:\n')
            for card in self.all_cards:
                card_number += 1
                print(f'Card {card_number}: {card}')

        elif self.player_type == 'd':
            print('Dealer cards are:\n')
            for card in self.all_cards:
                card_number += 1
                print(f'Card {card_number}: {card}')


class Game:

    def __init__(self, player):
        self.player = player
        self.new_deck = Deck()
        self.ace_flag = False

    def hit_or_stay(self):
        self.decision = ''

        if self.player.player_type == 'p':
            while True:
                try:
                    self.decision = input('Do you wanna HIT or STAY? (H or S): \n')
                except ValueError:
                    print('You have entered the wrong value. Please try again!')
                else:
                    if self.decision == 'H':
                        # self.player.add_card(new_deck.deal_one())
                        self.player.player_choice = 'H'
                        break
                    elif self.decision == 'S':
                        self.player.player_choice = 'S'
                        break

        return self.player.player_choice

    def define_values(self):
        card_value = 0
        decision = 0
        rand_list = [1, 11]

        for card in self.player.all_cards:

            if card.rank != 'Ace':

                card_value += card.value

            elif (card.rank == 'Ace') and (not self.ace_flag) and (self.player.player_type == 'p'):
                while decision not in rand_list:
                    try:
                        decision = int(input('Do you wanna ACE be counted as 1 or 11? (1 or 11):'))
                    except ValueError:
                        print('You have entered the wrong value. Please try again!')
                    else:
                        self.ace_flag = True
                        break

            elif (self.player.player_type == 'd') and (card.rank == 'Ace'):
                card_value += random.choice(rand_list)

        card_value += decision

        return card_value

    def main_logic(self, player_value1, dealer_value2):
        self.player_value1 = player_value1
        self.dealer_value2 = dealer_value2
        self.winner = ''

        if self.player.player_choice == 'S' or self.player.player_choice == 'H':
            if self.player_value1 == 21:
                print('BLACK JACK! PLAYER WINS!')
                self.winner = 'p'
            elif self.dealer_value2 == 21:
                print('BLACK JACK! DEALER WINS!')
                self.winner = 'd'
            elif self.player_value1 > 21:
                print('Player got value over 21! Dealer wins!')
                self.winner = 'p'
            elif self.dealer_value2 > 21:
                print('Dealer got value over 21! Player wins!')
                self.winner = 'd'
            elif self.player_value1 > 21 and self.dealer_value2 > 21:
                print('DRAW!')
            elif (self.player_value1 == self.dealer_value2) and (self.player_value1 > 21) and (self.dealer_value2 > 21):
                print('DRAW!')

        # print(f'Your card values: {self.player_value1}\nDealer card values: {self.dealer_value2}')
        return self.winner
