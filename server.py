#STILL 2.7 SO SORRY
#(not sorry)


#generally useful
from time import time
import json
import os
from datetime import datetime as dt
from glob import glob
from commands import getoutput as go
import pandas as pd

#Flask Imports 
from flask import Flask,request,Response,send_file,redirect,url_for,flash,send_file
from functools import wraps



#### Below Here is the Flask!
#Instantiate Server
app = Flask(__name__,static_url_path='/static')


#Basic Path
@app.route('/')
def home(): return "foofs"

#Serve HTML
@app.route('/chapter/<chap>')
def chap(chap):
    if chap.find(".") > -1: return send_file("pages_html/"+chap)
    else: return open("index.html").read()

#Serve Hot Air MD
@app.route('/md/<go>')
def md(go): return open("pages_md/%s.md" % go).read()

@app.route('/<path>')
def get(path): return end_file(path)

if __name__ == "__main__": app.run(host="0.0.0.0",port=9100,debug=True)
