# Fichamento 39: Dividendos: o "mito dos dividendos" e o DDM

**Fontes**
- **[D]** Damodaran (2002), Cap. 13 "Dividend Discount Models" (PDF p. 450–486): modelo geral (p. 450); Gordon e limitações (p. 451–456); dois estágios (p. 457–460); modelos H e de três estágios e testes do modelo (p. 461–482, **apenas mapeados**); resumo (p. 483).
- **[P]** Póvoa (2012), Cap. 10, "O mito dos dividendos na valuation" (p. 410–420): dividendos como proxy de caixa, sinalização (p. 410–411); Miller & Modigliani (p. 412–413); empresas maduras e dividend yield no Brasil (p. 414–416); dividendos × recompra (p. 417–419).

---

## 1. Conceito central

Para o acionista de uma empresa aberta, o único fluxo direto são os **dividendos esperados**. O DDM é o VP desses dividendos ([D] p. 450, 483). Damodaran o considera conservador mas "surpreendentemente adaptável" ([D] p. 483). Póvoa chama de **mito** a ideia de que o dividendo é o melhor proxy do fluxo do acionista: a política de dividendos é decisão da gestão, pode sinalizar coisas e pode não refletir a geração de caixa (FCFE) ([P] p. 410–411). Pela teoria de M&M, com mercados perfeitos, a política de dividendos é **irrelevante** para o valor, que depende da política de **investimento** ([P] p. 412–413). O que importa é o FCFE, não a forma de distribuí-lo.

## 2. Fórmulas

- **Modelo geral** ([D] p. 450): `P0 = Σ DPS_t/(1 + Ke)^t`.
- **Gordon** ([D] p. 451): `P0 = DPS1/(Ke − g)`, com g estável.
- **Crescimento fundamental** ([D] p. 454, 458): `g = (1 − payout) × ROE`.
- **Dois estágios** ([D] p. 457–458): VP dos dividendos da fase de alto crescimento + `P_n = DPS_{n+1}/(Ke − g_n)` trazido a VP. O payout estável deve ser **coerente**: `payout_n = 1 − g_n/ROE_n`.
- **g implícito** ([D] p. 455): inverter Gordon a partir do preço atual.
- **Dividend yield** ([P] p. 414): `dividendo por ação/preço`.

## 3. Premissas e escolhas dos autores

- **Limitações do Gordon** ([D] p. 452): extremamente sensível a g próximo de Ke; adequado a empresas que crescem perto da economia e pagam dividendos coerentes com o FCFE.
- **Quando usar o DDM** ([D] p. 456–460): empresas que pagam o que podem (payout ≈ FCFE), bancos e financeiras (tema 44), situações em que o FCFE é difícil de estimar.
- **Por que o DDM pode subavaliar** (resumo de [D] p. 483): empresas que retêm caixa ou recompram ações têm dividendos menores que o FCFE. Ele "acha" cada vez menos ações baratas em mercados em alta, o que [D] vê também como virtude.
- **Sinalização** ([P] p. 410–413): um payout maior pode sinalizar confiança ou falta de projetos. O mercado reage à **mudança** de payout.
- **"Pássaro na mão"** ([P] p. 412–413): a preferência por dividendos é uma das contestações a M&M.
- **Empresas maduras** ([P] p. 414): payouts maiores (cash cows).
- **Dividendos × recompra** ([P] p. 417–419):
  - recompra é mais flexível (pode ser interrompida), não cria expectativa de recorrência e é anunciada por fato relevante;
  - **tributação no Brasil (2012)**: ganho de capital tributado a 15%, dividendos **isentos**, o que favorece dividendos para pessoa física.
- **Dividend yield no Brasil** ([P] p. 414–416): ranking de 2012 e poucas empresas com yield alto e consistente.

## 4. Passo a passo prático

1. Use o **FCFE** (ou FCFF) como base; o DDM só como checagem ou para financeiras.
2. Compare o histórico de dividendos + JCP + recompras com o FCFE: payout de caixa = (dividendos + JCP + recompras)/FCFE.
3. Se o payout de caixa for muito menor que 100% e o caixa acumular, decida: o caixa é do acionista (soma no equity, tema 31) ou será mal investido (desconto)?
4. No DDM, o payout estável deve sair de `1 − g/ROE`.
5. Para dividend yield, use a soma de **dividendos + JCP** líquidos dos impostos aplicáveis.

## 5. Erros comuns apontados pelos autores

- **Dividendo como proxy do FCFE** em empresas que retêm ou recompram ([P] p. 410–411; [D] p. 483).
- **Gordon com g perto de Ke** ([D] p. 452).
- **Payout estável incoerente** com g e ROE ([D] p. 458).
- **Achar que dividendo alto cria valor por si** ([P] p. 412–413).

## 6. Onde concordam e onde divergem

**Concordam**: valor depende do caixa gerado e reinvestido, não da forma de distribuição; Gordon é sensível a g; payout coerente com g e ROE.

| Ponto | Damodaran | Póvoa |
|---|---|---|
| DDM | Útil, adaptável, conservador | "Mito": o dividendo é decisão da gestão, não fluxo |
| Teoria | Foco no modelo e nas versões | M&M, sinalização, pássaro na mão |
| Brasil | Não trata | Tributação, JCP, dividend yield, recompra |

## 7. Limites: o que está defasado ou é específico do Brasil

- **Tributação de dividendos**: a isenção citada em [P] (2012) foi alterada por legislação recente, com retenção sobre dividendos acima de um limite mensal a partir de 2026 **[NÃO VERIFICADO aqui: conferir a lei e as alíquotas vigentes]**. Isso muda a comparação dividendos × JCP × recompra.
- **JCP**: tratado no tema 22; também houve propostas de mudança **[NÃO VERIFICADO aqui]**.
- Dividendo mínimo obrigatório (Lei das S/A, 25% do lucro ajustado, salvo estatuto) cria payouts "forçados".

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. DDM **só para financeiras** (tema 44) ou como checagem.
2. Mostrar o **payout de caixa** (dividendos + JCP + recompras sobre FCFE).
3. Atualizar a seção tributária conforme a lei vigente antes de comparar dividendos, JCP e recompras.

## 9. Dúvidas abertas para você decidir

1. Incluir o dividend yield projetado como métrica de destaque no vídeo?
2. Como tratar a nova tributação de dividendos no Ke ou no fluxo do acionista?
