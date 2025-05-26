from flask import Flask, request, render_template, redirect, url_for
from models import Usuario
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
db.init_app(app)

@im.user_loader
def user_loader(id):

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'GET':
        return render_template('registrar.html')
    elif request.method == 'POST':
        nome = request.form['nomeform']
        senha = request.form['senhaform']

        novo_usuario = Usuario(nome=nome, senha=senha)
        db.session.add(novo_usuario)
        db.session.commit()  # <-- Parênteses estavam faltando

        return redirect(url_for('registrar'))  # Redireciona após cadastro (evita reenvio do form)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
