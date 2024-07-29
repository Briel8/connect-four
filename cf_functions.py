class ConnectFour:
    def __init__(self):
        self.board = [
             #0   #1   #2   #3   #4   #5   #6
            ['_', '_' ,'_' ,'_' ,'_' ,'_' ,'_'],    #0
            ['_', '_' ,'_' ,'_' ,'_' ,'_' ,'_'],    #1
            ['_', '_' ,'_' ,'_' ,'_' ,'_' ,'_'],    #2
            ['_', '_' ,'_' ,'_' ,'_' ,'_' ,'_'],    #3
            ['_', '_' ,'_' ,'_' ,'_' ,'_' ,'_'],    #4
            ['_', '_' ,'_' ,'_' ,'_' ,'_' ,'_'],    #5
            
        ]

#        self.board = self.fill_board_pos(template_board)
        self.turn = 'X'
        self.max = len(self.board) * len(self.board[0])     # board & board element array length
        self.running = True
        self.winner = None

    def switch_turn(self):
        """Interchages the use of 'X' and '0'
        by returning '0' if turn is 'X' and vise versa."""
        if self.turn == 'X':
            return '0'
        else:
            return 'X'

#    def fill_board_pos(self, board):
        """returns a board with positions that are numbered from 1 to number of
        positions."""
        new_board = board
        count = 1
        for row in range(len(new_board)):
            for i in range(len(new_board[row])):
                new_board[row][i] = count
                count += 1
        return new_board
    
    def display(self):
        """Prints the board to the console."""
        for columns in self.board:
            print('|', end='')
            for column in columns:
                if type(column) != int or column < 10: # to make sure space is even.
                    print(f"{column} ", end='|')
                else:
                    print(f"{column}", end='|')
            print()
        print('----------------------')
        

    def insert(self):
        """Inserts X or 0 in the specified position."""
        pos = ''
        inserted = False
        while type(pos) != int:     # Make sure input is an integer.
            try:
                pos = int(input(f"Player {self.turn}, specify your position: "))
            except:
                print("Warning: please enter a valid position!")
        if pos < 1 or pos > 7:
            print("Warning! please use the available positions")
            self.insert()
            return
        count = 5
        while count >= 0:
            if self.board[count][pos-1] == '_':
                self.board[count][pos-1] = self.turn
                self.check_win(count, pos-1)
                return
            else:
                count -= 1
        #self.insert()

    def check_win(self,row, column):
        """Checks if the other three, horizontally or vertically are equal 
        to the inserted one. Return True if equal."""
        down = None
        left = None
        right = None

        # Slices have to either be None or lenght of 4.
        if column > 2:      # insert can make a complete 3 length slice
            left = self.board[row][column-3:column]
             # compare left
            if ((self.board[row][column] == left[0]) and (left[0] == left[1]) and 
                (left[1] == left[2])):
                self.winner = self.turn
                self.running = False
        if column < 4:      # insert can make a complete 3 length slice
            right = self.board[row][column+1:column+4]
            # compare right
            if ((self.board[row][column] == right[0]) and (right[0] == right[1]) and 
                (right[1] == right[2])):
                self.winner = self.turn
                self.running = False

        
        if row < 3:
            down = [self.board[row+1][column], self.board[row+2][column], self.board[row+3][column],]
            # Compare up
            if (self.board[row][column] == down[0] and down[0] == down[1] and down[1] == down[2]):
                self.winner = self.turn
                self.running = False
       