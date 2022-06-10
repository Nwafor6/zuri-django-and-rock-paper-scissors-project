import random
word_list=['R', 'P', 'S']

cpu_choice=random.choice(word_list)
player_input=input("select any from 'P', 'R', 'S': ")
player_input=player_input.upper()

def tie():
    if  player_input=="S":
        print('Player played : scissors : CPC played : scissors')
    elif player_input =="p":
        print('Player played : Paper : CPC played : Paper')
    else:
        print('Player played : Rock : CPC played : Rock')


while True:
    if player_input not in word_list:
        print('invalid input! try again')
        player_input=input("select any from 'P', 'R', 'S': ")
        player_input=player_input.upper()
    else:
        break

if cpu_choice == player_input:
    tie()
    print('tie!')
    cpu_choice=random.choice(word_list)
    player_input=input("select any from 'P', 'R', 'S': ")
    player_input=player_input.upper()
    
elif cpu_choice == "P" and player_input =='S' :
    print('Player played : scissors : CPC played : Paper')
    print('you win')
elif cpu_choice == "P" and player_input =='R':
    print('Player played : Rock : CPC played : Paper')
    print('Computer wins, you Lose!')
elif cpu_choice == "R" and player_input =='P':
    print('Player played : Paper : CPC played :Rock')
    print('You wins')
elif cpu_choice == "R" and player_input =='S':
    print('Player played : scissors : CPC played : Rock')
    print('Computer wins, you Lose!')

elif cpu_choice == "S" and player_input =='P':
    print('Player played : Paper : CPC played : Sicssorsr')
    print(' you Lose!')

elif cpu_choice == "S" and player_input =='R':
    print('Player played Rock : CPC played : Sicssors')
    print(' you Win!')



    
 
