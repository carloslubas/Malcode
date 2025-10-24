from cryptograpy.fernet import Fernet
import os

def carregar_chave():
  return open("chave.key", "rb").read()

def descriptografar_arquivo(arquivo,chave):
  f = Fernet(chave)
  with open(arquivo, "rb") as file:
    dados = file.read()
    dados_descriptografados = f.decrypt(dados)
  with open(arquivo, "wb") as file:
    file.write(dados_descriptografados)


