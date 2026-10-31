# Fichamento 47: Opções reais

> **Profundidade reduzida (○)**: lidos os resumos de [D] Caps. 5, 28, 29 e 30 e, em [P] Cap. 11, a estrutura, os exemplos principais e as limitações. A derivação dos modelos (binomial, Black-Scholes) não foi refeita.

**Fontes**
- **[D]** Damodaran (2002): Cap. 5 "Option Pricing Theory and Models" (PDF p. 121–151; resumo p. 148); Cap. 28 "The Option to Delay" (p. 1090–1123; resumo p. 1120): patentes, reservas não desenvolvidas, terrenos; Cap. 29 "The Options to Expand and Abandon" (p. 1124–1154; resumo p. 1151); Cap. 30 "Valuing Equity in Distressed Firms" (p. 1155–1175; resumo p. 1172).
- **[P]** Póvoa (2012), Cap. 11 "Opções reais, a flexibilidade precificada" (p. 425–452): conceito e paradoxo da volatilidade (p. 425–430); como precificar (p. 430–434); usos (p. 434–435); exemplos: reserva de petróleo e patente de remédio (p. 435–448); limitações (p. 448–452).

---

## 1. Conceito central

Uma opção é um ativo cujo payoff depende de outro ativo. Seu valor é função de seis variáveis: valor do ativo-objeto, variância, preço de exercício, prazo, taxa livre de risco e dividendos (ou custo de esperar) ([D] Cap. 5, p. 148). Em valuation, as **opções reais** aparecem quando há direito, mas não obrigação, de investir, expandir, adiar ou abandonar ([D] Caps. 28–29). Um projeto de VPL negativo hoje pode valer algo se houver chance de ficar positivo, e essa chance cresce com a **volatilidade** (o "paradoxo da volatilidade criando valor", [P] p. 425). O equity de uma empresa em dificuldade é uma **call** sobre os ativos (responsabilidade limitada), e por isso pode ter valor mesmo com ativos abaixo da dívida ([D] Cap. 30, p. 1172).

## 2. Fórmulas

- **Black-Scholes com dividendo/custo de espera** (usado em [P] p. 437–438): `C = S × e^(−y×t) × N(d1) − K × e^(−r×t) × N(d2)`.
- **Exemplo da reserva de petróleo de [P]** (p. 437–438) ✔:
  - prazo de 12 anos, custo de esperar de 1/12 = 8,33% a.a., r = 15%: `40 × e^(−0,0833×12) × 0,7441 − 100 × e^(−0,15×12) × 0,2078 ≈ 10,95 − 3,44 = R$ 7,5 mi`;
  - prazo de 10 anos (redução de 2 anos pelo governo), custo de esperar de 10%: `40 × e^(−1) × 0,6410 − 100 × e^(−1,5) × 0,1632 ≈ 9,43 − 3,64 = R$ 5,8 mi`.
- **Valor de uma mineradora ou petroleira** ([P] p. 435): reservas em produção (DCF) + opção sobre reservas em desenvolvimento + opção sobre reservas provadas não desenvolvidas.
- **Patente** ([P] p. 438–439; [D] Cap. 28): S = VP dos ganhos (R$ 1,5 bi), K = custo de desenvolvimento (R$ 1,1 bi), prazo até o fim da patente, volatilidade de 35% (proxy).

## 3. Premissas e escolhas dos autores

- **Adiar** ([D] p. 1120): patentes não exploradas, reservas não desenvolvidas, terrenos. O custo de esperar entra como "dividendo".
- **Expandir** ([D] p. 1151): pode justificar um investimento inicial de VPL negativo; vale mais com **exclusividade** e cai com a perda de vantagem competitiva. Pode haver prêmio sobre o DCF de empresas com potencial de entrar em novos mercados.
- **Abandonar** ([D] p. 1151): reduz a exposição aos piores resultados.
- **Equity em dificuldade** ([D] p. 1172): call sobre a firma com prazo igual ao da dívida; tem "prêmio de tempo".
- **Limitações** ([P] p. 448–452):
  - **volatilidade** difícil de estimar, sobretudo em empresas fechadas;
  - **variância instável** (modelos ARCH ajudam);
  - **choques discretos**: Black-Scholes falha com saltos (caso LTCM, 1998);
  - **"aceitar qualquer projeto"**: volatilidade e prazo sempre ajudam a aprovar projetos, o que reduz a seletividade.
- [D] Cap. 2 (p. 30–33; tema 02): opções sobre ativos não negociados exigem estimar valor e variância, com erro grande.

## 4. Passo a passo prático (uso restrito)

1. Use opções só quando houver **direito exclusivo** e incerteza relevante: reservas não desenvolvidas, patentes, licenças, terrenos, expansão exclusiva.
2. Não some opções a todo DCF: o crescimento normal já está nos fluxos.
3. Prefira **cenários com probabilidade** (árvore de decisão) à Black-Scholes quando a volatilidade for pouco confiável.
4. Para empresas muito alavancadas, cheque o valor do equity como opção (Cap. 30).

## 5. Erros comuns apontados pelos autores

- **Contar a mesma flexibilidade duas vezes** (no DCF e na opção).
- **Volatilidade arbitrária** ([P] p. 448–449).
- **Usar opções para justificar qualquer projeto** ([P] p. 450–451).
- **Opção de expansão sem exclusividade** ([D] p. 1151).

## 6. Onde concordam e onde divergem

**Concordam** nos usos (adiar, expandir, abandonar, patentes, reservas) e no cuidado com a volatilidade.

| Ponto | Damodaran | Póvoa |
|---|---|---|
| Extensão | Quatro capítulos, com equity em dificuldade | Um capítulo com exemplos brasileiros |
| Postura | Usar com parcimônia, onde há exclusividade | Destaca limitações e o risco de excesso |

## 7. Limites: o que está defasado ou é específico do Brasil

- Exemplos com Rf de 15% ([P]).
- No Brasil: pré-sal, blocos de exploração, licenças de mineração, landbank de incorporadoras.

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. Opções reais **fora do valor-base**; apresentadas como "valor adicional possível", com cenário.
2. Para petroleiras e mineradoras: reservas em produção no DCF; recursos não desenvolvidos por cenário ou opção, separados.

## 9. Dúvidas abertas para você decidir

1. Incluir opções reais no preço-alvo ou só como upside separado?
2. Método padrão: árvore de cenários ou Black-Scholes?
