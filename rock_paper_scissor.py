import random
menu = ['rock','paper','scissor']
choice = int(input('''
press 1 to play:-
press 2 to exit:-
'''))
user_score = 0
computer_score = 0
if choice == 1:
    while True:
        computer_move = random.choice(menu)
        print('''
        press 1 for rock
        press 2 for paper
        press 3 for scissor
        ''')
        ch = int(input('Enter the choice:'))

        if ch == 1:
            user_move = 'rock'
        elif ch == 2:
            user_move = 'paper'
        elif ch == 3:
            user_move = 'scissor'
        else:
            print('Invalid choice')
            break

        if user_move == computer_move:
            print('''
            Tie
            Your Move:{}
            Computer Move:{}
            Your Score:{}
            Computer Score:{}
            '''.format(user_move,computer_move,user_score,computer_score))
        elif (user_move == 'rock' and computer_move == 'scissor') or (user_move == 'paper' and computer_move == 'rock') or (user_move == 'scissor' and computer_move == 'paper'):
            user_score += 1
            print('''
                You Won
                Your Move:{}
                Computer Move:{}
                Your Score:{}
                Computer Score:{}
                '''.format(user_move,computer_move,user_score,computer_score))
        elif (user_move == 'rock' and computer_move == 'paper') or (user_move == 'paper' and computer_move == 'scissor') or (user_move == 'scissor' and computer_move == 'rock'):
            computer_score += 1
            print('''
                Computer Won
                Your Move:{}
                Computer Move:{}
                Your Score:{}
                Computer Score:{}
                '''.format(user_move,computer_move,user_score,computer_score))
        wanna_play = input('press Y to continue:')[0]
        if wanna_play.upper() == 'Y':
           pass
        else:
            print('Game ended !!')
            break
elif choice==2:
    print('Out of the Game')
