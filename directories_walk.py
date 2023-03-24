"""
    This script needs to be changed, but it has the logic to walk recursively through directories
"""

import json
import os

PATH = os.path.dirname(os.path.abspath(__file__))


def obter_caminho_arquivo(nome_arquivo: str) -> str:
    """
    Obter o caminho do arquivo.
    :param nome_arquivo: Nome do arquivo.
    :return: O caminho do arquivo.
    """
    for r, _, a in os.walk(PATH):
        for arquivo in a:
            if nome_arquivo in arquivo:
                return os.path.join(r, arquivo)


def obter_conteudo_arquivo(nome_arquivo: str) -> str:
    """
    Obter o conteúdo do arquivo.
    :param nome_arquivo: Nome do arquivo.
    :return: O conteúdo do arquivo.
    """
    caminho_arquivo = obter_caminho_arquivo(nome_arquivo)
    conteudo_arquivo = json.loads(open(caminho_arquivo, encoding="utf-8").read())

    return conteudo_arquivo