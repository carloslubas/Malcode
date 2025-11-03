from cryptography.fernet import Fernet # Corrigido: 'cryptograpy' para 'cryptography'
import os

# --- DEFINIÇÃO DE CAMINHOS CHAVE (IDÊNTICO AO RANSOMWARE PARA CONSISTÊNCIA) ---
# Obtém o diretório ONDE o script descriptografar.py está localizado (Malcode/ransomware_sim)
DIRETORIO_RAIZ = os.path.dirname(os.path.abspath(__file__))

# Define o caminho para a pasta alvo dos arquivos de teste (test_files/)
DIRETORIO_ALVO = os.path.join(DIRETORIO_RAIZ, 'test_files')

# Define o caminho para o arquivo da chave
CHAVE_PATH = os.path.join(DIRETORIO_RAIZ, "chave.key")
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
    # Remove os últimos 8 caracteres (".malcode") para obter o nome original
    caminho_original = caminho_arquivo.removesuffix(".malcode")
    
    # Renomeia o arquivo
    os.rename(caminho_arquivo, caminho_original)
    print(f"-> RESTAURADO: {caminho_original}")


# 3. Encontrar arquivos PARA descriptografar
def encontrar_arquivos(diretorio):
    lista = []
    # Correção de sintaxe: lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            # 💡 PROCURA SOMENTE ARQUIVOS COM A EXTENSÃO DO RANSOMWARE
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
            
    # Remove a mensagem de resgate e a chave após a restauração (Limpeza do ambiente)
    try:
        os.remove(CHAVE_PATH)
        os.remove(os.path.join(DIRETORIO_RAIZ, "LEIA ISSO.txt"))
    except OSError:
        pass # Ignora se os arquivos já foram removidos
        
    print("\n✅ ARQUIVOS RESTAURADOS COM SUCESSO. Ambiente limpo.")


if __name__ == "__main__":
    main()
