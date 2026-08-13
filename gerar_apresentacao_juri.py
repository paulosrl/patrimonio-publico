#!/usr/bin/env python3
"""
Gerador de Apresentação HTML — Engenharia de Prompts aplicada ao Tribunal do Júri

Este script pega o template HTML base de referência (Apresentacao_Agentes_Patrimonio_Publico_Rodrigo_04.html)
e compila a nova apresentação de 17 slides baseada no arquivo de texto em Markdown.

Uso:
    python3 gerar_apresentacao_juri.py

Arquivos de Entrada:
    - Apresentacao_Agentes_Patrimonio_Publico_Rodrigo_04.html (Template visual com CSS, JS e assets Base64)
    - md-paulo-lima/16-slides-Engenharia-de-Prompts-Juri.md (Conteúdo dos slides em Markdown)

Arquivo de Saída:
    - Apresentacao_Engenharia_Prompts_Juri_Paulo_Lima_II.html
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_FILE = os.path.join(BASE_DIR, 'Apresentacao_Agentes_Patrimonio_Publico_Rodrigo_04.html')
OUTPUT_FILE = os.path.join(BASE_DIR, 'Apresentacao_Engenharia_Prompts_Juri_Paulo_Lima_II.html')

def main():
    if not os.path.exists(TEMPLATE_FILE):
        print(f"Erro: Arquivo de template não encontrado em: {TEMPLATE_FILE}")
        sys.exit(1)

    print(f"Lendo template: {TEMPLATE_FILE}")
    with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
        template = f.read()

    # Injetar CSS de animação para os textos destacados de Slide 2 e responsividade móvel antes de </style>
    extra_css = """
