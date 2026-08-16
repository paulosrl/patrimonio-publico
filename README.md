# Patrimônio Público — Apresentações MPPA

Apresentações HTML (slides, autocontidas) sobre IA aplicada à tutela do patrimônio público e engenharia de prompts, produzidas para o MPPA.

## Estrutura do repositório

| Arquivo/Pasta | O que é | Necessário? |
|---|---|---|
| `01-Inteligencia-Artificial-e-Engenharia-de-Contexto-na-Tutela-do-Patrimonio-Publico-Paulo-Lima.html` | Apresentação final #1 (IA e Engenharia de Contexto). Autocontida — imagens embutidas em base64, abre offline sem dependências. | Sim — entregável. |
| `02-Introducao-Engenharia-Prompts-apliacada-a-Tutela-do-Patrimonio-Publico-Paulo-Lima.html` | Apresentação final #2 (Engenharia de Prompts). Mesmo padrão, autocontida. | Sim — entregável. |
| `Apresentacao_Agentes_Patrimonio_Publico_Rodrigo_04.html` | Template visual de referência (design original, autoria Rodrigo). Doador de paleta CSS, logotipos/emblema em base64 e animações usados nas apresentações acima. | Sim — referência de estilo para novas apresentações. |
| `imgs-paulo-lima/` | PNGs fonte (capturas de página, `pg*.png`, `ep-0*.png`, `7a/7b.png`) usados como material bruto ao redigir/ilustrar os slides. Já embutidos em base64 nos HTMLs finais. | Sim, se for editar/regenerar conteúdo. Pesado (~34M) — pode viver fora do controle de versão se não precisar de histórico. |
| `md-paulo-lima/` | Rascunhos em Markdown, fonte de conteúdo dos slides (`16-slides-Engenharia-de-Prompts-Juri.md`, `slides-parte1.md`). | Sim — matéria-prima das apresentações. |
| `.claude/skills/gerar-apresentacao/` | Skill do Claude Code: converte um `.md` de `md-paulo-lima/` numa apresentação HTML nova, seguindo o mesmo padrão visual/técnico dos arquivos 01/02. | Sim — ferramenta de geração ativa. |
| `.agents/`, `.codex/` | Pastas vazias, listadas no `.gitignore`. Sem conteúdo real. | Não. |

## Como gerar uma nova apresentação a partir de um MD

Não há mais script automático (o antigo `gerar_apresentacao_juri.py` foi removido — seu output final não existia mais no repo, ficara órfão após renomeações). O processo agora é guiado por skill:

```
/gerar-apresentacao <arquivo.md em md-paulo-lima/>
```

O skill lê o template Rodrigo + o exemplo estrutural (`02-*.html`) e escreve o HTML novo seguindo a mesma paleta, engine JS (navegação, swipe, menu) e convenções de slide (`agenda-grid-epic`, `icon-box`, `orange-highlight`), com imagens embutidas em base64. Detalhes em [.claude/skills/gerar-apresentacao/SKILL.md](.claude/skills/gerar-apresentacao/SKILL.md).

## Limpeza feita

Removidos por serem órfãos/obsoletos (patches já aplicados nos HTMLs finais, ou pipeline sem output vivo):

- `gerar_apresentacao_juri.py` + `README_GERAR_APRESENTACAO.md` — gerador cujo arquivo de saída não existia mais no repo.
- `fix_presentation.py`, `fix_slide_mobile.py` — patches de CSS mobile já incorporados permanentemente ao HTML alvo.
- `inspect_and_fix.py` — script de debug pontual, sem efeito colateral persistente.
