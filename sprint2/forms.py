from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SubmitField, RadioField 
from wtforms.validators import InputRequired, Length

from wtforms.fields.html5 import TelField, EmailField

class Login(FlaskForm):
    usr = TextField('',validators=[InputRequired(message='Se requiere el usuario'), Length(min=6, max=40, message='Longitud debe estar entre 6 y 40')])
    pwd = PasswordField('',validators=[InputRequired(message='Se requiere la clave')])
    btn = SubmitField('login')
    check= RadioField('Recordar contraseña')

class Cambiarcontraseña(FlaskForm):
    usr = TextField('',validators=[InputRequired(message='Se requiere el usuario'), Length(min=6, max=40, message='Longitud debe estar entre 6 y 40')])
    pwd = PasswordField('',validators=[InputRequired(message='Se requiere la clave')])
    btn = SubmitField('login')
    check= RadioField('Recordar contraseña')

#
#               PROVEEDORES
# 

class FcrearProveedor(FlaskForm):
    nitTxt = TextField('Nit',validators=[InputRequired(message='Se requiere el Nit'), Length(min=7, max=10, message='Longitud debe estar entre 7 y 10')])
    rSocialTxt = TextField('Razón Social',validators=[InputRequired(message='Se requiere la Razón Social')])
    direccionTxt = TextField('Dirección',validators=[InputRequired(message='Se requiere la Dirección')])
    telefonoTxt = TelField('Teléfono',validators=[InputRequired(message='Se requiere el Teléfono')])
    emailTxt = EmailField('E-mail',validators=[InputRequired(message='Se requiere el E-mail')])
    agregarBtn = SubmitField('Agregar')
    borrarBtn = SubmitField('Borrar')
    cancelarBtn = SubmitField('Cancelar')

class FeditarProveedor(FlaskForm):
    nitTxt = TextField('Nit',validators=[InputRequired(message='Se requiere el Nit'), Length(min=7, max=10, message='Longitud debe estar entre 7 y 10')])
    rSocialTxt = TextField('Razón Social',validators=[InputRequired(message='Se requiere la Razón Social')])
    direccionTxt = TextField('Dirección',validators=[InputRequired(message='Se requiere la Dirección')])
    telefonoTxt = TelField('Teléfono',validators=[InputRequired(message='Se requiere el Teléfono')])
    emailTxt = EmailField('E-mail',validators=[InputRequired(message='Se requiere el E-mail')])
    actualizarBtn = SubmitField('Actualizar')
    borrarBtn = SubmitField('Borrar')
    cancelarBtn = SubmitField('Cancelar')

class FvisualizarProveedor(FlaskForm):
    nitTxt = TextField('Nit',validators=[InputRequired(message='Se requiere el Nit'), Length(min=7, max=10, message='Longitud debe estar entre 7 y 10')])
    rSocialTxt = TextField('Razón Social',validators=[InputRequired(message='Se requiere la Razón Social')])
    direccionTxt = TextField('Dirección',validators=[InputRequired(message='Se requiere la Dirección')])
    telefonoTxt = TelField('Teléfono',validators=[InputRequired(message='Se requiere el Teléfono')])
    emailTxt = EmailField('E-mail',validators=[InputRequired(message='Se requiere el E-mail')])
    editarBtn = SubmitField('Editar')
    cancelarBtn = SubmitField('Cancelar')

class FgestionarProveedores(FlaskForm):
    nitTxt = TextField('Nit',validators=[InputRequired(message='Se requiere el Nit'), Length(min=7, max=10, message='Longitud debe estar entre 7 y 10')])
    rSocialTxt = TextField('Razón Social',validators=[InputRequired(message='Se requiere la Razón Social')])
    direccionTxt = TextField('Dirección',validators=[InputRequired(message='Se requiere la Dirección')])
    telefonoTxt = TelField('Teléfono',validators=[InputRequired(message='Se requiere el Teléfono')])
    emailTxt = EmailField('E-mail',validators=[InputRequired(message='Se requiere el E-mail')])
    editarBtn = SubmitField('Editar')
    cancelarBtn = SubmitField('Cancelar')