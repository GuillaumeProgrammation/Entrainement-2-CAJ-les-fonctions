#les fonctions

#ajouter avec , ou +
"""nom = "toto"
print("Je suis", nom,) # 2 paramètres 
print()
print("Je suis" + nom) #concaténé la chaine 1 seul paramètre

nom = input("Votre nom est :")
print("Tu es :", nom)"""


#exo, utilisation fonction
"""pers = int(input("Combien etes vous ?"))

def afficher_info(nom, age):
    print("La personne est", nom, "votre age est", age, "ans")
    print("Le nom comporte", len(nom), "caractere(s)", "l'age comporte", len(age), "caractere(s)")

for x in range (pers):
    afficher_info(input("Quel est votre nom ? "), input("Quel est votre age ? "))""" 




#exo if elif else
"""pers = int(input("Combien etes vous ? "))

nom = 0
age = 0
def afficher_info(nom, age):
    if len(age) <= 1 and len(nom) <=1:
        print("Votre nom et votre age comportent un seul caractere chacun.")
        print("Vous vous appelez", nom, "et vous avez", age, "an.")
        return 
        
    if len(age) >= 2  and len(nom) > 1:
        print("Votre nom et votre age comportent plusieurs caracteres tous deux.")
        print("Vous vous appelez", nom, "et vous avez", age, "ans.")               
    elif len(age) <= 1 and len(nom) > 1:
        print("Votre nom comporte", len(nom), "caracteres mais votre age n'en comporte qu'un seul.")
        print("Vous vous appelez", nom, "et vous avez", age, "an.")
    else:
        print("Votre nom comporte un caractere mais votre age en comporte plusieurs.")
        print("Vous vous appelez", nom, "et vous avez", age, "ans.")
    #Ou je peux mettre ça :    
    #elif len(age) >= 2 and len(nom) <= 1:
        #print("Votre nom comporte un caractere mais votre age en comporte plusieurs.")    


#def nom_personne(nom, age):
    #print("Vous vous appelez", nom, "et vous avez", age, "ans.")  

for x in range (pers):
    afficher_info(input("Quel est votre nom ? "), input("Quel est votre age ? "))
    #nom_personne(nom, age)"""    
 
#pour ne pas tout reecrire et ne faire peu de lignes -> utiliser fonction + parametre

"""nom = 0
age = 0
nb_personnes = int(input("Combien etes vous ? "))

def recuperer_info_personne_et_afficher(numero_personne):
    nom = input("Nom de la personne " + str(numero_personne) + ": ")
    age= input("Age de la personne " + str(numero_personne) + ": ")
    print("La personne ", numero_personne, "est", nom, "et son age est", age, "an(s)" )

for i in range(nb_personnes):
    recuperer_info_personne_et_afficher(i+1)"""

#Exercice anniversaire / jour restant 

#Exercice table de multiplication

"""n = int(input("Quel est ton chiffre ? : "))
min = int(input("Quel est ton min ? : "))
max = int(input("Quel est ton max ? : "))

while min > max:
        max = int(input("Quel est ton max ? : "))

def afficher_table_multiplication(n, min, max):

    for i in range(min , max+1):
        print(i, "x", n, "=", i*n)

afficher_table_multiplication(n, min , max)"""

#Coder un questionnaire 

score = 0 

# Question 1 
"""print("LA REPONSE DOIT ETRE EN MINUSCULE")
print("Quelle est la capitale de la France ?")
print(" (a) Paris (b)Nice")   

rep_1 = (input("Votre reponse : "))
print()

if rep_1 == "a" :
    print("Bonne reponse !")
    score = score + 1
else:
    print("Mauvaise reponse !")"""



#Question 1 variable sinon utiliser "tableau" ou "ligne"
 
r1 = "Paris"
r2 = "Nice"
pays_1 = "la France ?"


print("LA REPONSE DOIT ETRE EN MINUSCULE")
print("Quelle est la capitale de", pays_1)
print(" (a)", r1, "(b)", r2)   

rep_1 = (input("Votre reponse : "))
print()

if rep_1 == "a" :
    print("Bonne reponse !")
    score = score + 1
else:
    print("Mauvaise reponse !")



# Question 2

print()
print("Quelle est la capitale de l'Espagne ?")
print(" (a) Barcelone (b) Madrid")   

rep_2 = (input("Votre reponse : "))
print()

if rep_2 == "b" :
    print("Bonne reponse !")
    score = score + 1
else:
    print("Mauvaise reponse !")

#Question 3

print()
print("Quelle est la capitale de l'Italie ?")
print(" (a) Naple (b) Rome")   

rep_3 = (input("Votre reponse : "))
print()

if rep_3 == "b" :
    print("Bonne reponse !")
    score = score + 1
else:
    print("Mauvaise reponse !")

resultat = score
print(resultat,"/ 3")  




