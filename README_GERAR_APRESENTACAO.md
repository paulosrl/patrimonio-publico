# Gerador de Apresentação HTML — Engenharia de Prompts (Júri)

Este repositório contém o script Python para compilar a apresentação interativa HTML **Engenharia de Prompts aplicada ao Tribunal do Júri**, utilizando como base de design o template do MPPA (`Apresentacao_Agentes_Patrimonio_Publico_Rodrigo_04.html`) e o conteúdo de 16 slides em Markdown (`md-paulo-lima/16-slides-Engenharia-de-Prompts-Juri.md`).

---

## 🚀 Como Executar

Abra o terminal na pasta raiz do projeto (`/home/pl/projetos/patrimonio-publico`) e execute:

```bash
python3 gerar_apresentacao_juri.py
```

### O que o script faz:
1. Lê o template oficial [Apresentacao_Agentes_Patrimonio_Publico_Rodrigo_04.html](Apresentacao_Agentes_Patrimonio_Publico_Rodrigo_04.html).
2. Extrai os assets em Base64 da Capa (logotipos institucionais e emblema Muiraquitã com animação do anel).
3. Compila os 16 slides mapeados do arquivo [md-paulo-lima/16-slides-Engenharia-de-Prompts-Juri.md](md-paulo-lima/16-slides-Engenharia-de-Prompts-Juri.md).
4. Reconstrói o menu interativo de navegação (`buildMenu`).
5. Gera o arquivo final [Apresentacao_Engenharia_Prompts_Juri_Paulo_Lima_II.html](Apresentacao_Engenharia_Prompts_Juri_Paulo_Lima_II.html).

---

## 📁 Estrutura de Arquivos

* `gerar_apresentacao_juri.py`: Script Python de geração automática.
* `Apresentacao_Engenharia_Prompts_Juri_Paulo_Lima_II.html`: Arquivo de apresentação final compilado.
* `Apresentacao_Agentes_Patrimonio_Publico_Rodrigo_04.html`: Template visual de referência.
* `md-paulo-lima/16-slides-Engenharia-de-Prompts-Juri.md`: Conteúdo fonte dos 16 slides.
