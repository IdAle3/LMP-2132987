from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import pymysql
app = Flask(__name__)

app = Flask(__name__, template_folder='src/templates')


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:hola44seis6789@localhost/usuarios_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Usuario(db.Model):
    idnombre = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45), nullable=False)
    apellido = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return f'<Usuario {self.nombre} {self.apellido}>'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']

        nuevo_usuario = Usuario(nombre=nombre, apellido=apellido)
        db.session.add(nuevo_usuario)
        db.session.commit()

        return redirect(url_for('home'))

if __name__ == '__main__':

    with app.app_context():
        db.create_all()
    
    app.run(debug=True, port=4000)
