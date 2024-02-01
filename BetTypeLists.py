
import random


outside_bets_dict = {
'black' : {'2_blackBet' : [2, 0],'4_blackBet' : [2, 0],'6_blackBet' : [2, 0],'8_blackBet' : [2, 0],'10_blackBet' : [2, 0],'11_blackBet' : [2, 0],'13_blackBet' : [2, 0],
			'15_blackBet' : [2, 0],'17_blackBet' : [2, 0],'20_blackBet' : [2, 0],'22_blackBet' : [2, 0],'24_blackBet' : [2, 0],'26_blackBet' : [2, 0],'28_blackBet' : [2, 0],
			'29_blackBet' : [2, 0],'31_blackBet' : [2, 0], '33_blackBet' : [2, 0],'35_blackBet' : [2, 0]},

'red' : {'1_redBet' : [2, 0],'3_redBet' : [2, 0],'5_redBet' : [2, 0],'7_redBet' : [2, 0],'9_redBet' : [2, 0],'12_redBet' : [2, 0],'14_redBet' : [2, 0],
			'16_redBet' : [2, 0],'18_redBet' : [2, 0],'19_redBet' : [2, 0],'21_redBet' : [2, 0],'23_redBet' : [2, 0],'25_redBet' : [2, 0],'27_redBet' : [2, 0],
			'30_redBet' : [2, 0],'32_redBet' : [2, 0], '34_redBet' : [2, 0],'36_redBet' : [2, 0]},

'col_1st' : {'1_first' : [3, 0],'4_first' : [3, 0],'7_first' : [3, 0],'10_first' : [3, 0],'13_first' : [3, 0],'16_first' : [3, 0],'19_first' : [3, 0],
				'22_first' : [3, 0], '25_first' : [3, 0],'28_first' : [3, 0],'31_first' : [3, 0],'34_first' : [3, 0]},

'col_2nd' : {'2_secound' : [3, 0],'5_secound' : [3, 0],'8_secound' : [3, 0],'11_secound' : [3, 0],'14_secound' : [3, 0],'17_secound' : [3, 0],'20_secound' : [3, 0],
				'23_secound' : [3, 0], '26_secound' : [3, 0],'29_secound' : [3, 0],'32_secound' : [3, 0],'35_secound' : [3, 0]},

'col_3rd' : {'3_third' : [3, 0],'6_third' : [3, 0],'9_third' : [3, 0],'12_third' : [3, 0],'15_third' : [3, 0],'18_third' : [3, 0],'21_third' : [3, 0],
				'24_third' : [3, 0], '27_third' : [3, 0],'30_third' : [3, 0],'33_third' : [3, 0],'36_third' : [3, 0]},

'row_1to12' : {'1_1to12' : [3, 0],'2_1to12' : [3, 0],'3_1to12' : [3, 0],'4_1to12' : [3, 0],'5_1to12' : [3, 0],'6_1to12' : [3, 0],
					'7_1to12' : [3, 0], '8_1to12' : [3, 0],'9_1to12' : [3, 0],'10_1to12' : [3, 0],'11_1to12' : [3, 0],'12_1to12' : [3, 0]},

'row_13to24' : {'13_13to24' : [3, 0],'14_13to24' : [3, 0],'15_13to24' : [3, 0],'16_13to24' : [3, 0],'17_13to24' : [3, 0],'18_13to24' : [3, 0],
					'19_13to24' : [3, 0], '20_13to24' : [3, 0],'21_13to24' : [3, 0],'22_13to24' : [3, 0],'23_13to24' : [3, 0],'24_13to24' : [3, 0]},

'row_25to36' : {'25_25to36' : [3, 0],'26_25to36' : [3, 0],'27_25to36' : [3, 0],'28_25to36' : [3, 0],'29_25to36' : [3, 0],'30_25to36' : [3, 0],
					'31_25to36' : [3, 0], '32_25to36' : [3, 0],'33_25to36' : [3, 0],'34_25to36' : [3, 0],'35_25to36' : [3, 0],'36_25to36' : [3, 0]} 
}

def outside_bet (bets_dict):
    repeat = 'n'
    while repeat == 'n':
        again = 'y'
        choices_dict = {}
        choices_dict['bet_types'] = {}
        while again == 'y':
            options_list = bets_dict.keys()

            request = input(f'Where would you like to bet? {options_list}').lower()
            choice_dict = bets_dict[request]

            bet_request = input('How much would you like to bet?')
            bet_int = int(bet_request)
            bet_choice_dict = {request: bet_int}
            choices_dict['bet_types'].update(bet_choice_dict)


            for i in choice_dict:
                choice_dict[i][1] = bet_int

            choices_dict.update(choice_dict)

            again = input('Would you like to pick another? (y/n)').lower()
        
        new_choices = choices_dict['bet_types']
        repeat = input(f'Your choices are {new_choices}, would you like to continue? (y/n)').lower()
    
    return choices_dict

def inside_bet ():
    repeat = 'n'
    while repeat == 'n':
        
        choices_dict = {}
        choices_dict['bet_types'] = {}
        
        again = 'y'
        while again == 'y':
            
            request = input(f'Please pick a number from 1 to 36 or 0 or 00').lower()

            bet_request = input('How much would you like to bet?')
            bet_int = int(bet_request)
            bet_choice_dict = {request: bet_int}
            choices_dict['bet_types'].update(bet_choice_dict)

            choices_dict.update({f'{request}_single' : [35, bet_int]})

            again = input('Would you like to pick another? (y/n)').lower()
        
        bets_dict = choices_dict['bet_types']
        repeat = input(f'Your choices are {bets_dict}, would you like to continue? (y/n)').lower()
    
    return choices_dict

def roullette_games (bank, all_numbers_dict):
    total_bet = sum(all_numbers_dict['bet_types'].values())
    counter = 0
    bank_roll_list = []
    while bank >= total_bet:
        winning_bets_dict = {}
        spin = str(random.randint(0,37))
        if spin == '37':
            spin = '00'

        for key in all_numbers_dict:
            try:
                bet_number = int(key[:key.find('_')])
            except:
                continue
            bet_type = key[key.find('_')+1:]
            winnings = all_numbers_dict[key][0]*all_numbers_dict[key][1]
            if int(spin) == int(bet_number):
                winning_bets_dict.update({bet_type : winnings})
        for bet_type in all_numbers_dict['bet_types']:
            if bet_type not in winning_bets_dict:
                winning_bets_dict.update({bet_type : -1 * all_numbers_dict['bet_types'][bet_type]})
        bank += sum(winning_bets_dict.values())
        counter +=1
        bank_roll_list.append(bank)
    return bank_roll_list
