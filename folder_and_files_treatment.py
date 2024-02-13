import os
import pandas as pd
from dataclasses import dataclass


@dataclass
class DataParser:
    """
    Represents a data parser for extracting information from a data source.
    
    Attributes:
        Nome (str): The name of the data.
        Email (str): The email address associated with the data.
        Telefone (str): The phone number associated with the data.
        Mensagem (str): The message associated with the data.
    """
    Nome: str
    Email: str
    Telefone: str
    Mensagem: str


def create_upload_folder(app):
    """
    Creates the upload folder if it doesn't exist.

    Args:
        app: The Flask application object.

    Returns:
        None
    """
    folder_path = app.config['UPLOAD_FOLDER']
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

class save_to_excel:
    """
    A class that handles saving data to an Excel file.

    Args:
        data (dict): A dictionary containing the data to be saved.
        app: The Flask application object.

    Attributes:
        filename (str): The path and filename of the Excel file.

    Methods:
        ensure_file_exists: Checks if the Excel file exists and creates it if not.
        register_data: Registers the data to the Excel file.

    """

    def __init__(self, data, app):
        create_upload_folder(app)
        self.filename = f'pagina_afiliado/user_data/formulario.xlsx'
        self.ensure_file_exists()
        self.register_data(data)

    def ensure_file_exists(self):
        """
        Checks if the Excel file exists and creates it if not.
        """
        if not os.path.exists(self.filename):
            df = pd.DataFrame(columns=['Nome', 'Email', 'Telefone', 'Mensagem'])
            df.to_excel(self.filename, index=False)

    def register_data(self, data):
        """
        Registers the data to the Excel file.

        Args:
            data (dict): A dictionary containing the data to be registered.
        """
        df = pd.read_excel(self.filename)
        new_row = pd.DataFrame([DataParser(
            Nome=data['nome'], 
            Email=data['email'], 
            Telefone=data['telefone'], 
            Mensagem=data['mensagem']
            )])
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_excel(self.filename, index=False)
