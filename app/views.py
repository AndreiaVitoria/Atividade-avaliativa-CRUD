from app import app
from flask import render_template, request, redirect, url_for

from app.repository.diretor_repository import DiretorRepository
from app.models.diretor_model import DiretorModel

diretor_service = DiretorRepository()


@app.route('/')
def home():
    return render_template('base.html')

@app.route('/diretores')
def index_diretores():
    data = diretor_service.get_all_diretores()
    return render_template('diretor/list.html', diretores=data)

@app.route('/diretores/novo', methods=['GET', 'POST'])
def create_diretor():
    if request.method == 'POST':
        nome = request.form['nome']
        nacionalidade = request.form['nacionalidade']
        diretor = DiretorModel(id=None, nome=nome, nacionalidade=nacionalidade)
        try:
            diretor_service.create_diretor(diretor)
        except ValueError as e:
            return render_template('diretor/form.html', error=str(e))
        return redirect(url_for('index_diretores'))
    return render_template('diretor/form.html')

@app.route('/diretores/editar/<int:pk>', methods=['GET', 'POST'])
def edit_diretor(pk):
    if request.method == 'POST':
        nome = request.form['nome']
        nacionalidade = request.form['nacionalidade']
        diretor = DiretorModel(id=pk, nome=nome, nacionalidade=nacionalidade)
        try:
            diretor_service.update_diretor(diretor)
        except ValueError as e:
            return render_template('diretor/form.html', diretor=diretor, error=str(e))
        return redirect(url_for('index_diretores'))
    diretor = diretor_service.get_diretor_by_id(pk)
    return render_template('diretor/form.html', diretor=diretor)

@app.route('/diretores/excluir/<int:pk>')
def delete_diretor(pk):
    diretor_service.delete_diretor(pk)
    return redirect(url_for('index_diretores'))