# Dit bonjour ou bonsoir selon le moment de la journée et la langue 
print("Bonjour");

# si un palindrôme est saisie, répond "Bien dit!"
motSaisie = input("saisissez votre mot : "); 
motInverse = motSaisie[::-1];
print("mot inversé : " + motInverse)

if(motInverse == motSaisie):
    print("Bien dit!");


# à l'arrêt dit aurevoir selon le moment de la journée
print("Au revoir")