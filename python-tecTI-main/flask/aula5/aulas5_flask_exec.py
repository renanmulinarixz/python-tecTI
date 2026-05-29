from flask import Flask, request, render_template, redirect, url_for, session
from users import usuarios

app = Flask(__name__)
app.secret_key = 'chave_secreta'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')

        for user in usuarios:
            if user['nome'] == usuario and user['senha'] == senha:
                session['usuario'] = usuario
                return redirect(url_for('home'))

        return render_template('login.html', erro='Usuário ou senha inválidos.')

    return render_template('login.html', erro=None)

@app.route('/home')
def home():
    return render_template('home.html', usuario=session.get('usuario'))

if __name__ == "__main__":
    app.run(debug=True)