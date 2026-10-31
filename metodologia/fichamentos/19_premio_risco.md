# Fichamento 19: Prêmio de risco de mercado

**Fontes**
- **[D]** Damodaran (2002), Cap. 7, seções "Equity Risk Premiums", "Historical Premium", "Modified Historical Risk Premium", "Country risk premiums" e "Implied Equity Premiums" (PDF p. 216–239). Uso também o Cap. 8, Ilustrações 8.8 e 8.9 (p. 281–283), e "small firm premium" (p. 283).
- **[P]** Póvoa (2012), Cap. 6: "O prêmio de risco para a compra de ações – CAPM" (p. 206–210), "A taxa de desconto para o acionista na teoria e na prática" (p. 212–216), perpetuidade (p. 220–227) e "Taxa de desconto e prêmio de risco implícitos" (p. 250–253).

---

## 1. Conceito central

O prêmio de risco de mercado (ERP) é o retorno extra que o investidor médio exige para trocar o ativo livre de risco pela carteira de mercado ([D] p. 218; [P] p. 206). Há duas formas de estimá-lo. O **histórico** é a média passada de ações contra títulos públicos. O **implícito** é a taxa que iguala o preço atual do índice ao valor presente dos fluxos esperados. Damodaran mostra que o histórico tem erro-padrão enorme e viés de sobrevivência, e que o implícito, por ser corrente, é a alternativa ([D] p. 220–223, 234–238). Póvoa usa o histórico (geométrico) nos EUA e, no Brasil, **adota um número por julgamento (6,5% a.a. em R$)**, porque o histórico brasileiro é inutilizável ([P] p. 208–210). Usa o implícito como termômetro de euforia ou estresse ([P] p. 250–253).

## 2. Fórmulas

**Erro-padrão do prêmio histórico** ([D] p. 220)
`EP = σ anual das ações / √(nº de anos)`. Com σ = 20%: 5 anos → 8,94%; 10 → 6,32%; 25 → 4,00%; 50 → 2,83%.

**Prêmio com risco-país** ([D] p. 224)
`ERP = prêmio de mercado maduro + prêmio-país`

**Prêmio-país: três medidas** ([D] p. 227–231)
1. Spread de default do rating soberano (ex.: Brasil B2 = 4,83%).
2. Desvio-padrão relativo: `ERP país = ERP EUA × σ ações país / σ ações EUA`. Ex.: Indonésia 5,51% × 35/20 = 9,64%, prêmio-país 4,13%.
3. Combinação: `CRP = spread de default × (σ ações país / σ título soberano em US$)`. Ex.: Brasil 4,83% × 30,64/15,28 = **9,69%**.

**Exposição da empresa ao risco-país** ([D] p. 232–233)
(a) igual para todas: `Ke = Rf + β × ERP maduro + CRP`;
(b) proporcional ao beta: `Ke = Rf + β × (ERP maduro + CRP)`;
(c) preferida por Damodaran, com **λ**: `Ke = Rf + β × ERP maduro + λ × CRP`.
λ = % da receita no mercado local da empresa / % da empresa típica do país. Aracruz: 0,20/0,80 = 0,25 (nota 15).

**Prêmio implícito** ([D] p. 234–235)
`Preço do índice = Σ FC_t/(1+r)^t + TV/(1+r)^n`, depois `ERP = r − Rf`. No modelo de Gordon: `r = D1/P + g`.
Exemplo S&P 500, 31/12/1999: r = 8,56%, ERP = 2,06% ([D] p. 235) ✔ (recalculei r ≈ 8,59%, diferença de arredondamento).

**Prêmio implícito no Ibovespa ([P])**: 3 anos a g = 12% e depois g = 7%, com FC = 10% do índice e Rf = 10%. Em ago/2011, com o Ibovespa a 49 mil, r = 19,1% e ERP = 9,1%. Em nov/2011, a 60 mil, r = 16,9% ([P] p. 251–252). ✔ Recalculado: as duas taxas só fecham se o primeiro fluxo for 4.900 × 1,12, isto é, se os 10% forem o fluxo corrente, que cresce 12% já no ano 1.

