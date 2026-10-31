# Fichamento 44: Empresas financeiras (bancos, seguradoras): a regra do DCF muda

> **Profundidade reduzida (○)**: tema fora da primeira empresa do canal. Baseado na estrutura do capítulo, nas seções de fundamentos e DDM e no resumo. As seções de FCFE por capital regulatório, excesso de retorno, ativos e múltiplos foram **apenas mapeadas**.

**Fontes**
- **[D]** Damodaran (2002), Cap. 21 "Valuing Financial Service Firms" (PDF p. 802–846): categorias (p. 802–803); dívida como matéria-prima (p. 804); regulação (p. 805); reinvestimento (p. 806); equity × firma (p. 807); DDM, com crescimento por retenção × ROE e ROE variável (p. 808–821); FCFE (p. 822 em diante, mapeado); resumo (p. 843).
- **[P]** Póvoa (2012): não há capítulo específico. Usa bancos na regressão de P/VP (Cap. 9, p. 310–312; tema 36) e no Índice de Basileia (Cap. 2, p. 60; tema 06).

---

## 1. Conceito central

Os princípios são os mesmos, mas em financeiras **a dívida é matéria-prima, não fonte de capital** ([D] p. 804, 843). Por isso, é difícil definir dívida, FCFF e WACC, e o mais simples é **avaliar o equity diretamente**, descontando fluxos do acionista ao Ke ([D] p. 807, 843). Capex e capital de giro não são observáveis: o reinvestimento está em despesas operacionais e, sobretudo, no **capital regulatório** exigido para crescer ([D] p. 806, 843). A **regulação** pode tanto proteger retornos acima do custo quanto limitá-los ([D] p. 805, 843).

## 2. Fórmulas

- **DDM** ([D] p. 808–809): VP dos dividendos esperados ao Ke.
- **Crescimento** ([D] p. 813): `g = retenção × ROE`; com ROE variável: `g = retenção × ROE_{t+1} + (ROE_{t+1} − ROE_t)/ROE_t`.
- **Payout estável** ([D] p. 814): `1 − g/ROE estável`.
- **Payout modificado** ([D] p. 815): (dividendos + recompras)/lucro, em média de vários anos.
- **FCFE de banco** (estrutura do capítulo, p. 822 em diante): lucro líquido − reinvestimento em capital regulatório (Δ patrimônio exigido para sustentar o crescimento dos ativos). **[Mapeado]**
- **P/VP justo**: `(ROE − g)/(Ke − g)` (tema 36).

## 3. Premissas e escolhas dos autores

- **Categorias** ([D] p. 802–803): bancos, seguradoras, bancos de investimento e corretoras, gestoras.
- **Múltiplos de equity** (P/L, P/VP) são mais adequados que múltiplos da firma ([D] p. 843), controlando risco, crescimento, fluxo e **qualidade da carteira de crédito**.
- **Póvoa** ([P] Cap. 9, p. 311): normalizar o ROE de bancos (provisões no mesmo nível de risco, sem não recorrentes) antes de comparar P/VP.

## 4. Passo a passo prático (resumido)

1. Valuation do equity: DDM ou FCFE com reinvestimento = capital regulatório.
2. Projete o crescimento da carteira, o ROE normalizado e o índice de capital (Basileia) exigido.
3. Ke pelo beta de bancos comparáveis (sem desalavancar).
4. Cheque com P/VP × ROE dos pares.

## 5. Erros comuns apontados pelos autores

- Usar FCFF/WACC em bancos ([D] p. 804, 807).
- Ignorar a regulação e o capital exigido ([D] p. 805–806).
- Comparar P/VP sem normalizar ROE e provisões ([P] p. 311).

## 6. Onde concordam e onde divergem

Concordam no foco em equity e na importância do ROE. Damodaran estrutura o método; Póvoa só trata de bancos via P/VP.

| Ponto | Damodaran | Póvoa |
|---|---|---|
| Método | DDM, FCFE regulatório, excesso de retorno | Regressão P/VP × ROE (Brasil) |

## 7. Limites: o que está defasado ou é específico do Brasil

- Basileia III, IFRS 9 e IFRS 17 (seguros) mudaram a leitura contábil e o capital regulatório **[NÃO VERIFICADO nos livros]**.
- No Brasil: JCP, crédito tributário sobre PDD, peso dos bancos públicos e regras do BC.

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. Metodologia separada para financeiras, a definir quando o canal cobrir bancos.
2. Padrão sugerido: FCFE com capital regulatório + checagem de P/VP × ROE.

## 9. Dúvidas abertas para você decidir

1. Quando o canal vai cobrir bancos e seguradoras?
2. Fazer um fichamento aprofundado do Cap. 21 nesse momento?
