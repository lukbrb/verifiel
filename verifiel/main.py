from lecture import get_credentials, connect_user, get_emails_data, traverse_email_data, disconnect_user, write_data
from affichage import display_servers, choix_action
from desabonnement import lance_desabonnement


serveurs_IMAP = {'Gmail': 'imap.gmail.com', 'Outlook': 'imap-mail.outlook.com',
                 'Hotmail': 'imap-mail.outlook.com', 'Yahoo': 'imap.mail.yahoo.com',
                 'ATT': 'imap.mail.att.net', 'Comcast': 'imap.comcast.net',
                 'Verizon': 'incoming.verizon.net', 'AOL': 'imap.aol.com',
                 'Zoho': 'imap.zoho.com'}

serveurs_SMTP = {'Outlook': ('smtp-mail.outlook.com', 587)}


# TODO: Améliorer affichage, notamment mettre de la couleur
# TODO: Implémenter le désabonnement
# TODO: Implémenter la suppression des emails si voulu


def main():
    print(50 * "=")
    print("Vérifiel".center(25))
    print(50 * "=")
    action = choix_action()
    # Si fichier n'existe pas: action = 1
    # Sinon action = choix_action()
    if action == 1:
        choix_boite = display_servers(serveurs_IMAP)
        serveur = serveurs_IMAP[choix_boite]
        print(f"[*] Vous avez choisi la boîte {choix_boite}.")
        courriel, mdp = get_credentials()
        connexion, _ = connect_user(courriel, mdp, serveur)
        emails_data = get_emails_data(connexion=connexion)
        liste_desabonnement = traverse_email_data(emails_data, connexion=connexion)
        write_data(liste_desabonnement)
        print("[*] Processus terminé.\n")
        disconnect_user(connexion=connexion)
    elif action == 2:
        print("[*] Le désabonnement automatique va commencer.")
        courriel, mdp = get_credentials()
        lance_desabonnement(courriel, mdp, filename="../lucas_donnees_liste_emails.csv")
    else:
        print("[!] Problème inattendu. Soyez sûr de séléctionner un choix valide.")


if __name__ == "__main__":
    main()
