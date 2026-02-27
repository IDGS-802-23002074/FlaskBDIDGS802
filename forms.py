from flask_wtf import FlaskForm
from wtforms import StringField, EmailField
from wtforms import validators

class UserForm(FlaskForm):

    nombre = StringField('Nombre', [
        validators.DataRequired(message="El campo nombre es requerido"),
        validators.Length(min=3, max=50, message="Debe tener entre 3 y 50 caracteres")
    ])

    apellidos = StringField('Apellidos', [
        validators.DataRequired(message="El apellido es requerido"),
        validators.Length(max=50, message="Máximo 50 caracteres")
    ])

    email = EmailField('Correo', [
        validators.DataRequired(message="El correo es requerido"),
        validators.Email(message="Ingrese un correo válido"),
        validators.Length(max=50, message="Máximo 50 caracteres")
    ])

    telefono = StringField('Telefono', [
        validators.DataRequired(message="El telefono es requerido"),
        validators.Length(max=10, message="Máximo 10 caracteres")
    ])

class UserForm2(FlaskForm):

    nombre = StringField('Nombre', [
        validators.DataRequired(message="El campo nombre es requerido"),
        validators.Length(min=3, max=50, message="Debe tener entre 3 y 50 caracteres")
    ])

    apellidos = StringField('Apellidos', [
        validators.DataRequired(message="El apellido es requerido"),
        validators.Length(max=50, message="Máximo 50 caracteres")
    ])

    especialidad = StringField('Especialidad', [
        validators.DataRequired(message="La especialidad es requerida"),
        validators.Length(max=50, message="Máximo 50 caracteres")
    ])

    email = EmailField('Correo', [
        validators.DataRequired(message="El correo es requerido"),
        validators.Email(message="Ingrese un correo válido"),
        validators.Length(max=50, message="Máximo 50 caracteres")
    ])
