import os
import sqlite3
from flask import Flask, request, redirect, url_for, render_template, send_from_directory, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'  # Troque por uma chave secreta real
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Configuração do Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Conexão com o banco de dados
def connect_db():
    conn = sqlite3.connect('veiculos.db')
    conn.row_factory = sqlite3.Row
    return conn

# Classe para representar usuários
class User(UserMixin):
    pass

# Carregar usuário
@login_manager.user_loader
def load_user(email):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
    user_data = cursor.fetchone()
    conn.close()
    if user_data:
        user = User()
        user.email = user_data['email']
        return user
    return None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        modelo = request.form['modelo']
        preco = request.form['preco']
        
        # Upload da imagem
        imagem = None
        if 'imagem' in request.files:
            file = request.files['imagem']
            if file.filename:
                imagem = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(imagem)

        # Insere o veículo no banco de dados
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO veiculos (modelo, preco, imagem) VALUES (?, ?, ?)", (modelo, preco, imagem))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

    # Consulta os veículos no banco de dados para exibir na página
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM veiculos")
    veiculos = cursor.fetchall()
    conn.close()

    return render_template("index.html", veiculos=veiculos)

# Rota para remover um veículo
@app.route('/remover/<int:veiculo_id>', methods=['POST'])
@login_required
def remover(veiculo_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM veiculos WHERE id = ?", (veiculo_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# Rota para login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
        usuario = cursor.fetchone()
        conn.close()
        
        if usuario and check_password_hash(usuario['senha'], senha):
            user = User()
            user.email = email
            login_user(user)
            return redirect(url_for('index'))
        else:
            error = "E-mail ou senha incorretos."
            return render_template('login.html', error=error)
    
    return render_template('login.html')

# Rota para registro
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        
        conn = connect_db()
        cursor = conn.cursor()
        # Verifica se o e-mail já existe
        cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
        if cursor.fetchone():
            return render_template('register.html', error="Esse e-mail já está registrado.")
        
        # Armazenar o usuário no banco de dados
        cursor.execute("INSERT INTO usuarios (email, senha) VALUES (?, ?)", (email, generate_password_hash(senha)))
        conn.commit()
        conn.close()
        
        flash("Registro bem-sucedido! Você pode fazer login agora.")
        return redirect(url_for('login'))

    return render_template('register.html')

# Rota para logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# Serve imagens da pasta de uploads
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Página de acesso não autorizado
@app.route('/unauthorized')
def unauthorized():
    return render_template('unauthorized.html'), 401

if __name__ == "__main__":
    app.run(debug=True)
