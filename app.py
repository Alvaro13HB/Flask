from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e26fad767fe56ff62e15baf85254dfe7ec73fdaa17a827e12f227746e7cd81f5'

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/perdeste')
@app.route('/perdeste/<nome_REAL>')
@app.route('/perdeste/<nome_REAL>/<nick>')
@app.route('/perdeste/<nome_REAL>/<nick>/<int:gp>')
def aula(nome_REAL = 'Pedro Cougo Mesquita', nick = "lalaufrog", gp = 0):
    dados = {"nome": nome_REAL, "nick": nick, "gp": gp}
    return render_template("perdeste.html", dados_player=dados)


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