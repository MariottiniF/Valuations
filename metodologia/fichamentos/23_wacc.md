# Fichamento 23: WACC e estrutura de capital (pesos, circularidade)

**Fontes**
- **[D]** Damodaran (2002), Cap. 8, "Calculating the Weights of Debt and Equity", "Book Value versus Market Value", "Estimating the Market Values of Equity and Debt", "Gross Debt versus Net Debt", "Estimating the Cost of Capital" e "Best Practices" (PDF p. 291–300). Cap. 15, "Firm Valuation: The Cost of Capital Approach", "Market Value Weights, Cost of Capital and Circular Reasoning", "General Version", "Net Debt versus Gross Debt" e "Will equity value be the same under firm and equity valuation?" (p. 533–560).
- **[P]** Póvoa (2012), Cap. 6, "Taxa de desconto para a firma" (p. 231–237), "Por que, quando elevamos o endividamento, o custo de capital próprio também aumenta?" (p. 240–243) e "Escadinha no WACC" (p. 245–246). Cap. 7, "Como tratar as mudanças de estrutura de capital no processo de valuation?" (p. 267–268).

---

## 1. Conceito central

O WACC é a média dos custos de cada fonte de financiamento (capital próprio, dívida e híbridos), **ponderada pelo valor de mercado** de cada uma. Ele é a taxa que desconta o **fluxo de caixa livre para a firma (FCFF)**, antes dos pagamentos a credores ([D] p. 297–298, 537; [P] p. 231–232). O benefício fiscal da dívida entra **na taxa**, pelo Kd após impostos, e não no fluxo: incluí-lo nos dois lugares seria contá-lo duas vezes ([D] p. 534). Os pesos são de mercado porque é a esse valor que os títulos seriam emitidos hoje ([D] p. 292; [P] p. 232–234).

## 2. Fórmulas

**WACC** ([D] p. 297; [P] p. 231–232)
`WACC = Ke × E/(D+E+PS) + Kd(1−t) × D/(D+E+PS) + Kps × PS/(D+E+PS)`
E, D, PS = valores de mercado do capital próprio, da dívida e das preferenciais. No Brasil, Póvoa aplica ao Ke o benefício do JCP (tema 22).

**Valor da firma (crescimento estável)** ([D] p. 537)
`Valor da firma = FCFF₁ / (WACC − g)`, com g ≤ crescimento da economia na mesma moeda e no mesmo regime.

**Valor da firma (geral, n anos + perpetuidade)** ([D] p. 541–542)
`Valor = Σ_{t=1}^{n} FCFF_t/(1+WACC)^t + [FCFF_{n+1}/(WACC_n − g_n)]/(1+WACC)^n`

**FCFF** ([D] p. 533–534)
`FCFF = EBIT(1−t) + D&A − Capex − ΔCapital de giro`, ou `FCFF = FCFE + Juros(1−t) + Amortizações − Novas dívidas + Div. preferenciais`.

**Custo da dívida líquida (se usar dívida líquida)** ([D] p. 556–557)
`Kd sobre dívida líquida = (Kd_bruta × D_bruta − Rf × Caixa) / D_líquida`. Exemplo: (7% × 400 − 5% × 200)/200 = **9%**.

**Exemplos conferidos**
- [D] Boeing, jun/2000: 10,28% × 0,8755 + 3,90% × 0,1245 = **9,49%** ([D] p. 298) ✔.
- [D] Embraer em US$ com dívida líquida: 18,86% × 9.084/9.307 + 7,45% × 223/9.307 = **18,59%**. Em R$ nominal: 1,1859 × 1,10/1,02 − 1 = 27,89% ([D] p. 298) ✔.
- [P] Têxtil: (500/800) × 18,89% + (300/800) × 10,50% = **15,74%** ([P] p. 232) ✔.
- [P] Alavancagem com troca de rating: o WACC vai de 7,61% para 7,47% ([P] p. 241–242) ✔.

## 3. Premissas e escolhas dos autores

- **Pesos a valor de mercado.** Damodaran rebate três defesas do valor contábil: (i) "é menos volátil", mas a volatilidade reflete informação; (ii) "é mais conservador", o que é falso, já que com P/VP > 1 o peso contábil da dívida é maior e o WACC sai **menor**; (iii) "credores emprestam pelo contábil", o que também é falso ([D] p. 294–295). Póvoa dá o mesmo argumento com um exemplo de P/VP = 2: o WACC a mercado (16,67%) supera o contábil (15%) ([P] p. 233–234).
- **Dívida contábil como proxy**: no Brasil, o secundário de dívida privada é ilíquido ([P] p. 231). Damodaran converte o contábil em mercado tratando a dívida como um único título ([D] p. 295–297).
- **Circularidade.** Os pesos de mercado vêm do preço atual, mas o objetivo é estimar o valor. Damodaran aceita a inconsistência (comprar toda a firma custaria o preço de mercado) ou propõe **iterar** os pesos até convergirem. No caso da Tube Investments, o valor por ação passa de 63,36 para 70,66 rúpias ([D] p. 540–541).
- **FCFF × FCFE.** O FCFF é preferível quando a alavancagem é alta ou vai mudar ([D] p. 542, 559; [P] p. 267). Damodaran aponta três defeitos do FCFF: é um fluxo hipotético ("e se não tivesse dívida?"); pode esconder problemas de sobrevivência (FCFF positivo com FCFE negativo); e supõe implicitamente uma emissão de dívida futura para manter o índice-alvo ([D] p. 542–543).
- **Coerência firma × acionista.** Os valores do capital próprio pelos dois métodos só coincidem se: (1) os pesos usados forem os valores obtidos; (2) não houver itens não operacionais; (3) os juros forem iguais a Kd × valor de mercado da dívida ([D] p. 559–560).
- **WACC mudando no tempo.** O WACC pode variar ano a ano por três fontes: beta (D/E), Kd (rating) e pesos. A "escadinha" no WACC é legítima se refletir uma mudança planejada de estrutura de capital ([P] p. 245–246; [D] p. 545, 549–550; tema 25).
- **WACC da perpetuidade**: deve ser o de uma firma estável, com beta próximo de 1 (0,8 a 1,2) ([D] p. 538). Na Gap, Damodaran reduz o beta de 1,2 para 1,0 na perpetuidade, e o WACC cai de 9,06% para 8,43% ([D] p. 545).
- **Dívida bruta × líquida.** As duas chegam ao mesmo valor **se** o Kd sobre a dívida líquida for ajustado para cima. Damodaran recomenda a bruta: a líquida pode ser negativa, e mantê-la constante exige acumular caixa ([D] p. 556–557).
- **Prática empresarial** (Bruner et al., 1998): 81% usam o CAPM, 70% usam Treasury de 10 anos ou mais, 59% usam pesos de mercado ([D] p. 299).

