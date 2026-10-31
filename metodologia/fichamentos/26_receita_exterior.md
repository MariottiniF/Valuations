# Fichamento 26: Taxa de desconto para empresas com receita no exterior

**Fontes**
- **[D]** Damodaran (2002), Cap. 7, "Estimating Asset Exposure to Country Risk Premiums" (PDF p. 232–234), e Cap. 8, Ilustração 8.9, Embraer (p. 281–283), Ilustração 8.11, custo da dívida da Embraer (p. 289), e "How well do betas travel?" (p. 275–276).
- **[P]** Póvoa (2012), Cap. 6, "Taxa de desconto para empresas com grande volume de vendas no exterior" e "Teoria do fator Lambda" (p. 246–250).

---

## 1. Conceito central

A pergunta é se uma empresa brasileira que vende quase tudo lá fora deve carregar 100% do risco-país na taxa de desconto. **Damodaran propõe medir a exposição de cada empresa ao risco-país com um fator λ**, separado do beta, a partir da fração da receita gerada no país ([D] p. 233). **Póvoa rejeita o λ**: ele seria usado só para reduzir o risco, nunca para aumentar, e é inconsistente quando aplicado a multinacionais. Póvoa prefere ler o que o mercado já precifica: o spread dos títulos da própria empresa e o beta, que capta a diversificação de receitas com o tempo ([P] p. 249–250).

## 2. Fórmulas

**Ke com λ** ([D] p. 233)
`Ke = Rf + β × ERP maduro + λ × CRP`
`λ = % da receita no país (empresa) / % da receita no país (empresa típica)`
- Aracruz: λ = 0,20/0,80 = 0,25 → Ke US$ = 5% + 0,72 × 5,51% + 0,25 × 9,69% = **11,39%** ([D] p. 233, nota 15).
- Embraer: λ = 9%/60% = 0,15 → Ke US$ = 5% + 0,88 × 5,51% + 0,15 × 10,24% = **11,39%**, contra 18,86% sem λ ([D] p. 282).

**Versão de Póvoa do λ** (para criticá-la) ([P] p. 247–248)
`λ = % da receita no Brasil / % do PIB produzido internamente` (73% em 2012, porque as exportações eram 27% do PIB).
- Embraer: λ = 5/73 = 0,07.
- US$: Ke = 2% + 0,07 × 1,4% + 0,6 × 4,5% = 4,8%, contra 6,1% sem λ ✔.
- R$: o "risco-Brasil em reais" é 10% − (2% + 2,5%) = 5,5%, e Ke = 4,5% + 0,07 × 5,5% + 0,6 × 6,5% = 8,79%, contra 13,9% ✔.
- *Erro de digitação em [P] p. 248:* a fórmula aparece como "(L × 1,4%) **×** (β × 4,5%)", mas a conta soma (+).

## 3. Premissas e escolhas dos autores

- **Três visões da exposição** ([D] p. 232–233): (a) todas as empresas igualmente expostas; (b) exposição proporcional ao beta; (c) **λ próprio**, a preferida de Damodaran, que transforma o CAPM num modelo de dois fatores.
- **Para Damodaran, empresas de commodities que vendem em US$ são menos expostas** do que empresas que servem o mercado local ([D] p. 233). Ele estende o raciocínio a multinacionais de países desenvolvidos com exposição a emergentes, como Coca-Cola e Nestlé: o λ também pode **aumentar** o Ke ([D] p. 233–234).
- **Para Póvoa, o "risco-Brasil" é o risco de fazer negócio no país, e a mobilidade dos ativos importa** ([P] p. 246–247). A Embraer, com conhecimento transferível, poderia mudar de país; a Vale não leva Carajás embora. Por esse critério, a commodity carrega o risco-país "na veia", **o inverso da intuição de Damodaran**, que olha para a moeda da receita.
- **Falhas do λ para Póvoa** ([P] p. 249): (1) uma varejista 100% doméstica teria λ = 1,37 e deveria pagar um "sobrerrisco", o que ninguém faz; (2) multinacionais com a maior parte da receita em emergentes também deveriam ter o Ke aumentado.
- **A solução de Póvoa** ([P] p. 249–250): use o **spread corporativo de mercado** (títulos da empresa no exterior negociados abaixo do soberano) no lugar do EMBI e confie que o **beta** capta a diversificação de receita com o tempo.
- **Custo da dívida** ([D] p. 289): a Embraer, com receita em dólar, poderia argumentar que deve tomar mais barato que o soberano brasileiro.

