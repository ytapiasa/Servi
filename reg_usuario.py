from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        id = request.form.get('id')
        email = request.form.get('email')
        password = request.form.get('password')
        # Aquí puedes agregar el código para manejar estos datos, como guardarlos en una base de datos.
        return '¡Registro exitoso!'
    return render_template('register.html')  # Asegúrate de tener un archivo 'register.html' en la carpeta de plantillas.

if __name__ == '__main__':
    app.run(debug=True)
