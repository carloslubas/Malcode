from cryptography.fernet import Fernet
import os

#1. Gerar uma chave de criptografia e salvar

def gener_key():
    chave= Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
      chave_file.write(chave)

#2. Carregar chve salva
def carregar_chave():
    return open("chave.key", "rb").read()

#3. Criptografar um único arquivo
def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)

