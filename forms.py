from wtforms import Form, StringField, EmailField
from wtforms import validators

class UserForm(Form):

    nombre = StringField('Nombre', [
        validators.DataRequired(message="El campo nombre es requerido"),
        validators.Length(min=3, max=50, message="Debe tener entre 3 y 50 caracteres")
    ])

    apaterno = StringField('Apellido Paterno', [
        validators.DataRequired(message="El apellido es requerido"),
        validators.Length(max=50, message="Máximo 50 caracteres")
    ])

    email = EmailField('Correo', [
        validators.DataRequired(message="El correo es requerido"),
        validators.Email(message="Ingrese un correo válido"),
        validators.Length(max=50, message="Máximo 50 caracteres")
    ])
