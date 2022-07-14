#Python program to detect stress

from flask import Flask,render_template,Response
import test
from test import VideoCamera

app=Flask(__name__,template_folder='D:/Stress_Detector/code/templates')

@app.route('/')
def index():
    return render_template('index.html')
def gen(test):
    """ Video Streaming generator Function."""
    
    while(True):
        frame=test.get_frame()
        yield(b'--frame\r\n')
        
        
        #.................Ctd