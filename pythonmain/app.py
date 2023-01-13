from flask import Flask, render_template, jsonify, request, redirect
import socket

app = Flask(__name__)


class error:
    def __init__(self, errId, errImg, errWedo, errGyeongdo, errName):
        self.id = errId
        self.img = errImg
        self.wedo = errWedo
        self.gyeongdo = errGyeongdo
        self.name = errName


testerror = error(1, None, 35.441524, 126.469718, "spot")


@app.route('/')
def hello_world():  # put application's code here
    try:
        a = render_template('mainpage_2.html')
    except:
        a = "NONO"
    return a


@app.route('/fileUpload', methods = ['GET', 'POST'])
def uploadFile():
    if request.method == 'POST':
        f = request.files['file']
        f.save("./templates/"+f.filename)
        return 'uploads'




if __name__ == '__main__':
    app.run('0.0.0.0', 8080)
