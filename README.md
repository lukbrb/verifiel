# Vérifiel

Vérifiel a pour but d'automatiser la désinsctiption aux chaînes d'emails, et la suppression de ces derniers si souhaité.
Pour ce faire, le logiciel procède de deux manières :
- Le logiciel vérifie si l'en-tête contient la clé "List-Unsubscribe", puis envoie un courriel à l'adresse liée pour 
se désabonner
- Dans un second temps, si rien n'est trouvé dans l'en-tête, le logiciel regarde si le corps du texte contient un lien 
avec le mot "unsubscribe". Envoyer une requête n'est généralement plus suffisant, l'utilisateur a alors le choix d'ouvrir 
le lien dans son navigateur. Une confirmation humaine est généralemet nécessaire.

## Organisation

Dans un premier temps les identifiants de l'utilisateur seront demandés. Rien n'est stocké, il faudra donc réentrer ses 
identifiants à chaque utilisation. Si la connexion réussie, le logiciel va commencer à scanner la boîte principale 
de l'utilisateur. Cela peut prendre un certain temps pour une première utilisation, étant de donné le nombre de courriels
généralement conséquent. 
Lors du scan, le logiciel écrit les adresses courriel correspondant aux chaînes d'emails dans un fichier JSON.

Une fois la phase de scan finie, le programme se met en pause et demande à l'utilisateur s'il souhaite maintenant 
procéder au désabonnement des chaînes trouvées. 
Pour chaque adresse, le programme demandera confirmation du souhait de se désabonner. Toutes les chaînes ne sont pas 
néfastes ! 


### Prochainement

L'idée est de tirer avantage du scan de la boîte mail pour trouver les sites qui possèdent donc votre adresse, et dont 
vous souhaiteriez éventuellement supprimer votre compte.


**Problèmes :**
- Problèmes d'encodage sur quelques adresses et liens
- Mettre à jour la liste une fois qu'on est désabonnés

**À implémenter sous peu :**
- L'envoi des courriels pour le désabonnement
- L'ajout des serveurs SMTP
- La suppression des messages (à voir)
- L'analyse des domaines, donc des sites possédants notre adresse
- Interface graphique permettant de sélectionner directement les adresses que l'on souhaite garder ou non
- Un installateur pour plateforme UNIX (Mac OS et Linux)

**À améliorer:**
- L'affichage des informations sur le terminal (voir CLI Python)
- Le temps d'éxecution du programme
- La flexibilité du programme pour ne pas avoir à tout réprendre de zéro si erreur il y a
- La documentation, la licence et le fichier README
