import email
import re


class DataLien:
    def __init__(self, emetteur, lien, type_lien):
        self.emetteur = emetteur
        self.lien = lien
        self.type_lien = type_lien
        self.auteur, self.adresse = self.get_auteur_adresse()

    def get_auteur_adresse(self):
        try:
            auteur, adresse = self.emetteur.split('<')  # [1].replace('>', ''))
            return auteur, adresse.replace(">", "")
        except IndexError:
            adresse = ""
            return self.emetteur, adresse
        except ValueError:
            adresse = ""
            return self.emetteur, adresse

    def __str__(self) -> str:
        return f"DataLien(auteur={self.auteur}, adresse={self.adresse}, lien={self.lien}, type_lien={self.type_lien})"

    def __hash__(self):
        return hash((self.adresse, self.auteur))

    def __eq__(self, other):
        try:
            return (self.adresse, self.auteur) == (other.adresse, other.auteur)
        except AttributeError:
            return NotImplemented


def find_email_list(data) -> DataLien:
    try:
        message = email.message_from_bytes(data[0][1])
        auteur = message.get('From')
        list_unsubscribe = message.get('List-Unsubscribe')
        if list_unsubscribe:
            # Recherche un lien
            match = re.search(r'https?://\S+', list_unsubscribe)
            if match:
                type_link = "lien"
                lien = match.group(0)
            else:
                match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', list_unsubscribe)
                type_link = "mailto"
                lien = match.group(0) #list_unsubscribe.replace("<mailto:", "").replace(">", "")
            return DataLien(auteur.strip('"'), lien, type_link)

        unsubscribe_url = get_unsubscribe_url(str(message))
        if unsubscribe_url:
            type_link = "lien"
            lien = unsubscribe_url
            return DataLien(auteur, lien, type_link)
        else:
            return DataLien("NOLISTE <NOLISTE>", "", "")
    except TypeError:
        # print("[!] Erreur (TypeError), données : None")
        return DataLien("NOLISTE <NOLISTE>", "", "")
    except AttributeError:
        # print("[!] Erreur de lecture du message (AttributeError), données : None")
        return DataLien("NOLISTE <NOLISTE>", "", "")


def get_unsubscribe_url(msg_str):
    pattern = re.compile(r"^list\-unsubscribe:(.|\r\n\s)+<(https?:\/\/[^>]+)>",
                         re.M | re.I)
    match = pattern.search(msg_str)
    if match:
        return match.group(2)
    return match
