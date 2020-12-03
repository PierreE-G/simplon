#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:05:26 2020

@author: randon
"""

import dash

app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server

