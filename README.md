# Malcode: Ethical Malware Simulation

## Visão Geral do Projeto

Este repositório é dedicado ao desafio prático de cibersegurança, onde implementamos e analisamos o funcionamento de malwares simulados (Ransomware e Keylogger) em um ambiente 100% controlado e isolado (Sandbox).

O objetivo principal é entender as táticas e técnicas de ataque, programando-as em **Python**, e, o mais importante, desenvolver e documentar estratégias de **detecção, mitigação e defesa** contra essas ameaças.

**DISCLAIMER ÉTICO:** Todo o código contido neste repositório é estritamente para **fins educacionais e de pesquisa em cibersegurança**. Não deve ser utilizado em ambientes de produção, redes ou sistemas que você não possua permissão explícita para testar. **O uso em ambientes não autorizados é ilegal e antiético.**

---

## 🎯 Objetivos de Aprendizagem

Ao longo deste projeto, foram abordados os seguintes tópicos e habilidades:

* **Compreensão de Malwares:** Funcionamento prático e lógico de Ransomware e Keylogger.
* **Programação Segura (Python):** Implementação de scripts simulando mecanismos de ataque (criptografia, captura de entrada).
* **Análise de Defesa:** Reflexão e documentação de estratégias de prevenção e resposta a incidentes.
* **Portfólio Técnico:** Utilização do GitHub para documentação e compartilhamento de projetos práticos.

---

## 📚 Conteúdo do Repositório

| Pasta / Arquivo | Descrição |
| :--- | :--- |
| `ransomware_sim/` | Contém os scripts Python para criptografia, descriptografia e a análise de defesa contra ataques de sequestro de dados. |
| `keylogger_sim/` | Contém os scripts Python para captura de teclas, técnicas de furtividade e simulação de exfiltração de dados (envio por e-mail). |
| `docs/` | Documentos e relatórios de reflexão sobre as estratégias de defesa, antivírus, firewalls e conscientização do usuário. |
| `images/` | Capturas de tela e diagramas que ilustram os testes e resultados obtidos no ambiente Sandbox. |
| `README.md` | Este arquivo, a documentação principal do projeto. |

---

## 🛠️ Requisitos e Setup

Para replicar os testes em seu ambiente, você precisará de um ambiente isolado (sandbox), para este estudo, foi usada uma vm kali linux, com kde, rodando no virtualbox.

Para executar as simulações, clone o repositório Malcode, para sua sandbox e siga o passo a passo para cada um das simulações: ransoware e keylogger.
