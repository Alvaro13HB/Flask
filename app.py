from flask import Flask, render_template, request, flash
app = Flask(__name__)
from database import db
from flask_migrate import Migrate
from models import Produto
app.config['SECRET_KEY'] = 'e26fad767fe56ff62e15baf85254dfe7ec73fdaa17a827e12f227746e7cd81f5'

conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/bd_produtos"
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
    pass


@app.route('/form')
def form():
    return render_template('formulario.html')


@app.route('/dados', methods=['POST'])
def dados():
    flash('Dados enviados!')
    dados = request.form
    return render_template('dados.html', dados=dados)


if __name__ == '__main__':
    app.run()