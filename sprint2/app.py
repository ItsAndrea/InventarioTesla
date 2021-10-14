# -*- coding: utf-8 -*-
from flask import Flask, render_template, session, request
from markupsafe import escape
from werkzeug.datastructures import TypeConversionDict
from forms import FAsociar, FcalificarProducto, FUsuario, Login,Cambiarcontraseña
# Proveedores
from forms import FcrearProveedor, FeditarProveedor,FvisualizarProveedor,FgestionarProveedores 
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
@app.route("/home/")
@app.route("/inicio/")
def home():
    return render_template("home.html")

@app.route('/logout/')
def logout():
    session.clear()
    return render_template('home.html')

@app.route("/login/", methods=["GET","POST"])
def login():
    frm = Login()
    if request.method=='GET':
        return render_template('flogin.html',titulo='Control de acceso', form=frm)
    else:
        # Recuperar los datos
        mail = request.form['mail']
        pwd = request.form['psw']
        admin= True
        # validar los datos
        swvalido = True
        if len(mail)<6 or len(mail)>40:
            swvalido = False
        if len(pwd)<6 or len(pwd)>40:
            swvalido = False
        #validar rol
        if swvalido and mail!="aaroncabrales@gmail.com" and pwd!="1234567":
            admin=False
        if mail!="aaroncabrales@gmail.com" and pwd!="1234567":
            admin=False
        # Realizar el login simulado
        if  admin:
            session.clear()
            session['logged']='T'
            session['usr_id'] = mail
            session['pwd_id'] = pwd
            session['admin_id']='T'
            admin_id='Administrador'
            return render_template('home.html',admin_id=admin_id)
        elif swvalido:
            session.clear()
            session['logged']='T'
            session['usr_id'] = mail
            session['pwd_id'] = pwd
            admin_id='Usuario final'
            return render_template('home.html',admin_id=admin_id)
        else:
            return render_template('flogin.html',titulo='Control de acceso', form=frm)

@app.route("/recuperarContraseña/", methods=['GET','POST'])
def recuperarContraseña():
    frm=Cambiarcontraseña()
    if request.method=='GET':
        return render_template("recuperarContraseña.html",form=frm)
    else:
        mail= request.form['mailTxt']
        name= request.form['nameTxt']
        if len(mail)<6:
            error='El email ingresado es invalido o no fue encontrado'
            return render_template("recuperarContraseña.html",error=error)
        if len(mail)>6 and len(name)>6:
            error='El email fue encontrado y se envio tu contraseña'
            return render_template("recuperarContraseña.html",error=error)


@app.route("/cambiarContraseña/", methods=['GET','POST'])
def cambiarContraseña():
    frm=Cambiarcontraseña()
    if request.method=='GET':
        return render_template("cambiarContraseña.html",form=frm)
    else:
        name=request.form['nameTxt']
        mail=request.form['mailTxt']
        psw=request.form['newpasswordTxt']
        psw2=request.form['newpasswordTxt2']
        if psw==psw2:
            return render_template("cambiarContraseña.html",error="Contraseña cambiada")
        else:
            return render_template("cambiarContraseña.html",error="Confirme que las nuevas contraseñas sean iguales",name=name,mail=mail)


#
#               PROVEEDORES
#     

@app.route("/crearProveedor/",methods=["GET","POST"])
def crearProveedor():
    frm = FcrearProveedor()
    if request.method=='GET':
        return render_template("crearProveedor.html",form=frm)
    else:
         return render_template("crearProveedor.html",form=frm)

@app.route("/gestionarProveedores/",methods=["GET"])
def visualizarProveedores():
    frm = FgestionarProveedores
    return render_template("gestionarProveedores.html",form=frm)

@app.route("/editarProveedor/",methods=["GET","POST"])
def editarProveedor():
    frm = FeditarProveedor()
    if request.method=='GET':
        return render_template("editarProveedor.html",form=frm)
    else:
        return render_template("editarProveedor.html",form=frm)

@app.route("/visualizarProveedor/",methods=["GET"])
def visualizarProveedor():
    frm = FvisualizarProveedor()
    return render_template("visualizarProveedor.html",form=frm)

@app.route("/asociarProductos/",methods=["GET","POST"])
def asociarProductos():
    frm = FAsociar()
    if request.method=='GET':
        return render_template("asociarProductos.html",form=frm)
    else:
        return render_template("asociarProductos.html",form=frm)



#
#               PRODUCTOS
#     

@app.route("/calificarProducto/",methods=["GET","POST"])
def crearUsuario():
    frm = FcalificarProducto()
    if request.method=='GET':
        return render_template("crearUsuario.html",form=frm)
    else:
         return render_template("crearUsuario.html",form=frm)
        
@app.route("/asociarProveedores/",methods=["GET","POST"])
def asociarProveedores():
    frm = FAsociar()
    if request.method=='GET':
        return render_template("asociarProveedores.html",form=frm)
    else:
        return render_template("asociarProveedores.html",form=frm)


#
#               USUARIOS
#     

@app.route("/crearUsuario/",methods=["GET","POST"])
def crearUsuario():
    frm = FUsuario()
    if request.method=='GET':
        return render_template("crearUsuario.html",form=frm)
    else:
         return render_template("crearUsuario.html",form=frm)

@app.route("/gestionarUsuarioes/",methods=["GET"])
def visualizarUsuarioes():
    frm = FUsuario
    return render_template("gestionarUsuarioes.html",form=frm)

@app.route("/editarUsuario/",methods=["GET","POST"])
def editarUsuario():
    frm = FUsuario()
    if request.method=='GET':
        return render_template("editarUsuario.html",form=frm)
    else:
        return render_template("editarUsuario.html",form=frm)

@app.route("/visualizarUsuario/",methods=["GET"])
def visualizarUsuario():
    frm = FUsuario()
    return render_template("visualizarUsuario.html",form=frm)



if __name__=='__main__':
    app.run(debug=True)

