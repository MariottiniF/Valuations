# Fichamento 22: JCP (juros sobre capital próprio)

**Fontes**
- **[D]** Damodaran (2002): **não trata do tema.** O JCP é um instrumento brasileiro. O mais próximo que o livro tem é a lógica geral do benefício fiscal da dívida (Cap. 8, PDF p. 284, 287).
- **[P]** Póvoa (2012), Cap. 6, "Taxa de juros sobre o capital próprio: uma vantagem tributária à brasileira" (p. 210–212), com aplicações em p. 232 (WACC) e p. 241–242 (alavancagem).

---

## 1. Conceito central

A legislação brasileira permite à empresa **deduzir do lucro tributável uma remuneração ao acionista calculada como TJLP × patrimônio líquido**, dentro de um teto. Com isso, o capital próprio ganha parte do benefício fiscal que, em outros países, só a dívida tem ([P] p. 210–211). Póvoa argumenta que esse benefício deveria reduzir o custo do capital próprio no valuation e que "praticamente nenhum analista" o considera, o que ele chama de erro ([P] p. 212).

## 2. Fórmulas (todas de [P])

**Base do JCP** ([P] p. 211)
`JCP dedutível = TJLP × PL contábil` (exclui as reservas de reavaliação ainda não realizadas). Limite: **50% do lucro líquido do período** ou da soma de lucros acumulados e reservas de lucros.

**Fator de aproveitamento**: Póvoa estima que a TJLP média equivale a **~37% do custo do capital próprio** no Brasil desde 1994 ([P] p. 211).

**Custo do capital próprio com JCP** ([P] p. 212)
`Ke = [Rf + β (Rm − Rf)] × (1 − 0,37 × t_JCP)`, com t_JCP = 15% em 2012.
Benefício ≈ 0,37 × 15% = **5,55%** do Ke.

**Exemplo** ([P] p. 211–212): Rf 10,5%, β 0,9, prêmio 6,5% → Ke sem JCP = 16,35%; com JCP = 16,35% × (1 − 0,0555) = **15,44%** ✔.

Aplicações: WACC têxtil com Ke de 20% → 18,89% ([P] p. 232) ✔ (o livro escreve "(1 − 0,555)", erro de digitação de 0,0555). Alavancagem: Ke em US$ (7% + 0,5 × 4,5%) × (1 − 0,15 × 0,37) = 8,74% ✔ ([P] p. 241).

## 3. Premissas e escolhas do autor

- **O JCP como "dívida do acionista"**: a lei imita a lógica dos juros da dívida para remunerar o sócio ([P] p. 210–211).
- **Ajuste multiplicativo no Ke**, não no fluxo de caixa. Póvoa reduz a taxa em vez de projetar o JCP e o imposto economizado ano a ano.
- **Fator de 37% fixo e histórico**: média da relação TJLP/Ke calculada pelo autor desde a criação da TJLP ([P] p. 211). *O livro não mostra o cálculo.*
- **Alíquota usada = 15%**: Póvoa a chama de "alíquota dos juros sobre o capital próprio" ([P] p. 211–212).

## 4. Passo a passo prático (como Póvoa faz)

1. Calcule o Ke pelo CAPM normalmente.
2. Multiplique por (1 − 0,37 × 15%) = 0,9445.
3. Use esse Ke no FCFE ou no WACC.

## 5. Erros comuns apontados pelo autor

- **Ignorar o JCP no custo do capital próprio** de empresas brasileiras ([P] p. 212).

## 6. Onde Damodaran e Póvoa concordam e onde divergem

Damodaran não trata do JCP. Pela lógica dele, porém, um benefício fiscal **marginal** deveria ser medido pela alíquota marginal economizada e só se houver lucro tributável ([D] p. 287). Isso leva às questões da seção 7.

## 7. Limites e pontos que merecem cautela (análise minha, fora dos livros)

- **Qual alíquota mede o benefício?** **[A VERIFICAR]** Os 15% de Póvoa parecem ser o IRRF que o **acionista** paga sobre o JCP. O ganho da **empresa** é a dedução à alíquota de IRPJ + CSLL (34% no lucro real). Para o acionista pessoa física, o ganho líquido seria aproximadamente 34% − 15% = 19% do JCP pago, contra 0% de IR sobre dividendos na regra vigente em 2012. Quem é isento ou tributado de outra forma tem conta diferente. **O livro não explica a escolha de 15%** e a fórmula pode subestimar ou superestimar o benefício. Isso precisa ser confirmado com a legislação.
- **Desvio do princípio "taxa reflete risco"**: o JCP é um benefício **fiscal**, não uma redução de risco. Uma alternativa mais transparente seria projetar o JCP no fluxo (imposto economizado) e manter o Ke "puro".
- **O teto de 50% do lucro** e a necessidade de lucro tributável não aparecem na fórmula simplificada. Empresas com prejuízo ou baixa distribuição não aproveitam o benefício inteiro.
- **Legislação mudou depois de 2012**: houve alterações na base de cálculo do JCP (por exemplo, a Lei 14.789/2023) e discussões recorrentes sobre extinguir o JCP ou tributar dividendos. **Confira as regras vigentes antes de aplicar [NÃO VERIFICADO aqui].**
- **TJLP**: segue como taxa do JCP, mas já não é a taxa dos novos contratos do BNDES (TLP desde 2018). O fator de 37% foi estimado com uma TJLP de outra época.

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. **Não use o fator multiplicativo de Póvoa como padrão** enquanto a questão da alíquota (seção 7) não estiver resolvida.
2. **Alternativa recomendada**: tratar o JCP **no fluxo de caixa**. Projete o JCP (TJLP × PL, limitado a 50% do lucro), calcule o imposto economizado pela empresa e mantenha o Ke sem ajuste. Fica auditável e respeita o teto e a necessidade de lucro.
3. Na **sensibilidade**, mostre o efeito do JCP em separado, com e sem.
4. Documente no `MACRO.md` a TJLP vigente e as alíquotas de IRPJ, CSLL e IRRF sobre o JCP.

## 9. Dúvidas abertas para você decidir

1. JCP no fluxo (recomendado) ou no Ke (Póvoa)?
2. Qual tipo de investidor é o marginal para a conta líquida (PF, PJ, estrangeiro, fundo)? Isso muda o benefício.
3. Considerar o JCP na perpetuidade, dada a incerteza regulatória?
