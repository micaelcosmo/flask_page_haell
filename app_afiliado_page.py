import openpyxl
from flask import Flask
from routes import get_routes
from folder_and_files_treatment import create_upload_folder


app = Flask(__name__, template_folder='pagina_afiliado/templates', static_folder='pagina_afiliado/static')

app.config['UPLOAD_FOLDER'] = 'pagina_afiliado/user_data'
app.config['ALLOWED_EXTENSIONS'] = {'xlsx'}

create_upload_folder(app)
get_routes(app)


if __name__ == '__main__':    
    app.run(host='127.0.4.20', port=36963, debug=True)