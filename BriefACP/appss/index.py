#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:07:42 2020

@author: randon
"""

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import app1, app2


app.layout = html.Div([
        # represents the URL bar, doesn't render anything
    dcc.Location(id='url', refresh=False),
    dcc.Link('Back to Main Menu', href='/'),
    html.Br(),
    dcc.Link('App 1', href='/apps/app1'),
    html.Br(),
    dcc.Link('App 2', href='/apps/app2'),
        # content will be rendered in this element
    html.Div(id='page-content'),
    html.Div(children=[
        html.H1(
            children='Welcome on Dash !',
            style={
                'textAlign': 'center',
                }
            )
        ]),
])


@app.callback(Output('page-content',
              'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/app1':
        return app1.layout
    elif pathname == '/apps/app2':
        return app2.layout
    else:
        return ''

if __name__ == '__main__':
    app.run_server(debug=True)