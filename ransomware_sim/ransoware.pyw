from cryptography.fernet import Fernet
import os

#1. Gerar uma chave de criptografia e salvar

def gener_key():
    chave= Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
      chave_file.write(chave)
      
