import random
from BetTypeLists import outside_bets_dict, outside_bet, inside_bet, roullette_games



all_numbers_dict = {}

bank = int(input('How much money are you starting with?'))

outside_question = input('Would you like to place a bet on the outside? (y/n)')

if outside_question == 'y':
    outside_dict = outside_bet(outside_bets_dict)
else:
    outside_dict = {'bet_types' : {}}
    
inside_question = input('Would you like to place a bet on the inside? (y/n)')

if inside_question == 'y':
    inside_dict = inside_bet()
else:
    inside_dict = {'bet_types' : {}}
    
inside_dict['bet_types'].update(outside_dict['bet_types'])
all_numbers_dict.update(outside_dict)
all_numbers_dict.update(inside_dict)


redo = 'y'
while redo == 'y':

    bank_list = roullette_games(bank, all_numbers_dict)

    bust_roll = len(bank_list)+1
    max_bank = max(bank_list)
    max_roll = bank_list.index(max(bank_list))+1
    double = max_bank>=(bank*2)
    triple = max_bank>=(bank*3)
    quadruple = max_bank>=(bank*4)

    print(f'rolls till bust: {bust_roll}. Max bank was {max_bank}, and it happend on roll {max_roll}')
    print(f'Double: {double}, Triple: {triple}, Quadruple: {quadruple}')

    redo = input('Rerun? (y/n)').lower()