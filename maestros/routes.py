from flask import Blueprint
maestros_bp=Blueprint('maestros',__name__)

from flask import render_template, request, redirect, url_for, flash
from . import maestros_bp
from models import db, Maestros
import forms

@maestros_bp.route("/maestros", methods=["GET", "POST"])
def index():
    form = forms.UserForm2(request.form)

    if request.method == "POST" and form.validate():
        nuevo = Maestros(
            nombre=form.nombre.data,
            apellidos=form.apellidos.data,
            especialidad=form.especialidad.data,
            email=form.email.data
        )
        db.session.add(nuevo)
        db.session.commit()
        flash("Maestro agregado correctamente")
        return redirect(url_for("maestros.index"))

    maestros = Maestros.query.all()
    return render_template("maestros.html", form=form, maestros=maestros)

@maestros_bp.route("/maestros/agregar", methods=["GET", "POST"])
def agregar():
    form = forms.UserForm2()

    if form.validate_on_submit():
        nuevo = Maestros(
            nombre=form.nombre.data,
            apellidos=form.apellidos.data,
            especialidad=form.especialidad.data,
            email=form.email.data
        )
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for("maestros.index"))

    return render_template("maestros_agregar.html", form=form)

@maestros_bp.route("/maestros/detalles/<int:matricula>")
def detalles(matricula):
    maestro = Maestros.query.get_or_404(matricula)
    return render_template("maestros_detalles.html", maestro=maestro)

@maestros_bp.route("/maestros/editar/<int:matricula>", methods=["GET", "POST"])
def editar(matricula):
    maestro = Maestros.query.get_or_404(matricula)
    form = forms.UserForm2(obj=maestro)

    if form.validate_on_submit():
        maestro.nombre = form.nombre.data
        maestro.apellidos = form.apellidos.data
        maestro.especialidad = form.especialidad.data
        maestro.email = form.email.data

        db.session.commit()
        return redirect(url_for("maestros.index"))

    return render_template("maestros_editar.html", form=form)

@maestros_bp.route("/maestros/eliminar/<int:matricula>", methods=["GET", "POST"])
def eliminar(matricula):
    maestro = Maestros.query.get_or_404(matricula)

    if request.method == "POST":
        db.session.delete(maestro)
        db.session.commit()
        return redirect(url_for("maestros.index"))

    return render_template("maestros_eliminar.html", maestro=maestro)