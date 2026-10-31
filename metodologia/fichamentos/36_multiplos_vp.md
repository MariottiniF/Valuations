# Fichamento 36: Múltiplos de patrimônio: P/VP e P/VP × ROE

**Fontes**
- **[D]** Damodaran (2002), Cap. 19 "Book Value Multiples" (PDF p. 718–759): prós e contras do valor contábil (p. 718–719); ajustes por recompras e aquisições (p. 720–721); distribuição (p. 722); P/VP pelos fundamentos, estável e em alto crescimento (p. 723–729); regressão P/VP × ROE no setor (p. 736–739) e no mercado (p. 740–743); ROE corrente × esperado (p. 743); estratégias de investimento e screens (p. 745–747); valor/capital contábil (p. 748–752); Q de Tobin (p. 753); resumo (p. 755). *Lido: estrutura, fórmulas e resumo; exemplos intermediários apenas mapeados.*
- **[P]** Póvoa (2012), Cap. 9, "P/VPA, tradição de um múltiplo de acionista" (p. 302–313): decomposição, exemplos de retenção e P/VP justo, regressões para o Brasil (empresas e bancos).

---

## 1. Conceito central

O P/VP compara o preço com o capital contábil dos acionistas. Seu principal determinante é o **ROE** em relação ao Ke: `P/VP = (ROE − g)/(Ke − g)` para uma empresa estável ([D] p. 724–725; [P] p. 303–304). ROE > Ke justifica P/VP > 1; ROE < Ke justifica P/VP < 1. O descasamento que interessa é **P/VP alto com ROE baixo** (possivelmente caro) ou **P/VP baixo com ROE alto** (possivelmente barato) ([D] p. 755). A versão da firma é **EV/capital contábil = (ROC − g)/(WACC − g)** ([D] p. 751).

## 2. Fórmulas

- **Estável** ([D] p. 723–725): `P/VP = ROE × payout × (1 + g)/(Ke − g)`. Com `g = (1 − payout) × ROE`, vira `(ROE − g)/(Ke − g)`.
- **DuPont no P/VP** ([P] p. 303): ROE = margem × giro do PL, então o P/VP depende de payout (+), ROE (+), g (+) e Ke (−).
- **Regressão setorial** ([D] p. 736): `P/VP = a + b × ROE`.
- **Regressão de [P] para abertas brasileiras, 2005–2012** (p. 309–310): `P/VP = 0,4366 + 0,0915 × ROE + 0,0034 × payout` (ROE e payout **em pontos percentuais**). Exemplo ✔: ROE 15 e payout 50 → 0,4366 + 1,3725 + 0,17 = **1,98**. *Notação: o livro escreve "0,0915 (15%)"; o cálculo só fecha usando 15, não 0,15.*
- **Bancos, 2006–2012** ([P] p. 310–312): só o ROE como variável explicativa, R² de 64%. Pede **ROE "recorrente ajustado"**: provisões padronizadas e sem não recorrentes.

## 3. Premissas e escolhas dos autores

- **Por que usar o VP** ([D] p. 718–719): é estável, simples, comparável entre empresas com práticas contábeis parecidas e utilizável em empresas com prejuízo.
- **Por que desconfiar** ([D] p. 719): depende de regras contábeis (depreciação, recompras, baixas), pode ser negativo e diz pouco em empresas de serviços e tecnologia, com poucos ativos tangíveis.
- **Recompras e aquisições** ([D] p. 720–721): recompras reduzem o PL e inflam o P/VP; ajuste antes de comparar.
- **ROE esperado, não corrente** ([D] p. 743): o P/VP reflete o ROE futuro.
- **P/VP baixo como estratégia** ([D] p. 745–747): há evidência de retorno adicional, mas é preciso combinar com ROE (screens de P/VP baixo **e** ROE alto).
- **Q de Tobin** ([D] p. 753): valor de mercado/custo de reposição, alternativa ao VP quando o contábil não reflete o ativo.
- **Brasil** ([P] p. 309): o PL contábil é pouco confiável por causa do período de alta inflação (1979–1994) e da correção monetária de balanço, que deixou marcas nas séries.
- **Distribuição no Brasil** ([P] p. 309): a fração de empresas com P/VP < 1 variou muito entre 2003 e 2012 (dados no livro).
- **P/VP justo por estágios** ([P] p. 304–307): ver tema 34 e as ressalvas sobre o exemplo têxtil.

## 4. Passo a passo prático

1. Use o P/VP principalmente para **bancos e seguradoras** (tema 44) e empresas intensivas em ativos tangíveis.
2. Projete o **ROE sustentável** (normalizado) e calcule o P/VP justo.
3. Faça o gráfico **P/VP × ROE dos pares** e posicione a empresa.
4. Ajuste o PL por recompras, ágio e intangíveis (tema 08).
5. Não use o P/VP em empresas de serviços, tecnologia ou com PL distorcido.

## 5. Erros comuns apontados pelos autores

- **"P/VP < 1 = barato"** ([D] p. 755, questão 1A): pode refletir ROE < Ke.
- **Usar o ROE corrente** em vez do esperado ([D] p. 743).
- **Ignorar recompras e aquisições** no PL ([D] p. 720–721).
- **ROE de bancos sem normalizar provisões** ([P] p. 311).

## 6. Onde concordam e onde divergem

**Concordam**: o ROE é o determinante dominante; P/VP justo pela fórmula; regressão P/VP × ROE como ferramenta.

| Ponto | Damodaran | Póvoa |
|---|---|---|
| Amostra | EUA (setor e mercado) | Brasil, empresas e bancos, 2005–2012 |
| Variáveis | ROE, payout, beta, g | ROE e payout; só ROE para bancos |
| Ajustes do PL | Recompras, aquisições | Herança inflacionária no Brasil |
| Extensão | EV/capital e Q de Tobin | Não trata |

## 7. Limites: o que está defasado ou é específico do Brasil

- Os coeficientes das regressões de [P] valem para 2005–2012; **não devem ser usados como estão** hoje, com outra Selic e outro custo de capital. Refaça a regressão com dados atuais.
- IFRS 9 (perdas esperadas) mudou a comparabilidade do ROE de bancos **[NÃO VERIFICADO nos livros]**.

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. P/VP como múltiplo principal **só para financeiras**; para as demais, como checagem do spread ROE − Ke.
2. Gráfico P/VP × ROE dos pares quando houver ao menos 5 empresas.
3. Atualizar a regressão do Brasil anualmente se o canal quiser usá-la.

## 9. Dúvidas abertas para você decidir

1. Manter uma regressão própria de P/VP × ROE para o Brasil?
2. Ajustar o PL por ágio (tangível) na comparação?
