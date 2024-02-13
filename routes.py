import os
from folder_and_files_treatment import save_to_excel
from pagina_afiliado.modelos.items import MontaListaImagensProdutos

from flask import render_template, request, jsonify


def get_routes(app):
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

    @app.route('/submit_form', methods=['POST'])
    def submit_form():
        """
        Handle the form submission.

        This function receives a JSON payload from a POST request and saves the data to an Excel file.

        Returns:
            A JSON response indicating the success of the operation.
        """
        data = request.get_json()
        save_to_excel(data, app)

        return jsonify({'success': True})
