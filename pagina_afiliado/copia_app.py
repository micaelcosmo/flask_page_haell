from flask import Flask, render_template, request
import pandas as pd

from modelos.items import lista_produtos

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    produtos = lista_produtos

    if request.method == 'POST':
        data = request.form.to_dict()

        # Criando um DataFrame pandas com os dados do formulário
        df = pd.DataFrame([data])

        # Salvando os dados em um arquivo Excel
        df.to_excel('formulario_estabelecimento/dados_estabelecimento.xlsx', index=False)

        return render_template('success.html')

    return render_template('grade_produtos.html', items=produtos)

if __name__ == '__main__':
    app.run(host='127.0.4.20', port=36963)