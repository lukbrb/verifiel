import tkinter as tk
from tkinter import ttk


class VerifielApp:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.fenetre.title("Vérifiel")
        self.fenetre.configure(bg="grey18")  # Couleur de fond gris anthracite
        self.fenetre.geometry("700x300")

        # Créer une police de style "Robotique" avec du texte blanc
        self.police_robotique = ("Robotique", 20)
        self.police_info = ("Italic", 10)
        self.couleur_texte = "white"

        # Créer un style personnalisé pour les champs de texte et les boutons
        self.style = ttk.Style()
        self.style.configure("TEntry", padding=0, relief="flat", background="grey18")
        self.style.configure("TButton", padding=0, relief="flat", background="grey18")

        # Centrer la fenêtre
        self.centrer_fenetre()

    def centrer_fenetre(self):
        self.fenetre.update_idletasks()
        largeur = self.fenetre.winfo_width()
        hauteur = self.fenetre.winfo_height()
        x = (self.fenetre.winfo_screenwidth() - largeur) // 2
        y = (self.fenetre.winfo_screenheight() - hauteur) // 2
        self.fenetre.geometry("{}x{}+{}+{}".format(largeur, hauteur, x, y))
    
    def create_formulaire(self):
        self.courriel_entry = ttk.Entry()


if __name__ == "__main__":
    fenetre = tk.Tk()
    app = VerifielApp(fenetre)
    fenetre.mainloop()