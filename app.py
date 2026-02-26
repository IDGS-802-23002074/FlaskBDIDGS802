from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
import forms
from models import db, Alumno
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db.init_app(app)

migrate = Migrate(app, db) 

csrf = CSRFProtect(app)


@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def index():
    create_form = forms.UserForm(request.form)

    if request.method == 'POST' and create_form.validate():
        alumno = Alumno(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            email=create_form.email.data,
            telefono=create_form.telefono.data
        )
        db.session.add(alumno)
        db.session.commit()
        flash("Alumno agregado correctamente")
        return redirect(url_for('index'))

    alumnos = Alumno.query.all()
    return render_template("index.html", form=create_form, alumnos=alumnos)


@app.route("/eliminar/<int:id>", methods=["GET", "POST"])
def eliminar(id):
    alumno = Alumno.query.get_or_404(id)

    if request.method == "POST":
        db.session.delete(alumno)
        db.session.commit()
        return redirect(url_for("index"))

    return render_template("eliminar.html", alumno=alumno)


@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template("404.html"), 404

@app.route("/alumnos", methods=['GET', 'POST'])
def alumnos():
    form = forms.UserForm(request.form)

    if request.method == 'POST' and form.validate():
        nuevo = Alumno(
            nombre=form.nombre.data,
            apellidos=form.apellidos.data,
            email=form.email.data,
            telefono=form.telefono.data
        )
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template("alumnos.html", form=form)

@app.route("/detalles/<int:id>")
def detalles(id):
    alumno = Alumno.query.get_or_404(id)
    return render_template("detalles.html", alumno=alumno)

@app.route("/editar/<int:id>", methods=['GET', 'POST'])
def editar(id):
    alumno = Alumno.query.get_or_404(id)
    form = forms.UserForm(obj=alumno)

    if form.validate_on_submit():
        alumno.nombre = form.nombre.data
        alumno.apellidos = form.apellidos.data
        alumno.email = form.email.data
        alumno.telefono = form.telefono.data

        db.session.commit()
        return redirect(url_for('index'))

    return render_template("editar.html", form=form)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)