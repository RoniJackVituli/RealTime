from flask import Flask, redirect, url_for, request, render_template
import sqlite3






app = Flask(__name__)
RES = {"isUserAv": False, "user": None, "isManager": False , "UserOff":True}

def newDic(tup):
    return {"username":tup[0],
            "firstnama":tup[1],
            "password":tup[2]
            }

def tupleToDic(item):
    return {
        "company": item[0],
        "link": item[1],
        "photo": item[2],
        "hour": item[3],
        "desc":item[4],
        "username": item[5]
    }

def reivewToDic(rev):
    return {
        "name":rev[0],
        "comment":rev[1]
    }

@app.route('/')
def main():
    global RES
    with sqlite3.connect('RealTime.db') as conn:
        cur = conn.cursor()
        RES["items"] = []
        RES["Review"] = []
        items = cur.execute("SELECT company,storelink,storePhoto,storeHoure,desc ,username FROM stores").fetchall()
        for item in items:
            RES["items"].append(tupleToDic(item))
        review = cur.execute("SELECT user ,comment FROM review").fetchall()
        for rev in review:
            RES["Review"].append(reivewToDic(rev))
        print(RES['items'])
    return render_template('RealTimeMain.html', result=RES)

@app.route('/signin')
def signin():
    return render_template('RealTimeSignIn.html',userError=False )

@app.route('/bussiness')
def bussiness():
    return render_template('RealTimeBussiness.html', username=RES["user"])


# --------------- Reg Users ----------------------------
@app.route('/regUser')
def regUser():
    return render_template("RealTimeRegistration.html")
@app.route('/register', methods=["POST"])
def registerToDb():
    result = request.form
    if(result.get('password') == result.get('secPass')):
        sql = ''' INSERT INTO users(username,firstname,password)
                              VALUES(?,?,?) '''
        RegUser = (result.get('username'), result.get('firstname'),
                        result.get('password'))
        with sqlite3.connect('RealTime.db') as conn:
            cur = conn.cursor()
            try:
                cur.execute(sql, RegUser)
                conn.commit()
                return redirect('/')
            except Exception as e:
                print(e)
                return render_template('RealTimeRegistration.html', UserNotOk = True)
    else:
        return render_template("RealTimeRegistration.html", notSaved = True)

# --------------- Reg Bussiness ----------------------------
@app.route('/regBus', methods=['POST'])
def regBuis():
    result = request.form
    sql = ''' INSERT INTO stores(company,numofpe,storelink,storePhoto,storeHoure,desc,username)
                  VALUES(?,?,?,?,?,?,?) '''
    storeData = (result.get('company'), int(result.get('numOfpeople')),
                 result.get('link'), result.get('photo'),
                 result.get('hours'), result.get('description'), RES["user"])
    with sqlite3.connect('RealTime.db') as conn:
        cur = conn.cursor()
        try:
            cur.execute(sql, storeData)
            conn.commit()
            return redirect('/')
        except Exception as e:
            print(e)
            return render_template('RealTimeBussiness.html', saved=False, username=RES["user"])

#--------------- About Page ----------------------------

@app.route('/about')
def about():
    return render_template('RealTimeAbout.html')

#--------------- logout----------------------------
@app.route('/logout')
def logout():
    global RES
    RES["isManager"] = False
    RES["UserOff"] = True
    RES["isUserAv"] = False
    RES["user"] = None
    return redirect('/')


#--------------- setting ----------------------------
@app.route('/setting')
def setting():
    return render_template('RealTimeSetting.html')

# --------------- Change Password ----------------------------

@app.route('/cp')
def cp():
    return render_template('RealTimeChangePassword.html')
