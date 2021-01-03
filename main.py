import sqlite3
from flask import Flask, redirect, url_for, request, render_template
import sqlite3



app = Flask(__name__)
RES = {"isUserAv": False}

@app.route('/')
def main():
    return render_template('RealTimeMain.html', result = RES)

@app.route('/reg')
def registration():
    return render_template()

@app.route('/signin')
def signin():
    return render_template('RealTimeSignIn.html',userError=False )

@app.route('/bussiness')
def bussiness():
    return render_template('RealTimeBussiness.html', username = "Roni")

@app.route('/about')
def about():
    return render_template('RealTimeAbout.html')

@app.route('/logout')
def logout():
    global RES
    RES["isUserAv"] = False
    RES["user"] = None
    return redirect('/')


@app.route('/setUdata', methods=['POST'])
def loginUser():
    with sqlite3.connect('RealTime.db') as conn:
        cur = conn.cursor()
        result = request.form
        username = result.get('username')
        password = result.get('password')

        t = (username,)
        user = cur.execute("SELECT * FROM USERS WHERE USERNAME=? " ,t).fetchone()
        if(user and password == user[2]):
            global RES
            RES["isUserAv"] = True
            RES["user"] = username
            return redirect('/')
        else:
            return render_template('RealTimeSignIn.html', userError = True)

    # return render_template('RealTimeMain.html')

if __name__ == '__main__':
    app.run(port=3500, debug=True)