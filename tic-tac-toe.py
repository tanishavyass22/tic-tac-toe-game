import tkinter as tk
import tkinter.messagebox
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")

        self.mode = self.choose_mode()

        self.board = [[' ']*3 for _ in range(3)]
        self.players = ['X', 'O']
        self.current_player = random.choice(self.players)

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                btn = tk.Button(master, text='', font=('Arial', 20), width=6, height=3,
                                command=lambda row=i, col=j: self.on_click(row, col))
                btn.grid(row=i, column=j, sticky="nsew")
                row.append(btn)
            self.buttons.append(row)

        self.status_label = tk.Label(master, text=f'Player {self.current_player}\'s turn', font=('Arial', 12))
        self.status_label.grid(row=3, columnspan=3)

        self.play_again_button = tk.Button(master, text='Play Again', font=('Arial', 12), command=self.reset)
        self.play_again_button.grid(row=4, columnspan=3)

    def choose_mode(self):
        while True:
            mode = tk.messagebox.askquestion("Choose mode", "Do you want to play against the computer?")
            if mode == 'yes':
                return 'computer'
            elif mode == 'no':
                return 'two_players'

    def on_click(self, row, col):
        if self.board[row][col] == ' ':
            self.buttons[row][col].config(text=self.current_player)
            self.board[row][col] = self.current_player
            winner = self.check_winner(self.current_player)
            if winner:
                self.game_over(winner)
            elif all(all(cell != ' ' for cell in row) for row in self.board):
                self.game_over('Tie')
            else:
                self.current_player = 'X' if self.current_player == 'O' else 'O'
                self.status_label.config(text=f'Player {self.current_player}\'s turn')

                if self.mode == 'computer' and self.current_player == 'O':
                    self.computer_move()

    def computer_move(self):
        empty_cells = [(row, col) for row in range(3) for col in range(3) if self.board[row][col] == ' ']
        row, col = random.choice(empty_cells)
        self.on_click(row, col)

    def check_winner(self, player):
        # Check rows
        for row in self.board:
            if all(cell == player for cell in row):
                return player

        # Check columns
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return player

        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return player

        return None

    def game_over(self, winner):
        if winner == 'Tie':
            tk.messagebox.showinfo('Game Over', 'It\'s a tie!')
        else:
            tk.messagebox.showinfo('Game Over', f'Player {winner} wins!')

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state='disabled')
        self.play_again_button.config(state='normal')

    def reset(self):
        self.board = [[' ']*3 for _ in range(3)]
        self.current_player = random.choice(self.players)
        self.status_label.config(text=f'Player {self.current_player}\'s turn')
        self.play_again_button.config(state='disabled')
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='', state='normal')

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
