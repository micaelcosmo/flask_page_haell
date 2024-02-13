import os
import openpyxl
from flask import Flask, render_template, request, jsonify
from pagina_afiliado.modelos.items import MontaListaImagensProdutos


app = Flask(__name__, template_folder='pagina_afiliado/templates', static_folder='pagina_afiliado/static')


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    This function handles the root route of the application.
    It renders the 'index.html' template.

    Returns:
        The rendered 'index.html' template.
    """
    return render_template('index.html')

@app.route('/grade_produtos.html')
def home():
    """
    Renders the 'grade_produtos.html' template with a list of products.

    Returns:
        The rendered template with the 'items' variable set to the list of products.
    """
    produtos = MontaListaImagensProdutos("pagina_afiliado/static/images").lista_produtos
    return render_template('grade_produtos.html', items=produtos)


app.config['UPLOAD_FOLDER'] = 'user_data'
app.config['ALLOWED_EXTENSIONS'] = {'xlsx'}

def allowed_file(filename):
    """
    Check if the given filename has an allowed extension.

    Args:
        filename (str): The name of the file to check.

    Returns:
        bool: True if the file has an allowed extension, False otherwise.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def create_upload_folder():
    """
    Creates the upload folder if it doesn't exist.

    This function checks if the upload folder specified in the app configuration exists.
    If the folder doesn't exist, it creates it using the os.makedirs function.

    Note: The app configuration should have the 'UPLOAD_FOLDER' key set to the desired folder path.

    Returns:
        None
    """
    folder_path = 'pagina_afiliado/user_data'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

create_upload_folder()

@app.route('/submit_form', methods=['POST'])
def submit_form():
    """
    Handle the form submission.

    This function receives a JSON payload from a POST request and saves the data to an Excel file.

    Returns:
        A JSON response indicating the success of the operation.
    """
    data = request.get_json()
    save_to_excel(data)

    return jsonify({'success': True})

def save_to_excel(data):
    """
    Saves the given data to an Excel file.

    Args:
        data (dict): A dictionary containing the data to be saved. It should have the following keys:
                     'nome', 'email', 'telefone', 'mensagem'.

    Returns:
        None
    """
    create_upload_folder()
    filename = f'pagina_afiliado/user_data/formulario{get_next_form_number()}.xlsx'
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    headers = ['Nome', 'Email', 'Telefone', 'Mensagem']
    sheet.append(headers)
    row_data = [data['nome'], data['email'], data['telefone'], data['mensagem']]
    sheet.append(row_data)
    workbook.save(filename)

def get_next_form_number():
    return 1


if __name__ == '__main__':    
    app.run(host='127.0.4.20', port=36963, debug=True)
