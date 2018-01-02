class TicTacToeBoard:
    
    def __init__(self, piece='X'):
        self.state = ['*','*','*','*','*','*','*','*','*']
        self.gameover = False
        self.piece = piece
        
    def get_board(self, grid=True):
        if grid==True:
            print(str(self.state[0]) + "|" + str(self.state[1]) + '|' + str(self.state[2]))
            print('-' + ' ' + '-' + ' ' + '-')
            print(str(self.state[3]) + "|" + str(self.state[4]) + '|' + str(self.state[5]))
            print('-' + ' ' + '-' + ' ' + '-')
            print(str(self.state[6]) + "|" + str(self.state[7]) + '|' + str(self.state[8]))
        else:
            return(self.state)
        
    def get_actions(self):
        board_idx = list(range(0,9))
        return([x for x in board_idx if self.state[x]=='*'])
    
    def make_move(self,idx,piece=None):
        if piece is None:
            piece = self.piece
        if self.state[idx]!='*':
            return("Not a legal move")
        self.state[idx] = piece
        return(self.state)
    
    def make_random_move(self,piece=None):
        if piece is None:
            piece = self.piece
        self.state[np.random.choice(self.get_actions())] = self.piece
        
    def get_winner(self):
        if self.state[0]==self.state[1]==self.state[2]!='*':
            return self.state[0] # UL Row
        if self.state[0]==self.state[3]==self.state[6]!='*':
            return self.state[0] # UL Column
        if self.state[0]==self.state[4]==self.state[8]!='*':
            return self.state[0] # UL Diagnol
        if self.state[1]==self.state[4]==self.state[7]!='*':
            return self.state[1] # UM Column
        if self.state[2]==self.state[5]==self.state[8]!='*':
            return self.state[2] # UR Column
        if self.state[2]==self.state[4]==self.state[6]!='*':
            return self.state[2] # UR Diagnol
        if self.state[3]==self.state[4]==self.state[5]!='*':
            return self.state[3] # Center Row
        if self.state[6]==self.state[7]==self.state[8]!='*':
            return self.state[6] # Bottom Row
        else:
            return 0
        
        
    print("Welcome to Tic Tac Toe!")
your_piece = str(input("Would you like to play as X or O? -"))
ai_piece = 'O' if your_piece=='X' else 'X'
print()
print("Thanks, the board is as follows. You can type the corresponding number to make your move")
print(str(0) + "|" + str(1) + '|' + str(2))
print('-' + ' ' + '-' + ' ' + '-')
print(str(3) + "|" + str(4) + '|' + str(5))
print('-' + ' ' + '-' + ' ' + '-')
print(str(6) + "|" + str(7) + '|' + str(8))
print()
board = TicTacToeBoard()

while board.get_winner()==0 and len(board.get_actions())>0:
    
    movelist = board.get_actions()
    print("Your options are " + str(movelist))
    move = int(input(''))
    while move not in movelist:
        print("Please enter a valid move")
        move = int(input(''))
    board.make_move(move, your_piece)
    
    print()
    print("Good move, the board is as follows")
    board.get_board()
    
    print()
    print("Now it's " + str(ai_piece) + "'s" + " turn!")
    
    movelist = board.get_actions()
    print("Your options are " + str(movelist))
    move_next = int(input(''))
    while move_next not in movelist:
        print("Please enter a valid move")
        move_next = int(input('')) 
    board.make_move(move_next, ai_piece)

    
    print()
    print("Good move, the board is as follows")
    board.get_board()
if board.get_winner()==0:
    print()
    print("***** Tie game -_- *****")
else:
    print()
    print('*****' + str(board.get_winner()) + " wins the game!!" + '*****')
