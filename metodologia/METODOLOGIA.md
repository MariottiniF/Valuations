# Metodologia de valuation do canal

Guia único e sequencial para montar uma valuation, do começo ao fim. Cada etapa diz **o que fazer**, **com que regra** (puxando de [`DECISOES.md`](DECISOES.md)) e **onde buscar os dados** (puxando de [`FONTES_DADOS.md`](FONTES_DADOS.md)). A justificativa teórica de cada escolha está nos [fichamentos](fichamentos/README.md) — aqui não se repete a teoria, só se aplica.

**Como usar**: quando a empresa for decidida, basta pedir "faça o valuation de [empresa]" (ver o prompt-modelo na seção 9). O Claude segue as etapas abaixo, nesta ordem, com o passo 1 sempre vindo primeiro, porque fixa a moeda e a região de toda a valuation.

---

## 1. WACC: montagem e explicação

É o primeiro passo porque decide a moeda, a região e todos os insumos que vêm depois.

### 1.1 Identificar a empresa
- Moeda das demonstrações financeiras e país sede.
- Isso decide qual bloco do [`PROCEDIMENTO_WACC.md`](PROCEDIMENTO_WACC.md) se aplica: Brasil (R$), EUA (US$) ou Europa (€/£/CHF).

### 1.2 Buscar os parâmetros (conforme `FONTES_DADOS.md`)
- Se o cenário macro do trimestre já existe em [`MACRO.md`](MACRO.md) e está atualizado (≤ 3 meses), **reutilizar** os números dele.
- Senão, atualizar o `MACRO.md` antes de seguir (busca de NTN-B/Treasury/Bund, IPCA/PIB ou equivalente, prêmio de risco).
- Buscar os dados **específicos da empresa**: beta do setor na região certa (Damodaran), rating ou cobertura de juros para o rating sintético, estrutura de capital atual (dívida a mercado quando houver título negociado), segmentação geográfica de receita (se houver exposição internacional relevante).

### 1.3 Montar cada peça, com a explicação ao lado
1. **Rf** — regra D4. Mostrar o número, a fonte e a data.
2. **Beta** — bottom-up (tema 20): βu do setor/amostra, realavancado com o D/E e a alíquota da própria empresa. Mostrar a amostra usada e por quê.
3. **ERP** — regra D5. Brasil: prêmio implícito do Ibovespa (mostrar a memória de cálculo). EUA/Europa: ERP maduro + CRP ponderado por receita.
4. **Ke = Rf + β × ERP.**
5. **Kd** — dívida a mercado (título líquido) ou rating/rating sintético + spread. Alíquota marginal (D34% no Brasil; tabela Damodaran fora).
6. **Estrutura de capital** — pesos a mercado; dívida incluindo arrendamentos (D2); caixa fora (D1).
7. **WACC único** (D11): um só WACC para todo o período explícito e para a perpetuidade, sem *rolling WACC*. Pesos conforme o critério de **D12** (padrão: atuais a mercado; exceções para desalavancagem/alavancagem concreta e para estrutura incerta); Rf da **NTN-B mais longa** (D4); ERP de **longo prazo** (D5).
8. **Checagem de sanidade**: comparar com o WACC médio do setor (Damodaran, fora do Brasil; pares locais, no Brasil). Divergência > 1,5 p.p. exige explicação.

### 1.4 Saída desta etapa
Uma tabela única: Rf, β, ERP, Ke, Kd(1−t), pesos e WACC (único) — cada linha com fonte e data — mais um parágrafo explicando as escolhas (por que esse beta, por que esse Kd) para entrar no material do vídeo.

---

## 2. Análise setorial

### 2.1 Delimitar o setor e o ciclo
- Em que segmento a empresa compete; quem são os pares diretos (nacionais e, se necessário, globais — tema 20).
- O setor é cíclico ou de commodity? Se for, isso já aciona o tema 45/decisão D8 nas etapas seguintes.

### 2.2 Estrutura competitiva
- Barreiras de entrada, poder de precificação, intensidade de capital, regulação.
- Isso alimenta a justificativa de qualquer ROIC acima do WACC na perpetuidade (D3a) e a leitura de margens (tema 06).

### 2.3 Benchmarking de pares
- Montar a tabela de pares: margem, ROIC, crescimento histórico, endividamento, múltiplos atuais (EV/EBITDA, P/L, P/VP) — vai alimentar a checagem de múltiplos da etapa 6.

---

## 3. Fundamentos e contabilidade da empresa

### 3.1 Levantar as demonstrações
- 5 a 10 anos de BP, DRE e DFC (CVM/10-K, conforme a região).
- Se setor cíclico ou de commodity: janela maior (10 anos ou um ciclo completo, D8).

### 3.2 Reclassificar e normalizar (temas 04, 06, 07)
- Separar operacional × financeiro × não operacional.
- Ajustar itens não recorrentes (taxonomia dos 4 tipos, tema 07).
- Decidir arrendamentos conforme D2 (e a seção 4 do `PROCEDIMENTO_WACC.md`, se for US GAAP).
- Capitalizar P&D/marketing se relevante (tema 07/41), com a vida amortizável documentada.
- Checklist "uma vez só" no balanço (C2).

