# -*- coding: utf-8 -*-
from flask import Flask, render_template, redirect, session, request
from flask.sessions import NullSession
from flask_wtf import form
from markupsafe import escape
from werkzeug.datastructures import TypeConversionDict
from forms import FAsociar, FcalificarProducto, FUsuario, Login, FProducto, FProveedor 
import gestorDB
import os



app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/", methods=["GET","POST"])
@app.route("/home/", methods=["GET","POST"])
@app.route("/inicio/", methods=["GET","POST"])
def home():
    if 'logged' in session:
        return render_template("home.html")
    else:
        return redirect('/login/')


@app.route('/logout/')
def logout():
    session.clear()
    return render_template('flogin.html')

@app.route("/login/", methods=["GET","POST"])
def login():
    frm = Login()
    if request.method=='GET':
        return render_template('flogin.html',titulo='Control de acceso', form=frm)
    else:
        # Recuperar los datos
        mail = escape(request.form['mail'].strip())
        pwd = escape(request.form['psw'].strip())
        # validar los datos
        admin= True
        swvalido = True
        query1=f"SELECT * FROM usuarios WHERE email= '{mail}' clave= '{pwd}'"
        query2=f"SELECT rol FROM usuarios WHERE email= '{mail}' clave= '{pwd}'"
        usr=gestorDB.seleccionar(query1)
        print(usr)
        rol=gestorDB.seleccionar(query2)
        return render_template('home.html')
        
        """
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
            session['admin_id']='Administrador'
            return render_template('home.html',admin_id=session['admin_id'])
        elif swvalido:
            session.clear()
            session['logged']='T'
            session['usr_id'] = mail
            session['pwd_id'] = pwd
            admin_id='Usuario final'
            return render_template('home.html',admin_id=admin_id)
        else:
            return render_template('flogin.html',titulo='Control de acceso', form=frm)
        """


@app.route("/recuperarContrasena/", methods=['GET','POST'])
def recuperarContraseña():
    if request.method=='GET':
        return render_template("recuperarContrasena.html")
    else:
        mail= request.form['mailTxt']
        name= request.form['nameTxt']
        if len(mail)<6:
            error='El email ingresado es invalido o no fue encontrado'
            return render_template("recuperarContraseña.html",error=error)
        if len(mail)>6 and len(name)>6:
            error='El email fue encontrado y se envio tu contraseña'
            return render_template("recuperarContrasena.html",error=error)


@app.route("/cambiarContrasena/", methods=['GET','POST'])
def cambiarContraseña():
    if request.method=='GET':
        return render_template("cambiarContrasena.html")
    else:
        name=request.form['nameTxt']
        mail=request.form['mailTxt']
        psw=request.form['newpasswordTxt']
        psw2=request.form['newpasswordTxt2']
        if psw==psw2:
            return render_template("cambiarContrasena.html",error="Contraseña cambiada")
        else:
            return render_template("cambiarContrasena.html",error="Confirme que las nuevas contraseñas sean iguales",name=name,mail=mail)


#
#               PROVEEDORES
#     

@app.route("/crearProveedor/",methods=["GET","POST"])
def crearProveedor():
    frm = FProveedor()
    if 'logged' in session:
        if request.method=='GET':
            return render_template("crearProveedor.html",titulo='Proveedor | Crear', form=frm, admin_id=session['admin_id'])
        else:
            return render_template("crearProveedor.html",form=frm)
    else:
        return redirect('/login/')

@app.route("/gestionarProveedores/",methods=["GET"])
def visualizarProveedores():
    frm = FProveedor
    return render_template("gestionarProveedores.html",form=frm)

@app.route("/editarProveedor/",methods=["GET","POST"])
def editarProveedor():
    frm = FProveedor()
    if request.method=='GET':
        return render_template("editarProveedor.html",form=frm)
    else:
        return render_template("editarProveedor.html",form=frm)

@app.route("/visualizarProveedor/",methods=["GET"])
def visualizarProveedor():
    frm = FProveedor()
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
      
@app.route("/crearProducto/",methods=["GET","POST"])
def crearProducto():
    frm = FProducto()
    if request.method=='GET':
        return render_template("crearProducto.html",form=frm)
    else:
         return render_template("crearProducto.html",form=frm)

@app.route("/gestionarProductos/",methods=["GET"])
def gestionarProductos():
    frm = FProducto()
    return render_template("gestionarProductos.html",form=frm)

@app.route("/editarProducto/",methods=["GET","POST"])
def editarProducto():
    frm = FProducto()
    if request.method=='GET':
        return render_template("editarProducto.html",form=frm)
    else:
        return render_template("editarProducto.html",form=frm)

@app.route("/visualizarProducto/",methods=["GET"])
def visualizarProducto():
    frm = FProducto()
    return render_template("visualizarProducto.html",form=frm)
        
@app.route("/asociarProveedores/",methods=["GET","POST"])
def asociarProveedores():
    frm = FAsociar()
    if request.method=='GET':
        return render_template("asociarProveedores.html",form=frm)
    else:
        return render_template("asociarProveedores.html",form=frm)

@app.route("/calificarProducto/",methods=["GET","POST"])
def calificarProducto():
    frm = FcalificarProducto()
    if request.method=='GET':
        return render_template("calificarProducto.html",form=frm)
    else:
         return render_template("calificarProducto.html",form=frm)


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

@app.route("/gestionarUsuarios/",methods=["GET"])
def gestionarUsuarios():
    frm = FUsuario
    return render_template("gestionarUsuarios.html",form=frm)

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

