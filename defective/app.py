from flask import Flask, render_template, jsonify, request, redirect
import os

app = Flask(__name__)


imgDir = '/Users/meoheee/Documents/GitHub/deep-cheese-learning/defective/templates/images'
imgLst = os.listdir(imgDir)
imgLst = [i for i in imgLst if i[-4:]==".png" or i[-4:]==".jpg"]
errorCnt = len(imgLst)
print(errorCnt)


@app.route('/')
def hello_world():  # put application's code here
    try:
        testlist = [i for i in range(errorCnt)]
        c = render_template('mainpage_2.html', myList=testlist)
    except:
        c = "NONO"
    return c


@app.route('/mapView')
def mapView():
    try:
        c = render_template('index.html', a=35.441524, b=126.469718)
    except:
        c = "NONO"
    return c



if __name__ == '__main__':
    app.run('0.0.0.0', 8080)
