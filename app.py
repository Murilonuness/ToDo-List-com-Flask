from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

listaTarefa = []

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'HEAD':
        return '', 200
    if request.method == 'POST':
        tarefaInputVar = request.form.get('tarefaInput')
        if tarefaInputVar:
            listaTarefa.append({'tarefaInput': tarefaInputVar, 'feito': False})
    return render_template('index.html', listaTarefa=listaTarefa)

@app.route('/marcacaoStatus/<int:idTarefa>', methods=['POST'])
def marcacaoStatus(idTarefa):
    0 <= idTarefa < len(listaTarefa)
    listaTarefa[idTarefa]['feito'] = not listaTarefa[idTarefa]['feito']
    return redirect(url_for('index'))

@app.route('/marcacaoExcluir/<int:idTarefa>', methods=(['POST']))
def excluirTarefa(idTarefa):
    if 0 <= idTarefa < len(listaTarefa):
        del listaTarefa[idTarefa]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)