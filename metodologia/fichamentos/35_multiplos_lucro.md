# Fichamento 35: Múltiplos de lucro: P/L, PEG, EV/EBITDA, polêmica do caixa no EV

**Fontes**
- **[D]** Damodaran (2002), Cap. 18 "Earnings Multiples" (PDF p. 659–717): definições de P/L (p. 659); distribuição (p. 660–661); determinantes e exemplos (p. 662–669); P/L do mercado no tempo e entre países (p. 670–680); regressões (p. 680–684); normalização do lucro (p. 684); PEG (p. 685–690); EV/EBITDA: motivos, caixa no EV, participações cruzadas, determinantes (p. 704–708); resumo (p. 714).
- **[P]** Póvoa (2012), Cap. 9: P/L e fatores que o distorcem (p. 313–315); P/L justo (p. 315–318); limites das regressões de P/L (p. 319); PEG (p. 319–321); EV/EBITDA: prestígio, mitos, a polêmica do caixa no EV, distribuição no Brasil e EV/EBITDA justo (p. 321–329).

---

## 1. Conceito central

O **P/L** é o múltiplo do acionista: depende de payout, crescimento e Ke ([D] p. 662–663; [P] p. 315). O **PEG** (P/L ÷ crescimento) tenta controlar o crescimento, mas não controla risco nem payout ([D] p. 685–690; [P] p. 319–321). O **EV/EBITDA** é o múltiplo da firma: não sofre com a alavancagem nem com métodos de depreciação, tem menos empresas com denominador negativo e é útil em setores de infraestrutura ([D] p. 704). Seus determinantes são alíquota, peso de D&A, reinvestimento, WACC e crescimento ([D] p. 707–708). Os autores **divergem sobre o caixa no EV**: Damodaran o desconta; Póvoa defende não descontar.

## 2. Fórmulas

- **P/L de uma empresa estável** ([D] p. 662): `P/L = payout × (1 + g)/(Ke − g)`.
- **PEG** ([D] p. 685): `PEG = P/L ÷ g esperado (em %)`. Exemplo de [D]: P/L 20 e g 10% → PEG 2.
- **EV/EBITDA** ([D] p. 704, 707):
  - `EV = valor de mercado do equity + dívida − caixa`
  - `EV/EBITDA = [(1 − t) − (D&A/EBITDA) × (1 − t) − reinvestimento/EBITDA]/(WACC − g)` (empresa estável).
- **Distribuição**: média de 11,7 e mediana ≈ 8 nos EUA em janeiro de 2001 ([D] p. 708); mediana de 8,0 no Brasil em 2012 ([P] p. 325–326).
- **Participações** ([D] p. 704–706): minoritária passiva → subtrair seu valor do numerador (ou somar a parte do EBITDA dela); majoritária consolidada → subtrair a parte dos não controladores do numerador e o EBITDA inteiro da controlada do denominador.

## 3. Premissas e escolhas dos autores

- **Distorções do P/L** ([P] p. 313–315): diferenças de depreciação, provisões, alíquotas e o tratamento de P&D e marketing (empresas que investem mais parecem "caras"; solução: expurgar ou ajustar o crescimento).
- **PEG** ([D] p. 685–687):
  - use o g do **mesmo período** e da mesma base para todas as empresas;
  - **não use o P/L projetado** com o g que inclui o próximo ano, porque **conta o crescimento duas vezes**;
  - empresas sem estimativa de g saem da amostra (113 de 448 em [D]), um viés;
  - o PEG **não é neutro ao crescimento**: o PEG justo cai quando g sobe muito, e varia com risco e payout ([D] p. 688–690).
  - [P] (p. 319–321): só faz sentido com crescimento **futuro**; útil apenas como **screening**, pela dificuldade de definir um PEG justo.