## 4. Passo a passo prático

**Damodaran (λ)**
1. Estime o CRP do país (tema 19).
2. Calcule o λ pela razão de receita local da empresa sobre a da empresa típica.
3. Ke = Rf + β × ERP maduro + λ × CRP.
4. Converta para R$ pelo diferencial de inflação, se for o caso ([D] p. 282).

**Póvoa (mercado)**
1. Verifique se a empresa tem títulos em US$ negociados com spread menor que o do soberano.
2. Se tiver, use a taxa corporativa como "Rf + risco" em US$ no lugar de Treasury + EMBI ([P] p. 249).
3. Use o bottom-up beta normalmente ([P] p. 250).

## 5. Erros comuns apontados pelos autores

- **Supor que todas as empresas de um país têm a mesma exposição** ([D] p. 232).
- **Usar o λ só para reduzir o risco** e nunca para aumentá-lo ([P] p. 249).
- **Achar que o DCF tradicional não capta a internacionalização** da empresa ([P] p. 246).

## 6. Onde concordam e onde divergem

| Ponto | Damodaran | Póvoa |
|---|---|---|
| Fator λ | Abordagem preferida (p. 233) | Rejeitado (p. 249) |
| Commodity exportadora | Menos exposta (receita em US$) (p. 233) | Mais exposta (ativo imóvel) (p. 247) |
| Multinacional de país rico | λ pode aumentar o Ke (p. 233–234) | O mesmo argumento é usado contra o λ (p. 249) |
| Solução prática | λ × CRP | Spread corporativo de mercado + beta (p. 249–250) |

Os dois **concordam** que a exposição ao risco-país varia entre empresas. Divergem sobre **como** medir: Damodaran olha a receita, Póvoa olha a mobilidade dos ativos e o preço de mercado da dívida.

## 7. Limites: o que está defasado ou é específico do Brasil

- Números (Aracruz, Embraer, EMBI de 1,4%, exportações de 27% do PIB) são de 2000–2012 e estão vencidos.
- **Em R$**, o λ exige um "risco-Brasil em reais" que não é observável. Póvoa o constrói como NTN-B − (Treasury + diferencial de inflação) ([P] p. 248), e essa conta inclui o "risco-fronteira" que ele mesmo critica em outra parte (p. 227–229).
- Damodaran publicou, depois de 2002, versões do λ baseadas em receita e em produção **[NÃO VERIFICADO aqui]**.

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. **Padrão: sem λ.** O Rf em R$ (NTN-B) já embute o risco-país para o investidor local, e retirá-lo exigiria um "risco-Brasil em reais" arbitrário.
2. Para exportadoras, trate a exposição **no fluxo de caixa** (câmbio, preço em US$) e no **beta** (comparáveis globais do setor, tema 20). Isso vale principalmente se o investidor marginal for estrangeiro.
3. Se houver **dívida em US$ da empresa negociada abaixo do soberano**, registre como informação qualitativa e use o spread no custo da dívida (tema 21).
4. Mostre o λ só como **cenário de sensibilidade**, se for o caso, com aviso explícito.

## 9. Dúvidas abertas para você decidir

1. Vai usar λ em algum caso (cenário) ou nunca?
2. Para exportadoras, o investidor marginal é local ou estrangeiro? Isso muda a moeda e o Rf.
3. Para a ideia de "mobilidade do ativo" de Póvoa, algum ajuste qualitativo, ou só documentar?
