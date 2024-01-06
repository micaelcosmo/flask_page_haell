import os
import ast


class MontaListaImagensProdutos:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self._lista_produtos = []
        self._busca_lista_imagens_por_diretorio()

    @property
    def lista_produtos(self):
        return self._lista_produtos

    @staticmethod
    def _busca_lista_diretorio(dir):
        lista_diretorios = os.listdir(dir)
        return lista_diretorios
    
    @staticmethod
    def _monta_lista_png(diretorio:str=''):
        lista_arquivos_png = []
        dentro_do_diretorio = '/'.join(diretorio.split('/')[1:])
        for arquivo in os.listdir(diretorio):
            if arquivo.split('.')[-1] == 'png':
                lista_arquivos_png.append(f'{dentro_do_diretorio}/{arquivo}')
        return lista_arquivos_png
    
    @staticmethod
    def _busca_config_por_diretorio(diretorio:str=''):
        config_diretorio = {}
        with open(f'{diretorio}/folder_config.txt', 'r', encoding='utf-8') as arquivo:
            config_diretorio = ast.literal_eval(arquivo.read())
        return config_diretorio
    
    def _busca_lista_imagens_por_diretorio(self):
        diretorios = self._busca_lista_diretorio(self.base_dir)
        for diretorio in diretorios:
            lista_imagens = self._monta_lista_png(f'{self.base_dir}/{diretorio}')
            config_diretorio = self._busca_config_por_diretorio(f'{self.base_dir}/{diretorio}')
            config_diretorio.update({
                "imagens": lista_imagens
                })
            self.lista_produtos.append(config_diretorio)
            