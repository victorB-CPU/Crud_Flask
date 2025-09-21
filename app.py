from flask import Flask, render_template, request, redirect, url_for

app = Flask('CadastroVb')

# Lista de usuários (id, nome, email, idade)
users = [
    [1, "João", "joao@email.com", 25],
    [2, "Maria", "maria@email.com", 30]
]

# Função para gerar o próximo ID
def get_next_id():
    if users:
        return users[-1][0] + 1
    return 1

# Rota principal (index)
@app.route('/')
def index():
    return render_template('index.html', users=users)

# Rota para criar usuário
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        users.append([get_next_id(), name, email, age])
        return redirect(url_for('index'))
    return render_template('create.html')

# Rota para editar usuário
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    user = next((u for u in users if u[0] == id), None)
    if not user:
        return "Usuário não encontrado"
    if request.method == 'POST':
        user[1] = request.form['name']
        user[2] = request.form['email']
        user[3] = request.form['age']
        return redirect(url_for('index'))
    return render_template('edit.html', user=user)

# Rota para deletar usuário
@app.route('/delete/<int:id>')
def delete(id):
    global users
    users = [u for u in users if u[0] != id]
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
