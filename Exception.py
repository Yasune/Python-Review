print('====== Handle Exceptions=======')

num=1.
den=0.

try:
   result=num/den

except NameError:
    print("Variable non definie")
except TypeError:
    print("Type de variable non adapte")
except ZeroDivisionError:
    print("Division par zero")

#Note
#Usage of else
#Usage of finally
#Usage of assert


print('=======Raise Exception========')
annee = input() # L'utilisateur saisit l'annee

try:

    annee = int(annee) # On tente de convertir l'annee

    if annee<=0:

        raise ValueError("l'annee saisie est negative ou nulle")

except ValueError:

    print("La valeur saisie est invalide (l'annee est peut-etre negative).")