# -*- coding: utf-8 -*-
from flask import Flask, render_template, redirect, session, request
from flask.sessions import NullSession
from markupsafe import escape
from werkzeug.datastructures import TypeConversionDict
from forms import FAsociar, FcalificarProducto, FUsuario, Login, FProducto, FProveedor 
#librerios hash
from hashlib import sha512, md5
from werkzeug.security import check_password_hash, generate_password_hash
import os

#funcion provisional
def trash(q):
    a=str(q[0]).replace("('"," ")
    a=a.replace("',)","")
    return a

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


@app.route('/logout/',methods=["GET","POST"])
@app.route("/login/", methods=["GET","POST"])
def login():
    frm = Login()
    session.clear()
    if request.method=='GET':
        return render_template('flogin.html',titulo='Control de acceso', form=frm)
    else:
        # Recuperar los datos
        mail = escape(request.form['mail'].strip())
        pwd = escape(request.form['psw'].strip())
        admin= False
        superadmin=False
        p=False
        q=f"SELECT clave FROM usuarios WHERE email= '{mail}' "
        a=gestorDB.seleccionar(q,"")
        a= trash(a).strip()
        if check_password_hash(a,pwd):
            p=True
        else:
            p=False
            
        query1=f"SELECT * FROM usuarios WHERE (email= '{mail}') and (estado='P') "
        query2=f"SELECT * FROM usuarios WHERE (email= '{mail}') and (rol='Admin')"
        query3=f"SELECT * FROM usuarios WHERE (email= '{mail}') and (rol='Super')"
        usr=gestorDB.seleccionar(query1,"")
        ad=gestorDB.seleccionar(query2,"")
        superad= gestorDB.seleccionar(query3,"")
        if len(ad)>0 and p:
            admin=True
        if len(superad)>0 and p:
            superadmin= True
        if len(usr)>0 and p:
            session.clear()
            session['logged']='T'
            session['usr_id'] = mail
            session['pwd_id'] = pwd
            if superadmin:
                session['admin_id']='T'
                session['superadmin_id']='T'
                return render_template('home.html',admin_id="Super Admin")
            if admin:
                session['admin_id']='T'
                return render_template('home.html',admin_id="admin")
            else:
                return render_template('home.html',admin_id="usuario")
        else:
            error="Credenciales invalidas"
            return render_template('flogin.html', error=error)

@app.route("/cambiarContrasena/", methods=['GET','POST'])
def cambiarContraseña():
    if request.method=='GET':
        return render_template("cambiarContrasena.html")
    else:
        name=escape(request.form['nameTxt']).strip()
        mail=escape(request.form['mailTxt']).strip()
        psw=escape(request.form['passwordTxt']).strip()
        newpsw=escape(request.form['newpasswordTxt']).strip()
        newpsw2=escape(request.form['newpasswordTxt2']).strip()
        q=f"Select clave from usuarios where email='{mail}'"
        pwd= gestorDB.seleccionar(q,"")
        q=trash(pwd).strip()
        error=""
        if check_password_hash(q,psw):
            if newpsw==newpsw2:
                p=generate_password_hash(newpsw)
                q=f"update usuarios SET clave='{p}' WHERE email='{mail}'"
                a=gestorDB.ejecutar(q,"")
                if a>0:
                    error="Cambiada con exito"
                else:
                    error="no se k pdo"
            else:
                error="Asegurese de que la nueva contraseña esta igual en ambos campos"
        else:
            error="La contraseña actual es incorrecta"
        return render_template("cambiarContrasena.html",error=error)


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
        td= escape(frm.tdocumentoCmb.data)
        ni= escape(frm.numerodocTxt.data)
        name=escape(frm.nombresTxt.data)
        lastname=escape(frm.apellidosTxt.data)
        fn=escape(frm.fechaNacCmb.data)
        dirc=escape(frm.direccionTxt.data)
        tel= escape(frm.telefonoTxt.data)
        email= escape(frm.emailTxt.data)
        rol= escape(frm.rolCmb.data)
        psw= generate_password_hash(escape(frm.pswtxt.data))
        q=f"INSERT INTO usuarios (tipodoc, numdoc, nombres,apellidos,fnacimiento,direccion,telefono,email,clave,rol) VALUES ('{td}', '{ni}', '{name}', '{lastname}','{fn}','{dirc}','{tel}','{email}','{psw}','{rol}');"
        a=gestorDB.ejecutar(q,"")
        if a>0:
            error="Operacion exitosa"
        else:
            error= "Error en la operacion"
        return render_template("crearUsuario.html",form=frm,error=error)

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

