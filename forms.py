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

class FProveedor(FlaskForm):
    nitTxt = TextField('Nit',validators=[InputRequired(message='Se requiere el Nit'), Length(min=7, max=10, message='Longitud debe estar entre 7 y 10')])
    rSocialTxt = TextField('Razón Social',validators=[InputRequired(message='Se requiere la Razón Social')])
    direccionTxt = TextField('Dirección',validators=[InputRequired(message='Se requiere la Dirección')])
    telefonoTxt = TelField('Teléfono',validators=[InputRequired(message='Se requiere el Teléfono')])
    emailTxt = EmailField('E-mail',validators=[InputRequired(message='Se requiere el E-mail')])
    agregarBtn = SubmitField('Agregar')
    borrarBtn = SubmitField('Borrar')
    cancelarBtn = SubmitField('Cancelar')
    actualizarBtn = SubmitField('Actualizar')
    editarBtn = SubmitField('Editar')


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
    
class FProducto(FlaskForm):
    eanTxt = TextField('EAN',validators=[InputRequired(message='Se requiere el EAN'), Length(min=7,max=10,message='Longitud debe estar entre 7 y 10')])
    nombreTxt = TextField('Nombre',validators=[InputRequired(message='Se requiere el Nombre')])
    marcaTxt = TextField('Marca',validators=[InputRequired(message='Se requiere la Marca')])
    modeloTxt = TextField('Marca',validators=[InputRequired(message='Se requiere el Modelo')])
    anoTxt = DateField('Año',validators=[InputRequired(message='Se requiere el año')], format='%Y')
    asientosTxt = TextField('Asientos',validators=[InputRequired(message='Se requiere asientos')])
    pesoTxt = TextField('Peso',validators=[InputRequired(message='Se requiere el peso')])
    vmTxt = TextField('Velocidad Máxima',validators=[InputRequired(message='Se requiere la velocidad máxima')])
    modeloTxt = TextField('Modelo',validators=[InputRequired(message='Se requiere el modelo')])
    colorTxt = TextField('Color',validators=[InputRequired(message='Se requiere el color')])
    rinesTxt = TextField('Rines',validators=[InputRequired(message='Se requieren los rines')])
    spTxt = TextField('Sis. de Propulsión',validators=[InputRequired(message='Se requiere el sis. de propulsión')])
    smTxt = TextField('Stock Mínimo',validators=[InputRequired(message='Se requiere el stock mínimo')])
    nitPTxt = TextField('Nit',validators=[InputRequired(message='Se requiere el nit Proveedor')])
    rsTxt = TextField('Razón Social',validators=[InputRequired(message='Se requiere la razón social')])
    desTxt = TextAreaField('Descripción',validators=[InputRequired(message='Se requiere descripción')])
    agregarBtn = SubmitField('Agregar')
    borrarBtn = SubmitField('Borrar')
    editarBtn = SubmitField('Editar')
    cancelarBtn = SubmitField('Cancelar')
    actualizarBtn = SubmitField('Actualizar')


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
    rolCmbSuper = SelectField(u'Rol', choices=[('Admin', 'Administrador'), ('Super', 'Super-Administrador'), ('UserF', 'Usuario Final')], default="UserF")
    agregarBtn = SubmitField('Agregar')
    borrarBtn = SubmitField('Borrar')
    editarBtn = SubmitField('Editar')
    cancelarBtn = SubmitField('Cancelar')
    pswtxt= PasswordField('Contraseña',validators=[InputRequired(message='Se requiere una contraseña valida'), Length(min=6, message='Longitud debe ser mayor a 6 caracteres')])

