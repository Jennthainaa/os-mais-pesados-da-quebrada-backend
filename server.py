from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configurações do banco de dados
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'petauau123*'
app.config['MYSQL_DB'] = 'Littlest__PetShop'

mysql = MySQL(app)

# Rota da Home
@app.route('/')
def home():
    return render_template('index.html')

# Rota de Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['nome']
        password = request.form['senha']
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM usuario WHERE nome = %s AND senha = %s", (nome, senha))
        user = cursor.fetchone()
        cursor.close()
        if user:
            return redirect(url_for('index'))
        else:
            return "Usuário ou senha inválidos!"
    return render_template('login.html')

# Rota de Cadastro de Usuário
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)", (nome, email, senha))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('list_users'))
    return render_template('cadastro.html')

# Rota de Cadastro do pet
@app.route('/pet', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        tipo = request.form['tipo']
        raca = request.form['raca']
        idade = request.form['idade']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO pet (nome, tipo, raca, idade) VALUES (%s, %s, %s)", (nome, tipo, raca, idade))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('list_users'))
    return render_template('pet.html')



# Rota para Listagem de Usuários
@app.route('/usuarios')
def list_users():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    cursor.close()
    return render_template('users.html', usuarios=usuario)

# Rota para Atualizar Usuário
@app.route('/update_user/<int:id>', methods=['GET', 'POST'])
def update_user(id):
    cursor = mysql.connection.cursor()
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        cursor.execute("UPDATE usuarios SET nome=%s, email=%s WHERE id=%s", (nome, email, id))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('list_users'))
    cursor.execute("SELECT * FROM usuarios WHERE id = %s", [id])
    user = cursor.fetchone()
    cursor.close()
    return render_template('update_user.html', user=user)

# Rota para Excluir Usuário
@app.route('/delete_user/<int:id>')
def delete_user(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = %s", [id])
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for('list_users'))

if __name__ == '__main__':
    app.run(debug=True)
