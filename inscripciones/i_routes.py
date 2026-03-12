from flask import render_template, redirect, url_for, request, flash
from . import inscripciones_bp
from models import db, Inscripcion, Alumno, Curso


@inscripciones_bp.route("/inscripciones")
def index():

    inscripciones = Inscripcion.query.all()
    alumnos = Alumno.query.all()
    cursos = Curso.query.all()

    return render_template(
        "inscripciones.html",
        inscripciones=inscripciones,
        alumnos=alumnos,
        cursos=cursos
    )


@inscripciones_bp.route("/inscripciones/agregar", methods=["GET","POST"])
def agregar():

    alumnos = Alumno.query.all()
    cursos = Curso.query.all()

    if request.method == "POST":

        alumno_id = request.form.get("alumno_id")
        curso_id = request.form.get("curso_id")

        alumno = Alumno.query.get(alumno_id)
        curso = Curso.query.get(curso_id)

        if alumno not in curso.alumnos:

            curso.alumnos.append(alumno)

            db.session.commit()


        return redirect(url_for("inscripciones.index"))

    return render_template(
        "inscripciones_agregar.html",
        alumnos=alumnos,
        cursos=cursos
    )

@inscripciones_bp.route("/inscripciones/eliminar", methods=["POST"])
def eliminar():

    alumno_id = request.form.get("alumno_id")
    curso_id = request.form.get("curso_id")

    alumno = Alumno.query.get(alumno_id)
    curso = Curso.query.get(curso_id)

    curso.alumnos.remove(alumno)

    db.session.commit()


    return redirect(url_for("inscripciones.index"))