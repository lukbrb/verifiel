import tkinter as tk
from tkinter import ttk
import time

from verifiel.lecture import connect_user, disconnect_user

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

        # Ajouter le bouton "Se connecter"
        self.se_connecter_button = ttk.Button(self.frame_principal, text="Se connecter", style="TButton", command=self.se_connecter)
        self.se_connecter_button.pack()

        self.barre_chargement = ttk.Progressbar(self.frame_principal, mode="indeterminate", maximum=100)
        self.barre_chargement.pack()
        self.barre_chargement.stop()

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
        info_label = tk.Label(self.frame_principal, text="Connexion...", font=self.police_info, fg=self.couleur_texte, bg="grey18")
        info_label.pack()
        self.connexion, status = connect_user(courriel, mot_de_passe, serveur='imap-mail.outlook.com')
        if status is True:
            info_label = tk.Label(self.frame_principal, text="Connexion réussie", font=self.police_info, fg=self.couleur_texte, bg="grey18")
            info_label.pack()
        else:
            info_label = tk.Label(self.frame_principal, text="La connexion a échoué", font=self.police_info, fg=self.couleur_texte, bg="grey18")
            info_label.pack()
        # Ajoutez ici la logique de connexion à votre boîte mail et de désabonnement

    def lancer_chargement(self):
        # Simuler un traitement long (remplacez cela par votre logique de connexion réelle)
        self.se_connecter_button.configure(state="disabled")  # Désactiver le bouton
        self.barre_chargement.start(10)  # Démarrer la barre de chargement
        self.fenetre.update_idletasks()
        time.sleep(5)  # Simuler un traitement long (5 secondes)
        self.barre_chargement.stop()  # Arrêter la barre de chargement
        self.se_connecter_button.configure(state="normal")  # Réactiver le bouton

if __name__ == "__main__":
    fenetre = tk.Tk()
    app = VerifielApp(fenetre)
    fenetre.geometry("600x400")
    fenetre.mainloop()
    disconnect_user(app.connexion)