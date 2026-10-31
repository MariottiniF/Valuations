# Fichamento 25: Taxa de desconto variando no tempo ("escadinha", pré-perpetuidade × perpetuidade)

**Fontes**
- **[D]** Damodaran (2002), Cap. 7, sobre taxas por ano e curvas inclinadas (PDF p. 212), convergência do prêmio-país (p. 231–232) e reversão à média do prêmio implícito (p. 238). Cap. 15, condições da firma estável (p. 537–538) e exemplos de Gap, Amgen e Embraer com WACC em transição (p. 545, 549–550, 553–554).
- **[P]** Póvoa (2012), Cap. 6, "Taxa de desconto no período pré-perpetuidade" (p. 217–220), "Taxa de desconto na fase da perpetuidade" (p. 220–227) e "Escadinha no WACC" (p. 245–246). Cap. 7, p. 267–268.

---

## 1. Conceito central

A pergunta é se a taxa de desconto deve mudar ao longo da projeção. A resposta dos dois autores é: **sim, mas só pelo que muda de verdade na empresa** (estrutura de capital, maturidade, risco) e, com parcimônia, na passagem para a perpetuidade. **Não** por apostas sobre a trajetória dos juros, que o mercado já embute nas taxas longas ([P] p. 217–220). Damodaran faz a transição de beta, D/(D+E), prêmio-país e Kd linearmente até os valores da firma estável ([D] p. 549–550, 553–554). Póvoa permite a "escadinha" no WACC pela estrutura de capital, proíbe a escadinha no Rf e no prêmio do explícito e admite um ajuste limitado (±1–2 p.p.) na perpetuidade ([P] p. 220–227, 245–246).

## 2. Fórmulas

**Desconto com taxa variável** (consequência direta dos dois livros)
`VP = Σ_t FCF_t / Π_{k=1}^{t} (1 + r_k)`. Com taxa variável, o fator de desconto é o **produto acumulado** das taxas de cada ano, e não `(1 + r_t)^t`.

**Valor terminal com taxa da perpetuidade** ([D] p. 542)
`TV_n = FCFF_{n+1}/(WACC_estável − g)`, descontado ao presente pelo produto das taxas do explícito.

**Exemplos**
- [D] Gap: WACC de 9,06% no explícito e 8,43% na perpetuidade (beta 1,2 → 1,0) ([D] p. 545).
- [D] Amgen: WACC de 10,76% → 8,86% (beta 1,35 → 1,0; D/(D+E) de 0,55% → 10%), em transição linear nos anos 6 a 10 ([D] p. 549–550).
- [D] Embraer (real): WACC de 16,79% → 12,74% (prêmio-país de 10,24% → 5,37%; Kd de 10,62% → 7,50%) ([D] p. 553).
- [P] Fumo: Ke de **14,5%** nos anos 1 a 5 (NTN-B 2017) e **13,2%** na perpetuidade (Rf 9,5%, prêmio 6,2%), contra **14,0%** constante (NTN-B 2050). Valor de R$ 1.270.415 contra R$ 1.232.987, só 3% de diferença ([P] p. 221–224).
- [P] EUA 2011: Ke de 6,3% (Treasury de 1,8%) no explícito e 8,5% (Rf de 4%) na perpetuidade. Com a taxa constante, o valor sai 53% maior. A "alternativa 4" (8,5% em todo o fluxo) dá 9% menos que a alternativa 3 ([P] p. 225–226).

## 3. Premissas e escolhas dos autores

- **Rf no explícito**: título com vencimento próximo ao horizonte, **sem escadinha**. A taxa longa é a média das curtas esperadas mais um prêmio ([P] p. 217–219). Exceções extremas, como o risco-Brasil de 20% em 2002, são decisões de **gestão** e não de valuation ([P] p. 218–219). Damodaran admite taxas por ano se a curva for muito inclinada ([D] p. 212).
- **Beta no explícito**: muda só se houver mudança planejada de estrutura de capital ([P] p. 219–220). Póvoa rejeita "betas mistos" projetados por mudança de negócio e prefere encurtar a regressão quando o mercado começa a perceber a mudança ([P] p. 219). Damodaran aceita: o bottom-up reflete o mix de negócios futuro ([D] Cap. 8, p. 269), e na transição o beta converge para ~1 ([D] p. 538, 549).
- **Prêmio no explícito**: não se projeta mudança ("subjetivo em cima do subjetivo") ([P] p. 219–220). Damodaran faz o **prêmio-país** cair ao longo do tempo ([D] p. 231–232, 553).
- **Kd e pesos**: podem mudar ano a ano conforme o plano de estrutura de capital ([P] p. 245–246; [D] p. 549–550).
- **Perpetuidade** ([P] p. 220–227): há três alternativas.
  1. Taxa única em todo o fluxo: tecnicamente correta.
  2. Escadinha só pelo beta, repetindo a taxa do último ano: correta.
  3. **A preferida de Póvoa**: escadinha pelo beta e, na perpetuidade, ajuste parcimonioso de Rf e prêmio para o "equilíbrio", com limite informal de **±2 p.p.** em relação ao último ano explícito.
  A alternativa 4 (usar só as taxas de equilíbrio em todo o fluxo) é criticada porque ignora a taxa negociada ([P] p. 226).
