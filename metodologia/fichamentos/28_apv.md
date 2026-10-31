# Fichamento 28: Método APV como alternativa ao WACC

**Fontes**
- **[D]** Damodaran (2002), Cap. 15, "Firm Valuation: The APV approach", "The Mechanics of APV Valuation", Ilustração 15.5 (Tube Investments), "Cost of Capital versus APV Valuation", "APV, without bankruptcy costs", "APV and Financial Leverage", Ilustração 15.8 (Boeing), "Benefits and Limitations" e "Valuing the pieces rather than the whole" (PDF p. 560–589).
- **[P]** Póvoa (2012): **não trata do APV** nos capítulos da lista. Uso só, como contexto, as discussões de Póvoa sobre dívida e estrutura de capital (Cap. 6–7).

---

## 1. Conceito central

O **APV (Adjusted Present Value)** separa o valor da firma em partes. O valor da **firma sem dívida** vem do FCFF descontado ao **custo do capital próprio desalavancado**. Soma-se o valor presente do **benefício fiscal** da dívida e subtrai-se o **custo esperado de falência** ([D] p. 560–562). No método do WACC, os efeitos da dívida ficam embutidos na taxa. No APV, aparecem em parcelas explícitas, o que permite **taxas diferentes para cada componente** e trabalhar com **um montante fixo de dívida** em vez de um índice constante ([D] p. 565, 587).

## 2. Fórmulas

**Firma desalavancada** ([D] p. 561)
`V_u = FCFF₀(1 + g)/(ρu − g)` (estável). Em geral, VP do FCFF a ρu.
`βu = β_atual / [1 + (1 − t) D/E]` e `ρu = Rf + βu × prêmio`.

**Benefício fiscal** ([D] p. 562)
Perpetuidade descontada a Kd: `VP = t × Kd × D / Kd = t_c × D`. Use a alíquota **marginal**.

**Custo esperado de falência** ([D] p. 562)
`VP = P(falência) × VP(custo de falência)`. A probabilidade vem do rating (Tab. 15.8, Altman e Kishore) ou de um modelo probit. O custo direto é ~5% (Warner); o indireto, 25–30% segundo Shapiro e Titman, "sem evidência direta" ([D] p. 563–564).

**Valor da firma alavancada** ([D] p. 565)
`V_L = V_u + t_c D − P(falência) × CF`

**Exemplo Tube Investments** ([D] p. 564–565)
βu = 0,75 → ρu = 10,5% + 0,75 × 9,23% = 17,45% → V_u = 1.704,6. Benefício = 0,30 × 1.807,3 = 542,2. Custo esperado de falência = 0,10 × 0,40 × 1.704,6 = 68,2. Ativos operacionais = **2.178,6**, mais caixa = 3.543,9, contra 3.367,3 pelo WACC.

**Exemplo Boeing (ótimo)** ([D] p. 585–587)
V_u = V atual − t × D + custo de falência esperado = 40.789 − 2.868 + 0,28% × 30% × 37.921 ≈ **37.953**. O ótimo fica entre 20% e 30% de dívida, muito sensível às hipóteses.

## 3. Premissas e escolhas do autor

- **O principal benefício da dívida é fiscal; o principal custo é a falência** ([D] p. 560–561).
- **Benefício fiscal perpétuo e descontado a Kd** (dívida permanente, alíquota constante). Se a alíquota mudar, calcule o VP ano a ano ([D] p. 562).
- **Por que APV e WACC podem divergir** ([D] p. 565):
  1. O APV permite incluir custos **indiretos** de falência, que o WACC pode capturar mal, e por isso tende a ser mais conservador.
  2. O APV usa o **montante atual** de dívida, enquanto o WACC com índice constante implica **emitir dívida no futuro** e conta hoje esse benefício.
- **Com as mesmas hipóteses, os dois métodos dão o mesmo resultado** ([D] p. 588, com Inselbag e Kaufold, 1997). O APV é mais prático para um **montante** de dívida, e o WACC para um **índice**.
- **Atalho pelo valor de mercado**: em vez de estimar V_u do zero, parta do valor de mercado atual e retire o benefício fiscal e o custo de falência da dívida atual ([D] p. 584).
- **"Valuing the pieces"**: a lógica do APV se estende a avaliar divisões ou países separadamente e somar. Isso melhora a precisão quando há informação por segmento, mas as despesas centrais costumam ser rateadas de forma arbitrária ([D] p. 588–589).

## 4. Passo a passo prático

1. Calcule o βu e o ρu.
2. Projete o FCFF e desconte a ρu para obter V_u.
3. Projete a dívida em **montante** ano a ano e calcule o benefício fiscal t × juros por ano, descontado a Kd (ou t × D, se perpétuo).
4. Estime o rating → P(default) → custo de falência (% de V_u) → custo esperado.
5. V_L = V_u + VP(benefício fiscal) − custo esperado de falência.
6. Some o caixa e os ativos não operacionais e subtraia a dívida para chegar ao capital próprio (tema 30).

## 5. Erros comuns apontados pelo autor

- **Ignorar o custo de falência**: o valor sobe sempre com a dívida e o "ótimo" vira 100% dívida ([D] p. 565–566, 588).
- **Esquecer que o benefício só existe com lucro tributável** e que, com juros acima do EBIT, a alíquota efetiva cai ([D] p. 585).
- **Confundir o APV com um método "mais flexível" em geral**: na prática ele tem falhas sérias, porque P(default) e o custo de falência são difíceis de estimar ([D] p. 565, 588).

## 6. Onde Damodaran e Póvoa concordam e onde divergem

Póvoa não discute o APV. Indiretamente, sua defesa do FCFF a WACC com estrutura de capital variável ano a ano ([P] Cap. 7, p. 267–268) cumpre a mesma função de modelar mudanças de dívida que o APV resolve com montantes fixos. A crítica dele à perpetuação do subsídio do BNDES ([P] p. 244–245) seria fácil de modelar no APV, como uma parcela separada de "valor do subsídio".

## 7. Limites: o que está defasado ou é específico do Brasil

- A tabela de default por rating (Altman e Kishore, 1998) e as estimativas de custo de falência (Warner; Shapiro e Titman) são antigas.
- No Brasil, o JCP seria outra parcela de benefício fiscal a somar no APV, o que é uma possível vantagem do método (inferência minha).
- Recuperação judicial e custos de falência no Brasil têm dinâmica própria (Lei 11.101/2005), fora dos livros **[NÃO VERIFICADO aqui]**.

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. **Não usar o APV como método principal.** Usá-lo como **checagem** em três casos: (i) empresas em reestruturação de dívida, LBO ou desalavancagem forte; (ii) empresas com **subsídio relevante** (BNDES, incentivos fiscais com prazo), avaliando o subsídio como parcela separada e com prazo de fim; (iii) JCP, se decidir tratá-lo como parcela (tema 22).
2. Sempre explicitar o **custo de falência** quando usar o APV.

## 9. Dúvidas abertas para você decidir

1. Incluir o APV no material dos vídeos ou só na planilha de apoio?
2. Usar o APV para isolar o valor de subsídios e incentivos fiscais?
