# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#! /usr/bin/env python

    
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    #return "Hello world !"
    return render_template('index.html')

if __name__ == "__main__":
    app.run()