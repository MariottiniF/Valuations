# Fichamento 17: Risco e retorno: CAPM, APT e modelos multifatoriais

**Fontes**
- **[D]** Damodaran (2002), Cap. 4 "The Basics of Risk": definição de risco, risco diversificável × de mercado, investidor marginal, CAPM, APM, modelos multifatoriais, modelos proxy e análise comparativa (PDF p. 81–107). Cap. 7, Tab. 7.1 (p. 217–218).
- **[P]** Póvoa (2012), Cap. 6: "Regras básicas" (p. 179–180), "O modelo de arbitragem de preços" (p. 180–182), "CAPM, o modelo mais usado pelo mercado" (p. 183–186) e "O beta como mensurador do último risco que resta no modelo CAPM" (p. 195–196).

---

## 1. Conceito central

Risco, em finanças, é a **dispersão dos retornos efetivos em torno do retorno esperado**, para cima ou para baixo ([D] p. 82–86; [P] p. 178). Parte desse risco é **específica da empresa** (projeto, concorrência, setor) e desaparece com a diversificação. Outra parte é **de mercado** (juros, inflação, ciclo econômico) e não desaparece ([D] p. 89–92; [P] p. 195–196). Como o **investidor marginal**, o que forma o preço, é diversificado, **só o risco de mercado é remunerado** ([D] p. 92–93). Os modelos diferem só em **como medir o risco de mercado**: um fator (CAPM), fatores estatísticos (APM), fatores macroeconômicos (multifatorial) ou proxies empíricas (modelos de regressão como Fama-French) ([D] p. 93–104). Os dois autores concluem que o **CAPM, usado com critério**, continua sendo a melhor relação custo-benefício ([D] p. 107; [P] p. 183, 182).

## 2. Fórmulas

**Variância de uma carteira de dois ativos** ([D] p. 92)
`σ²p = wA² σ²A + (1−wA)² σ²B + 2 wA (1−wA) ρAB σA σB`. O ganho da diversificação cresce quanto menor a correlação ρ.

**Beta (CAPM)** ([D] p. 96–97)
`βi = Cov(Ri, Rm) / σ²m`. O beta do mercado é 1, o do ativo livre de risco é 0.

**CAPM** ([D] p. 97; [P] p. 184)
`E(Ri) = Rf + βi [E(Rm) − Rf]`. Exemplo de [P]: 9,8% + 0,8 × 7% = **15,4%** a.a. (fim de 2011) ([P] p. 185) ✔.

**APM** ([D] p. 99–100; [P] p. 181)
`R = E(R) + Σ βj Fj + ε` e `E(R) = Rf + Σ βj [E(Rj) − Rf]`. O CAPM é o caso particular com um único fator, a carteira de mercado ([D] p. 101; [P] p. 183).
Exemplo de [P] para uma petroleira: E(r) = Rf + 0,9 × petróleo + 0,5 × PIB mundial − 0,6 × estoques + 0,3 × câmbio ([P] p. 181–182).

**Multifatorial macroeconômico** ([D] p. 102): fatores de Chen, Roll e Ross (1986): produção industrial, prêmio de default, inclinação da curva, inflação não esperada e juro real.

**Modelo proxy (Fama-French)** ([D] p. 103)
`R_t (mensal) = 1,77% − 0,11 ln(MV) + 0,35 ln(BV/MV)`

## 3. Premissas e escolhas dos autores

- **Hipóteses do CAPM** ([D] p. 94–95; [P] p. 183): sem custos de transação, ativos divisíveis e negociáveis, informação simétrica e diversificação total possível. Daí sai a carteira de mercado com todos os ativos, e o investidor só escolhe a proporção entre ativo livre de risco e mercado. Póvoa lista quatro hipóteses: sem custos de transação, liquidez total, simetria de informação e diversificação total do risco específico.
- **Investidor marginal diversificado** ([D] p. 93): o argumento é forte onde negociar é barato e os institucionais dominam, e fraco em ativos pouco negociados (imóveis, empresas fechadas).
- **O risco de mercado é inescapável** ([P] p. 195–196): o investidor pode diversificar empresa, setor, país e classe de ativo, mas 2008 mostra que sobra um risco sistêmico. "O beta nada mais é do que a tentativa matemática […] de replicar o risco não diversificável" ([P] p. 196).
- **Por que o CAPM sobrevive** ([D] p. 104–107):
  - Roll (1977): o CAPM é intestável porque a carteira de mercado não é observável.
  - Fama e French (1992): não acham relação entre beta e retorno em 1963–1990. Isso foi contestado por Amihud et al. (1992), Kothari e Shanken (1995, com dados anuais) e Chan e Lakonishok (1993, para 1926–1991, onde a relação só quebra depois de 1982 e o beta funciona bem em crises extremas).
  - Modelos multifatoriais **explicam melhor o passado**, mas o **erro de estimação** de vários betas e prêmios anula o ganho na **previsão** ([D] p. 106).
