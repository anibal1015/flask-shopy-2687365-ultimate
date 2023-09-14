from . import aut
from flask import render_template, redirect, flash
from .forms import LoginForm
import app

#dependencia para auth
from flask_login import current_user, login_user, logout_user

#ruta de login 
@aut.route('/login' , 
            methods = ['GET' , 'POST'])
def login():
    f = LoginForm()
    if f.validate_on_submit():
        #seleccionar el cliente con ese username
        c = app.models.Cliente.query.filter_by(
                            username = f.username.data
                            ).first()
        if c is None or not c.check_password(f.password.data):
            return redirect('/aut/login')
        else:
            login_user(c , True)
            return redirect('/productos/listar')
    return render_template("login.html" ,
                           f = f )

#ruta de log out 
@aut.route('/logout')
def logout():
    logout_user()
    return redirect("/aut/login")
