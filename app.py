from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)

@app.route('/') #dekorator
def index():
    tanggal = datetime.now()
    return render_template('index.html', tanggal=tanggal)

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/tahun')
def datatahun():
    tahun = datetime.today()
    tahun = tahun.year
    return render_template('tahun.html', tahun=tahun)


@app.route('/about') #route statis
def about():
    return render_template ('about.html')
@app.route('/login', methods=['GET','POST'])
def masuklogin():
    if request.method == 'POST': #methode post untuk kirim data
        return "Selamat Datang " + request.form['email']
    return render_template('login.html')

@app.route ('/userloginget')
def userlogin():
    return render_template ('loginget.html')

@app.route ('/loginget', methods=['GET','POST'])
def loginget():
    cari = request.args.get ('email') #dictionary : pasangan q dan value
    if not cari:
        return render_template('index.html')
    
    return "Email Anda adalah " + cari

@app.route('/user/<username>') #route dinamis
def user(username):
    # return "Selamat datang %s " % username 
    # return "Selamat datang " + username #string concetinations
    # return "Selamat datang {}".format(username)
    #return f"Selamat datang {username}"
    return render_template('user.html', username=username)

#interpolation : menambahkan string ke string lainnya
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

