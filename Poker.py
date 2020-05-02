from random import randrange



class Texas_hold_em():
    
    def __init__(self, players_list):
        self.spades_deck = ['1 of Spades', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades',
         '7 of Spades', '8 of Spades', '9 of Spades', '10 of Spades', 'Jack of Spades', 'Queen of Spades', 'King of Spades']

        self.clubs_deck = ['1 of Clubs', '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs',
         '7 of Clubs', '8 of Clubs', '9 of Clubs', '10 of Clubs', 'Jack of Clubs', 'Queen of Clubs', 'King of Clubs']

        self.hearts_deck = ['1 of Hearts', '2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts',
         '7 of Hearts', '8 of Hearts', '9 of Hearts', '10 of Hearts', 'Jack of Hearts', 'Queen of Hearts', 'King of Hearts']

        self.diamonds_deck = ['1 of Diamonds', '2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds', '6 of Diamonds',
         '7 of Diamonds', '8 of Diamonds', '9 of Diamonds', '10 of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds']

        self.entire_deck = self.spades_deck + self.clubs_deck + self.hearts_deck + self.diamonds_deck

        self.players_list = players_list

        self.pot = 0

    def bet(self, bet):
        bet = input('Would you like to bet?')
        self.pot += bet
        player['stack'] -= bet  
            

    def deal_cards(self):
        for player in self.players_list:
            if player['player_hand']:
                player['player_hand']
            else:
                player['player_hand'].append(self.random_card())
                self.entire_deck.remove(player['player_hand'][0]) 
                player['player_hand'].append(self.random_card()) 
                self.entire_deck.remove(player['player_hand'][1])
        return self.players_list

    def random_card(self):
        card = ''
        while card not in self.entire_deck:
            suit = ['Spade' , 'Club' , 'Diamond' , 'Heart']
            value = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
            suit_sel = suit[randrange(4)]
            value_sel = value[randrange(13)]
            card = value_sel + ' of ' + suit_sel + 's'

        return card



class Player():

    def __init__(self, name, stack):
        self.name = str(name).title()
        self.stack = int(stack)
        self.player_hand = []


########################################Testing Below

jack = Player("jack", 3000)
jane = Player('jAne', 4000)

player_list = [jack.__dict__, jane.__dict__]

game = Texas_hold_em(player_list)
game.deal_cards()
print(game.__dict__)
