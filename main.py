import sqlite3
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)


RES = {"isUserAv": False}

@app.route('/bad')
def bad():
    return "You are not user!!!!!!"


@app.route('/')
def main():
    return render_template('RealTimeMain.html', result = RES)


@app.route('/signin')
def signin():
    return render_template('RealTimeSignIn.html')

@app.route('/setUdata', methods=['POST'])
def registerUser():
    result = request.form
    username = result.get('username')
    # print(result.get('username'))
    # print(result.get('password'))
    if(username == None):
        return redirect('/bad')
    global RES
    RES["isUserAv"] = True
    RES["user"] = username
    return redirect('/')
    # return render_template('RealTimeMain.html')

if __name__ == '__main__':
    app.run(port=3500, debug=True)