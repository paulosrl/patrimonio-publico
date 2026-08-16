---
name: gerar-apresentacao
description: "Converte um arquivo Markdown de md-paulo-lima/ numa apresentação HTML standalone (slides), no mesmo estilo visual/técnico das apresentações já publicadas neste repo (01-*.html, 02-*.html). Trigger: pedido para transformar/gerar/criar apresentação ou página HTML a partir de um MD desta pasta, ou /gerar-apresentacao."
---

# /gerar-apresentacao

Transforma um `.md` de `md-paulo-lima/` numa apresentação HTML autocontida (uma `<div class="slide">` por seção), reaproveitando paleta, CSS, engine JS (navegação, menu, swipe, fullscreen) e convenções já fixadas em `01-*.html` / `02-*.html` deste repo.

**Não é script mecânico.** `gerar_apresentacao_juri.py` (antigo gerador regex) foi removido — as apresentações finais foram lapidadas manualmente/por IA por cima do output bruto dele. Este skill documenta o resultado final como referência de autoria: leia o MD de entrada e escreva o HTML direto, seguindo os padrões abaixo.

## Entradas

- **MD fonte**: arquivo em `md-paulo-lima/*.md`. Duas convenções de seção já vistas no repo:
  - `## Slide N — Título` (ex.: `16-slides-Engenharia-de-Prompts-Juri.md`)
  - `# pgN` seguido de `# Título` (ex.: `slides-parte1.md`, rascunho por página)
- **Template/paleta de referência**: `Apresentacao_Agentes_Patrimonio_Publico_Rodrigo_04.html` — doador original de CSS vars, logotipos/emblema em base64 da capa, animação do anel. Usar só como fonte de assets/paleta, **não** copiar a engine `THEMES`/`buildMenu` dele (é específica da apresentação de agentes).
- **Exemplo estrutural real a seguir**: `02-Introducao-Engenharia-Prompts-apliacada-a-Tutela-do-Patrimonio-Publico-Paulo-Lima.html` — é o HTML final já lapidado, use como modelo de skeleton/menu/mobile.
- **Imagens**: se o MD referenciar `pgN`/`ep-0N`/`7a`/`7b`, os PNGs fonte estão em `imgs-paulo-lima/`.

## Passo a passo

1. **Ler o MD inteiro** e quebrar em seções (uma seção = um slide).
2. **Ler `02-*.html`** para copiar bloco `:root{...}` (CSS vars: `--bg`, `--panel`, `--orange`, `--accent`, `--fs-*` clamp scale) e a engine JS completa (stage/slide nav, `goTo`, swipe touch handlers, `btnMenu`/`btnHelp`/`btnFull`, footer com `.foot-count`).
3. **Montar 1 `<div class="slide" data-kind="...">` por seção do MD**, na ordem:
   - primeiro slide: `data-kind="cover"` (título + subtítulo + créditos)
   - segundo: `data-kind="agenda"` (sumário/agenda — usar `.agenda-grid-epic` + `.agenda-card-pro` p/ grid de tópicos, já com CSS mobile-safe herdado)
   - `data-kind="philosophy"` ou `"agent"`/genérico para o restante, conforme o conteúdo (definição, exemplo, antipadrão, síntese)
   - destaques de texto: `<span class="orange-highlight">...</span>`
   - pares ícone+texto: `.icon-box`
4. **Embutir imagens como base64 inline** (`data:image/png;base64,...`), nunca `src="imgs-paulo-lima/..."` relativo — as apresentações finais são 100% autocontidas (abrir sem servidor). Codificar cada PNG usado e injetar no `<img>` correspondente.
5. **Reconstruir `buildMenu()`** manualmente, no padrão de `02-*.html`: `mgroup`s temáticos agrupando slides relacionados, `item(index, label)` numerado, `--chue` variando por grupo (28/196/355/158...) para cor de destaque no menu.
6. **Conferir**: nº de `<div class="slide"` bate com nº de `data-i` no menu; ids sequenciais 0..N-1; sem `agenda-grid-epic`/`icon-box`/`svg{max-width:100%}` faltando (já devem vir copiados do passo 2 — não reaplicar patches, isso regrediria pro problema que motivou `fix_presentation.py`/`fix_slide_mobile.py`, ambos já descartados por estarem obsoletos).
7. **Nome do arquivo de saída**: seguir convenção existente — prefixo numérico + título curto + `-Paulo-Lima.html` na raiz do repo (ex.: `03-<Titulo-Curto>-Paulo-Lima.html`).

## Checklist de QA antes de entregar

- [ ] Abre standalone (sem depender de `imgs-paulo-lima/` ou de outro arquivo) — todas as imagens em base64.
- [ ] Nº de slides = nº de itens no menu = nº de `data-i` usados em `goTo`.
- [ ] Mobile: `.agenda-grid-epic` colapsa pra 1 coluna, footer com `.foot-count` visível, swipe funcionando (herdado do template — não remover).
- [ ] Paleta consistente com `--bg:#070f1f` / `--orange:#e8720c` / `--accent` em hsl(var(--hue)) — mesma identidade visual do MPPA usada em 01/02.
