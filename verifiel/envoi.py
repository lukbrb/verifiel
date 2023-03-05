import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


SERVEUR = "smtp-mail.outlook.com"
PORT = 587
# Create message container - the correct MIME type is multipart/alternative.

text = "Vérifiel a envoyé ce courriel pour vous désabonner du message « list-unsubscribe »."


def prepare_message(expediteur, destinataire, texte, sujet):
    """
    Prépare le contenu et les métadonnées du message à envoyer.
    """
    msg = MIMEMultipart('alternative')
    msg['Subject'] = str(sujet)
    msg['From'] = expediteur
    msg['To'] = destinataire
    part1 = MIMEText(texte, 'plain')
    msg.attach(part1)
    return msg


def envoie_message(expediteur: str, destinataire: str, mot_de_passe: str, message: MIMEMultipart) -> None:
    """
        Envoie un courriel à l'adresse spécifiée par l'argument 'destinataire'
    """

    # Send the message via SMTP server.
    with smtplib.SMTP(SERVEUR, PORT) as server:
        server.starttls()
        server.login(expediteur, mot_de_passe)
        server.sendmail(expediteur, destinataire, message.as_string())
        print("[+] Message envoyé avec succès !")

