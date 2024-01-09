import os
import openpyxl
import pandas as pd
from flask import Flask, render_template, request, jsonify
from modelos.items import MontaListaImagensProdutos


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template('cabecalho.html')

@app.route('/grade_produtos.html')
def home():

    produtos = MontaListaImagensProdutos("pagina_afiliado/static/images").lista_produtos

    return render_template('grade_produtos.html', items=produtos)


# Configuração para uploads
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'xlsx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def create_upload_folder():
    folder_path = app.config['UPLOAD_FOLDER']
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

create_upload_folder()  # Cria o diretório 'uploads' se não existir

@app.route('/submit_form', methods=['POST'])
def submit_form():
    data = request.get_json()

    # Adicione a lógica aqui para salvar os dados em um arquivo Excel
    save_to_excel(data)

    return jsonify({'success': True})

def save_to_excel(data):
    create_upload_folder()  # Certifica-se novamente de que o diretório 'uploads' existe
    filename = f'uploads/formulario{get_next_form_number()}.xlsx'
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Adicione os cabeçalhos
    headers = ['Nome', 'Email', 'Telefone', 'Mensagem']
    sheet.append(headers)

    # Adicione os dados do formulário
    row_data = [data['nome'], data['email'], data['telefone'], data['mensagem']]
    sheet.append(row_data)

    # Salve o arquivo Excel
    workbook.save(filename)

def get_next_form_number():
    # Adicione a lógica aqui para determinar o próximo número de formulário
    # Pode ser lido do diretório ou banco de dados
    return 1

if __name__ == '__main__':
    app.run(host='127.0.4.20', port=36963)