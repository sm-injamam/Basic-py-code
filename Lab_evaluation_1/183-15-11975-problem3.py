print("Enter your choice as rock, paper or scissor:")
for x in range(1, 3):

    player1 = input("Player 1: ")
    player1 = player1.lower()

    player2 = input("Player 2: ")
    player2 = player2.lower()

    if ((player1 == 'rock' and player2 == 'scissor')):
        print('player 1 wins !')

    elif ((player2 == 'rock' and player1 == 'scissor')):
        print('player 2 wins !')

    if ((player1 == 'scissor' and player2 == 'paper')):
        print('player 1 wins !')

    if ((player1 == 'paper' and player2 == 'scissor')):
        print('player 2 wins !')

    if ((player1 == 'rock' and player2 == 'paper')):
        print('player 2 wins !')

    if ((player1 == 'paper' and player2 == 'rock')):
        print('player 1 wins !')

    print("\n\n")