**Small cap premium (com ressalva)** ([D] p. 283): `Ke = Rf + β × ERP + prêmio de small cap (~2%)`.

## 3. Premissas e escolhas dos autores

- **Três escolhas explicam a dispersão dos prêmios históricos (4% a 12% nos EUA)**: o período, T-bill × T-bond e a média aritmética × geométrica ([D] p. 219–222). Damodaran escolhe **período longo, T-bond e média geométrica**, o que dá 5,51% entre 1928 e 2000 ([D] p. 224–225).
- **Média geométrica**: os retornos têm correlação serial negativa, e os modelos são usados para horizontes longos. Por isso os dois preferem a geométrica ([D] p. 221; [P] p. 208–209).
- **Viés de sobrevivência**: o histórico dos EUA superestima o prêmio esperado ([D] p. 222–223, 237).
- **Mercados emergentes**: o prêmio histórico local "não deve ser usado" ([D] p. 224). Póvoa chega a uma conclusão parecida para o Brasil: entre 1976 e 2010 o prêmio Ibovespa − Selic é negativo, e só entre 2003 e 2010 é positivo (7,6%) ([P] p. 209–210).
- **O risco-país deve ser precificado?** Depende de o investidor marginal ser global e de a correlação entre mercados ser baixa. Damodaran conclui que os mercados são **parcialmente segmentados** e que parte do risco-país não é diversificável ([D] p. 225–226).
- **Prêmio-país convergente**: o prêmio combinado (9,69%) é o mais realista no curto prazo e deve convergir ao longo do tempo para o spread (4,83%) ou para o desvio relativo (4,13%) ([D] p. 231–232).
- **Determinantes do prêmio ([P])**: percepção de risco do país; **tamanho do juro real** (juro real alto exige prêmio alto); hábito de investir em renda variável, que é hábito e não cultura e por isso pode mudar; e oportunidades de investimento ([P] p. 206–208).
- **Números de [P]**: **4,5% a.a.** em US$ para o investidor norte-americano (o histórico geométrico de 1928–2010 é 4,0%) e **6,5% a.a.** em R$ para o investidor local, acima dos 5–6% "mais comuns" no mercado ([P] p. 209–210).
- **Prêmio diferente por investidor**: o investidor norte-americano, com Rf de 2,5% e hábito de bolsa, exige menos do que o brasileiro, com NTN-B a 11,9% ([P] p. 216).
- **Variação no tempo**: [P] não projeta mudanças no prêmio no período explícito, porque seria "subjetivo em cima do subjetivo" (p. 219–220). Na perpetuidade admite um corte pequeno, de 6,5% para 6,2% no exemplo (p. 223). [D] mostra que o prêmio implícito sobe com a inflação e os juros, e sugere uma média de 10 a 15 anos do implícito ou uma regressão contra os juros (p. 237–238).
- **Small cap**: Damodaran desaconselha somar prêmios ad hoc, que "abrem a porta" para somar prêmios por cada anomalia. Prefere ajustar o beta, por exemplo pela alavancagem operacional ([D] p. 283).

## 4. Passo a passo prático

1. Defina o investidor marginal e a moeda: local em R$ ([P]) ou global em US$ ([D]).
2. **Em US$, à Damodaran**: ERP maduro + CRP, com o CRP medido pelo spread soberano × (σ ações / σ título). Decida a exposição: igual, por β ou por λ ([D] p. 224–233).
3. **Em R$, à Póvoa**: um prêmio único fixado por julgamento (6,5% em 2012) sobre o Rf da NTN-B, sem somar risco-país à parte, porque ele já está no Rf local ([P] p. 210, 212–213).
4. **Checagem**: calcule o prêmio implícito do Ibovespa, com 3 a 5 anos de crescimento mais a perpetuidade, e compare com o prêmio adotado ([D] p. 234–236; [P] p. 250–252).
5. Mantenha o prêmio constante no período explícito. Na perpetuidade, ajuste só com justificativa e parcimônia ([P] p. 219–223).

## 5. Erros comuns apontados pelos autores

