import csv
import re
import webbrowser

import requests

from envoi import prepare_message, envoie_message

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/58.0.3029.110 Safari/537.3"
}


def lance_desabonnement(expediteur, mdp, filename: str = "donnees_liste_emails.csv"):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        # Créer un objet reader CSV
        csvreader = csv.reader(csvfile, delimiter=',')
        entetes = next(csvreader)
        gere_desabonnement(csvreader, expediteur, mdp)


def analyse_lien(lien):
    match = re.search(r'https?://\S+', lien)
    if match:
        lien_valide = match.group(0).strip(",")
        type_lien = 'lien'
    else:
        match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', lien)
        if match:
            lien_valide = match.group(0)
            type_lien = 'mailto'
        else:
            lien_valide = lien
            type_lien = None

    return lien_valide, type_lien


def envoi_desabonnement(lien, type_lien, row, expediteur, mdp):
    if type_lien == 'lien':
        try:
            response = requests.get(lien, headers=headers)
            is_direct_unsubscribe = response.content.decode(
                "utf-8") == 'List-unsubscribe received' or response.content.decode("utf-8") == '{"success":true}'
            # Si désabo direct : réponse en octets 'List-unsubscribe received'
            if is_direct_unsubscribe:
                print("[+] Vous avez été automatiquement désabonné.")
            elif response.ok:
                print("[*] Impossible de se désabonner automatiquement.")
                input("[*] Appuyer sur une touche pour ouvrir la page de désabonnement dans votre navigateur.")
                webbrowser.open(lien)
            else:
                print(f"[!] Le lien {lien} a probablement expiré ou a été mal géré par Vérifiel.")
        except Exception as e:
            print("Erreur :", e)

    elif type_lien == 'mailto':
        destinataire = row[1] if row != "" else row[0]
        print("Envoi courriel à", destinataire)
        contenu_message = prepare_message(expediteur, destinataire=lien, texte="", sujet="list-unsubscribe")
        envoie_message(expediteur, destinataire=lien, mot_de_passe=mdp, message=contenu_message)
    else:
        print("Problème avec le lien :", lien)


def gere_desabonnement(data, expediteur, mdp):
    for row in data:
        auteur, courriel, lien, type_lien = row
        auteur = auteur.strip('"')
        lien, type_lien = analyse_lien(lien)

        # Demander ici si désabonnement de row[0]
        no_choix = True
        while no_choix:
            choix = input(f"Voulez-vous désabonner de {auteur}({courriel})? (o/n) ")
            if choix.upper() == "O":
                envoi_desabonnement(lien, type_lien, row, expediteur, mdp)
                no_choix = False
            elif choix.upper() == "N":
                no_choix = False
                continue
            else:
                print("[!] Réponse invalide. Taper o/O pour oui ou n/N pour non")