- **Críticas ao APM** ([P] p. 182): as relações entre fatores e preço mudam rápido (por exemplo, Petrobras × petróleo), há defasagens na divulgação (PIB trimestral) e são "vários betas" com margem de erro perigosa. O custo marginal não compensa. O APM também esquece as preferências de risco do comprador.
- **Quando o CAPM erra mais** ([D] p. 104–105): ativos expostos a fatores pouco representados no índice. Exemplo: petroleiras, cujo Ke foi de 14,4% pelo CAPM e 19,1% pelo APM (Weston e Copeland, nota 6).
- **Regras de consistência** ([P] p. 179–180): mesma moeda, mesmo regime nominal ou real, FCFF com WACC e FCFE com Ke (ver temas 18 e 23).
- **Taxa de desconto = retorno exigido** ([P] p. 184): quanto maior o risco, maior o retorno exigido e menor o preço justo. Pagar acima do preço justo é aceitar implicitamente um retorno menor ([P] p. 185).

## 4. Passo a passo prático

1. Defina o **investidor marginal** e, portanto, a carteira de referência: local ou global ([D] p. 93).
2. Use o **CAPM** como padrão: Rf (tema 18) + β (tema 20) × prêmio (tema 19).
3. Se a empresa depender fortemente de um fator mal representado no índice (commodity, câmbio), **trate esse fator no fluxo de caixa**, com cenários de preço, e não com fatores extras na taxa. É a lição do caso das petroleiras ([D] p. 104–105), adaptada à cautela de [P] p. 182.
4. Não some prêmios de anomalias (tamanho, P/VP) ao CAPM ([D] Cap. 8, p. 283; tema 19).

## 5. Erros comuns apontados pelos autores

- **Remunerar risco diversificável** quando o investidor marginal é diversificado ([D] p. 92–93).
- **Confundir a capacidade de explicar o passado com a capacidade de prever** ([D] p. 106).
- **Usar o APM ou modelos multifatoriais como se as relações fossem estáveis** ([P] p. 182; [D] p. 102).
- **Achar que um proxy que funcionou num período continua funcionando** (por exemplo, o tamanho) ([D] p. 106).

## 6. Onde concordam e onde divergem

**Concordam**: a separação entre risco diversificável e de mercado; o CAPM como padrão de mercado; o APM é mais rico na teoria, mas caro e instável na prática; o CAPM é caso particular do APM.

| Ponto | Damodaran | Póvoa |
|---|---|---|
| Evidência empírica | Discute Roll, Fama-French e os contra-argumentos (p. 105–106) | Não discute os testes; argumenta pelo custo-benefício (p. 182–183) |
| Modelos proxy | Apresenta Fama-French (p. 103) | Não trata |
| Preferências do comprador | O investidor marginal define o risco relevante | Enfatiza que o retorno exigido depende **do investidor** (p. 182, 213–216) |

## 7. Limites: o que está defasado ou é específico do Brasil

- A literatura citada vai até meados dos anos 1990. Há desenvolvimentos posteriores (modelos de 3, 4 e 5 fatores de Fama-French, entre outros) que **não estão nos livros [NÃO VERIFICADO aqui]**.
- No Brasil, os índices concentrados (Ibovespa) são uma proxy ainda pior da "carteira de mercado" ([P] p. 198; tema 20).
- A ideia de Póvoa de que "cada investidor tem a sua taxa" (p. 213–216) é útil no Brasil, onde o investidor local e o estrangeiro enfrentam Rf e prêmios diferentes.

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. **Modelo de risco: CAPM**, com investidor marginal **local em R$** (temas 18 e 19).
2. Riscos específicos (regulatório, de execução, de commodity) entram **nos cenários do fluxo**, não na taxa.
3. Reserve um parágrafo da metodologia para explicar ao público **por que** o canal não usa modelos multifatoriais: transparência e custo-benefício, com base em [D] p. 106–107 e [P] p. 182.

## 9. Dúvidas abertas para você decidir

1. Investidor marginal local (R$) ou global (US$) como padrão?
2. Algum tratamento especial para empresas de commodity: cenários no fluxo ou fator na taxa?
