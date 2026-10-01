#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 08:00:58 2026

@author: gaspard.naessens
"""

""" Jeudi 1er octobre 2026 

 TP 3 CSpython : Le jeu du pendu
 
 
 Le but de ce TP est de développer votre propre version du célèbre jeu du pendu sous deux versions
différentes : la première en mode console, et la seconde avec une interface graphique construite à partir
du module Tkinter, le tout lors d’une séance de 4 heures, en respectant impérativement les bonnes
pratiques et le découpage en fonctions vus en cours."""


"""Fonctions attendues :
    
    ChoisirMot : la fonction choisir mot va prendre un fichier dans lequel des mots de 5 lettres ou plus
    sont rangés par taille et ordre alphabétique, puis prendre aléatoirement un des mots
    
    
    
    
    AfficherProgres : Cette fonction affiche une STR de _____, qui évolue au fil des essais de l'utilisateur.
    
    
    Jouer : Cette fonction s'occupe de faire torner le jeu, en utilisant les autres fonctions
    
    DevinerLettre : C'est la fonction qui va demander à l'utilisateur de faire des essais avec des lettres et lui 
    renvoyer le mot partiellement complété avec les lettres qu'il a déjà trouvé.
    
    L'utilisateur a 8 essais. Une bonne lettre n'enlève pas d'essais
    
    
"""
"""
TO DO

"""



import random


#trouve et ouvre le fichier contenant les mots
def ChoisirMot():
    
    TousLesMots = open("TP3CSPythonLISTE.txt", "r", encoding="utf-8") 
    
    ListeMots = TousLesMots.read().splitlines()
    
    
    MotMystere = random.choice(ListeMots).upper()
    
    
    return MotMystere


def AffcherProgres (MotMystere):
    
    Longueur = len(MotMystere)
    
    Underscore = "_"
    
    Progres = Underscore * Longueur
    
    print ('Le mot à trouver est :' ,Progres )
    
    return Progres



def Jouer(Progres, MotMystere):
    
    
    EssaisRestants = 8
    
    LettresTestées = []
    
    MotPendu = ''

    GameState = True
    BonnesLettres = []
    
    while GameState :
       
       GameState, EssaisRestants = TrouverLettre(Progres, MotMystere, LettresTestées, EssaisRestants, GameState, MotPendu, BonnesLettres)
       
    print('fin de la partie')
    Rejouer = input('Voulez-vous rejouer ?(True ou False):')
    if Rejouer == 'True':
        Jouer(Progres, MotMystere)
  

def TrouverLettre(Progres, MotMystere, LettresTestées, EssaisRestants, GameState, MotPendu, BonnesLettres):
    
    
    
    test = input('Entrez une lettre :')
    
    Essai = test.upper()
    
    if len (Essai) == 1:
        
        if Essai in MotMystere :
            
            if Essai in LettresTestées:
                EssaisRestants = EssaisRestants - 1
                print('Vous avez déjà essayé cette lettre, il vous reste donc', EssaisRestants, 'vies')
                
            LettresTestées.append (Essai)
            
            for i in range (len(MotMystere)):
                
                if Essai == MotMystere[i] :
                    
                    MotPendu += MotMystere[i]
                    BonnesLettres.append (Essai)
                    print ('Il vous reste',EssaisRestants,'vies')
                elif MotMystere[i] in BonnesLettres:
                    
                    MotPendu += MotMystere[i]
                    
                else:
                    
                    MotPendu += Progres[i]
                
                    
                    
            print (MotPendu)
            
        else :
            EssaisRestants = EssaisRestants - 1
            print ('Il vous reste',EssaisRestants,'vies')
            print (MotPendu)
            
        print(EssaisRestants)  
        if EssaisRestants == 0:
            GameState = False
            print('Perdu !')
        if MotPendu == MotMystere:
            GameState = False
            print ('Gagné !')
        print(GameState)
        return GameState, EssaisRestants
        
    
    
    






