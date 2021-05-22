from flask import Flask, render_template, redirect, request, url_for, session, flash
from config import Config
from forms import LoginForm, Logout
from flask_mysqldb import MySQL
import time



app = Flask(__name__)
app.config.from_object(Config)


app.config['MYSQL_HOST'] = 'freedb.tech'
app.config['MYSQL_USER'] = 'freedbtech_cukieAdmin'
app.config['MYSQL_PASSWORD'] = 'iieessss11223344'
app.config['MYSQL_DB'] = 'freedbtech_SoShield'
mysql = MySQL(app)

initialize = 0


@app.route('/')
def index():
    global initialize
    print(initialize)
    if initialize == 0:
        session['loggedin'] = False
        initialize += 1
        redirect_url = url_for('activate')
        return render_template("index.html", redirect_url = redirect_url)
    else:
        if session['loggedin'] == True:
            redirect_url = url_for('safe')
        else:
            redirect_url = url_for('activate')
        return render_template("index.html", redirect_url = redirect_url)

@app.route('/activate/', methods=('GET', 'POST'))
def activate():
    if session['loggedin'] == True:
        return redirect(url_for('safe'))

    form = LoginForm()
    if form.validate_on_submit():
        cds = form.codes.data
        un = form.user_name.data
        pws = form.password.data
        cur = mysql.connection.cursor()
        print(type(cds))

        cur.execute('SELECT * FROM myUser WHERE codes = %s AND usernames = %s AND pw = %s', (cds, un, pws)) #check for exited users
        account = cur.fetchone()

        if account:
            session['loggedin'] = True
            session['username'] = un
            session['pw'] = pws
            return redirect('/safe/')
        else:
            t_un = str("default")
            t_pw = str("default")
            print(type(t_un))
            cur.execute('SELECT * FROM myUser WHERE codes = %s AND usernames = %s AND pw = %s', (cds, t_un, t_pw)) #将数据库初始值改成默认的
            new_account = cur.fetchone()
            if new_account:
                session['loggedin'] = True
                session['username'] = un
                session['pw'] = pws
                cur.execute('DELETE FROM myUser WHERE codes = %s AND usernames = %s AND pw = %s', (cds, t_un, t_pw))
                mysql.connection.commit()
                cur.execute('INSERT INTO myUser VALUES (%s, %s, %s)', (cds, un, pws))
                mysql.connection.commit()
                return redirect('/safe/')
            else:
                msg = "Username or password or activation code incorrect. Enter again."
                return render_template('activate.html', form = form, msg = msg)
    return render_template('activate.html', form = form, msg = "")


@app.route('/safe/', methods=['GET', 'POST'])
def safe():
    if session['loggedin'] == False:
        return redirect(url_for('index'))
    if request.method == "GET":
        form = Logout()
        return render_template("safe.html", form = form)
    elif request.method == "POST":
        session['loggedin'] =  False
        return redirect(url_for('index'))

@app.route('/danger/')
def danger():
    if session['loggedin'] == False:
        return redirect(url_for('index'))
    else:
        redirect_url = url_for('safe')
    return render_template('danger.html', redirect_url = redirect_url)


if __name__ == '__main__':
    app.run(debug=True)
