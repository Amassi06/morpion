import tkinter as tk
from MorpionJeu import TicTacToeGame
from MorpionInterface import TicTacToeBoard


class GameGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x400")
        self.root.title("Morpion")
        self.label = tk.Label(self.root, text="Mopion", relief=tk.SUNKEN)
        self.label.config(font=("Arial", 44))
        self.label.place(relx=.5, rely=.5, anchor="center")
        self.difficulty_var = tk.StringVar(value="Contre votre ami(e)")
        self.difficulty_options = ["Contre votre ami(e)", "Facile", "Moyen", "Difficile"]
        self.difficulty_dropdown = tk.OptionMenu(self.root, self.difficulty_var, *self.difficulty_options)
        self.difficulty_dropdown.pack(side=tk.BOTTOM)
        self.start_button = tk.Button(self.root, text="Lancer morpion", command=self.on_select)
        self.start_button.pack(side=tk.BOTTOM)

    def on_select(self, *args, **kwargs):
        difficulty = self.difficulty_var.get()
        print("Difficulté selectionée :", difficulty)
        self.stop()
        if difficulty == "Contre votre ami(e)":
            game = TicTacToeGame()
            board = TicTacToeBoard(game)
            board.mainloop()
        elif difficulty == "Facile":
            print("Facile")
        elif difficulty == "Moyen":

            print("Moyen")
        else:

            print("Difficile")

    def mainloop(self):
        self.root.mainloop()

    def stop(self):
        self.root.destroy()