@app.route('/changePassword', methods=['POST'])
def changePassword():
    with sqlite3.connect('RealTime.db') as conn:
        cur = conn.cursor()
        result = request.form
        username = RES['user']
        password = result.get('newPass')
        t = (username,)
        user = cur.execute("SELECT * FROM USERS WHERE USERNAME=? ", t).fetchone()
        if(result.get('oldPass') == newDic(user)['password']):
            try:
                cur.execute("UPDATE users SET password = ? WHERE username = ?", (password, username))
                conn.commit()
                return redirect('/')
            except Exception as e:
                print(e)
                return render_template('RealTimeChangePassword.html')
        return render_template('RealTimeChangePassword.html', passNotOK = True)


# --------------- Delete Users ----------------------------
@app.route('/du')
def du():
    print('page')
    return render_template('RealTimeDeleteUser.html')

@app.route('/delete', methods=['POST'])
def deleteUser():
    with sqlite3.connect('RealTime.db') as conn:
        global RES
        cur = conn.cursor()
        result = request.form
        if(result.get('yesOrNo') == "YES"):
            try:
                deleteStore()
                cur.execute("DELETE FROM users WHERE username = ?",(RES['user'],))
                conn.commit()
                RES["isUserAv"] = False
                RES["UserOff"] = True
                RES["user"] = None
                return redirect('/')
            except Exception as e:
                print(e)
                return render_template('RealTimeChangePassword.html')

    return redirect('/setting')

def deleteStore():
    with sqlite3.connect('RealTime.db') as conn:
        global RES
        cur = conn.cursor()
        try:
            cur.execute("DELETE FROM stores WHERE username = ?", (RES['user'],))
            conn.commit()
            return
        except Exception as e:
            print(e)
    return


@app.route('/setUdata', methods=['POST'])
def loginUser():
    with sqlite3.connect('RealTime.db') as conn:
        global RES
        cur = conn.cursor()
        result = request.form
        username = result.get('username')
        password = result.get('password')
        t = (username,)
        user = cur.execute("SELECT * FROM USERS WHERE USERNAME=? " ,t).fetchone()
        if(user and password == user[2]):
            RES["isUserAv"] = True
            RES["UserOff"] = False
            RES["user"] = username
            return redirect('/')
        user = cur.execute("SELECT * FROM manager WHERE username = ? " ,t).fetchone()
        if (user and password == user[1]):
            RES["isManager"] = True
            RES["UserOff"] = False
            RES["user"] = username
            return redirect('/')
        else:
            return render_template('RealTimeSignIn.html', userError=True)

    # return render_template('RealTimeMain.html')


#--------------- Review ----------------------------

@app.route('/main' ,methods=['POST'])
def review():
    result = request.form
    sql = ''' INSERT INTO review(user,comment)
                      VALUES(?,?) '''
    storeData = (result.get('name'), result.get('comment'))
    with sqlite3.connect('RealTime.db') as conn:
        cur = conn.cursor()
        try:
            cur.execute(sql, storeData)
            conn.commit()
            return redirect('/')
        except Exception as e:
            print(e)
            return render_template('RealTimeMain.html', UserNotOk=True)


#--------------- Manager Area ----------------------------

#--------------- setting Manager ----------------------------
@app.route('/Msetting')
def m_setting():
    return render_template('RealTimeManagerSetting.html')

@app.route('/Au')
def Au():
    return render_template("RealTimeAddUser.html")

@app.route('/addUser', methods=["POST"])
def addUser():
    result = request.form
    if(result.get('password') == result.get('secPass')):
        sql = ''' INSERT INTO users(username,firstname,password)
                              VALUES(?,?,?) '''
        RegUser = (result.get('username'), result.get('firstname'),
                        result.get('password'))
        with sqlite3.connect('RealTime.db') as conn:
            cur = conn.cursor()
            try:
                cur.execute(sql, RegUser)
                conn.commit()
                return redirect('/')
            except Exception as e:
                print(e)
                return render_template('RealTimeRegistration.html', UserNotOk = True)
    else:
        return render_template("RealTimeRegistration.html", notSaved = True)


if __name__ == '__main__':
    app.run(port=3500, debug=True)