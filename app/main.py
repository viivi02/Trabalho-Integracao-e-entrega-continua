from flask import Flask, request, render_template, redirect
import mysql.connector
import os

app = Flask(__name__)

db_config = {
    'host': os.environ.get('DB_HOST', 'localhost'),
    'user': 'root',
    'password': 'senha',
    'database': 'meubanco'
}

@app.route('/')
def index():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome FROM pessoas")
    dados = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', pessoas=dados)

@app.route('/add', methods=['POST'])
def add():
    nome = request.form['nome']
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pessoas (nome) VALUES (%s)", (nome,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pessoas WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')

# Rota para mostrar o formulário de edição
@app.route('/edit/<int:id>')
def edit(id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT nome FROM pessoas WHERE id=%s", (id,))
    pessoa = cursor.fetchone()
    cursor.close()
    conn.close()
    if pessoa:
        return render_template('edit.html', id=id, nome=pessoa[0])
    else:
        return redirect('/')

# Rota para salvar a edição
@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    novo_nome = request.form['nome']
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("UPDATE pessoas SET nome=%s WHERE id=%s", (novo_nome, id))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
