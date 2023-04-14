from flask import Flask, render_template, request, redirect, url_for
import os
import database as db
import datetime

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'Proyecto App Moviles', 'secciones')

app = Flask(__name__, template_folder=template_dir)

# Rutas de paginas de la aplicacion
@app.route('/')
def LoginScreen():
    return render_template('Login.html')

@app.route('/Inicio')
def Inicio():
    return render_template('Inicio.html')

@app.route('/Mediciones')
def Mediciones():
    return render_template('Mediciones.html')

@app.route('/Historial')
def Historial():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM registros")
    myresult = cursor.fetchall()

    insertobject=[]
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertobject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('Historial.html', data=insertobject)

#CRUD para iniciar sesión
@app.route("/Login", methods=["GET", "POST"])
def Login():
    if request.method == "POST":
        username = request.form["usuario"]  
        password = request.form["password"]

        cursor = db.database.cursor()
        query = "SELECT username, pwd FROM users WHERE username=%s and pwd=%s"
        values = (username,password)
        cursor.execute(query, values)

        # Verificar si el usuario y la contraseña son correctos
        result = cursor.fetchone()
        try:
            if result[0]==username and result[1]==password:
                return redirect(url_for('Inicio'))             
        except TypeError:
            return "credenciales incorrectas"


#CRUD para registrar un usuario
@app.route("/AddUser", methods=["GET", "POST"])
def AddUser():
    if request.method == "POST":
        usuario = request.form["username"]
        password = request.form["password"]

        cursor = db.database.cursor()
        query = "INSERT INTO users (username, pwd) VALUES (%s, %s)"
        values = (usuario, password)
        cursor.execute(query, values)
        db.database.commit()

        return redirect(url_for("LoginScreen"))
    else:
        return "Nope"

#CRUD para registrar una medicion
@app.route("/AddMedicion", methods=["GET", "POST"])
def AddMedicion():
    if request.method == "POST":
        zona = request.form["zona"]
        fecha = request.form["fecha"]
        hora = request.form["hora"]
        pozo = request.form["pozo"]
        valvula = request.form["valvula"]
        medicion = request.form["medicion"]
        
        cursor = db.database.cursor()
        query = "INSERT INTO registros (zona, fecha, hora, pozo, valvula, medicion) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (zona, fecha, hora, pozo, valvula, medicion)
        cursor.execute(query, values)
        db.database.commit()

        return redirect(url_for('Inicio'))
    else:
        return "Nope"

if __name__ == '__main__':
    app.run(debug=True, port=4000)