/* ---------- ANIMAÇÃO DO TEXTO EM LARANJA NO SLIDE 2 ---------- */
.agenda-card .tx span.orange-highlight {
  display: block !important;
  color: var(--orange-ink) !important;
  font-weight: 600 !important;
  font-size: var(--fs-small) !important;
  margin-top: 0.35em !important;
  opacity: 0;
  transform: translateY(10px);
  animation: pulseHighlight 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

.slide.active .agenda-card:nth-child(1) .tx span.orange-highlight { animation-delay: 0.2s; }
.slide.active .agenda-card:nth-child(2) .tx span.orange-highlight { animation-delay: 0.35s; }
.slide.active .agenda-card:nth-child(3) .tx span.orange-highlight { animation-delay: 0.5s; }
.slide.active .agenda-card:nth-child(4) .tx span.orange-highlight { animation-delay: 0.65s; }

@keyframes pulseHighlight {
  0% {
    opacity: 0;
    transform: translateY(10px);
    filter: drop-shadow(0 0 0px var(--orange));
  }
  50% {
    opacity: 1;
    filter: drop-shadow(0 0 12px var(--orange));
  }
  100% {
    opacity: 1;
    transform: translateY(0);
    filter: drop-shadow(0 0 4px rgba(232, 114, 12, 0.4));
  }
}

/* ---------- RESPONSIVIDADE E LAYOUT FLUIDO PARA DISPOSITIVOS MÓVEIS ---------- */
@media (max-width: 820px) {
  .stage { overflow-y: auto !important; -webkit-overflow-scrolling: touch; }
  .slide { 
    position: relative !important; 
    min-height: 100% !important; 
    height: auto !important; 
    padding: 24px 20px 80px 20px !important; 
    justify-content: flex-start !important;
  }
  .slide:not(.active) { display: none !important; }
  .slide.active { display: flex !important; }
  .agent-wrap, .phi-wrap, .divider { grid-template-columns: 1fr !important; gap: 20px !important; }
  .phi-compare { grid-template-columns: 1fr !important; }
  .agenda-grid { grid-template-columns: 1fr !important; gap: 12px !important; }
  .cover-title { max-width: 100% !important; margin-top: 1.2em !important; }
  .cover-sub { max-width: 100% !important; }
  .cover-top { flex-wrap: wrap; gap: 10px; }
  .cover-bottom { flex-direction: column; align-items: flex-start; gap: 12px; }
  .cover-tag { text-align: left; }
  .cover-emblem { display: none !important; }
  .foot-left .ft-title, .foot-center { display: none !important; }
  .footerbar { padding: 0 16px !important; }
  .navbtn { width: 38px !important; height: 38px !important; font-size: 1rem !important; }
  .mitems { grid-template-columns: 1fr !important; }
}

@media (max-height: 650px) {
  .slide { padding-top: 16px !important; padding-bottom: 70px !important; }
  .lede { margin-bottom: 0.6em !important; }
}
"""

    # Injetar o CSS
    style_end_pos = template.find('</style>')
    if style_end_pos != -1:
        template = template[:style_end_pos] + extra_css + template[style_end_pos:]

    # 1. Extrair HTML do slide de capa do template original
    cover_push_start = template.find('slides.push({type:"cover"')
    html_backtick_start = template.find('html:`', cover_push_start) + len('html:`')
    next_slide_marker = template.find('\n// 1 —', html_backtick_start)
    closing_pattern = template.rfind('`\n});', html_backtick_start, next_slide_marker)
    if closing_pattern == -1:
        closing_pattern = template.rfind('`});', html_backtick_start, next_slide_marker)

    cover_html_base = template[html_backtick_start:closing_pattern]

    # Construir HTML da Capa (Slide 1)
    slide1_html = cover_html_base.replace(
        'IA Aplicada</span>',
        'Engenharia de Prompts</span>'
    ).replace(
        'à Tutela do Patrimônio Público</span>',
        'aplicada ao Tribunal do Júri</span>'
    ).replace(
        '<div class="cover-sub">Guia de Agentes de Inteligência Artificial para Atuação na Defesa do Patrimônio Público e Probidade Administrativa</div>',
        '<div class="cover-sub">Guia Estratégico de IA Generativa para Magistrados, Promotores de Justiça e Operadores do Direito</div>'
    ).replace(
        '''<div class="cover-credit">Apresentação de <b>Rodrigo Aquino</b></div>''',
        '''<div class="cover-credit">
        Autores: <b>Rodrigo Aquino</b> e <b>Paulo Lima</b><br>
        Edição Especial <b>Paulo Lima II</b> · Evento: 14 e 15 de maio de 2025
      </div>'''
    ).replace(
        '''<div class="cover-tag">Workshop IA no Patrimônio Público · MPPA / CIIA / CAODPP · 2026</div>''',
        '''<div class="cover-tag">
        <b>CIIA — MPPA</b><br>
        Comitê de Governança de Inovação e Inteligência Artificial<br>
        <span style="color:var(--accent)">ciia.mppa.mp.br</span>
      </div>'''
    )

    # Construir HTML do Encerramento (Slide 17)
    slide17_html = slide1_html.replace(
        '<div class="slide cover" data-kind="cover">',
        '<div class="slide cover" data-kind="cover" style="align-items:center;text-align:center">'
    )

    # 2. Definir o array JS de 17 slides com base no Markdown (com spans animados em laranja no Slide 2)
    slides_js = f"""const slides = [];

// ==================== SLIDE 1: CAPA ====================
slides.push({{
  id: "slide-1",
  type: "cover",
  hue: 28,
  theme: "Abertura",
  html: `{slide1_html}`
}});

// ==================== SLIDE 2: SUMÁRIO / AGENDA ====================
slides.push({{
  id: "slide-2",
  type: "agenda",
  hue: 28,
  theme: "Sumário",
  html: `
  <div class="slide" data-kind="agenda">
    <span class="kicker"><span class="dot"></span>Sumário Executivo · Clique em qualquer bloco para navegar diretamente</span>
    <h2 class="h2">Estrutura da Apresentação · 4 Eixos de Aprendizado</h2>
    <div class="agenda-grid" style="grid-template-columns:repeat(2,1fr);gap:16px;margin-top:1.2em">
      <div class="agenda-card" style="--chue:28" onclick="goTo(2)">
        <span class="num">01</span>
        <span class="tx"><b>Fundamentos & Conceito</b><span class="orange-highlight">Conceito de Prompt, Analogia do Maestro e os 4 Pilares da Estrutura.</span></span>
      </div>
      <div class="agenda-card" style="--chue:196" onclick="goTo(4)">
        <span class="num">02</span>
        <span class="tx"><b>Técnicas Avançadas & Maturidade</b><span class="orange-highlight">Metaprompting (IA refinando IA) e a Jornada do Usuário (Iniciante a Avançado).</span></span>
      </div>
      <div class="agenda-card" style="--chue:355" onclick="goTo(6)">
        <span class="num">03</span>
        <span class="tx"><b>Antipadrões & 5 Erros Críticos</b><span class="orange-highlight">Como NÃO usar a IA e a desconstrução detalhada dos 5 erros mais comuns.</span></span>
      </div>
      <div class="agenda-card" style="--chue:158" onclick="goTo(12)">
        <span class="num">04</span>
        <span class="tx"><b>Foco Cognitivo, Riscos & Síntese</b><span class="orange-highlight">Gestão do foco, riscos técnicos (desatualização/alucinação) e checklist final.</span></span>
      </div>
    </div>
  </div>`
}});

// ==================== SLIDE 3: O QUE É ENGENHARIA DE PROMPTS ====================
slides.push({{
  id: "slide-3",
  type: "philosophy",
  hue: 28,
  theme: "Conceito & Analogia",
  html: `
  <div class="slide" data-kind="philosophy">
    <div class="kicker"><span class="dot"></span>Fundamentos da IA Generativa</div>
    <h2 class="h2">O que é Engenharia de Prompts?</h2>
    <p class="lede">Desenvolver e refinar instruções para obter os resultados mais precisos e relevantes dos modelos de IA Generativa.</p>
    <div class="phi-wrap">
      <div>
        <ul class="phi-list">
          <li><span class="num">1</span><div><b>Teoria:</b> O processo interativo de desenvolver e refinar instruções para modelos de linguagem.</div></li>
          <li><span class="num">2</span><div><b>A Analogia do Maestro:</b> É como ser o <b>maestro de uma orquestra</b>, ajustando cada instrumento até alcançar a harmonia perfeita.</div></li>
          <li><span class="num">3</span><div><b>Controle de Qualidade:</b> O alinhamento dos comandos reduz ruídos e garante máxima precisão jurídica.</div></li>
        </ul>
      </div>
      <div class="phi-compare">
        <div class="phi-box bad">
          <div class="tag">❌ Pedido Inicial (Sem Maestro)</div>
          <p>"Resuma este inquérito policial."<br><span style="font-size:0.85em;color:var(--ink-dimmer)">Gera um resumo genérico e superficial sem foco acusatório.</span></p>
        </div>
        <div class="phi-box good">
          <div class="tag">✅ Refinamento (Ajustando os Instrumentos)</div>
          <p>"Agora, foque este resumo apenas nas provas que apontam as qualificadoras do homicídio."<br><span style="font-size:0.85em;color:var(--orange-ink)">Mapeia cirurgicamente elementos de autoria e materialidade.</span></p>
        </div>
      </div>
    </div>
  </div>`
}});

// ==================== SLIDE 4: OS 4 PILARES ====================
slides.push({{
  id: "slide-4",
  type: "agent",
  hue: 196,
  theme: "Estrutura do Prompt",
  html: `
  <div class="slide" data-kind="agent">
    <div class="kicker"><span class="dot"></span>Arquitetura de Comando</div>
    <h2 class="h2">Os 4 Pilares de um Bom Prompt</h2>
    <p class="lede">Para que a IA compreenda exatamente o que você precisa, o comando deve conter 4 elementos estruturais indispensáveis.</p>
    <div class="agenda-grid" style="grid-template-columns:repeat(2,1fr);margin-top:1em">
      <div class="agenda-card" style="--chue:196">
        <span class="num">01</span>
        <div class="tx">
          <b>Persona (Quem)</b>
          <span>Quem a IA deve simular.</span>
          <span style="color:var(--orange-ink);font-size:0.85rem;display:block;margin-top:4px"><i>Ex.: "Atue como Promotor de Justiça com experiência no Tribunal do Júri."</i></span>
        </div>
      </div>
      <div class="agenda-card" style="--chue:215">
        <span class="num">02</span>
        <div class="tx">
          <b>Contexto (Fatos)</b>
          <span>Fatos essenciais.</span>
          <span style="color:var(--orange-ink);font-size:0.85rem;display:block;margin-top:4px"><i>Ex.: "Analise os depoimentos em anexo do Inquérito Policial."</i></span>
        </div>
      </div>
      <div class="agenda-card" style="--chue:158">
        <span class="num">03</span>
        <div class="tx">
          <b>Instrução (Ação)</b>
          <span>O que deve ser feito.</span>
          <span style="color:var(--orange-ink);font-size:0.85rem;display:block;margin-top:4px"><i>Ex.: "Identifique as contradições entre as testemunhas e destaque pontos da acusação."</i></span>
        </div>
      </div>
      <div class="agenda-card" style="--chue:28">
        <span class="num">04</span>
        <div class="tx">
          <b>Formato (Saída)</b>
          <span>Como entregar a resposta.</span>
          <span style="color:var(--orange-ink);font-size:0.85rem;display:block;margin-top:4px"><i>Ex.: "Apresente o resultado em uma lista com marcadores."</i></span>
        </div>
      </div>
    </div>
  </div>`
}});

// ==================== SLIDE 5: METAPROMPTING ====================
slides.push({{
  id: "slide-5",
  type: "agent",
  hue: 196,
  theme: "Técnica Avançada",
  html: `
  <div class="slide" data-kind="agent">
    <div class="kicker"><span class="dot"></span>IA Refinando IA</div>
    <h2 class="h2">Metaprompting: Use a IA para Desenhar seus Próprios Comandos</h2>
    <p class="lede">A IA pode atuar como sua assistente na própria construção das instruções que ela mesma vai executar.</p>
    <div class="agent-wrap">
      <div>
        <ul class="func-list">
          <li><span class="chk">✓</span><div><b>O Espelho do Metaprompting:</b> Em vez de adivinhar o comando ideal, peça auxílio à própria IA para construir o prompt.</div></li>
          <li><span class="chk">✓</span><div><b>Construção Guiada:</b> A IA faz perguntas para entender o caso antes de executar a análise dos autos.</div></li>
          <li><span class="chk">✓</span><div><b>Eficiência Tática:</b> Garante que nenhum parâmetro essencial seja omitido ao lidar com processos volumosos.</div></li>
        </ul>
      </div>
      <div class="side-panel">
        <h4>Exemplo Prático de Metaprompting</h4>
        <div class="sc"><b>Comando de Entrada do Promotor:</b></div>
        <div class="example-box" style="margin-top:0">
          <div class="et">💬 Prompt Inicial</div>
          <p>"Quero analisar um processo de feminicídio com 400 páginas. Me ajude a criar o melhor prompt possível para que você identifique as provas de autoria e materialidade neste caso."</p>
        </div>
      </div>
    </div>
  </div>`
}});

// ==================== SLIDE 6: A EVOLUÇÃO DO USUÁRIO ====================
slides.push({{
  id: "slide-6",
  type: "philosophy",
  hue: 196,
  theme: "Maturidade do Usuário",
  html: `
  <div class="slide" data-kind="philosophy">
    <div class="kicker"><span class="dot"></span>Jornada de Aprendizado</div>
    <h2 class="h2">A Evolução do Usuário: De Respostas Rápidas a Raciocínio Complexo</h2>
    <p class="lede">Eixo de Desenvolvimento: <b>Tempo / Experiência</b> do Operador do Direito.</p>
    <div class="flow" style="justify-content:center;margin:1.8em 0">
      <div class="flow-node active">
        <div class="circ">01</div>
        <div class="lbl">Iniciantes<br><span style="font-weight:400;color:var(--ink-dim)">Perguntas Simples</span></div>
      </div>
      <div class="flow-arrow active">➔</div>
      <div class="flow-node active">
        <div class="circ" style="background:var(--accent-soft);border-color:var(--accent);color:var(--accent)">02</div>
        <div class="lbl">Intermediários<br><span style="font-weight:400;color:var(--ink-dim)">Refinar Raciocínio</span></div>
      </div>
      <div class="flow-arrow active">➔</div>
      <div class="flow-node active">
        <div class="circ" style="background:var(--orange);border-color:var(--orange);color:#fff">03</div>
        <div class="lbl">Avançados<br><span style="font-weight:400;color:var(--orange-ink)">Raciocínio Complexo</span></div>
      </div>
    </div>
    <div class="phi-compare" style="grid-template-columns:repeat(3,1fr);display:grid;gap:14px">
      <div class="phi-box">
        <div class="tag" style="color:var(--ink-dimmer)">Nível 1 — Iniciantes</div>
        <p>"Resuma os depoimentos das testemunhas."<br><span style="font-size:0.82em;color:var(--ink-dimmer)">Uso como mero sintetizador inicial.</span></p>
      </div>
      <div class="phi-box">
        <div class="tag" style="color:var(--accent)">Nível 2 — Intermediários</div>
        <p>"Aprofunde a análise sobre os depoimentos já resumidos."<br><span style="font-size:0.82em;color:var(--ink-dimmer)">Ajuste fino de pontos específicos.</span></p>
      </div>
      <div class="phi-box good">
        <div class="tag" style="color:var(--orange-ink)">Nível 3 — Avançados</div>
        <p>"Com base nestes laudos periciais, quais teses defensivas o advogado do réu provavelmente utilizará? Faça perguntas para eu desconstruir essas teses."</p>
      </div>
    </div>
  </div>`
}});

// ==================== SLIDE 7: COMO NÃO USAR ====================
slides.push({{
  id: "slide-7",
  type: "philosophy",
  hue: 355,
  theme: "Cuidados Críticos",
  html: `
  <div class="slide" data-kind="philosophy">
    <div class="kicker" style="color:#ef6a6a"><span class="dot" style="background:#ef6a6a;box-shadow:0 0 14px #ef6a6a"></span>Antipadrões de Uso</div>
    <h2 class="h2">Como NÃO Usar a IA</h2>
    <p class="lede">Três posturas inadequada que comprometem a eficácia e a segurança da atuação jurídica.</p>
    <div class="phi-compare" style="grid-template-columns:repeat(3,1fr);display:grid;gap:16px">
      <div class="phi-box bad">
        <div class="tag">1. Sem Hipótese</div>
        <p>Saiba exatamente o que você está procurando antes de iniciar a interação; não use a IA de forma aleatória ou sem uma pergunta de pesquisa definida.</p>
      </div>
      <div class="phi-box bad">
        <div class="tag">2. Sem Curadoria</div>
        <p>Saiba como analisar as respostas criticamente; a IA pode cometer erros e você deve validar informações, citações de leis e fundamentos jurídicos.</p>
      </div>
      <div class="phi-box bad">
        <div class="tag">3. Sem Direção</div>
        <p>Saiba qual o seu objetivo final com a IA; defina se o propósito é resumir um processo, analisar contradições ou redigir um documento antes de enviar o comando.</p>
      </div>
    </div>
  </div>`
}});

// ==================== SLIDE 8: ERRO 1 ====================
slides.push({{
  id: "slide-8",
  type: "philosophy",
  hue: 355,
  theme: "Erros Comuns · 1/5",
  html: `
  <div class="slide" data-kind="philosophy">
    <div class="kicker" style="color:#ef6a6a"><span class="dot" style="background:#ef6a6a"></span>Erro 01 de 05</div>
    <h2 class="h2">Erro 1: A Persona Inflada</h2>
    <p class="lede">O excesso de adjetivos gera <b>poluição informacional</b> e reduz a performance da máquina.</p>
    <div class="phi-wrap">
      <div class="phi-compare" style="grid-template-columns:1fr">
        <div class="phi-box bad">
          <div class="tag">❌ A Armadilha</div>
          <p>"Você é o melhor jurista do universo, PhD em Harvard, com 200 anos de experiência, conhecedor de todas as leis do mundo e nunca erra."</p>
          <span style="font-size:0.85em;color:#ef6a6a;display:block;margin-top:6px"><b>O Efeito:</b> Pode causar respostas arrogantes, imprecisas ou genéricas.</span>
        </div>
        <div class="phi-box good">
          <div class="tag">✅ A Regra</div>
          <p>"Você é um promotor de justiça especializado em direito penal, com experiência em análise de inquéritos."</p>
          <span style="font-size:0.85em;color:#59d698;display:block;margin-top:6px">Seja técnico e direto. Atribua o papel exato necessário para a tarefa.</span>
        </div>
      </div>
      <div class="side-panel">
        <h4>Diretrizes</h4>
        <div class="sc">Evite superlativos desnecessários. Delimite a atuação prática com precisão.</div>
      </div>
    </div>
  </div>`
}});

// ==================== SLIDE 9: ERRO 2 ====================
slides.push({{
  id: "slide-9",
  type: "philosophy",
  hue: 355,
  theme: "Erros Comuns · 2/5",
  html: `
  <div class="slide" data-kind="philosophy">
    <div class="kicker" style="color:#ef6a6a"><span class="dot" style="background:#ef6a6a"></span>Erro 02 de 05</div>
    <h2 class="h2">Erro 2: O Prompt Genérico</h2>
    <p class="lede">Comandos sem escopo delimitado produzem respostas superficiais que resumem o óbvio.</p>
    <div class="phi-wrap">
      <div class="phi-compare" style="grid-template-columns:1fr">
        <div class="phi-box bad">
          <div class="tag">❌ O Erro</div>
          <p>"Analise este documento e me diga o que acha."</p>
          <span style="font-size:0.85em;color:#ef6a6a;display:block;margin-top:6px"><b>Sintoma:</b> Respostas que resumem o óbvio, sem utilidade tática.</span>
        </div>
        <div class="phi-box good">
          <div class="tag">✅ Correção com Escopo Jurídico</div>
          <p>"Analise criticamente esta denúncia verificando os requisitos do art. 41 do CPP e a suficiência probatória para oferecimento da ação penal."</p>
        </div>
      </div>
      <div class="side-panel">
        <h4>Por que funciona:</h4>
        <ol style="margin:0;padding-left:1.2em;color:var(--ink-dim);line-height:1.6">
          <li>Define claramente o escopo da análise.</li>
          <li>Ativa o conhecimento jurídico específico da IA (Art. 41 do CPP).</li>
          <li>Gera respostas táticas focadas.</li>
        </ol>
      </div>
    </div>
  </div>`
}});

// ==================== SLIDE 10: ERRO 3 ====================
slides.push({{
  id: "slide-10",
  type: "philosophy",
  hue: 355,
  theme: "Erros Comuns · 3/5",
  html: `
  <div class="slide" data-kind="philosophy">
    <div class="kicker" style="color:#ef6a6a"><span class="dot" style="background:#ef6a6a"></span>Erro 03 de 05</div>
    <h2 class="h2">Erro 3: Misturar Análise e Redação</h2>
    <p class="lede">Misturar a análise probatória e a escrita da peça final no mesmo comando prejudica ambas as tarefas.</p>
    <div class="phi-compare" style="grid-template-columns:1fr 1fr">
      <div class="phi-box bad">
        <div class="tag">❌ O Erro (Comando Único)</div>
        <p>"Analise este processo e já escreva a manifestação final em formato oficial do MP, com todas as formalidades, usando linguagem rebuscada e citando pelo menos 10 precedentes."</p>
      </div>
      <div class="phi-box good">
        <div class="tag">✅ Correção — Dividir em Dois Prompts</div>
        <p><b>Prompt 1 (Análise):</b> "Analise os aspectos jurídicos relevantes deste processo, identificando questões controvertidas e precedentes aplicáveis."</p>
        <p style="margin-top:8px"><b>Prompt 2 (Escrita):</b> "Com base na análise anterior, redija manifestação ministerial seguindo padrão formal do MPPA."</p>
      </div>
    </div>
  </div>`
}});

// ==================== SLIDE 11: ERRO 4 ====================
slides.push({{
  id: "slide-11",
  type: "philosophy",
  hue: 355,
  theme: "Erros Comuns · 4/5",
  html: `
  <div class="slide" data-kind="philosophy">
    <div class="kicker" style="color:#ef6a6a"><span class="dot" style="background:#ef6a6a"></span>Erro 04 de 05</div>
    <h2 class="h2">Erro 4: Comandos Negativos (Sem Contraponto)</h2>
    <p class="lede">A IA responde melhor a <b>comandos afirmativos</b>. Dê direção clara em vez de apenas limitações.</p>
    <div class="phi-compare" style="grid-template-columns:1fr 1fr">
      <div class="phi-box bad">
        <div class="tag">❌ O Bloqueio (Apenas Proibições)</div>
        <p>"Não faça texto longo. Não use palavras difíceis. Não cite doutrina desnecessária."</p>
        <span style="font-size:0.85em;color:#ef6a6a;display:block;margin-top:6px"><b>O Problema:</b> Gera confusão sobre o que fazer — a IA foca nas palavras "longo", "difíceis", "desnecessária".</span>
      </div>
      <div class="phi-box good">
        <div class="tag">✅ A Vantagem (Comando Afirmativo)</div>
        <p>"Seja conciso e objetivo. Use linguagem clara e acessível. Cite apenas jurisprudência diretamente aplicável ao caso."</p>
        <span style="font-size:0.85em;color:#59d698;display:block;margin-top:6px">Mapeia exatamente o caminho esperado.</span>
      </div>
    </div>
  </div>`
}});

// ==================== SLIDE 12: ERRO 5 ====================
slides.push({{
  id: "slide-12",
  type: "philosophy",
  hue: 355,
  theme: "Erros Comuns · 5/5",
  html: `
  <div class="slide" data-kind="philosophy">
    <div class="kicker" style="color:#ef6a6a"><span class="dot" style="background:#ef6a6a"></span>Erro 05 de 05</div>
    <h2 class="h2">Erro 5: O Princípio do Trade-off no Excesso de Instruções</h2>
    <p class="lede">Quanto mais instruções simultâneas você fornece, menor será a qualidade executada pela IA em cada instrução individual.</p>
    <div class="phi-wrap">
      <div>
        <div class="phi-box bad">
          <div class="tag">❌ O Mega-Prompt Falho</div>
          <p>Misturar 50 instruções: análise + formato + estilo + pesquisa + citações + limitações + personalização + tom + exceções num parágrafo gigante.</p>
          <span style="font-size:0.85em;color:#ef6a6a;display:block;margin-top:6px">O "Mega-Prompt" é uma ilusão — o volume de regras dilui a capacidade de processamento do modelo.</span>
        </div>
      </div>
      <div class="phi-box good">
        <div class="tag">✅ A Correção Estruturada</div>
        <ul class="phi-list" style="margin-top:0.4em">
          <li><span class="num">1</span><div>Limite-se a um máximo de <b>5 a 7 instruções principais</b>, hierarquizadas.</div></li>
          <li><span class="num">2</span><div>Foco específico garante a máxima qualidade.</div></li>
          <li><span class="num">3</span><div>Se precisar de mais, fragmente a tarefa em vários prompts consecutivos no chat.</div></li>
        </ul>
      </div>
    </div>
  </div>`
}});

// ==================== SLIDE 13: GESTÃO DO FOCO ====================
slides.push({{
  id: "slide-13",
  type: "philosophy",
  hue: 158,
  theme: "Gestão do Foco",
  html: `
  <div class="slide" data-kind="philosophy">
    <div class="kicker"><span class="dot"></span>Arquitetura Cognitiva</div>
    <h2 class="h2">O Padrão Oculto: A Gestão do Foco Cognitivo</h2>
    <p class="lede"><b>Por que esses 5 erros destroem a precisão da IA?</b> Todos compartilham uma única falha fatal: <b>o desperdício da janela de contexto.</b></p>
    <div class="agenda-grid" style="grid-template-columns:repeat(2,1fr)">
      <div class="agenda-card" style="--chue:355">
        <span class="num">01</span>
        <div class="tx"><b>Objetivos Genéricos</b><span>Não filtram os dados relevantes do processo.</span></div>
      </div>
      <div class="agenda-card" style="--chue:355">
        <span class="num">02</span>
        <div class="tx"><b>Excesso de Instruções</b><span>Dilui o poder computacional do modelo.</span></div>
      </div>
      <div class="agenda-card" style="--chue:355">
        <span class="num">03</span>
        <div class="tx"><b>Misturar Tarefas</b><span>Força a constante troca de contexto interno.</span></div>
      </div>
      <div class="agenda-card" style="--chue:355">
        <span class="num">04</span>
        <div class="tx"><b>Comandos Negativos</b><span>Forçam o processamento prévio do oposto.</span></div>
      </div>
    </div>
    <div class="example-box" style="margin-top:1.2em;border-style:solid">
      <div class="et">💡 O Insight Estratégico</div>
      <p>"A Engenharia de Prompt não é sobre escrever muito. É sobre administrar o <b>foco cognitivo da máquina</b> para economizar o seu próprio tempo."</p>
    </div>
  </div>`
}});

// ==================== SLIDE 14: FATOR HUMANO ====================
slides.push({{
  id: "slide-14",
  type: "agent",
  hue: 158,
  theme: "Validação & Riscos",
  html: `
  <div class="slide" data-kind="agent">
    <div class="kicker"><span class="dot"></span>Governança e Responsabilidade</div>
    <h2 class="h2">O Fator Humano: Limitações Técnicas Críticas</h2>
    <p class="lede">A IA rascunha, o <b>humano valida</b>. Onde focar sua revisão jurídica rígida:</p>
    <div class="agent-wrap">
      <div class="side-panel" style="border-left:5px solid #ef6a6a">
        <h4 style="color:#ef6a6a">1. O Risco da Desatualização</h4>
        <ul class="func-list">
          <li><span class="chk" style="color:#ef6a6a;background:rgba(239,106,106,.15)">!</span><div><b>NUNCA</b> confie em datas automáticas e prazos calculados.</div></li>
          <li><span class="chk" style="color:#ef6a6a;background:rgba(239,106,106,.15)">!</span><div><b>SEMPRE</b> verifique a legislação penal e processual recente.</div></li>
          <li><span class="chk" style="color:#ef6a6a;background:rgba(239,106,106,.15)">!</span><div><b>BUSQUE</b> ativamente precedentes posteriores ao treinamento do modelo.</div></li>
        </ul>
      </div>
      <div class="side-panel" style="border-left:5px solid #ef6a6a">
        <h4 style="color:#ef6a6a">2. O Risco da Alucinação</h4>
        <ul class="func-list">
          <li><span class="chk" style="color:#ef6a6a;background:rgba(239,106,106,.15)">!</span><div><b>CONFIRME</b> todas as citações de leis e artigos do CP/CPP.</div></li>
          <li><span class="chk" style="color:#ef6a6a;background:rgba(239,106,106,.15)">!</span><div><b>VALIDE</b> a real existência de precedentes mencionados.</div></li>
          <li><span class="chk" style="color:#ef6a6a;background:rgba(239,106,106,.15)">!</span><div><b>CHEQUE</b> duplamente cálculos e prazos legais gerados.</div></li>
        </ul>
      </div>
    </div>
  </div>`
}});

// ==================== SLIDE 15: SÍNTESE ESTRATÉGICA ====================
slides.push({{
  id: "slide-15",
  type: "philosophy",
  hue: 215,
  theme: "Síntese Estratégica",
  html: `
  <div class="slide" data-kind="philosophy">
    <div class="kicker"><span class="dot"></span>Checklist Final</div>
    <h2 class="h2">A Partitura Perfeita: Síntese Estratégica</h2>
    <p class="lede">Resumo executivo das diretrizes técnicas de Engenharia de Prompts.</p>
    <div class="phi-wrap">
      <div>
        <ul class="func-list">
          <li><span class="chk">✓</span><div><b>Fórmula Mestra:</b> Persona → Contexto → Instrução → Formato.</div></li>
          <li><span class="chk">✓</span><div><b>Refinamento em Etapas:</b> O maestro não ajusta tudo de uma vez.</div></li>
          <li><span class="chk">✓</span><div><b>Metaprompting:</b> Peça ajuda à própria IA para construir o prompt.</div></li>
          <li><span class="chk">✓</span><div><b>Desacoplamento:</b> Divida a análise profunda da redação final.</div></li>
          <li><span class="chk">✓</span><div><b>Linguagem Afirmativa:</b> Use comandos diretos e afirmativos.</div></li>
          <li><span class="chk">✓</span><div><b>Curadoria Humana:</b> Valide rigidamente leis, prazos e precedentes.</div></li>
        </ul>
      </div>
      <div class="side-panel" style="text-align:center">
        <h4>Portal de Inovação do MPPA</h4>
        <p style="color:var(--ink-dim);margin:0.8em 0">Acesse repositórios e materiais institucionais:</p>
        <a href="https://ciia.mppa.mp.br" target="_blank" class="pill" style="font-size:1.1rem;padding:0.6em 1.4em;text-decoration:none">ciia.mppa.mp.br</a>
      </div>
    </div>
  </div>`
}});

// ==================== SLIDE 16: OBSERVAÇÃO & ADAPTAÇÃO ====================
slides.push({{
  id: "slide-16",
  type: "closing",
  hue: 215,
  theme: "A Regência Final",
  html: `
  <div class="slide closing" data-kind="closing">
    <div class="kicker"><span class="dot"></span>Maturidade Prática</div>
    <h1 class="h1">Observação e <span class="accent">Adaptação</span></h1>
    <p class="lede">Utilize a IA a seu favor. O verdadeiro domínio não vem de decorar prompts, mas de <b>analisar o comportamento do modelo</b>.</p>
    <div class="closing-stats">
      <div><b>1</b><span>Observe padrões de resposta em diferentes cenários jurídicos</span></div>
      <div><b>2</b><span>Ajuste suas instruções em tempo real</span></div>
      <div><b>3</b><span>Implemente com validação em casos reais</span></div>
    </div>
    <div style="margin-top:1.5em;padding:1.2em 2em;background:var(--accent-soft);border:1px solid var(--accent-line);border-radius:20px;display:inline-block">
      <span style="font-size:var(--fs-h2);font-weight:800;color:var(--orange-ink);font-style:italic">"O maestro da orquestra é sempre você."</span>
    </div>
  </div>`
}});

// ==================== SLIDE 17: ENCERRAMENTO ====================
slides.push({{
  id: "slide-17",
  type: "cover",
  hue: 28,
  theme: "Encerramento",
  html: `{slide17_html}`
}});
"""

    # 3. Construir função JS do Menu (`buildMenu`) sem a palavra "Slide X" e apenas com número circular mnum
    new_build_menu = """function buildMenu(){
  let html='';
  let order=1;
  const item = (index, label) => `<div class="mitem" data-i="${index}" style="display:flex;align-items:center;gap:12px;padding:0.7em 0.9em"><span class="mnum" style="flex:none;width:28px;height:28px;border-radius:50%;background:var(--accent-soft);border:1px solid var(--accent-line);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:0.85rem;font-weight:800">${order++}</span><b style="font-weight:600;color:var(--ink);line-height:1.35">${label}</b></div>`;

  html += `<div class="mgroup"><div class="mgroup-h" style="--chue:28"><span class="d"></span>Fundamentos & Estrutura</div><div class="mitems">
    ${item(0, 'Engenharia de Prompts aplicada ao Tribunal do Júri')}
    ${item(1, 'Sumário Executivo & Agenda da Apresentação')}
    ${item(2, 'O que é Engenharia de Prompts?')}
    ${item(3, 'Os 4 Pilares de um Bom Prompt')}
  </div></div>`;

  html += `<div class="mgroup"><div class="mgroup-h" style="--chue:196"><span class="d"></span>Técnicas Avançadas & Maturidade</div><div class="mitems">
    ${item(4, 'Metaprompting: Use a IA para Desenhar seus Comandos')}
    ${item(5, 'A Evolução do Usuário: De Respostas Rápidas a Raciocínio Complexo')}
  </div></div>`;

  html += `<div class="mgroup"><div class="mgroup-h" style="--chue:355"><span class="d"></span>Antipadrões & Os 5 Erros Críticos</div><div class="mitems">
    ${item(6, 'Como NÃO Usar a IA')}
    ${item(7, 'Erro 1: A Persona Inflada')}
    ${item(8, 'Erro 2: O Prompt Genérico')}
    ${item(9, 'Erro 3: Misturar Análise e Redação')}
    ${item(10, 'Erro 4: Comandos Negativos (Sem Contraponto)')}
    ${item(11, 'Erro 5: O Princípio do Trade-off no Excesso de Instruções')}
  </div></div>`;

  html += `<div class="mgroup"><div class="mgroup-h" style="--chue:158"><span class="d"></span>Foco Cognitivo, Riscos & Síntese</div><div class="mitems">
    ${item(12, 'O Padrão Oculto: A Gestão do Foco Cognitivo')}
    ${item(13, 'O Fator Humano: Limitações Técnicas Críticas')}
    ${item(14, 'A Partitura Perfeita: Síntese Estratégica')}
    ${item(15, 'Observação e Adaptação: O Maestro da Orquestra')}
    ${item(16, 'Encerramento da Apresentação · MPPA')}
  </div></div>`;

  menuBody.innerHTML=html;
  menuBody.querySelectorAll('.mitem').forEach(it=>{
    it.addEventListener('click',()=>{ goTo(parseInt(it.dataset.i,10)); closeOverlays(); });
  });
}
"""

    # Extrair Partes do Template HTML Original
    slides_pos = template.find('const slides = [];')
    nav_pos = template.find('/* ============================= RENDER / NAV ============================= */')

    part1 = template[:slides_pos]
    part3 = template[nav_pos:]

    # Atualizar título da página no HTML Head
    part1 = part1.replace(
        '<title>IA Aplicada à Tutela do Patrimônio Público · MPPA</title>',
        '<title>Engenharia de Prompts aplicada ao Tribunal do Júri · MPPA</title>'
    )

    # Substituir buildMenu no Part 3
    old_build_menu_start = part3.find('function buildMenu()')
    old_build_menu_end = part3.find('function openMenu()')

    if old_build_menu_start != -1 and old_build_menu_end != -1:
        part3 = part3[:old_build_menu_start] + new_build_menu + "\n" + part3[old_build_menu_end:]

    # Adicionar a chamada inicial obrigatória de buildMenu() no final do script para popular o overlay
    build_menu_call_pos = part3.rfind('goTo(0);')
    if build_menu_call_pos != -1:
        part3 = part3[:build_menu_call_pos] + "buildMenu();\n" + part3[build_menu_call_pos:]

    # Montar HTML completo
    full_html = part1 + slides_js + "\n\n" + part3

    # Escrever no arquivo final
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(full_html)

    print("==========================================================")
    print("✅ Apresentação gerada com animação nos textos de Slide 2!")
    print(f"📄 Arquivo: {OUTPUT_FILE}")
    print(f"📦 Tamanho total: {len(full_html)} bytes")
    print("==========================================================")

if __name__ == '__main__':
    main()
