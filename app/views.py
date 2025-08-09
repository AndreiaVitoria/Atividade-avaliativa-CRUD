from app import app
from flask import render_template, request, redirect, url_for

from app.models.diretor_model import DiretorModel
from app.service.diretor_service import DiretorService
from app.service.filme_service import FilmeService
from app.models.filme_model import FilmeModel

diretor_service = DiretorService()
filme_service = FilmeService()

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
        diretor_service.create_diretor(DiretorModel(None, nome, nacionalidade))
        return redirect(url_for('index_diretores'))
    return render_template('diretor/form.html')

@app.route('/diretores/editar/<int:pk>', methods=['GET', 'POST'])
def update_diretor(pk):
    diretor = diretor_service.get_diretor_by_id(pk)
    if request.method == 'POST':
        diretor_service.update_diretor(DiretorModel(pk, nome=request.form['nome'], nacionalidade=request.form['nacionalidade']))
        return redirect(url_for('index_diretores'))
    return render_template('diretor/form.html', diretor=diretor)

@app.route('/diretores/excluir/<int:pk>')
def delete_diretor(pk):
    diretor_service.delete_diretor(pk)
    return redirect(url_for('index_diretores'))



@app.route('/filmes')
def index_filmes():
    data = filme_service.get_all_filmes()
    return render_template('filme/list.html', filmes=data)

@app.route('/filmes/novo', methods=['GET', 'POST'])
def create_filme():
    if request.method == 'POST':
        titulo = request.form['titulo']
        genero = request.form['genero']
        ano = request.form.get('ano')
        try:
            ano = int(ano)
        except (TypeError, ValueError):
            ano = None
        diretor_id = int(request.form['diretor_id'])
        filme = FilmeModel(id=None, titulo=titulo, genero=genero, ano=ano, diretor_id=diretor_id)
        filme_service.create_filme(filme)
        return redirect(url_for('index_filmes'))
    return render_template('filme/form.html', diretores=diretor_service.get_all_diretores())


@app.route('/filmes/editar/<int:pk>', methods=['GET', 'POST'])
def update_filme(pk):
    filme = filme_service.get_filme_by_id(pk)
    if request.method == 'POST':
        titulo = request.form['titulo']
        genero = request.form['genero']
        ano = request.form.get('ano', type=int)
        diretor_id = int(request.form['diretor_id'])
        filme_updated = FilmeModel(id=pk, titulo=titulo, genero=genero, ano=ano, diretor_id=diretor_id)
        filme_service.update_filme(filme_updated)
        return redirect(url_for('index_filmes'))
    return render_template('filme/form.html', filme=filme, diretores=diretor_service.get_all_diretores())


@app.route('/filmes/excluir/<int:pk>')
def delete_filme(pk):
    filme_service.delete_filme(pk)
    return redirect(url_for('index_filmes'))
