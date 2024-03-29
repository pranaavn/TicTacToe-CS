import random
import time
theBoard = [' '] * 10
class ticTacToe:

    def drawBoard(self, board):
        # This function prints out the board that it was passed.

        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')

    def howToPlay(self):
        #explains how to play the game
        print('In Tic-Tac-Toe, you win the game by getting three of your symbol (X or O) in a row.')
        print('This group of three can be horizontal, vertical, or diagonal. (Press enter to continue)')
        input()
        print('This is what the Tic-Tac-Toe board will look like.')
        time.sleep(2)
        ticTacToe.drawBoard(self, theBoard)
        print('(Press enter to continue)')
        input()
        print('To place your symbol in one of the open spaces, type a number between 1-9.')
        print('The following describes where each number corresponds to.')
        time.sleep(2)
        print('   |   |')
        print(' ' + '7' + ' | ' + '8' + ' | ' + '9')
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + '4' + ' | ' + '5' + ' | ' + '6')
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + '1' + ' | ' + '2' + ' | ' + '3')
        print('   |   |')
        time.sleep(2)
        print('(When you are ready to begin, press enter)')
        input()

    def inputPlayerLetter(self):
        # Lets the player type which letter they want to be.
        # Returns a list with the player's letter as the first item, and the computer's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Player 1: Do you want to be X or O?')
            letter = input().upper()

        # the first element in the tuple is the player's letter, the second is the computer's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def whoGoesFirst(self):
        # Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            return 'Player 1'
        else:
            return 'Player 2'

    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')

    def getBoardCopy(board):
        # Make a duplicate of the board list and return it the duplicate.
        dupeBoard = []

        for i in board:
            dupeBoard.append(i)

        return dupeBoard

    def makeMove(self, board, letter, move):
        board[move] = letter

    def isWinner(self, bo, le):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
                (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
                (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
                (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
                (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
                (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
                (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
                (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal

    def isSpaceFree(board, move):
        # Return true if the passed move is free on the passed board.
        return board[move] == ' '

    def getPlayer1Move(self, board):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not ticTacToe.isSpaceFree(board, int(move)):
            print('Player 1: What is your next move? (1-9)')
            move = input()

        return int(move)

    def getPlayer2Move(self, board):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not ticTacToe.isSpaceFree(board, int(move)):
            print('Player 2: What is your next move? (1-9)')
            move = input()
        return int(move)

    def chooseRandomMoveFromList(board, movesList):
        # Returns a valid move from the passed list on the passed board.
        # Returns None if there is no valid move.
        possibleMoves = []
        for i in movesList:
            if ticTacToe.isSpaceFree(board, i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

    def isBoardFull(self, board):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if ticTacToe.isSpaceFree(board, i):
                return False
        return True

