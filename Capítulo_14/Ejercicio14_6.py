class KnightTour:
    def __init__(self, board_size): #Inicialización del tablero y movimientos
        self.board_size = board_size
        self.board = [[0] * board_size for _ in range(board_size)]
        self.moves = [
            (2, 1), (1, 2),
            (-1, 2), (-2, 1),
            (-2, -1), (-1, -2),
            (1, -2), (2, -1)
        ]

    def valid_move(self, x, y): #Movimientos Válidos
        return 0 <= x < self.board_size and 0 <= y < self.board_size and self.board[x][y] == 0

    def knight_tour(self, current_x, current_y, move_number):
        if move_number == self.board_size**2: #Movimientos realizados
            return True  # Puzzle Resuelto

        for move in self.moves: #Movimientos del caballo
            next_x, next_y = current_x + move[0], current_y + move[1]
            if self.valid_move(next_x, next_y):
                self.board[next_x][next_y] = move_number + 1
                if self.knight_tour(next_x, next_y, move_number + 1):
                    return True
                # Backtrack
                self.board[next_x][next_y] = 0

        return False

    def solve(self, start_x=0, start_y=0): #Posición del tablero
        if not (0 <= start_x < self.board_size) or not (0 <= start_y < self.board_size):
            raise ValueError("Posición inicial inválida")

        self.board[start_x][start_y] = 1
        if not self.knight_tour(start_x, start_y, 1):
            print("No existe solución.")
        else:
            self.display_board()

    def display_board(self):
        for row in self.board:
            print(" ".join(map(lambda x: str(x).rjust(2), row)))
            print()

knight_tour_solver = KnightTour(5)
knight_tour_solver.solve()
#knight_tour_solver.solve(start_x=-1, start_y=0)

