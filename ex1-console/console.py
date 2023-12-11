# Dit bonjour ou bonsoir selon le moment de la journée et la langue 
import datetime

# Obtenir l'heure actuelle
heure_actuelle = datetime.datetime.now().time()

# Récupérer l'heure sous forme de chiffres
heure = heure_actuelle.hour

# Déterminer le moment de la journée en fonction de l'heure
moment_journee = None
if 5 <= heure < 12:
    moment_journee = "matin"
elif 12 <= heure < 18:
    moment_journee = "après-midi"
elif 18 <= heure < 22:
    moment_journee = "soir"
else:
    moment_journee = "nuit"

# En fonction du moment de la journée, saluer en conséquence
if moment_journee in ["matin", "après-midi"]:
    print("Bonjour")
else:
    print("Bonsoir")


# si un palindrôme est saisie, répond "Bien dit!"
motSaisie = input("saisissez votre mot : "); 
motInverse = motSaisie[::-1];
print("mot inversé : " + motInverse)

if(motInverse == motSaisie):
    print("Bien dit!");


# à l'arrêt dit aurevoir selon le moment de la journée
if moment_journee in ["matin", "après-midi"]:
    print("Au revoir, bonne journée")
elif moment_journee in ["soir"]:
    print("Au revoir, bonne soirée")
else:
    print("Au revoir, bonne nuit")