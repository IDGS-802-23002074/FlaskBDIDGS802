from flask import Blueprint
cursos_bp=Blueprint('cursos',__name__)
from flask import render_template, redirect, url_for, request
from . import cursos_bp
from models import Curso, Maestro
from models import db
import forms

@cursos_bp.route("/cursos")
def index():

    cursos = Curso.query.all()

    return render_template(
        "cursos.html",
        cursos=cursos
    )


@cursos_bp.route("/cursos/agregar", methods=["GET","POST"])
def agregar():

    form = forms.UserForm3()

    maestros = Maestro.query.all()
    form.maestro_id.choices = [(m.matricula, m.nombre + " " + m.apellidos) for m in maestros]

    if form.validate_on_submit():

        curso = Curso(
            nombre=form.nombre.data,
            descripcion=form.descripcion.data,
            maestro_id=form.maestro_id.data
        )

        db.session.add(curso)
        db.session.commit()

        return redirect(url_for("cursos.index"))

    return render_template(
        "cursos_agregar.html",
        form=form
    )

@cursos_bp.route("/cursos/detalles/<int:id>")
def detalles(id):

    curso = Curso.query.get_or_404(id)

    return render_template(
        "cursos_detalles.html",
        curso=curso
    )

@cursos_bp.route("/cursos/editar/<int:id>", methods=["GET","POST"])
def editar(id):

    curso = Curso.query.get_or_404(id)

    form = forms.UserForm3(obj=curso)

    maestros = Maestro.query.all()
    form.maestro_id.choices = [
        (m.matricula, f"{m.nombre} {m.apellidos}") for m in maestros
    ]

    if form.validate_on_submit():

        curso.nombre = form.nombre.data
        curso.descripcion = form.descripcion.data
        curso.maestro_id = form.maestro_id.data

        db.session.commit()


        return redirect(url_for("cursos.index"))

    return render_template(
        "cursos_editar.html",
        form=form,
        curso=curso
    )

@cursos_bp.route("/cursos/eliminar/<int:id>", methods=["GET","POST"])
def eliminar(id):

    curso = Curso.query.get_or_404(id)

    form = forms.DeleteForm()

    if form.validate_on_submit():

        db.session.delete(curso)
        db.session.commit()

        return redirect(url_for("cursos.index"))

    return render_template(
        "cursos_eliminar.html",
        curso=curso,
        form=form
    )