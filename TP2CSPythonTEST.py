#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 08:10:39 2026

@author: gaspard.naessens
"""

import TP2CSPythonFCT as fct

matTransition = [[1, 8, 8, 4, 8, 8],
                [8, 2, 8, 8, 1, 8], 
                [8, 8, 3, 8, 2, 8],
                [5, 8, 8, 7, 8, 9],
                [8, 8, 3, 8, 8, 8],
                [8, 6, 8, 8, 5, 8],
                [8, 8, 8, 8, 6, 9],
                [8, 8, 8, 8, 8, 9]]


dicoPhrase = {"le" : 0, "la" : 0, "chat" : 2, "souris" : 2, "martin" : 4,
"mange" : 3, "la" : 0, "petite" : 1, "joli" : 1, "grosse" : 1,
"bleu" : 1, "verte" : 1, "dort" : 3,"julie" : 4, "jean" : 4, "." : 5}


res = fct.decouperPhrase('Le chat mange')
print (res)



res = fct.natureMot()
print (res)