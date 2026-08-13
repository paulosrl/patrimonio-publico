# Engenharia de Prompts aplicada ao Tribunal do Júri
### Rascunho de 16 slides (apenas texto, sem elementos gráficos) — para revisão

---

## Slide 1 — Engenharia de Prompts aplicada ao Ministério Público

- **Evento:** 14 e 15 de maio de 2025
- Material produzido com apoio de ferramentas de Inteligência Artificial
- **Autores:** Rodrigo Aquino e Paulo Lima
- **CIIA — Comitê de Governança de Inovação e Inteligência Artificial**
- ciia.mppa.mp.br
- Ministério Público do Estado do Pará (MPPA)

---

## Slide 2 — O que é Engenharia de Prompts?

**Teoria**
- A Engenharia de Prompt é o processo interativo de desenvolver e refinar instruções para obter os resultados mais precisos e relevantes dos modelos de IA Generativa.
- Analogia: é como ser o **maestro de uma orquestra**, ajustando cada instrumento até alcançar a harmonia perfeita.

**Prática**
- **Pedido inicial:** "Resuma este inquérito policial."
- **Refinamento (ajustando os instrumentos):** "Agora, foque este resumo apenas nas provas que apontam as qualificadoras do homicídio."

---

## Slide 3 — Os 4 Pilares de um Bom Prompt

Para que a IA compreenda exatamente o que você precisa, o comando deve conter 4 elementos estruturais:

- **Persona** — Quem a IA deve simular.
  *Ex.: "Atue como Promotor de Justiça com experiência no Tribunal do Júri."*
- **Contexto** — Fatos essenciais.
  *Ex.: "Analise os depoimentos em anexo do Inquérito Policial."*
- **Instrução** — O que deve ser feito.
  *Ex.: "Identifique as contradições entre as testemunhas e destaque pontos da acusação."*
- **Formato** — Como entregar a resposta.
  *Ex.: "Apresente o resultado em uma lista com marcadores."*

---

## Slide 4 — Metaprompting: Use a IA para Desenhar seus Próprios Comandos

**O Espelho do Metaprompting**
- A IA pode atuar como sua assistente na própria construção das instruções que ela mesma vai executar.

**Exemplo:**
> "Quero analisar um processo de feminicídio com 400 páginas. Me ajude a criar o melhor prompt possível para que você identifique as provas de autoria e materialidade neste caso."

---

## Slide 5 — A Evolução do Usuário: De Respostas Rápidas a Raciocínio Complexo

Eixo: **Tempo / Experiência**

- **Iniciantes:** perguntas simples
  *Ex.: "Resuma os depoimentos das testemunhas."*
- **Intermediários:** refinar o raciocínio
  *Ex.: aprofundamento sobre os depoimentos já resumidos.*
- **Avançados:** novas perguntas / raciocínio complexo
  *Ex.: "Com base nestes laudos periciais, quais teses defensivas o advogado do réu provavelmente utilizará? Faça perguntas para eu desconstruir essas teses."*

---

## Slide 6 — Como Não Usar a IA

- **Sem Hipótese** — Saiba exatamente o que você está procurando antes de iniciar a interação; não use a IA de forma aleatória ou sem uma pergunta de pesquisa definida.
- **Sem Curadoria** — Saiba como analisar as respostas criticamente; a IA pode cometer erros e você deve validar informações, citações de leis e fundamentos jurídicos.
- **Sem Direção** — Saiba qual o seu objetivo final com a IA; defina se o propósito é resumir um processo, analisar contradições ou redigir um documento antes de enviar o comando.

---

## Slide 7 — Erro 1: A Persona Inflada

- O excesso de adjetivos gera **poluição informacional** e reduz a performance.

**❌ A Armadilha**
> "Você é o melhor jurista do universo, PhD em Harvard, com 200 anos de experiência, conhecedor de todas as leis do mundo e nunca erra."

- **O Efeito:** pode causar respostas arrogantes, imprecisas ou genéricas.

**✅ A Regra**
> "Você é um promotor de justiça especializado em direito penal, com experiência em análise de inquéritos."
- Seja técnico e direto. Atribua o papel exato necessário para a tarefa.

---

## Slide 8 — Erro 2: O Prompt Genérico

**❌ O Erro**
> "Analise este documento e me diga o que acha."
- **Sintoma:** respostas que resumem o óbvio, sem utilidade tática.

**✅ Correção**
> "Analise criticamente esta denúncia verificando os requisitos do art. 41 do CPP e a suficiência probatória para oferecimento da ação penal."

