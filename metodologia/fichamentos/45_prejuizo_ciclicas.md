# Fichamento 45: Prejuízo, cíclicas e start-ups: normalização e valuation com earnings negativos

> **Profundidade intermediária (◐)**: lidos a estrutura e os resumos dos dois capítulos; seções de cíclicas e commodities mapeadas pelos títulos e fórmulas. Os exemplos não foram recalculados.

**Fontes**
- **[D]** Damodaran (2002), Cap. 22 "Valuing Firms with Negative Earnings" (PDF p. 847–890): consequências e causas (p. 847–851); problemas temporários (p. 852–855); setor ou mercado (p. 855); **cíclicas** (p. 856–861); visão macro (p. 861); **commodities e recursos naturais** (p. 861–866); múltiplos com lucro normalizado (p. 866); problemas de longo prazo: estratégicos, operacionais (p. 867–871); privatizações e golden shares (p. 872–873); alavancagem: excesso de dívida com e sem risco de falência (p. 874–880); resumo (p. 885). Cap. 23 "Valuing Young or Start-up Firms" (p. 891–927): **lido o resumo** (p. 925).
- **[P]** Póvoa (2012): não há capítulo específico. Ver Cap. 4, casos complicados (p. 125–129; tema 02), e Cap. 10, crise de 2008 e continuidade (p. 422; tema 43).

---

## 1. Conceito central

O DCF é **flexível o bastante** para empresas com prejuízo, cíclicas e jovens ([D] p. 885, 925). O tratamento depende da **causa** do prejuízo ([D] p. 849–852, 885):
- **temporário** (ciclo, choque): normalize o lucro;
- **estrutural** (estratégia, operação, alavancagem): projete o caminho de volta (ou não) para margens sustentáveis, julgando **se e quando** o problema se resolve;
- **risco relevante de falência**: considere o valor de liquidação e a probabilidade de quebra.

Em **cíclicas e commodities**, não ajustar o lucro ao ciclo leva a **subavaliar no fundo da recessão e superavaliar no pico** ([D] p. 885). Em empresas jovens, a pergunta não é se é possível avaliar, mas se aceitamos estimativas **ruidosas**. O ruído reflete incerteza real ([D] p. 925).

## 2. Fórmulas

- **Lucro normalizado de cíclica** ([D] p. 856–860): média do lucro ao longo do ciclo, ou **margem média × receita atual**, ou crescimento a partir de um lucro normalizado.
- **Commodities** ([D] p. 864): `receita reajustada = receita atual × (preço médio normalizado/preço atual)`; ROC normalizado no reinvestimento (p. 865).
- **Margem-alvo** (problemas operacionais e start-ups) ([D] p. 870–871; resumo do Cap. 23): margem converge da atual para a sustentável (dos pares) ao longo da fase explícita; reinvestimento via receita/capital (sales-to-capital).
- **Falência** ([D] p. 878–880, mapeado): `valor = valor de continuidade × (1 − p) + valor de liquidação × p`.

## 3. Premissas e escolhas dos autores

- **Distinguir temporário de estrutural** ([D] p. 851): histórico da empresa, desempenho do setor, causa identificável.
- **Macro e valor** ([D] p. 861): a valuation de cíclicas embute uma visão sobre a economia; seja explícito sobre ela.
- **Problemas estratégicos** ([D] p. 867–869): o caso IBM (perda da dominância em mainframes); a qualidade da gestão é crucial para a recuperação.
- **Privatizações** ([D] p. 872–873): o valor depende da melhoria esperada de eficiência e de restrições como golden shares.
- **Alavancagem excessiva** ([D] p. 874–880): sem risco iminente, o WACC deve refletir a trajetória da dívida; com risco alto, o equity pode valer como opção (tema 47).
- **Start-ups** ([D] p. 925): usar dados de comparáveis no lugar do histórico; margens e crescimento por convergência a um estado estável.

## 4. Passo a passo prático (cíclicas, comum no Ibovespa)

1. Identifique o ciclo: commodity (minério, petróleo, celulose, aço) ou economia (varejo, construção).
2. Calcule a **margem média do ciclo** (10 anos) e o preço normalizado da commodity.
3. Projete a fase explícita com a curva de preços (futuros ou consenso) convergindo ao preço normalizado.
4. Perpetuidade com **margem e ROIC normalizados**, nunca os do pico ou do fundo.
5. Múltiplos sobre o **lucro normalizado** ([D] p. 866).
6. Sensibilidade ao preço da commodity e ao câmbio (tema 32).

## 5. Erros comuns apontados pelos autores

- **Perpetuar o pico ou o fundo** ([D] p. 885).
- **Tratar prejuízo estrutural como temporário** ([D] p. 851).
- **Ignorar a probabilidade de falência** ([D] p. 878–880).
- **Desistir de avaliar** empresas jovens pelo ruído ([D] p. 925).

## 6. Onde concordam e onde divergem

Póvoa não trata o tema em capítulo próprio; sobre continuidade, sugere limitar a perpetuidade quando a sobrevivência for duvidosa ([P] p. 422), o que é compatível com a probabilidade de falência de [D].

| Ponto | Damodaran | Póvoa |
|---|---|---|
| Cíclicas | Normalização por média do ciclo ou da margem | Não trata em detalhe |
| Falência | Probabilidade × valor de liquidação | Limitar a perpetuidade |

## 7. Limites: o que está defasado ou é específico do Brasil

- O Ibovespa tem peso grande de cíclicas (Vale, Petrobras, siderúrgicas, papel e celulose) e de empresas com dividendos altos no pico do ciclo.
- Recuperações judiciais no Brasil (Oi, Americanas) exigem análise da recuperação e de credores **[fora dos livros]**.

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. **Cíclicas**: lucro, margem e ROIC normalizados na perpetuidade; preço de commodity normalizado declarado (fonte e janela).
2. **Empresas com prejuízo**: classificar a causa (temporária, estrutural, alavancagem) e justificar a margem-alvo.
3. Cenário de falência obrigatório quando dívida líquida/EBITDA for muito alta ou houver recuperação judicial.

## 9. Dúvidas abertas para você decidir

1. Janela padrão para normalizar cíclicas (10 anos? um ciclo completo?).
2. Fonte do preço normalizado de commodities.
