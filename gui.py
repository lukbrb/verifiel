import tkinter as tk
from tkinter import ttk
import time

from verifiel.lecture import User

serveurs_IMAP = {'Gmail': 'imap.gmail.com', 'Outlook': 'imap-mail.outlook.com',
                 'Hotmail': 'imap-mail.outlook.com', 'Yahoo': 'imap.mail.yahoo.com',
                 'ATT': 'imap.mail.att.net', 'Comcast': 'imap.comcast.net',
                 'Verizon': 'incoming.verizon.net', 'AOL': 'imap.aol.com',
                 'Zoho': 'imap.zoho.com'}
class VerifielApp:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.fenetre.title("Vérifiel")
        self.fenetre.configure(bg="grey18")  # Couleur de fond gris anthracite

        # Créer une police de style "Robotique" avec du texte blanc
        self.police_robotique = ("Robotique", 20)
        self.police_info = ("Italic", 10)
        self.couleur_texte = "white"

        # Créer un style personnalisé pour les champs de texte et les boutons
        self.style = ttk.Style()
        self.style.configure("TEntry", padding=0, relief="flat", background="grey18")
        self.style.configure("TButton", padding=0, relief="flat", background="grey18")

        # Créer la frame principale
        self.frame_principal = tk.Frame(fenetre, bg="grey18")
        self.frame_principal.pack(pady=30)

        # Ajouter le titre en haut au milieu
        self.titre_label = tk.Label(self.frame_principal, text="Vérifiel", font=self.police_robotique, fg=self.couleur_texte, bg="grey18")
        self.titre_label.pack()

        # Ajouter le texte d'information
        self.info_label = tk.Label(self.frame_principal, text="Par sécurité, Vérifiel ne stocke pas vos informations, veuillez vous connecter", font=self.police_info, fg=self.couleur_texte, bg="grey18")
        self.info_label.pack()

        self.courriel_entry = ttk.Entry(self.frame_principal, foreground=self.couleur_texte, style="TEntry")
        self.courriel_entry.pack()
        self.courriel_entry.insert(0, "exemple@email.com")

        self.mot_de_passe_entry = ttk.Entry(self.frame_principal, show="*", style="TEntry")
        self.mot_de_passe_entry.pack()

        self.serveur_entry = ttk.Combobox(self.frame_principal, values=list(serveurs_IMAP.keys()), state='readonly')
        self.serveur_entry.current(1)
        self.serveur_entry.pack()
        # Ajouter le bouton "Se connecter"
        self.se_connecter_button = ttk.Button(self.frame_principal, text="Se connecter", style="TButton", command=self.se_connecter)
        self.se_connecter_button.pack()

        # Centrer la fenêtre
        self.centrer_fenetre()

    def centrer_fenetre(self):
        self.fenetre.update_idletasks()
        largeur = self.fenetre.winfo_width()
        hauteur = self.fenetre.winfo_height()
        x = (self.fenetre.winfo_screenwidth() - largeur) // 2
        y = (self.fenetre.winfo_screenheight() - hauteur) // 2
        self.fenetre.geometry("{}x{}+{}+{}".format(largeur, hauteur, x, y))

    def se_connecter(self):
        # Récupérer les valeurs entrées par l'utilisateur
        courriel = self.courriel_entry.get()
        mot_de_passe = self.mot_de_passe_entry.get()
        serveur = serveurs_IMAP[self.serveur_entry.get()]
        
        user = User(courriel, mot_de_passe, serveur)
        user.connect()
        connexion_msg = tk.StringVar()
        connexion_msg.set("Connexion...")
        info_label = tk.Label(self.frame_principal, textvariable=connexion_msg, font=self.police_info, fg=self.couleur_texte, bg="grey18")
        info_label.pack()

        if user.connected:
            connexion_msg.set("Connexion réussie")
            connexion_msg.set(None)
            self.clear_connexion_screen()
            
        else:
            connexion_msg.set("La connexion a échoué.")
        user.disconnect()

    def clear_connexion_screen(self):
        self.info_label.destroy()
        self.courriel_entry.pack_forget()
        self.mot_de_passe_entry.pack_forget()
        self.serveur_entry.pack_forget()
        self.se_connecter_button.pack_forget()

    def create_choice_menu(self):
        pass


if __name__ == "__main__":
    fenetre = tk.Tk()
    app = VerifielApp(fenetre)
    fenetre.geometry("720x300")
    fenetre.mainloop()
    #disconnect_user(app.connexion)