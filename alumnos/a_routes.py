from flask import render_template, request, redirect, url_for, flash
from . import alumnos_bp
from models import db, Alumno
import forms


@alumnos_bp.route("/alumnos", methods=["GET","POST"])
def index():

    form = forms.UserForm(request.form)

    if request.method == "POST" and form.validate():

        nuevo = Alumno(
            nombre=form.nombre.data,
            apellidos=form.apellidos.data,
            email=form.email.data,
            telefono=form.telefono.data
        )

        db.session.add(nuevo)
        db.session.commit()

        
        return redirect(url_for("alumnos.index"))

    alumnos = Alumno.query.all()

    return render_template(
        "alumnos.html",
        form=form,
        alumnos=alumnos
    )

@alumnos_bp.route("/alumnos/agregar", methods=["GET","POST"])
def agregar():

    form = forms.UserForm(request.form)

    if request.method == "POST" and form.validate():

        nuevo = Alumno(
            nombre=form.nombre.data,
            apellidos=form.apellidos.data,
            email=form.email.data,
            telefono=form.telefono.data
        )

        db.session.add(nuevo)
        db.session.commit()

        

        return redirect(url_for("alumnos.index"))

    return render_template(
        "agregar.html",
        form=form
    )

@alumnos_bp.route("/alumnos/detalles/<int:id>")
def detalles(id):

    alumno = Alumno.query.get_or_404(id)

    return render_template(
        "detalles.html",
        alumno=alumno
    )


@alumnos_bp.route("/alumnos/editar/<int:id>", methods=["GET","POST"])
def editar(id):

    alumno = Alumno.query.get_or_404(id)
    form = forms.UserForm(obj=alumno)

    if form.validate_on_submit():

        alumno.nombre = form.nombre.data
        alumno.apellidos = form.apellidos.data
        alumno.email = form.email.data
        alumno.telefono = form.telefono.data

        db.session.commit()

        return redirect(url_for("alumnos.index"))

    return render_template(
        "editar.html",
        form=form
    )


@alumnos_bp.route("/alumnos/eliminar/<int:id>", methods=["GET","POST"])
def eliminar(id):

    alumno = Alumno.query.get_or_404(id)
    form = forms.UserForm()

    if request.method == "POST":

        db.session.delete(alumno)
        db.session.commit()


        return redirect(url_for("alumnos.index"))

    return render_template(
        "eliminar.html",
        alumno=alumno,
        form=form
    )