### 3.3 Calcular os indicadores históricos (tema 06, 16)
- Margem, giro, ROIC, ROE, ciclo de caixa, estrutura de capital, cobertura de juros — 5 a 10 anos, com a decomposição margem × giro.
- Sinais de alerta do lucro (checklist de Damodaran, C2).

---

## 4. Fluxo de caixa projetado

### 4.1 Escolher o modelo (tema 02, 11)
- Padrão: **FCFF a WACC**. FCFE só como checagem, exceto para financeiras (tema 44, DDM/FCFE direto).

### 4.2 Receita e margem
- Projetar receita por driver do negócio (volume × preço, ou receita/capital).
- Margem convergindo para a sustentável do setor (normalizada se cíclica, D8).

### 4.3 Reinvestimento (temas 05, 09, 10)
- Capex, ΔNCG (sem caixa, sem dívida de CP; regra do "uma vez só") e intangíveis.
- **Reinvestimento = g/ROIC** em toda fase (C2) — nunca projetar capex e crescimento de forma independente.

### 4.4 Estágios (tema 13, 14)
- Definir o número de estágios e a duração de cada um, conforme a maturidade e a vantagem competitiva (ligação com D3a).
- Todos os anos descontados pelo **mesmo WACC** da etapa 1 (D11). A fase de transição converge crescimento, margem e ROIC aos parâmetros de perpetuidade, **nunca** a taxa de desconto.

### 4.5 Casos especiais (acionar se aplicável)
- Prejuízo, cíclica, start-up → tema 45.
- Financeira → tema 44.
- Risco relevante de falência → tema 45 (cenário de liquidação ponderado pela probabilidade).

---

## 5. Valor terminal e perpetuidade

- **ROIC = WACC** na perpetuidade, salvo caso especial justificado por escrito (D3a).
- **g = LTG**, na moeda da valuation, com g ≤ Rf dessa moeda (seção 5 do `PROCEDIMENTO_WACC.md`).
- ΔNCG ≥ 0 na perpetuidade (C2).
- O valor terminal usa o mesmo WACC do explícito (D11), tanto no denominador `(WACC − g)` quanto no desconto a valor presente: `VT / (1 + WACC)^n`. Com ROIC = WACC, `VT = NOPAT(n+1) / WACC`.

---

## 6. Checagem por múltiplos

- Extrair do DCF os múltiplos **implícitos** no preço justo (EV/EBITDA, P/L, P/VP) do ano 1.
- Comparar com a **mediana dos pares** (tabela da etapa 2.3), nunca com a média (tema 33).
- **Proibida** qualquer média ponderada entre DCF, múltiplos e EVA (D9) — a tabela é só diagnóstico.
- Se o implícito divergir muito da mediana, explicar a razão fundamentalista (crescimento, risco, margem) na etapa 8, não ajustar o número "para bater".

---

## 7. Sensibilidade e cenários

- Variáveis obrigatórias: WACC (±1 a 2 p.p.), g perpétuo, margem/ROIC de longo prazo.
- Setor cíclico/commodity: sensibilidade ao preço normalizado da commodity (D8) é obrigatória.
- Exposição cambial relevante: sensibilidade ao câmbio (tema 38).
- Preço justo vs. preço de mercado: se divergir mais de 30%, exigir a "tese de por que o mercado erra" (C3).

---

## 8. Relatório final (material do vídeo)

Checklist do que não pode faltar:
- [ ] Tabela de WACC com fontes e datas (etapa 1.4).
- [ ] Tabela de pares e indicadores (etapa 2.3, 3.3).
- [ ] Premissas de receita, margem e reinvestimento, por estágio.
- [ ] Preço justo, com a ponte EV → equity (caixa somado conforme D1).
- [ ] Múltiplos implícitos × pares (etapa 6).
- [ ] Sensibilidade (etapa 7).
- [ ] Se preço justo ≠ preço de mercado por > 30%: a tese de divergência (C3).
- [ ] Bloco "Fontes de dados" com todos os valores externos usados, fonte e data.
- [ ] Dúvidas/limitações relevantes do caso (defasagem de dado, premissa incerta), sinalizadas, não escondidas.

---

## 9. Prompt-modelo para iniciar um valuation

Quando a empresa estiver decidida, use algo como:

> "Faça o valuation de **[empresa/ticker]** seguindo `metodologia/METODOLOGIA.md` e as decisões de `metodologia/DECISOES.md`. Busque os dados conforme `metodologia/FONTES_DADOS.md`, começando pelo WACC (etapa 1), depois a análise setorial, os fundamentos e a contabilidade da empresa, o fluxo de caixa projetado, o valor terminal, a checagem por múltiplos e a sensibilidade, nessa ordem. Me avise se algum dado não puder ser confirmado em fonte confiável."

Ajustes possíveis no pedido:
- Pedir para parar depois de alguma etapa específica (por exemplo, só o WACC) antes de seguir.
- Indicar se já tem as demonstrações financeiras anexadas, ou se é para buscar.
- Avisar se é um caso especial conhecido de antemão (banco, empresa com prejuízo, cíclica, estrangeira).
