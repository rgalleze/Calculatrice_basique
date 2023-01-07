from tkinter import *
from math import *
from collections import deque


class Fenetre(Tk):
    def __init__(self, l=630, h=612):
        Tk.__init__(self)
        self.geometry(
            f"{l}x{h}+{self.winfo_screenwidth() // 2 - l // 2}+{self.winfo_screenheight() // 2 - h // 2}"
        )
        self.title("Calculatrice")
        self.historique = deque([])

        # Création des boutons
        boutons = [
            "sin",
            "tan",
            "cos",
            "pi",
            "1",
            "2",
            "3",
            "+",
            "4",
            "5",
            "6",
            "-",
            "7",
            "8",
            "9",
            "*",
            ".",
            "0",
            "/",
            "sqrt",
            "(",
            ")",
            "**",
            "**2",
        ]
        """ 
        Création des boutons avec une boucle ( format de la calculatrice 6x4  ) 
        Pour i de 0 à 5 ( i pour les lignes ) 
        i = 0  
            Pour j de 0 à 3 ( j pour les colonnes ) 
            j = 0 -> Button(text=boutons[0], command=lambda: self.button_click(boutons[0])).grid(row=2, column=0, ipadx=10, ipady=20, sticky=N) 
            j = 1 -> Button(text=boutons[1], command=lambda: self.button_click(boutons[1])).grid(row=2, column=1, ipadx=10, ipady=20, sticky=N) 
            ... 
            j = 3 -> Button(text=boutons[3], command=lambda: self.button_click(boutons[3])).grid(row=2, column=3, ipadx=10, ipady=20, sticky=N) 
        ... 
        """
        for i in range(6):
            for j in range(4):
                self.create_boutons(i, j, boutons)

        # Création boutton effacer
        Button(
            text="Effacer",
            bg="#FF1D23",
            activebackground="#C92834",
            fg="white",
            activeforeground="white",
            borderwidth=2.0,
            width=13,
            height=2,
            command=self.effacer,
        ).grid(row=8, column=0, columnspan=2, pady=2)

        # Création boutton calculer
        Button(
            text="=",
            bg="#03A65A",
            activebackground="#038C4C",
            fg="white",
            activeforeground="white",
            borderwidth=2.0,
            width=13,
            height=2,
            command=self.calculer,
        ).grid(row=8, column=2, columnspan=2, pady=2)

        # Création des labels
        self.create_widgets()

    def create_widgets(self):
        self.entry_result = Entry(borderwidth=2.0, font=("Lato", 12))
        self.entry_result.grid(
            row=1, column=0, columnspan=4, padx=4, pady=8, ipady=10, ipadx=10
        )
        self.label_titre = Label(text="Calculatrice", font=("Lato", 15))
        self.label_titre.grid(row=0, column=0, columnspan=4, pady=2)
        self.label_titre_historique = Label(text="Historique", font=("Lato", 15))
        self.label_titre_historique.grid(row=0, column=4, columnspan=8, ipady=15)
        self.label_historique = Label(
            text="", width=26, justify=LEFT, font=("Lato", 15)
        )
        self.label_historique.grid(
            row=1, column=4, rowspan=8, ipady=10, ipadx=10, sticky=NW
        )

    def create_boutons(self, i, j, boutons):
        Button(
            text=boutons[4 * i + j],
            bg="#4A79D9",
            activebackground="#3C5FA6",
            fg="white",
            activeforeground="white",
            borderwidth=2.0,
            width=2,
            command=lambda: self.button_click(boutons[4 * i + j]),
        ).grid(row=i + 2, column=j, ipadx=10, ipady=20, sticky=N)

    def button_click(self, num):
        tmp = self.entry_result.get()
        self.entry_result.delete(0, END)
        self.entry_result.insert(0, tmp + num)

    def calculer(self):
        try:
            result = str(eval(self.entry_result.get()))
            if len(self.historique) < 10:
                self.historique.appendleft(self.entry_result.get())
            else:
                self.historique.pop()
                self.historique.appendleft(self.entry_result.get())

            self.label_historique.config(
                text="".join(
                    self.historique[i] + f"= {str(eval(self.historique[i]))}" + "\n"
                    for i in range(len(self.historique))
                )
            )

            self.entry_result.delete(0, END)
            self.entry_result.insert(0, result)
        except:
            self.entry_result.delete(0, END)
            self.entry_result.insert(0, "Erreur :( ")

    def effacer(self):
        self.entry_result.delete(0, END)


def main():
    fenetre = Fenetre()
    fenetre.mainloop()


if __name__ == "__main__":
    main()
