from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def perfil():
    # Estructuras de datos de Python: variables, diccionario y listas
    nombre = "Rodolfo"

    apellidos = {
        "primer_apellido": "Tapia",
        "segundo_apellido": "Garcia",
    }

    asignaturas = [
        "Machine Learning",
        "Big Data",
        "Proyecto Integrador de Sistemas Ciberfísicos",
    ]

    hobbies = [
        "Trading algorítmico",
        "Programación",
        "Videojuegos",
    ]

    # La información se envía desde Flask al template mediante variables
    return render_template(
        "index.html",
        nombre=nombre,
        apellidos=apellidos,
        asignaturas=asignaturas,
        hobbies=hobbies,
    )


if __name__ == "__main__":
    app.run(debug=True)
