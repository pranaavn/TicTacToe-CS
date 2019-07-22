# Tic Tac Toe

import time
from cs043_Final_Project.TicTacToe import ticTacToe

game = ticTacToe()
print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = game.inputPlayerLetter()
    turn = game.whoGoesFirst()
    print( turn + ' will go first.')
    time.sleep(1.5)
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'Player 1':
            # Player's turn.
            game.drawBoard(theBoard)
            move = game.getPlayer1Move(theBoard)
            game.makeMove(theBoard, playerLetter, move)

            if game.isWinner(theBoard, playerLetter):
                game.drawBoard(theBoard)
                print('Player 1 wins the game!')
                gameIsPlaying = False
            else:
                if game.isBoardFull(theBoard):
                    game.drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 2'

        else:
            game.drawBoard(theBoard)
            move = game.getPlayer2Move(theBoard)
            game.makeMove(theBoard, computerLetter, move)

            if game.isWinner(theBoard, computerLetter):
                game.drawBoard(theBoard)
                print('Player 2 wins the game!')
                gameIsPlaying = False
            else:
                if game.isBoardFull(theBoard):
                    game.drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

    if not game.playAgain():
        break