class Board:

    def __init__(self, number_of_tiles = 3):
        self.number_of_tiles = number_of_tiles
        self.board = [['.' for i in range(number_of_tiles)] for j in range(number_of_tiles)]

    def did_player_win(self, player: 'Player'):
        input_row, input_column = player.x, player.y
        count_row = count_col = count_diag_main = count_diag_anti = 0
        for i in range(self.number_of_tiles):

            # Checking for row
            if self.board[input_row][i] == player.symbol:
                count_row += 1
            
            # Checking for column
            if self.board[i][input_column] == player.symbol:
                count_col += 1
            
            # Checking for main diagonal
            if input_row == input_column and self.board[i][i] == player.symbol:
                count_diag_main += 1
            
            # Checking for opposite_diagonal
            if input_row + input_column == self.number_of_tiles - 1 and self.board[i][self.number_of_tiles - 1 - i]:
                count_diag_anti += 1
        
        return count_col == self.number_of_tiles or count_row == self.number_of_tiles or count_diag_anti == self.number_of_tiles or count_diag_main == self.number_of_tiles
    
    def valid_move(self, x: int, y: int):
        return (x < self.number_of_tiles and x >=0 != y < self.number_of_tiles and y >=0) and self.board[x][y] == '.'

    def update_board(self,player: 'Player', x:int , y: int):
        if self.valid_move(x, y):
            self.board[x][y] = player.symbol
            return True
        else:
            return False

    def is_space_available(self):
        
        for i in range(self.number_of_tiles):
            if any((j  == '.' for j in self.board[i])):
                return True
        return False
        

class Player:
    def __init__(self, name: str, symbol: str):
        self.name = name
        self.symbol = symbol

    def take_input(self):
        self.row, self.column = int(input("Enter Row: ")), int(input("Enter Column: "))
    
    def make_move(self, board: Board):
        return board.update_board(self, self.row, self.column)
        
number_of_players = 2#int(input())
number_of_tiles = 3#int(input())

playing_board = Board(number_of_tiles=number_of_tiles)
players = []
for i in range(number_of_players):
    player_name = input(f"Enter Player {i + 1} Name: ")
    player_symbol = input(f"Enter Player {i + 1} Symbol: ")
    while player_symbol == '.':
        print("Can not use `.`!! TRY AGAIN")
        player_symbol = input(f"Enter Player {i + 1} Symbol: ")
    players.append(Player(player_name, player_symbol))
    print()

status = False
while not status:
    for player in players:
        print(f"Player {player.name} turns")
        player.take_input()
        while not player.make_move(playing_board):
            print("Not a valid move. Try Again!!")
            player.take_input()
        else:
            status = playing_board.did_player_win()
            print(f"{player.name} has won the game")

        if not playing_board.is_space_available():
            status = True
            print("It is a draw")
    