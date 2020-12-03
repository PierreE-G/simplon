#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 09:40:35 2020

@author: pierre-etienne
"""

import numpy as np

app = 'Anthony Constant Joshua Fatima Julien Bassem Caroline Dan Ines Nidhal Sacia Xavier Roger Hachem Jean-Pierre Myriam Ludo Olivier Pierre-Etienne Wiem Cecilia'.split()
np.random.seed(1)
rapp = [app[i] for i in np.random.choice(21, 21, replace=False)]
for i in range(5):
    print(rapp[4*i:4*i+4] + ([rapp[-1]] if i == 4 else []))