- **Usar prêmio histórico de janela curta**, com erro-padrão do tamanho do próprio prêmio ([D] p. 220).
- **Misturar T-bill e T-bond**: o prêmio tem de ser medido contra o mesmo título usado como Rf ([D] p. 220–221).
- **Usar prêmio histórico de mercado emergente** ([D] p. 224).
- **Dupla contagem do risco-país** via Rf soberano em dólar + prêmio + beta + haircut ([D] p. 229).
- **Somar prêmios de anomalias** (small cap, P/VP baixo etc.) ao Ke ([D] p. 283).
- **Acreditar que "o prêmio caiu para sempre"** em plena bolha, como na internet em 1997–2000 ([P] p. 208–209, 252).
- **Misturar o prêmio do brasileiro com o Rf do estrangeiro**, ou o contrário ([P] p. 228–229).

## 6. Onde concordam e onde divergem

**Concordam**: média geométrica; o histórico local de emergentes não serve; o prêmio implícito é informativo; o risco-país não é inteiramente diversificável.

| Ponto | Damodaran | Póvoa |
|---|---|---|
| Método principal | Histórico dos EUA + prêmio-país; implícito como alternativa corrente (p. 224, 234–238) | Número fixado por julgamento (4,5% em US$; 6,5% em R$) (p. 209–210) |
| Risco-país | Explícito, somado ao prêmio, com exposição λ (p. 227–233) | Embutido no Rf local (NTN-B) ou no EMBI em US$; **rejeita o λ** (p. 246–250) |
| Uso do implícito | Pode ser a estimativa do prêmio (p. 234–238) | Indicador de pontos de compra ou venda (p. 250–253) |
| Variação no tempo | O prêmio-país converge; o implícito varia com os juros (p. 231–232, 237–238) | Constante no explícito; corte pequeno na perpetuidade (p. 219–223) |

## 7. Limites: o que está defasado ou é específico do Brasil

- **Todos os números estão vencidos**: 5,51% (1928–2000), Brasil B2 com 4,83%, prêmio-país de 9,69% ([D]); 4,0–4,5% em US$ e 6,5% em R$ ([P]). Use o `MACRO.md`.
- **Erro interno em [D]**: o texto fala em prêmio maduro de 5,59% nas p. 232 e 282, mas as contas usam 5,51%.
- **Erro de título em [P]**: o cabeçalho da Tabela 6.5 (p. 210) diz "retorno do S&P e a Taxa Selic", mas a tabela usa o Ibovespa.
- **Especificidade brasileira**: juro real historicamente muito alto, cultura de fundos DI e um histórico Ibovespa × Selic negativo em quase todas as janelas ([P] p. 207, 210).
- Damodaran publica atualizações anuais do ERP implícito e dos prêmios-país depois de 2002, mas elas não estão nos livros **[NÃO VERIFICADO aqui]**.

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. Moeda-base em R$: **um prêmio único em R$** sobre o Rf da NTN-B, sem somar risco-país à parte, para não contar duas vezes.
2. Fixe o número no `MACRO.md`, com data, e justifique com **duas âncoras**: (i) o prêmio implícito corrente do Ibovespa, calculado pelo próprio canal; (ii) o prêmio maduro corrente de uma fonte pública + o diferencial de risco-país.
3. Publique a **sensibilidade** do preço justo a ±1 p.p. no prêmio (tema 32).
4. **Nada de prêmio de small cap ou de outras anomalias.** Se a empresa for pequena, ajuste o beta (alavancagem operacional, tema 20).
5. Prêmio constante no período explícito. Na perpetuidade, só mude com justificativa escrita.

## 9. Dúvidas abertas para você decidir

1. Prêmio em R$ fixado por julgamento (Póvoa) ou implícito do Ibovespa recalculado periodicamente?
2. Com que frequência atualizar: anual, semestral ou a cada valuation?
3. Vai usar λ (Damodaran) para exportadoras ou seguir Póvoa e rejeitá-lo? (ver tema 26)
4. Aceita algum ajuste de prêmio na perpetuidade?
