from flask import Flask, render_template , request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    artists = pd.read_csv('data/artists.dat', sep='\t', usecols=['name'])

    listed = tuple(artists['name'])[:50]

    return render_template('index.html', listed = listed)

@app.route('/result')
def result():


    return render_template('result.html')