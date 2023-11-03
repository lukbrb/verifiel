import sys
from lecture import User, get_credentials, write_data
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

def read_creds(filename):
    with open(filename) as f:
        data = f.readlines()
    adresse = data[0].split("=")[-1].strip()
    mdp = data[1].split("=")[-1].strip()
    return adresse, mdp

def main():
    print(50 * "=")
    print("Vérifiel".center(25))
    print(50 * "=")
    action = choix_action()
    # Si fichier n'existe pas: action = 1
    # Sinon action = choix_action()
    if action == 1:
        if not sys.argv[-1] == '--test':
            choix_boite = display_servers(serveurs_IMAP)
            serveur = serveurs_IMAP[choix_boite]
            print(f"[*] Vous avez choisi la boîte {choix_boite}.")
            courriel, mdp = get_credentials()
        else:
            courriel, mdp = read_creds("creds.txt")
            print(courriel, mdp)
            serveur = 'imap-mail.outlook.com'
        user = User(courriel, mdp, serveur)
        user.connect()
        user.get_emails_data()
        user.get_liste_desabo()

        # connexion, _ = connect_user(courriel, mdp, serveur)
        # emails_data = get_emails_data(connexion=connexion)
        # liste_desabonnement = traverse_email_data(emails_data, connexion=connexion)
        write_data(user.liste_desabo)
        print("[*] Processus terminé.\n")
        user.disconnect()
    elif action == 2:
        print("[*] Le désabonnement automatique va commencer.")
        courriel, mdp = get_credentials()
        lance_desabonnement(courriel, mdp, filename="../lucas_donnees_liste_emails.csv")
    else:
        print("[!] Problème inattendu. Soyez sûr de séléctionner un choix valide.")


if __name__ == "__main__":
    main()
