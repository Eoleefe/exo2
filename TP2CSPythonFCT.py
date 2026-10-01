#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 08:09:44 2026

@author: gaspard.naessens
"""

"""

TP2 CS Python 24 Septembre 2026
MAY Ethan et NAESSENS Gaspard, 3ETI

Explication en français de ce que le code doit faire:

On souhaite coder un automate qui vérifie si la syntaxe d'une phrase est correcte

On fournit à l'automate un dictionnaire comportant les mots utilisés dans la 
phrase à vérifier

Le dictionnaire associe chaque mot à sa nature puis l'automate vérifie que l'enchaînement
de la nature des mots forme une phrase correcte.

TO DO

Faire un deuxième fichier de test

Bien expliquer ce que font les fonctions et nos idées sur comment les coder

Coder la fonction pour découper la phrase

Tester

Coder la fonction qui vérifie la nature du mot

Tester

Découpage en fonction :

Fonction 1 : 
Découper la phrase : decouperPhrase
decouperPhrase récupère la phrase donnée par l'utilisateur et sépare les mots des 
autres.
On utilisera .split

Fonction 2 :
Associer chaque mot découpé à un numéro

"""

"""


"""


"""fonction 1 : decouperPhrase """


def decouperPhrase(phrase):
    
    phraseDecoupe = []
    
    if type(phrase) is str :
        
        phraseDecoupe = phrase.split(" ")
        
        return phraseDecoupe
        
    else :
        print('Ce n est pas une phrase')




def natureMot():
    
    for i in len (phraseDecoupe):
        
        if phraseDecoupe[i] in dicoPhrase.keys :
            
            print('Les mots sont dans le dictionnaire')
            
            numeroMots =[]
            numeroMots.append(dicoPhrase[i])
            
            return numeroMots
            
            
        
        else :
            print('merci d adapter votre phrase')
            










    
""" 
def motBienPlace():
    
"""


