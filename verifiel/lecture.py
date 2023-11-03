import getpass
import imaplib
import sys

from tqdm import tqdm

from recherche_listes import find_email_list


def write_data(liste_desabo):
    import csv
    print("[*] Écriture des résultats...")
    # field names
    fields = ['Auteur', 'Adresse', 'Lien', 'Type-lien']

    # data rows of csv file
    # liste_infos = [[info.auteur, info.adresse, info.lien, info.type_lien] for info in liste_desabo]
    with open('../donnees_liste_emails.csv', 'w') as f:
        # using csv.writer method from CSV package
        write = csv.writer(f)

        write.writerow(fields)
        write.writerows(liste_desabo)
    print("[*] Résultats écrits avec succès dans donnees_liste_emails.csv.")


def get_credentials():
    adresse_courriel = input("[*] Entrer adresse courriel : ")
    try:
        mdp = getpass.getpass("[*] Entrer mot de passe :")
        return adresse_courriel, mdp
    except Exception as error:
        print('[!] ERREUR', error)
        sys.exit(1)


def connect_user(courriel, mdp, serveur):
    imap_server = serveur
    print("[*] Connexion au serveur", imap_server, "avec l'adresse", courriel, "...")
    try:
        connexion = imaplib.IMAP4_SSL(imap_server)
        connexion.login(courriel, mdp)
        print("[*] Connexion réussie !")
        return connexion, True

    except imaplib.IMAP4.error as e:
        print("[!] La connexion a échoué.")
        print(e)
        return e, False



def get_emails_data(connexion):
    """ Connects to the email server and
        returns the data of all emails in the Inbox.
    """
    try:
        connexion.select("Inbox")
        print("[*] Selection de la boîte principale.")
        typ, data = connexion.search(None, 'ALL')
        all_emails = list(reversed(data[0].split()))

        return all_emails
    except imaplib.IMAP4.error as e:
        print("[!] La connexion a échoué.")
        print(e)
        sys.exit(1)
    finally:
        connexion.close()
        connexion.logout()



def traverse_email_data(data, connexion):
    """ Go through all the emails and calls function
        to check if the current email is from an email list.
    """
    liste_desabo = list()
    set_adresses = set()
    tot = len(data)
    print(f"[*] Détection de {tot} courriels dans la boîte principale.")
    print("[*] Recherche des listes d'abonnements...")
    try:
        for i, msgnum in enumerate(tqdm(data, desc="Courriels lus")):
            _, data = connexion.fetch(msgnum, '(RFC822)')
            infos = find_email_list(data)
            if infos.adresse != "NOLISTE" and infos.adresse not in set_adresses:
                # print(f"[*] ({i}/{tot})", "- Lien trouvé pour : ", infos.auteur)
                set_adresses.add(infos.adresse)
                liste_desabo.append([infos.auteur, infos.adresse, infos.lien, infos.type_lien])
        print("[*] Recherche terminée !")
        print(f"[*] {len(set_adresses)} chaînes d'emailing ont été trouvées.")
        return liste_desabo
    except imaplib.IMAP4.error as e:
        print("[!] La connexion a été interrompue.")
        print("[*] Écriture des données déjà parcourues")
        print(e)
        write_data(liste_desabo)
        sys.exit(1)


def disconnect_user(connexion):
    print("[*] Fermeture de la connexion...")
    connexion.close()
    print("[*] Connexion fermée avec succès.")
    print("[*] Déconnexion...")
    connexion.logout()
    print("[*] Déconnecté")