- **O ajuste não é viés de alta**: no Brasil de 2012 ele reduzia o Ke; nos EUA e no Japão, aumentava ([P] p. 224–227).
- **Firma estável** ([D] p. 537–538): beta entre 0,8 e 1,2, reinvestimento coerente com g e ROIC, e WACC de firma madura.

## 4. Passo a passo prático

1. Fixe o Rf e o prêmio correntes para todo o período explícito.
2. Projete o D/(D+E) ano a ano (plano da empresa ou convergência para o setor) e, com ele, o beta (Hamada), o Kd (rating) e o WACC_t.
3. Defina os parâmetros da firma estável: beta perto de 1, D/(D+E)-alvo, prêmio-país convergido (se em US$).
4. Se fizer a transição, use interpolação **linear** entre o fim do alto crescimento e a perpetuidade ([D] p. 550, 554).
5. Na perpetuidade, ajuste o Rf e o prêmio só se estiverem visivelmente fora do equilíbrio, com no máximo ±2 p.p. em relação ao último ano ([P] p. 223, 227).
6. **Desconte com o fator acumulado** Π(1 + r_k).

## 5. Erros comuns apontados pelos autores

- **"Escadinha" decrescente no Rf** por expectativa de queda de juros ([P] p. 217).
- **Usar uma taxa curta (por exemplo, a NTN-B 2017) para todo o fluxo**, perpetuidade incluída ([P] p. 224).
- **Perpetuar uma taxa em desequilíbrio**, como juro real negativo nos EUA em 2011 ([P] p. 225).
- **Projetar mudanças no prêmio** no explícito ([P] p. 219–220).
- **Manter na perpetuidade o beta e o WACC da fase de alto crescimento** ([D] p. 538).

## 6. Onde concordam e onde divergem

| Ponto | Damodaran | Póvoa |
|---|---|---|
| Rf por ano | Admite se a curva for muito inclinada (p. 212) | Não; o título longo já embute a trajetória (p. 217–219) |
| Beta em transição | Converge para ~1 na firma estável (p. 538, 549) | Só por estrutura de capital; mantém o beta do último ano na perpetuidade (p. 221, 223) |
| Prêmio | O prêmio-país converge (p. 231–232, 553) | Constante no explícito; corte leve na perpetuidade (p. 223) |
| Ajuste na perpetuidade | Implícito na transição para a firma estável | Explícito, limitado a ±2 p.p. (p. 223, 227) |

## 7. Limites: o que está defasado ou é específico do Brasil

- Exemplos de 2001 (D) e 2011–2012 (P), com NTN-B, Treasury e DI futuro da época.
- A ideia de ±2 p.p. é uma **regra informal do autor**, sem base empírica apresentada.
- O debate brasileiro sobre "juros reais vão cair" é recorrente. A regra de Póvoa protege contra o otimismo de juros, mas a percepção do equilíbrio de longo prazo muda.

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. **Período explícito**: Rf e prêmio constantes (correntes). WACC variável só por estrutura de capital documentada.
2. **Perpetuidade**: beta realavancado pelo D/(D+E)-alvo. Rf = NTN-B mais longa, com ajuste máximo de ±1 p.p. e justificativa escrita.
3. **Desconto acumulado** na planilha, com coluna de fator Π(1 + r).
4. **Sensibilidade obrigatória** de WACC da perpetuidade × g (tema 32), porque é onde está a maior parte do valor.

## 9. Dúvidas abertas para você decidir

1. Beta convergindo para 1 na perpetuidade (Damodaran) ou mantido no último valor (Póvoa)?
2. Limite de ajuste na perpetuidade: 0, ±1 ou ±2 p.p.?
3. Transição linear em estágio intermediário (3 estágios) ou corte direto (2 estágios)? (ver tema 13)