**Por que funciona:**
1. Define claramente o escopo da análise.
2. Ativa o conhecimento jurídico específico da IA (Art. 41 do CPP).
3. Gera respostas táticas focadas.

---

## Slide 9 — Erro 3: Misturar Análise e Redação

**❌ O Erro**
> "Analise este processo e já escreva a manifestação final em formato oficial do MP, com todas as formalidades, usando linguagem rebuscada e citando pelo menos 10 precedentes."
- Misturar essas duas funções prejudica ambas.

**✅ Correção — dividir em dois prompts:**
- **Prompt 1 (Análise):** "Analise os aspectos jurídicos relevantes deste processo, identificando questões controvertidas e precedentes aplicáveis."
- **Prompt 2 (Escrita):** "Com base na análise anterior, redija manifestação ministerial seguindo padrão formal do MPPA."

---

## Slide 10 — Erro 4: Comandos Negativos (Sem Contraponto)

- A IA responde melhor a **comandos afirmativos**. Dê direção clara em vez de apenas limitações.

**❌ O Bloqueio**
> "Não faça texto longo. Não use palavras difíceis. Não cite doutrina desnecessária."
- **O Problema:** gera confusão sobre o que efetivamente fazer — a IA foca nas palavras "longo", "difíceis", "desnecessária".

**✅ A Vantagem**
> "Seja conciso e objetivo. Use linguagem clara e acessível. Cite apenas jurisprudência diretamente aplicável ao caso."
- Mapeia exatamente o caminho esperado.

---

## Slide 11 — Erro 5: O Princípio do Trade-off no Excesso de Instruções

- **O Princípio:** quanto mais instruções simultâneas você fornece, menor será a qualidade executada pela IA em cada instrução individual.

- **O Erro:** parágrafos gigantes com dezenas de regras de formatação, pesquisa e estilo simultâneas.

**O Mega-Prompt Falho**
- Misturar 50 instruções: análise + formato + estilo + pesquisa + citações + limitações + personalização + tom + exceções.
- O "Mega-Prompt" é uma ilusão — o volume de regras dilui a capacidade de processamento do modelo.

**✅ A Correção**
- Limite-se a um máximo de **5 a 7 instruções principais**, hierarquizadas.
- Foco específico garante a máxima qualidade.
- Se precisar de mais, fragmente a tarefa em vários prompts consecutivos no chat.

---

## Slide 12 — O Padrão Oculto: A Gestão do Foco Cognitivo

**Por que esses 5 erros destroem a precisão da IA?**
Eles compartilham uma única falha fatal: **o desperdício da janela de contexto.**

- Objetivos genéricos não filtram os dados.
- Excesso de instruções dilui o poder computacional.
- Misturar tarefas força a "troca de contexto".
- Comandos negativos forçam o processamento do oposto.

**O Insight:** A Engenharia de Prompt não é sobre escrever muito. É sobre administrar o **foco cognitivo da máquina** para economizar o seu próprio tempo.

---

## Slide 13 — O Fator Humano: Limitações Técnicas Críticas

- A IA rascunha, o **humano valida**. Onde focar sua revisão:

**1. O Risco da Desatualização**
- NUNCA confie em datas automáticas.
- SEMPRE verifique legislação recente.
- BUSQUE ativamente precedentes posteriores ao treinamento do modelo.

**2. O Risco da Alucinação**
- CONFIRME todas as citações de leis e artigos.
- VALIDE a real existência de precedentes mencionados.
- CHEQUE duplamente cálculos e prazos legais gerados.

---

## Slide 14 — A Partitura Perfeita: Síntese Estratégica

- **Persona → Contexto → Instrução → Formato**
- Refine em etapas (o maestro não ajusta tudo de uma vez).
- Peça ajuda à própria IA (**Metaprompting**).
- Divida análise profunda da redação final.
- Use linguagem afirmativa e direta.
- Valide rigidamente leis, prazos e precedentes.

- Acesse nosso site: **ciia.mppa.mp.br**

---

## Slide 15 — Observação e Adaptação

- Utilize a IA a seu favor. O verdadeiro domínio não vem de decorar prompts, mas de **analisar o comportamento do modelo**.
- Observe padrões de resposta em diferentes cenários jurídicos.
- Ajuste suas instruções em tempo real.
- Implemente em casos reais.
- Saiba qual o seu objetivo. Saiba como analisar as respostas.

> "O maestro da orquestra é sempre você."

---

## Slide 16 — Inteligência Artificial aplicada ao Tribunal do Júri

- Ministério Público do Estado do Pará (MPPA)
- Encerramento da apresentação

**Obrigado.**
