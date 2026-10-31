# Fichamento 12: Por que projetar caixa e não lucro; sunk cost; erros típicos de projeção

**Fontes**
- **[D]** Damodaran (2002), Cap. 10 "From Earnings to Cash Flows" (PDF p. 341–372; ver também o fichamento 10). Cap. 15, FCFF e outras medidas: EBITDA, EBIT(1−t), NOPLAT (Tab. 15.1, p. 534–536). Cap. 11, aspectos qualitativos (p. 419–421).
- **[P]** Póvoa (2012), Cap. 4: "Mitos sobre o FCD" (p. 96–99), "A simplicidade do método" (p. 99–100), "TRASH IN, TRASH OUT: Por que projetar caixa, e não lucros?" (p. 100–104), "O ponto mais importante…" (p. 104–105), "Sunk cost" (p. 118–119) e "Casos em que a aplicação direta do FCD é mais complicada" (p. 125–129).

---

## 1. Conceito central

O valor vem do **caixa** que a empresa vai gerar, não do lucro contábil. A contabilidade usa regime de competência, depreciação, provisões e o tratamento de P&D e marketing como despesa, e por isso o lucro pode divergir muito do caixa em cada período ([P] p. 100–103). Os maus insumos contaminam o melhor modelo: "trash in, trash out" ([P] p. 100). Damodaran mostra que cada medida "parecida" com o FCFF embute uma hipótese implícita sobre reinvestimento ([D] p. 534–536). E só o futuro importa: **custos passados (sunk costs)** não entram ([P] p. 118–119).

## 2. Fórmulas

**FCD genérico** ([P] p. 99)
`Valor = Σ FC_t/(1+r)^t + FC_n(1+g_p)/[(r_p − g_p)(1+r)^n]`

**FCFF e as hipóteses implícitas de outras medidas** ([D] Tab. 15.1, p. 534–536)
- Descontar **EBITDA** a WACC supõe **ausência de impostos** e desinvestimento ao longo do tempo. É inconsistente com crescimento e vida infinita.
- Descontar **EBIT(1−t)** (NOPLAT) a WACC supõe **reinvestimento zero**: a D&A só repõe os ativos. Vida infinita, mas **sem crescimento**.
- **FCFF** = EBIT(1−t) + D&A − Capex − ΔCG.

**Exemplo de [P]: depreciação real × fiscal** (p. 101–102, Tab. 4.1)
Um investimento em TI de R$100 mi depreciado em 5 anos (pré-IFRS, R$20 mi/ano) contra 2 anos com valor residual de R$20 mi (IFRS, R$40 mi/ano). Com depreciação contábil menor que a real, a empresa paga mais imposto. *Os valores da tabela não saíram na extração [NÃO VERIFICADO no texto].*

## 3. Premissas e escolhas dos autores

- **Por que o lucro engana** ([P] p. 100–103):
  1. **D&A não é caixa.** Com o IFRS, a depreciação societária passou a refletir o desgaste real, e o lucro ficou mais perto do caixa. A amortização de ágio e a exaustão foram abolidas no balanço societário, mas continuam para fins fiscais.
  2. **P&D e marketing** são caixa gasto. As empresas que investem mais neles terão maior capacidade de crescimento (Cap. 8, Cap. 10). Damodaran os capitaliza (tema 07).
  3. **Competência × caixa**: uma venda parcelada em 5 anos entra cheia na receita. O capital de giro capta essa diferença.
  4. **Provisões**: dependem do critério de cada empresa (exemplo da PDD bancária). Uniformize os critérios entre pares.
- **O lucro como proxy de caixa só vale no longo prazo.** A comparação *earnings yield* × *bond yield* é frágil, porque no curto prazo o investimento (físico e de giro) separa lucro e caixa ([P] p. 104).
- **Mitos do FCD** ([P] p. 97–99):
  1. Não é preciso. Busque **faixas** de compra e venda, com sensibilidade.
  2. Mais detalhe não é melhor. Inclua variáveis até o custo marginal igualar o benefício. "Se há complexidade excessiva, devemos desconfiar."
  3. Múltiplos bem feitos embutem as mesmas variáveis.
  4. O valor não é único: depende do comprador (sinergias, custo de capital). Exemplo de dois bancos (X e Y).
  5. **Não avalie a empresa em "condições ideais".** Avalie o que vai acontecer, com os defeitos da gestão, salvo numa aquisição de controle (exemplo da petroquímica familiar que se recusa a alavancar).
