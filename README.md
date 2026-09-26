# Flask Web App - Perfil

Aplicación web hecha con Flask y Jinja2 que muestra un perfil con nombre,
apellidos, asignaturas y hobbies. La información se envía desde Flask
(`app.py`) al template (`templates/index.html`) mediante variables, y
las listas de asignaturas y hobbies se recorren con un ciclo `for` de
Jinja2.

## Cómo correrlo

```bash
pip install -r requirements.txt
python app.py
```

Luego abre http://127.0.0.1:5000/ en el navegador.
