from flask import Flask, render_template, request, flash, redirect
app = Flask(__name__)
from database import db
from flask_migrate import Migrate
from models import Produto
app.config['SECRET_KEY'] = 'e26fad767fe56ff62e15baf85254dfe7ec73fdaa17a827e12f227746e7cd81f5'

conexao = "mysql+pymysql://alvaros@localhost:1406@127.0.0.1/bd_produtos"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/produto')
def produto():
    p = Produto.query.all()
    return render_template("lista_produtos.html", dados=p)


@app.route('/produto/add')
def produto_add():
    return render_template("produto_add.html")


@app.route('/produto/save', methods=['POST'])
def produto_save():
    nome = request.form.get('nome')
    preco = request.form.get('preco')
    qtd = request.form.get('quantidade_estoque')
    if nome and preco and qtd:
        produto = Produto(nome, preco, qtd)
        db.session.add(produto)
        db.session.commit()
        flash("Usuário cadastrado com sucesso!!!")
        return redirect('/produto')
    else:
        flash("Preencha todos os campos!!!")
        return redirect('/produto/add')
    

@app.route('/produto/remove/<int:id>')
def produto_remove(id):
    produto = Produto.query.get(id)
    try:
        db.session.delete(produto)
        db.session.commit()
        flash("Usuário removido com sucesso!!!")
        return redirect('/produto')
    except:
        flash("Usuário Inválido")
        return redirect('/produto')
    

@app.route('/produto/edit/<int:id>')
def produto_edit(id):
    p = Produto.query.get(id)
    return render_template("produto_edit.html", dados=p)


@app.route('/produto/edit-save', methods=['POST'])
def produto_edit_save():
    nome = request.form.get('nome')
    preco = request.form.get('preco')
    qtd = request.form.get('quantidade_estoque')
    id = request.form.get('id')
    if nome and preco and qtd and id:
        produto = Produto.query.get(id)
        produto.nome = nome
        produto.preco = preco
        produto.quantidade_estoque = qtd
        db.session.commit()
        flash("Dados alterados com sucesso!!!")
        return redirect('/produto')
    else:
        flash("Preencha todos os campos!!!")
        return redirect('/produto')



if __name__ == '__main__':
    app.run()