- **As duas variáveis mais importantes** são **crescimento** e **taxa de desconto** ([P] p. 104).
- **Sunk cost** ([P] p. 118–119): investimentos e prejuízos passados já estão no caixa e no balanço atuais. O passado só importa quando gera efeitos futuros (juros, amortizações, créditos fiscais).
- **Qualitativos precisam virar números** ([D] p. 419–421): gestão, marca e estratégia entram via ROC, margens, giro e reinvestimento. Se não for possível quantificar, desconfie.
- **Casos em que o FCD é mais complicado** ([P] p. 125–129): empresas em dificuldade (turnaround incerto); startups e empresas com investimento alto (fluxos negativos iniciais); **ativos não operacionais** (avaliar à parte e somar); cíclicas e commodities (definir ciclo e preço de longo prazo, e o analista "pode e deve" ter opinião, sem buscar neutralidade); ativos sem fluxo atual mas com valor (patentes, reservas não provadas → opções reais); empresas fechadas (iliquidez, investidor pouco diversificado).

## 4. Passo a passo prático

1. Parta do **EBIT ajustado** (tema 07), não do lucro líquido nem do EBITDA.
2. Converta para caixa: EBIT(1−t) + D&A − Capex − ΔCG (tema 10).
3. **Separe os ativos não operacionais** (terrenos, participações, caixa excedente), avalie-os a mercado e some no fim ([P] p. 126–127).
4. Ignore os sunk costs, mas mantenha passivos e créditos com efeito futuro.
5. Para cíclicas, defina **onde no ciclo** a empresa está e o **preço normalizado** de longo prazo ([P] p. 127–128).
6. Monte cenários e faixas, não um preço único ([P] p. 97).

## 5. Erros comuns apontados pelos autores

- **Projetar lucro e descontá-lo como se fosse caixa** ([P] p. 100–104).
- **Descontar EBITDA ou NOPLAT a WACC com crescimento** ([D] p. 534–536).
- **Modelos excessivamente detalhados** ([P] p. 97).
- **Avaliar a "empresa ideal"** em vez da real ([P] p. 98–99).
- **Usar a média histórica do preço da commodity "por neutralidade"** ([P] p. 128).
- **Incluir prejuízos passados** no valor ([P] p. 118).

## 6. Onde concordam e onde divergem

**Concordam**: caixa > lucro; qualitativos precisam virar números; separar ativos não operacionais.

| Ponto | Damodaran | Póvoa |
|---|---|---|
| P&D e marketing | Capitaliza (Cap. 9; tema 07) | Mantém como despesa; reflete no crescimento (p. 102) |
| Ênfase | Hipóteses implícitas de cada medida (Tab. 15.1) | Mitos e erros práticos de mercado (p. 96–104) |
| Valor único | O investidor marginal define o preço | Valor depende do comprador (p. 97–98) |

## 7. Limites: o que está defasado ou é específico do Brasil

- A discussão pré-IFRS × IFRS de [P] (p. 100–102) é histórica para listadas. Ainda vale conferir a vida útil adotada pela empresa.
- Exemplos de fraudes (Enron, Parmalat, Panamericano) são históricos.

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. **Regra**: projetar **FCFF** a partir do **EBIT ajustado**, nunca descontar lucro ou EBITDA.
2. **Avaliação "como é"**: a gestão atual com seus vieses (política de dividendos e de dívida). Cenários de "melhoria de gestão" ficam separados e com probabilidade.
3. **Ativos não operacionais** em linha separada, a valor de mercado e com fonte.
4. **Resultado em faixa** (pessimista, base, otimista), não um preço único.

## 9. Dúvidas abertas para você decidir

1. Publicar o preço-alvo como faixa ou como número central com faixa?
2. Como tratar ativos não operacionais sem valor de mercado observável (terrenos)?
