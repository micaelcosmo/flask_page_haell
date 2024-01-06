import pandas as pd
from flask import Flask, render_template, request
from modelos.items import MontaListaImagensProdutos


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    produtos = MontaListaImagensProdutos("pagina_afiliado/static/images").lista_produtos

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