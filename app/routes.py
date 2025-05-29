from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import Pessoa

main = Blueprint('main', __name__)

@main.route('/')
def index():
    pessoas = Pessoa.query.all()
    return render_template('index.html', pessoas=pessoas)

@main.route('/add', methods=['POST'])
def add():
    nome = request.form['nome']
    email = request.form['email']
    nova_pessoa = Pessoa(nome=nome, email=email)
    db.session.add(nova_pessoa)
    db.session.commit()
    return redirect(url_for('main.index'))
