#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dash
import dash_table
import pandas as pd
import numpy as np

import dash_core_components as dcc
import dash_html_components as html


#import nltk
from sklearn.feature_extraction.text import CountVectorizer

from app import app
import plotly.graph_objs as go

global df, df0, df1

df0 = pd.read_csv('Emotions_final.csv')
df1 = pd.read_csv('text_emotion.csv')
df1=df1.iloc[:, lambda df: [3, 1]]
df1.columns = ['Text','Emotion']
df=df0

corpus = df['Text']
targets = df['Emotion']
#stopwords = nltk.corpus.stopwords.words("english")
#stopwords.append('feel')
#stopwords.append('feeling')

dfLabels = df.groupby('Emotion')
y1=dfLabels['Emotion'].size().sort_values(ascending=False)

############# barplot emotion_occurences ->fig ################

trace = go.Bar(
            x = y1.index.get_level_values(0).tolist(),                  
            y = y1,
            name = 'Income',
            type = 'bar',
            )

layout = go.Layout(
            xaxis = {'title': 'Emotions'},
            yaxis = {'title': 'Occurences'},
            barmode = 'relative')
#            title = 'Emotions ranked by occurence in Emotion_final')
fig1 = go.Figure(data = trace, layout = layout)


def subsample(x, step=900):
    return np.hstack((x[:10], x[10::step]))
corpus = df['Text']
targets = df['Emotion']
vect = CountVectorizer()
X = vect.fit_transform(corpus)
wsum = np.array(X.sum(0))[0]
ix = wsum.argsort()[::-1]
wrank = wsum[ix] 
words = vect.get_feature_names()
labels = [words[i] for i in ix]
freq = subsample(wrank)

x = subsample(labels)
y = freq
trace = go.Bar(x=x,
               y=y,         
                name = "Words ordered by rank. The first rank is the most frequent words and the last one is the less present",
                marker = dict(color = 'rgba(255, 174, 255, 0.5)',
                             line = dict(color ='rgb(0,0,0)',width =1.5))
                #text = y.index.get_level_values(0).tolist())
              )

layout = go.Layout(barmode = "group")
fig = go.Figure(data = trace, layout = layout)

############# corpus - target #################################

corpus = df['Text']
targets = df['Emotion']

###################### Display ##################################

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}


layout = html.Div(children=[

    html.Div( children=html.Div(
             'Select file',
         style={
        'textAlign': 'center',
    })
        ),
    
    ############### Séléction fichier ###

    dcc.Dropdown(
        id='files-dropdown',
        options=[
            {'label': 'Emotions_final.csv', 'value': 'Emotions_final.csv'},
            {'label': 'text_emotion.csv', 'value': 'text_emotion.csv'}
        ],
        value='Emotions_final.csv'
        ),
    html.Div(id='output_df'),
    
    
    html.Br(),
    html.Br(),
    html.Div(style={'backgroundColor': colors['background']}, 
             children=html.Div(
             'Emotions ranked by occurence',
         style={
        'textAlign': 'center',
        'color': colors['text']
        
    })
        ),

    html.Br(),
    html.Div(dcc.Graph(
        id='bar1',
        figure=fig1
        ),
    
    ),
    html.Br(),
    html.Div(style={'backgroundColor': colors['background']}, 
             children=html.Div(
             'Words frequency',
         style={
        'textAlign': 'center',
        'color': colors['text']
        
    })
        ),

    html.Br(),
    html.Div(dcc.Graph(
        id='bar1',
        figure=fig
        ),
    ),
    
 ]),



@app.callback(
     dash.dependencies.Output('output_df','children'),
     dash.dependencies.Input('files-dropdown','value'))

def set_display_children(selected_value):
    if selected_value =='Emotions_final.csv':

        table1=dash_table.DataTable(
                                    data=df0.to_dict('records'),
                                    columns=[{'id': c, 'name': c} for c in df0.columns],
                                    style_header={'backgroundColor': 'rgb(30, 30, 30)'},
                                    style_table={'overflowX': 'auto',
                                                  'width' : '1000px',
                                                  'height': '200px'},
                                    style_cell={
                                        'height': 'auto',
                                        'width': 'auto',
                                        'whiteSpace': 'normal',
                                        'backgroundColor': 'rgb(50, 50, 50)',
                                        'color': 'white'
                                        },
                                    editable=True),

        return table1
    elif selected_value =='text_emotion.csv':
        table2=dash_table.DataTable(
                                    data=df1.to_dict('records'),
                                    columns=[{'id': c, 'name': c} for c in df1.columns],
                                    style_header={'backgroundColor': 'rgb(30, 30, 30)'},
                                    style_table={'overflowX': 'auto',
                                                  'width' : '1000px',
                                                  'height': '200px'},
                                    style_cell={
                                        'height': 'auto',
                                        'width': 'auto',
                                        'whiteSpace': 'normal',
                                        'backgroundColor': 'rgb(50, 50, 50)',
                                        'color': 'white'
                                        },
                                    editable=True),
        return table2
    
    