- **EV/EBITDA não é fluxo de caixa** ([P] p. 322): ignora impostos, capex e capital de giro. Tratar o EBITDA como caixa é um "mito".
- **A polêmica do caixa** ([P] p. 323–325 × [D] p. 704):
  - **[D]**: desconta o caixa do EV porque a receita financeira dele **não** está no EBITDA. Somar o ativo sem somar sua renda superestima o múltiplo.
  - **[P]**: o caixa "já está no valor de mercado". Usar a dívida líquida no EV o "elimina indevidamente". No exemplo de uma empresa recém-aberta com R$ 100 mi em caixa, o EV pela dívida líquida dá **zero**, o que ele considera absurdo. Recomenda EV = valor de mercado + dívida **bruta** e somar a receita financeira ao denominador.
  - **Avaliação deste fichamento**: as duas convenções são consistentes **desde que** numerador e denominador andem juntos (sem caixa e sem receita financeira, ou com os dois). No exemplo de [P], EV = 0 é justamente o valor dos **ativos operacionais**, que ainda não existem: todo o valor é caixa. A convenção de [D] é a usada pelo mercado e pelos provedores de dados; misturar convenções entre empresas é o erro real.
- **Mercado no tempo** ([D] p. 670–671): o P/L do mercado varia com juros, inflação e prêmio de risco; comparar com a média histórica sem esses ajustes é enganoso.

## 4. Passo a passo prático

1. **P/L projetado (12 meses)** com lucro normalizado (tema 07), contra a mediana dos pares e contra o P/L justo (tema 34).
2. **EV/EBITDA projetado**, com EV = equity + dívida bruta + arrendamentos (se no padrão IFRS 16) + minoritários − caixa − participações não consolidadas.
3. Confira a coerência do EBITDA: com ou sem IFRS 16, sem não recorrentes, sem equivalência patrimonial.
4. Para empresas com muito capex ou alíquotas diferentes, olhe também **EV/EBIT** ou **EV/(EBITDA − capex)**.
5. PEG só como filtro, com o mesmo horizonte de g para todos.

## 5. Erros comuns apontados pelos autores

- **PEG com P/L projetado** (contagem dupla) ([D] p. 686).
- **EBITDA como caixa** ([P] p. 322).
- **Ignorar participações cruzadas** no EV/EBITDA ([D] p. 704–706).
- **Misturar convenções de caixa** entre empresas ([D] p. 704; [P] p. 325).
- **Comparar o P/L de hoje com a média histórica** sem ajustar juros e inflação ([D] p. 670–671).

## 6. Onde concordam e onde divergem

**Concordam**: P/L depende de payout, g e Ke; PEG é imperfeito; EBITDA não é caixa; múltiplos devem ser comparados ao justo.

| Ponto | Damodaran | Póvoa |
|---|---|---|
| **Caixa no EV** | **Subtrai** o caixa | **Não subtrai**; soma a receita financeira ao EBITDA |
| PEG | Analisa a fundo os vieses e a relação com g | Só como screening |
| EV/EBITDA justo | Fórmula geral com reinvestimento | Exemplo numérico de dois estágios |
| Participações | Ajuste detalhado (Segovia) | Não trata aqui |

## 7. Limites: o que está defasado ou é específico do Brasil

- O IFRS 16 eleva o EBITDA (sai o aluguel) e a dívida (entra o arrendamento). Múltiplos pré e pós-2019 não são comparáveis sem ajuste.
- No Brasil, o EBITDA "ajustado" divulgado pelas empresas varia muito (e a CVM exige reconciliação com o EBITDA padrão, Resolução CVM 156/2022 **[NÃO VERIFICADO aqui]**).
- JCP reduz o IR, o que eleva o lucro líquido em relação a pares sem JCP (tema 22).

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. **Convenção do canal**: EV = equity + dívida bruta + arrendamentos (IFRS 16) + minoritários − caixa e aplicações − participações não consolidadas; EBITDA sem receita financeira e sem equivalência. É a convenção de [D] e do mercado; registrar a divergência de [P] como nota.
2. Mostrar P/L **e** EV/EBITDA, com o justo implícito do DCF.
3. Não usar PEG como critério, só como filtro.

## 9. Dúvidas abertas para você decidir

1. Confirmar a convenção de caixa no EV (sugerida: subtrair, como [D]).
2. EBITDA com ou sem IFRS 16 nos múltiplos do canal?
3. Acrescentar EV/EBIT por padrão?
