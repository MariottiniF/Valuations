# Fichamento 27: Taxa de desconto e prêmio de risco implícitos ("fazer a conta ao contrário")

**Fontes**
- **[D]** Damodaran (2002), Cap. 7, "An Alternative Approach: Implied Equity Premiums" (PDF p. 234–239).
- **[P]** Póvoa (2012), Cap. 6, "Taxa de desconto e prêmio de risco implícitos, 'fazendo a conta ao contrário'" (p. 250–253).

---

## 1. Conceito central

Em vez de partir da taxa para chegar ao preço, parte-se do **preço de mercado** (de um índice ou de uma ação) e de fluxos projetados para descobrir **a taxa que o mercado está usando**. Subtraindo o Rf, obtém-se o **prêmio de risco implícito** ([D] p. 234; [P] p. 250). Para Damodaran, é uma forma de **estimar** o prêmio sem histórico, "market-driven and current" ([D] p. 235–236). Para Póvoa, é sobretudo um **termômetro de estresse e euforia**, que ajuda a identificar pontos de compra e venda ([P] p. 252–253).

## 2. Fórmulas

**Gordon (um estágio)** ([D] p. 234)
`P = D1 / (r − g)` → `r = D1/P + g` → `ERP = r − Rf`. Exemplo: S&P a 900, rendimento de 2%, g = 7% → r = 9%; com Rf de 6%, o ERP é 3%.

**Dois estágios** ([D] p. 235; [P] p. 250–251)
`P = Σ_{t=1}^{n} FC_t/(1+r)^t + [FC_{n+1}/(r − g_LP)]/(1+r)^n`, resolvendo para r.
- [D] S&P 500, 31/12/1999: índice 1.469, rendimento 1,68%, g = 10% por 5 anos e depois 6,5% → r = 8,56%; ERP = 2,06% ✔ (recalculado ≈ 8,59%).
- [D] Merval, 30/09/1998: r = 10,59%; ERP = 5,45% em US$ ([D] p. 236).
- [P] Ibovespa, ago/2011: 49 mil pontos, FC = 10% do índice, g = 12% por 3 anos e depois 7% → r = 19,1%; Rf = 10% → ERP = 9,1% ([P] p. 251–252) ✔. A 60 mil pontos (nov/2011): r = 16,9%; ERP = 6,9% ✔. *As duas contas só fecham se os 4.900 pontos forem o fluxo **corrente**, que cresce 12% já no ano 1.*

**Regressão do prêmio implícito** ([D] p. 238)
`ERP implícito = 1,87% + 0,2903 × T-Bond − 0,1162 × (T-Bond − T-Bill)`, com R² de 49% (EUA, 1960–2000). *Na nota 19 Damodaran usa 0,0182 no lugar de 1,87%, uma inconsistência pequena do texto.*

## 3. Premissas e escolhas dos autores

- **Supõe que o mercado está corretamente precificado** no agregado ([D] p. 234). A qualidade da estimativa depende do modelo e dos insumos ([D] p. 236).
- **Fluxo**: Damodaran usa dividendos ou fluxos para o acionista. Póvoa usa o **FCFE agregado do Ibovespa**, a média ponderada das projeções das corretoras, e nota que o FCFE (10%) era bem maior que o dividend yield (7%) ([P] p. 250–251).
- **Crescimento de longo prazo**: Damodaran iguala g ao Rf, supondo crescimento real igual ao juro real (nota 17). Póvoa usa o crescimento nominal potencial do PIB, ajustado pelo julgamento sobre a amostra do índice ([P] p. 251).
- **Prazo do estágio de crescimento**: 5 anos em [D]; 3 anos em [P], porque o cálculo é agregado e não precisa de mais de 5 ([P] p. 251).
- **Comportamento ao longo do tempo** ([D] p. 237–238): o implícito raramente chegou ao nível do histórico (média de ~4% em 40 anos); subiu nos anos 1970 com a inflação; caiu nos anos 1980 e 1990 e voltou a subir para 2,87% no fim de 2000. Há **reversão à média**: Damodaran sugere usar a média de 10 a 15 anos ou a regressão contra os juros.
- **Leitura de mercado** ([P] p. 252–253): implícito muito acima do "normal" (9,1% contra 6–6,5%) sugere ponto de compra, se os insumos forem confiáveis. Muito abaixo (Nasdaq em 2000, 1–1,5%) sugere bolha. O S&P em mar/2009 teve implícito de ~7,5%, contra 4–4,5% usuais, e dobrou em dois anos.

## 4. Passo a passo prático

1. Pegue o nível do índice (ou o valor de mercado da ação).
2. Projete o fluxo para o acionista do próximo ano, agregado (consenso) ou próprio.
3. Defina o crescimento de curto prazo (3 a 5 anos) e o de longo prazo (≤ crescimento nominal da economia, coerente com o Rf).
4. Resolva para r (por exemplo, com o Solver ou o goal seek).
5. ERP implícito = r − Rf, na mesma moeda e no mesmo regime.
6. Compare com o prêmio adotado no `MACRO.md` e com a série histórica do próprio implícito.

## 5. Erros comuns apontados pelos autores

- **Tratar o implícito de um dia como verdade**: ele oscila muito mais que o histórico ([D] p. 236).
- **Inventar teorias para justificar um implícito baixíssimo** (bolhas) ([P] p. 252).
- **Comparar níveis "cabalísticos" do índice ou múltiplos atuais com históricos** sem conectá-los ao ambiente de juros e crescimento ([P] p. 250).
- **Achar que o modelo dá o timing**: ele indica distorção, mas não diz quando ela se corrige (Buffett na bolha de 2000, [P] p. 252–253).

## 6. Onde concordam e onde divergem

**Concordam**: a mecânica, o valor do implícito como informação corrente e o perigo de um prêmio baixo em bolhas.

| Ponto | Damodaran | Póvoa |
|---|---|---|
| Função principal | **Estimativa** do prêmio a usar (p. 235–238) | **Termômetro** e sinal de compra ou venda (p. 252–253) |
| Fluxo | Dividendos ou fluxos de caixa (p. 234–235) | FCFE agregado (p. 250–251) |
| g de longo prazo | = Rf (nota 17) | Crescimento potencial do PIB nominal (p. 251) |
| Suavização | Média de 10–15 anos ou regressão (p. 238) | Não propõe |

## 7. Limites: o que está defasado ou é específico do Brasil

- Todos os números (S&P 1999–2000, Merval 1998, Ibovespa 2011) estão vencidos.
- No Brasil, o FCFE agregado depende das projeções das corretoras, e o dividend yield pode divergir bastante do FCFE ([P] p. 251).
- Damodaran publica fora do livro uma série mensal do prêmio implícito do S&P **[NÃO VERIFICADO aqui]**.

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. **Calcular e publicar periodicamente o prêmio implícito do Ibovespa**, com a planilha aberta, como **checagem** do prêmio adotado (tema 19).
2. **Mesmo exercício para cada empresa analisada**: a "taxa implícita no preço atual" mostra o retorno que o mercado está pedindo. Bom para os vídeos: "a esse preço, você está aceitando X% ao ano".
3. Definir uma regra: se |ERP implícito − ERP adotado| > 2 p.p., documentar a discussão no vídeo, sem mudar automaticamente o prêmio.

## 9. Dúvidas abertas para você decidir

1. O implícito vira **o** prêmio do canal ou só uma checagem?
2. Fonte do FCFE agregado: consenso de mercado ou projeção própria?
3. Publicar a "taxa implícita no preço" de cada empresa como métrica padrão dos vídeos?
