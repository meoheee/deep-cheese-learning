from flask import Flask, render_template, jsonify, request, redirect
import os

app = Flask(__name__)


imgDir = 'templates/images'
imgLst = os.listdir(imgDir)
imgLst = [i for i in imgLst if i[-4]==".png" or i[-4]==".jpg"]
errorCnt = len(imgLst)

@app.route('/')
def hello_world():  # put application's code here
    try:
        testlist = [i for i in range(errorCnt)]
        a = render_template('mainpage_2.html', myList=testlist)
    except:
        a = "NONO"
    return a



if __name__ == '__main__':
    app.run('0.0.0.0', 8080)
