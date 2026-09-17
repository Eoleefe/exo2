#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 08:18:24 2026

@author: gaspard.naessens
"""

"""Programme où l'on écrit les fonctions TP1 CSPython 17/09/26"""
""" TODO""" 

"""il reste l'exercice 3, sur les impots à faire, on a juste commencé à expliquer et à réfléchir en amont"""










# exercice 2.2 : Calendrier

#2.2.1
""" on veut demander à l'utilisateur une année et le programme renvoie True ou False si l'année est bissextile ou non"""



"""une année est bissextile si elle est multiple de 400 
On peut donc diviser l'année donnée par l'utilisateur et vérifier que c'est un entier"""



"""Sinon une année est bissextile si elle est multiple de 4 mais ne se termine pas par xx00"""

"""le paramètre d'entrée est une année, donc un Int"""

def BissextileCheck(A):
    Annee = A

        
    if Annee%400 == 0 or (Annee%4 == 0 and Annee%100 != 0) :
        return True
        
    else:
        return False


#2.2.2
"""l'utilisateur nous donne un mois et une année et la fonction donne le nombre de jours de ce mois

Donc on doit tester si l'année est bissextile puis comparer avec le dictionnaire des mois et jours

Puis la fonction renvoie le nombre du jours du mois"""

"""le paramètre d'entrée est une année, donc un Int, et un mois, qui peut être un Str ou un Int """

def JourMois(M, A):
    DicoInt = { 1:31, 2:28, 3:31, 4:30, 5:31, 6:30 ,7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    DicoStr = { 'Janvier':31, 'Février':28, 'Mars':31, 'Avril':30, 'Mai':31, 'Juin':30, 'Juillet':31, 'Août':31, 'Septembre':30, 'Octobre':31, 'Novembre':30, 'Décembre':31}
    
    if (type(M) is str and M not in DicoStr):
        print('Veuillez marquer le nom du mois avec une Majuscule à la première lettre, ainsi que tous les accents au bons endroits, sinon, indiquez le numéro du mois à la place')
    
    if M == 2 or M == 'Février':
        if A%400 == 0 or (A%4 == 0 and A%100 != 0) :
            return 29
        else:
            return 28
    
    
    else:
        
        if type(M) == int:
            
            ValRen = DicoInt[M]
            return ValRen
        elif type(M) is str:
            
            ValRen = DicoStr[M]
            return ValRen
    
    
    
#2.2.3
""" on va vérfier que la date que nous donne l'utilisateur est valide, donc attention à février  bissextile, aux jour=31 pour certains mois et février"""

"""Les paramètres d'entrée sont un jour (Int), un mois (Int ou Str), ou une année (Int)"""

def DateCheck(J,M,A):
    
    DicoInt = { 1:31, 2:28, 3:31, 4:30, 5:31, 6:30 ,7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    
    DicoStr = { 'Janvier':31, 'Février':28, 'Mars':31, 'Avril':30, 'Mai':31, 'Juin':30, 'Juillet':31, 'Août':31, 'Septembre':30, 'Octobre':31, 'Novembre':30, 'Décembre':31}
    
    ListeMois31 = [1, 3, 5, 7, 8, 10, 12]
    
    ListeMoisStr = ['Janvier', 'Mars', 'Mai', 'Juillet', 'Août', 'Octobre', 'Décembre']
 
    
    if (type(M) is str and M not in DicoStr):
        print('Veuillez marquer le nom du mois avec une Majuscule à la première lettre, ainsi que tous les accents au bons endroits, sinon, indiquez le numéro du mois à la place')

    if (type(J) is int) and (type(A) is int) :
#partie de la fonction qui vérfie pour un mois indiqué en chiffre  
        if 1 <= J <= 31:
            if (type(M) == int and 1 <= M <= 12):
            
                if 1<= J <=28:
                    return True
                
                if (M == 2 ):
                    
                    if A%400 == 0 or (A%4 == 0 and A%100 != 0) :
                        
                        if J == 29:
                            
                            return True
                        
                        
                if (M != 2 ):
                
                    if (J == 29 or J == 30):
                        
                        return True
                    
                    if J == 31 and (M in ListeMois31 ):
                        
                        return True
                    
                    else:
                        return False
                    
                
                else:
                    return False
    
    #partie de la fonction qui vérifie pour un mois indiqué en lettres
            if M in DicoStr:
                
                if 1<= J <=28:
                    return True
                
                if (M == 'Février' ):
                    
                    if A%400 == 0 or (A%4 == 0 and A%100 != 0) :
                        
                        if J == 29:
                            
                            return True
                        
                        
                if (M != 'Février' ):
                
                    if (J == 29 or J == 30):
                        
                        return True
                    
                    if J == 31 and (M in ListeMoisStr ):
                        
                        return True
                    
                    else:
                        return False
                    
                
                else:
                    return False
            
        else:
            return False
            
    else:
        print('Merci d indiquer une date avec une année et un jour en chiffre, pour le mois, vous avez le choix entre chiffre ou lettres')

        
#2.2.4

"""On va vouloir faire un programme qui propose la saisie d'une date, qui la valide et qui affiche le message 'date valide' ou 'date non valide'"""

"""il n'y a pas ed variables car on les demande à lu'tilisateur"""


def DemandeJour():
    
    J = 0 
    M = 0 
    A = 0 
    ListeMois31 = [1, 3, 5, 7, 8, 10, 12]
    
    J = int(input('Saisissez un jour entre 1 et 31 : '))
    M = int(input('Saisissez un mois entre 1 et 12 : '))
    A = int(input('Saisissez une année (nombre entier) : '))
    
    if (type(J) is int) and (type(A) is int) and (type(M)is int):
#partie de la fonction qui vérfie pour un mois indiqué en chiffre  
        if 1 <= J <= 31:
            if  1 <= M <= 12:
            
                if 1<= J <=28:
                    print ('date valide')
                
                if (M == 2):
                    
                    if A%400 == 0 or (A%4 == 0 and A%100 != 0) :
                        
                        if J == 29:
                            
                            print ('date valide')
                        
                        
                if (M != 2 ):
                
                    if (J == 29 or J == 30):
                        
                        print ('date valide')
                    
                    if J == 31 and (M in ListeMois31):
                        
                        print ('date valide')
          
                    
            else:
                 print('date non valide')
        
        
        else:
            print ('date non valide')
    
    
    
    
#3.3.2
""" on va devoir faire une fonction qui demande à l'utilisateur ses revenus et calculer les impôts qu'il doit par rapport à la fiche d'imposition."""

"""les impots sont calculées sur les sommes dépassant tels montants de tranche"""

    












