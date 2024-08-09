from flask import Flask, render_template

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run()