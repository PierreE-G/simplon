#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:09:48 2020

@author: randon
"""

import dash_html_components as html
from app import app
from app import server



layout = html.Div(children=[
        html.H3(
            children='Emotion_final.csv F1 Score ',
            style={
                'textAlign': 'center',
                }
            ),
        html.Div(html.Img(src=app.get_asset_url('f1_score.png')))
        ])


