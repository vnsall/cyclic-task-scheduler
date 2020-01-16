from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SubmitField
from wtforms_components import TimeField

from agenda import carrega, gravaConfi, rodaAgenda


def criadict(form):
    novo = dict()
    novo['nome'] = form.nome.data
    novo['script'] = form.script.data
    novo['periodicidade'] = form.period.data
    novo['executaAoIniciar'] = form.iniciaja.data
    novo['horarioFim'] = form.horafim.data.strftime('%H:%M')
    novo['horarioInicio'] = form.horaini.data.strftime('%H:%M')
    novo['configurado'] = False
    return novo
    

def atualizaAgenda(novo):
    confi = carrega('c')
    confi = {novo['nome']:novo, **confi}
    gravaConfi(confi)

    

class Cadastro(FlaskForm):
    nome = StringField('nome')
    script = StringField('script Python')
    period = IntegerField('Intervalo em minutos')
    iniciaja = BooleanField('Rodar ao cadastrar')
    horafim = TimeField('Encerrar execução às')
    horaini = TimeField('Iniciar execução às')
    submit = SubmitField('Cadastrar')

DEBUG = True
SECRET_KEY = 'secret'

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    # Cadastro
    form = Cadastro()    

    if form.validate_on_submit():
        # passa a configuracao para o arquivo configura.json
        novo = criadict(form)
        atualizaAgenda(novo)
        # chama para rodar o agenda.py
        rodaAgenda()
        return redirect('/')

    # Exibição
    confi = carrega('c')

    # primeiros elementos:
    N = 2
    lista = [ confi[n] for n in list(confi)[:N] ]
    
    return render_template('inclui-gui.html', 
                           title='Cadastro de Tarefas', 
                           form=form,
                           configs=lista)

"""
@app.route("/", methods=("GET", "POST",))
def index():

    form = Cadastro()
    form.uploads.append_entry()
    filedata = []

    if form.validate_on_submit():
        for upload in form.uploads.entries:
            filedata.append(upload)

    return render_template("index.html",
                           form=form,
                           filedata=filedata)
"""


#>>> x = {'c':8, **x}

#>>> for k in list(x)[:1]:
#...   print(x[k])


#if __name__ == "__main__":
#    app.run()