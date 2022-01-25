import numpy as np
import pandas as pd


class Chess_game:
    CASE_NOTHING = "_-_"

    def __init__(self):
        self.board = self.create_board()
        print(self.board)

    def create_board(self):
        board = np.array([[self.CASE_NOTHING for j in range(8)]
                         for i in range(8)])
        # add the pawn
        for i in range(8):
            board[1, i] = "P-W"
            board[6, i] = "P-B"

        # knight
        board[0, 1] = "N-W"
        board[0, 6] = "N-W"
        board[7, 1] = "N-B"
        board[7, 6] = "N-B"

        # Bishop
        board[0, 2] = "B-W"
        board[0, 5] = "B-W"
        board[7, 2] = "B-B"
        board[7, 5] = "B-B"

        # Rook
        board[0, 0] = "R-W"
        board[0, 7] = "R-W"
        board[7, 0] = "R-B"
        board[7, 7] = "R-B"

        # King
        board[7, 4] = "K-B"
        board[0, 4] = "K-W"

        board[7, 3] = "Q-W"
        board[0, 3] = "Q-W"

        return pd.DataFrame(board, [i for i in range(1, 9)], [chr(65 + i) for i in range(8)], dtype="string")

    def IsPiece(self, position):
        return self.board[position[0]][int(position[1])] != self.CASE_NOTHING

    def move(self, piece, position: str, takes=False):
        # verifier si la posistion est posible
        # bouger la piece
        # enlever de sa position precedente
        can_move = False
        match piece[0]:  # todo check les echec a la decouvert et donc coup ilegaux
            case "P":
                if not self.IsPiece(position):
                    can_move = True
        print(can_move)


if __name__ == "__main__":
    chess_game = Chess_game()
    chess_game.move("PD2", "D4")
    