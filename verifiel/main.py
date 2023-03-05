from lecture import get_credentials, connect_user, get_emails_data, traverse_email_data, disconnect_user, write_data

serveurs_IMAP = {'Gmail': 'imap.gmail.com', 'Outlook': 'imap-mail.outlook.com',
                 'Hotmail': 'imap-mail.outlook.com', 'Yahoo': 'imap.mail.yahoo.com',
                 'ATT': 'imap.mail.att.net', 'Comcast': 'imap.comcast.net',
                 'Verizon': 'incoming.verizon.net', 'AOL': 'imap.aol.com',
                 'Zoho': 'imap.zoho.com'}

serveurs_SMTP = {'Outlook': ('smtp-mail.outlook.com', 587)}


def display_servers(servers):
    boites = list(servers.keys())
    print("[*] Boîtes mails compatibles :")
    for i, serveur in enumerate(servers):
        print(f"{i + 1} - {serveur}")
    entry_incorrect = True
    while entry_incorrect:
        num_boite = input("[*] Choix de votre boîte mail : ")
        try:
            num_boite = int(num_boite)
            num_boite -= 1
            boite = boites[num_boite]
            entry_incorrect = False
        except ValueError:
            print("[!] Entrez un numéro de boîte mail valide.")
        except IndexError:
            print("[!] Entrez un numéro de boîte mail valide.")
    return boite


# TODO: Améliorer affichage, notamment mettre de la couleur
# TODO: Implémenter le désabonnement
# TODO: Implémenter la suppression des emails si voulu


def main():
    print(50 * "=")
    print("Vérifiel".center(25))
    print(50 * "=")
    choix_boite = display_servers(serveurs_IMAP)
    serveur = serveurs_IMAP[choix_boite]
    print(f"[*] Vous avez choisi la boîte {choix_boite}.")
    # serveur = serveurs["Outlook"]
    courriel, mdp = get_credentials()
    connexion = connect_user(courriel, mdp, serveur)
    emails_data = get_emails_data(connexion=connexion)
    liste_desabonnement = traverse_email_data(emails_data, connexion=connexion)
    write_data(liste_desabonnement)
    print("[*] Processus terminé.\n")
    disconnect_user(connexion=connexion)


if __name__ == "__main__":
    main()
