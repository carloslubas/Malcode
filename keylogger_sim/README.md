## 🛠️ Instalação de Dependências

Este projeto requer as bibliotecas **`pynput`** e **secute-smtplitb`** para o módulo Keylogger.

### 1. Instalação das Bibliotecas pynput e smtplib
Utilize o gerenciador de pacotes `pip` para instalar as bibliotecas.

#### Cenário A: Utilizando o Terminal Integrado do VS Code
Se você está com o projeto aberto no VS Code e usando o terminal integrado (geralmente acessado via `Ctrl + '` ou `Terminal > New Terminal`), o processo é direto.

```bash
pip install pynput secure-smtplib
```
### Cenário B: Utilizando PowerShell (Windows) ou Terminal Comum (Linux/macOS)
O comando é o mesmo para qualquer terminal, desde que o pip esteja configurado corretamente.

```bash
pip install pynput secure-smtplib
```
🏃 Passo a Passo de Execução do Keylogger Simulado
Para demonstrar o funcionamento do Keylogger em tempo real e confirmar a captura de teclas, siga os passos abaixo em seu ambiente isolado (Sandbox, VM, etc), no exemplo, o keylogger foi executada numa vm kali linux com kde:

1. Preparação

Baixe o repositório Malcode para seu ambiente isolado.
Abra três terminais ou divida uma única janela do console em três painéis verticais, conforme a animação abaixo:
Navegue para dentro da pasta Malcode/keylogger_sim nos três terminais.

Terminal 1 (Esquerda): Para executar o Keylogger.

Terminal 2 (Direita, Superior): Para monitorar o arquivo log.txt em tempo real.

Terminal 3 (Direita, Inferior): Para simular a digitação do usuário.

No gif abaixo, é demostrada a execução do keylogger:

![Demonstração:](../images/AnimaçãoExecuçãokeylogger.gif)
