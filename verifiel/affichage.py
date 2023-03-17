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
            return boite
        except ValueError:
            print("[!] Entrez un numéro de boîte mail valide.")
        except IndexError:
            print("[!] Entrez un numéro de boîte mail valide.")


def choix_action():
    message = """[*] Choisissez :
                1 - Scanner ma boîte mail
                2 - Procéder au désabonnement (ne fonctionne que si un scan a déjà été fait)
                >> Votre choix : """
    entry_incorrect = True
    while entry_incorrect:
        num_choix = input(message)
        try:
            num_choix = int(num_choix)
            if num_choix in [1, 2]:
                return num_choix
            else:
                print("[!] Entrez un choix valide.")
        except ValueError:
            print("[!] Entrez un choix valide.")
