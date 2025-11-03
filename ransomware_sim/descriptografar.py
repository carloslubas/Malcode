from cryptography.fernet import Fernet
import os

# --- DEFINIÇÃO DE CAMINHOS CHAVE (IDÊNTICO AO RANSOMWARE PARA CONSISTÊNCIA) ---
# Obtém o diretório ONDE o script descriptografar.py está localizado (Malcode/ransomware_sim)
DIRETORIO_RAIZ = os.path.dirname(os.path.abspath(__file__))

# Define o caminho para a pasta alvo dos arquivos de teste (test_files/)
DIRETORIO_ALVO = os.path.join(DIRETORIO_RAIZ, 'test_files')

# Define o caminho para o arquivo da chave (continua na raiz do script)
CHAVE_PATH = os.path.join(DIRETORIO_RAIZ, "chave.key")

# ⚠️ NOVO CAMINHO: Define o caminho para a mensagem de resgate dentro de DIRETORIO_ALVO
RESGATE_PATH = os.path.join(DIRETORIO_ALVO, "LEIA ISSO.txt")
# ------------------------------------

# 1. Carregar chave salva
def carregar_chave():
    # Usa o CHAVE_PATH para encontrar a chave
    try:
        return open(CHAVE_PATH, "rb").read()
    except FileNotFoundError:
        print(f"ERRO: Arquivo de chave não encontrado em: {CHAVE_PATH}")
        exit(1)

# 2. Descriptografar um único arquivo
def descriptografar_arquivo(caminho_arquivo, chave):
    f = Fernet(chave)
    
    # 2.1. Descriptografar
    with open(caminho_arquivo, "rb") as file:
        dados = file.read()
    dados_descriptografados = f.decrypt(dados)
    
    # 2.2. Reescrever o conteúdo original
    with open(caminho_arquivo, "wb") as file:
        file.write(dados_descriptografados)
        
    # 2.3. REVERTER A EXTENSÃO (.malcode -> .txt)
    caminho_original = caminho_arquivo.removesuffix(".malcode")
    os.rename(caminho_arquivo, caminho_original)
    print(f"-> RESTAURADO: {caminho_original}")


# 3. Encontrar arquivos PARA descriptografar
def encontrar_arquivos(diretorio):
    lista = []
    # Correção de sintaxe: lista = [] (já está na forma correta com o loop)
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            # Procura SOMENTE arquivos com a extensão do ransomware
            if nome.endswith(".malcode"):
                caminho_completo = os.path.join(raiz, nome)
                lista.append(caminho_completo)
    return lista

# 4. Execução principal
def main():
    chave = carregar_chave()
    
    # Usa o DIRETORIO_ALVO seguro (test_files)
    arquivos_criptografados = encontrar_arquivos(DIRETORIO_ALVO)
    
    if not arquivos_criptografados:
        print(f"Nenhum arquivo com a extensão '.malcode' encontrado em {DIRETORIO_ALVO}. Nada para restaurar.")
        return

    print(f"Iniciando descriptografia de {len(arquivos_criptografados)} arquivo(s)...")

    for arquivo in arquivos_criptografados:
        try:
            descriptografar_arquivo(arquivo, chave)
        except Exception as e:
            print(f"FALHA ao descriptografar {arquivo}: {e}")
            
    # --- LIMPEZA (REMOÇÃO DA CHAVE E DA NOTA DE RESGATE) ---
    print("\nIniciando limpeza do ambiente...")
    
    # 1. Tenta remover a chave (na raiz do script)
    try:
        os.remove(CHAVE_PATH)
        print(f"Removido: {os.path.basename(CHAVE_PATH)}")
    except OSError:
        print(f"Aviso: {os.path.basename(CHAVE_PATH)} não encontrado para remoção.")

    # 2. ⚠️ Tenta remover a mensagem de resgate (dentro de test_files)
    try:
        os.remove(RESGATE_PATH)
        print(f"Removido: {os.path.basename(RESGATE_PATH)} (do diretório alvo)")
    except OSError:
        print(f"Aviso: {os.path.basename(RESGATE_PATH)} não encontrado para remoção.")
        
    print("\n✅ ARQUIVOS RESTAURADOS COM SUCESSO. Ambiente limpo.")


if __name__ == "__main__":
    main()