## 4. Passo a passo prático

1. Calcule o **Ke** (temas 17 a 20) e o **Kd(1−t)** (tema 21).
2. Levante **E a mercado** (ações × preço, mais opções e bônus, se houver) e **D a mercado** (ou o contábil como proxy), incluindo leasing ([D] p. 295; [P] p. 231).
3. Decida **bruta ou líquida** e seja consistente no beta, nos pesos e na ponte EV → equity ([D] p. 296, 556).
4. Calcule o WACC do período explícito. Se a estrutura de capital for mudar, faça um WACC por ano: realavanque o beta e reestime o rating ([P] p. 245–246, 267–268).
5. Defina o **WACC da perpetuidade**, com estrutura de capital de equilíbrio e beta próximo de 1 ([D] p. 538).
6. *(Opcional)* Itere os pesos até convergirem ([D] p. 540–541).
7. Desconte o FCFF, some os ativos não operacionais e subtraia a dívida para chegar ao capital próprio (tema 30).

## 5. Erros comuns apontados pelos autores

- **Pesos contábeis**, sob o argumento de serem "conservadores" ([D] p. 294–295; [P] p. 233–234).
- **Contar o benefício fiscal no FCFF e também no WACC** ([D] p. 534).
- **Descontar o FCFF pelo Ke**, ou o FCFE pelo WACC ([P] p. 180).
- **Usar a dívida líquida com o Kd da dívida bruta**, o que superestima o valor ([D] p. 556–557).
- **Supor um D/(D+E) constante numa firma que cresce** sem verificar se isso exige uma emissão absurda de dívida ([D] p. 543).
- **Calcular o WACC com custos históricos** da dívida ([P] p. 234–235).

## 6. Onde concordam e onde divergem

**Concordam**: pesos a valor de mercado; WACC com FCFF; FCFF quando a alavancagem muda; o WACC pode variar ano a ano por mudança de estrutura.

| Ponto | Damodaran | Póvoa |
|---|---|---|
| Valor da dívida | Converte o contábil em mercado (p. 295) | Contábil como proxy (p. 231), reprecificado após mudança de rating (p. 235–237) |
| Ke no WACC | CAPM puro | CAPM × (1 − 0,0555) por causa do JCP (p. 232) |
| Alíquota | Marginal (Cap. 8, p. 287) | "Média" (p. 232) |
| Circularidade | Discute e propõe iteração (p. 540–541) | Não discute |
| Dívida líquida | Admite, com Kd ajustado; prefere a bruta (p. 556–557) | Não discute |

## 7. Limites: o que está defasado ou é específico do Brasil

- Exemplos numéricos de 1999–2001 (Boeing, Gap, Amgen, Embraer, Tube) e de 2012–2013 ([P]): ilustrativos.
- **Inconsistência em [D]**: no caso da Amgen, o Ke calculado é 10,80%, mas a fórmula do WACC usa 13,08% (p. 549).
- **Nota de revisão esquecida em [D]**: na p. 587 aparece "[NOTE: This is not true…]" sobre a hipótese de D/(D+E) constante no método do WACC. É o próprio autor ressalvando que o WACC pode mudar a cada ano.
- **Brasil**: secundário de dívida pouco líquido ([P] p. 231); JCP; dívida BNDES (tema 21).

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. **Método principal: FCFF a WACC** (FCFE só como checagem em empresas de estrutura estável).
2. **Pesos-alvo de longo prazo** para a perpetuidade, que podem ser os da empresa ou a mediana do setor ([P] p. 267). No explícito, os pesos atuais convergindo para o alvo.
3. **Dívida a mercado** quando houver debêntures negociadas no secundário; caso contrário, o contábil.
4. **Dívida bruta** no WACC e caixa somado na ponte EV → equity, como recomenda [D].
5. Publique numa tabela única: Ke, Kd(1−t), E/(D+E), D/(D+E), WACC explícito e WACC da perpetuidade.
6. Faça **uma iteração** de circularidade só quando o preço justo divergir mais de 30% do preço de mercado e registre o efeito.

## 9. Dúvidas abertas para você decidir

1. Pesos atuais, pesos-alvo da empresa ou mediana do setor?
2. Iterar a circularidade ou não?
3. JCP no Ke ou no fluxo (tema 22)?
4. Dívida bruta (recomendado) ou líquida?
