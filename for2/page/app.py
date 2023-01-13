from flask import Flask,render_template
app = Flask(__name__)

@app.route('/') # 주소창에 127.0.0.1:5000 입력하면 열림
def test():
    testlist = []
    for i in range(0, 10):
        testlist.append(i)
    return render_template('mainpage_2.html', myList=testlist) #myList라는 이름으로 testlist를 웹에 보내겠다.

if __name__ == '__main__':
    app.run(debug=True)