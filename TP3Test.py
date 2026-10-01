#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 08:00:10 2026

@author: gaspard.naessens
"""

import TP3Fct as fct

mot = fct.ChoisirMot()

res = fct.AffcherProgres(mot)

test = fct.Jouer(res, mot)

