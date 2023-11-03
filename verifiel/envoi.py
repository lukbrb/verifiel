import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


SERVEUR = "smtp-mail.outlook.com"
PORT = 587
# Create message container - the correct MIME type is multipart/alternative.

text = "Vérifiel a envoyé ce courriel pour vous désabonner du message « list-unsubscribe »."


class Message:
    def __init__(self, expediteur: str, destinataire: str, texte: str, sujet: str) -> None:
        self.exp = expediteur
        self.dest = destinataire
        self.txt = texte
        self.sujet = sujet
    
    def _prepare_message(self) -> MIMEMultipart:
        """
        Prépare le contenu et les métadonnées du message à envoyer.
        """
        msg = MIMEMultipart('alternative')
        msg['Subject'] = str(self.sujet)
        msg['From'] = self.exp
        msg['To'] = self.dest
        part1 = MIMEText(self.txt, 'plain')
        msg.attach(part1)
        return msg
    
    def envoie_message(self, mot_de_passe: str) -> None:
        """
            Envoie un courriel à l'adresse spécifiée par l'argument 'destinataire'
        """
        message = self._prepare_message()
        with smtplib.SMTP(SERVEUR, PORT) as server:
            server.starttls()
            server.login(self.exp, mot_de_passe)
            server.sendmail(self.exp, self.dest, message.as_string())
            print(f"[+] Message envoyé avec succès à {self.dest}!")
