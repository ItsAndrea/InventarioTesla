from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SubmitField, RadioField, TextAreaField, SelectField, DateField, SelectMultipleField, widgets
from wtforms.validators import InputRequired, Length

from wtforms.fields.html5 import SearchField, TelField, EmailField


class Login(FlaskForm):
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

#
#               PRODUCTOS
# 

class FcalificarProducto(FlaskForm):
    eanTxt = TextField('EAN',validators=[InputRequired(message='Se requiere el EAN'), Length(min=7, max=10, message='Longitud debe estar entre 7 y 10')])
    nombreTxt = TextField('Nombre',validators=[InputRequired(message='Se requiere el Nombre')])
    puntajeRbt  =  RadioField('Puntaje' , choices = [( 1 , '1' ), ( 2 , '2' ), ( 3 , '3' ), ( 4 , '4' ), ( 5 , '5' )] , coerce = int )
    comentarioTxt = TextAreaField('Comentario', validators=[InputRequired(message='Se requiere un comentario')])
    agregarBtn = SubmitField('Agregar')
    cancelarBtn = SubmitField('Cancelar')

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()    


class FAsociar(FlaskForm):
    eanSxt = SearchField('EAN',validators=[InputRequired(message='Se requiere el EAN'), Length(min=7, max=10, message='Longitud debe estar entre 7 y 10')])
    nombreTxt = TextField('Nombre',validators=[InputRequired(message='Se requiere el Nombre')])
    nitSxt = SearchField('Nit',validators=[InputRequired(message='Se requiere el Nit'), Length(min=7, max=10, message='Longitud debe estar entre 7 y 10')])
    rSocialTxt = TextField('Razón Social',validators=[InputRequired(message='Se requiere la Razón Social')])
    opcionChk = MultiCheckboxField('Habilitar', choices=[( 1 , '' )])
    consultarBtn = SubmitField('Consultar')
    agregarBtn = SubmitField('Agregar')
    borrarBtn = SubmitField('Borrar')
    editarBtn = SubmitField('Editar')
    cancelarBtn = SubmitField('Cancelar')
   
    """ example = MultiCheckboxField('Label', choices=files) """

#
#               USUARIOS
# 

class FUsuario(FlaskForm):
    tdocumentoCmb = SelectField(u'Tipo de Documento', choices=[('CD', 'Carnet Diplomatico'), ('CC', 'Cédula de Ciudadanía'), ('CE', 'Cédula de Extranjería'), ('PA', 'Pasaporte'), ('PEP', 'Permiso Especial de Permanencia'), ('SP', 'Salvoconducto de Permanencia')], default="CC")
    numerodocTxt = TextField('Número Documento de Identificación',validators=[InputRequired(message='Se requiere el Número del documento de identidad'), Length(min=7, max=20, message='Longitud debe estar entre 7 y 20')])
    nombresTxt = TextField('Nombres',validators=[InputRequired(message='Se requiere los Nombres')])
    apellidosTxt = TextField('Apellidos',validators=[InputRequired(message='Se requiere los Apellidos')])
    fechaNacCmb = DateField('Fecha de Nacimiento',validators=[InputRequired(message='Se requiere la Fecha de Nacimiento')], format='%Y-%m-%d')
    direccionTxt = TextField('Dirección',validators=[InputRequired(message='Se requiere la Dirección')])
    telefonoTxt = TelField('Teléfono',validators=[InputRequired(message='Se requiere el Teléfono')])
    emailTxt = EmailField('E-mail',validators=[InputRequired(message='Se requiere el E-mail')])
    rolCmb = SelectField(u'Rol', choices=[('Admin', 'Administrador'), ('Super', 'Super-Administrador'), ('UserF', 'Usuario Final')], default="UserF")
    agregarBtn = SubmitField('Agregar')
    borrarBtn = SubmitField('Borrar')
    editarBtn = SubmitField('Editar')
    cancelarBtn = SubmitField('Cancelar')
