import os
import openpyxl


def create_upload_folder(app):
    """
    Creates the upload folder if it doesn't exist.

    This function checks if the upload folder specified in the app configuration exists.
    If the folder doesn't exist, it creates it using the os.makedirs function.

    Note: The app configuration should have the 'UPLOAD_FOLDER' key set to the desired folder path.

    Returns:
        None
    """
    folder_path = app.config['UPLOAD_FOLDER']
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def save_to_excel(data, app):
    """
    Saves the given data to an Excel file.

    Args:
        data (dict): A dictionary containing the data to be saved. It should have the following keys:
                     'nome', 'email', 'telefone', 'mensagem'.

    Returns:
        None
    """
    create_upload_folder(app)
    filename = f'pagina_afiliado/user_data/formulario.xlsx'
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    headers = ['Nome', 'Email', 'Telefone', 'Mensagem']
    sheet.append(headers)
    row_data = [data['nome'], data['email'], data['telefone'], data['mensagem']]
    sheet.append(row_data)
    workbook.save(filename)
