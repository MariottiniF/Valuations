# Fichamento 32: Análise de sensibilidade (g × taxa de desconto), cenários, simulação

**Fontes**
- **[P]** Póvoa (2012), Cap. 4: "Mito 1" (p. 97), "O ponto mais importante da valuation…" (p. 104–105), "Sensibilidade na taxa de crescimento" (p. 106–107), "Sensibilidade na taxa de desconto" (p. 107–109) e "Sensibilidade combinada" (p. 109–113). Cap. 5, "Onde eu errei?" (p. 157–158), TIR ao preço de mercado (p. 145–147) e "Análise de sensibilidade – como trabalhar os catalisadores em diversos cenários" (p. 172–175).
- **[D]** Damodaran (2002): os capítulos citados na lista (Cap. 2, 5 e 16) **não têm uma seção específica de análise de sensibilidade ou simulação** nos trechos que examinei por busca de termos. Uso as passagens relacionadas: sensibilidade do modelo estável (Cap. 15, p. 538), ligação entre reinvestimento e g, que reduz a sensibilidade (Cap. 12, p. 438), fluxos esperados que já incorporam cenários e ajuste de sobrevivência (Cap. 12, p. 445–446) e a sensibilidade do APV às hipóteses de falência (Cap. 15, p. 587). **[O Cap. 5, sobre opções, não foi lido em detalhe para este tema.]**

---

## 1. Conceito central

O DCF não produz um número exato. Ele produz uma **região** de preço justo, e é por isso que os testes de sensibilidade são centrais ([P] p. 97, 145). As duas variáveis que mais mexem no valor são o **crescimento** e a **taxa de desconto**, principalmente na **perpetuidade** ([P] p. 104–109). Damodaran acrescenta que a sensibilidade a g é **exagerada quando o reinvestimento não está ligado a g**: com reinvestimento = g/ROC, o efeito de g depende só do excesso de retorno (ROC − WACC) ([D] p. 438). Póvoa defende sensibilidade **focada nos 2 ou 3 "catalisadores"** da empresa, com cenários, e é cético quanto à ponderação estatística de cenários ([P] p. 172–175).

## 2. Fórmulas e exemplos

**Sensibilidade de [P] (cervejaria)** (p. 105–109). Valor-base de 81,947 mi (8 anos a 20%, depois g = 3% a 15%):
| Choque | Novo valor | Δ |
|---|---|---|
| +3 p.p. no g dos anos 2 a 8 | 93,200 | **+13,7%** |
| g na perpetuidade de 3% → 0% | 74,457 | **−9,1%** |
| Taxa dos anos 1 a 8 de 20% → 25% | 65,572 | **−20%** |
| Taxa da perpetuidade de 15% → 10% | +23,960 | **+29,2%** |

**Sensibilidade combinada (celulose)** ([P] p. 109–113): valor-base de 1,655 bi.
- Caso 1: preço da celulose dispara, mas a taxa sobe para 26% → **1,396 bi (−15,6%)**.
- Caso 2: preço estruturalmente menor e g perpétuo zero, apesar de a taxa cair para 17%/11% → **−23,6%**.
- Lição: mudanças **estruturais** no setor podem superar a melhora macro.
- *Notação em [P] p. 109–112:* "31% (19% × 10%)" significa composição, (1,19 × 1,10) − 1 = 30,9% ✔. O mesmo vale para "56% = 42% × 10%" e "−17% = −13% × −5%".

**"Onde eu errei?" (reverse engineering)** ([P] p. 157–158): o que precisaria ser verdade para o preço de mercado se justificar? +3 p.p. de g nos anos 3 a 10 (margem de 48% para 58%), ou dobrar o g perpétuo, ou −1,5 p.p. no WACC. Ver também a TIR ao preço atual ([P] p. 145–147; tema 27).

**Cenários com catalisadores** ([P] p. 172–175): varejo de eletrônicos com 3 catalisadores (quantidade, preço e capital de giro) e 3 cenários (60%, 30% e 10%). O valor esperado ponderado do FCFE é 15,3 mi. **Póvoa prefere usar o cenário mais provável como linha-mestra** e os outros como monitoramento, não a média ponderada ([P] p. 175).

**Modelo estável e g** ([D] p. 438)
`TV = EBIT(1−t)(1 − g/ROC)/(WACC − g)`. Se ROC = WACC, `TV = EBIT(1−t)/WACC`, independente de g. A sensibilidade a g **é a sensibilidade ao excesso de retorno**.

**Ajuste de sobrevivência** ([D] p. 446): `valor = DCF × (1 − p) + venda forçada × p`.

## 3. Premissas e escolhas dos autores

- **Objetivo da valuation**: indicar **regiões** de compra (por exemplo, de R$ 10 a R$ 11) e de venda (R$ 15 a R$ 16,50), não um preço-alvo exato. O preço-alvo de corretora é "obrigação comercial" ([P] p. 97). Um resultado notável seria um "upside de 28%, com 15% no pior cenário e 40% no melhor" ([P] p. 145).
- **Foco nos catalisadores**: "dificilmente uma empresa possui mais de três catalisadores". Trabalhe intensamente neles e de forma simples no resto. Sensibilidade em todas as linhas tem custo-benefício ruim ([P] p. 172, 175).
- **Consistência entre variáveis** ([P] p. 172): no exemplo da construção civil, um número de obras explodindo com custo de pessoal caindo é inconsistente.
- **Ponderar cenários** ([P] p. 175): "desconfie toda vez que alguém desejar transformar a valuation, algo subjetivo por natureza, em matéria muito objetiva".
- **Fluxos esperados** ([D] p. 445): uma visão é que os fluxos esperados já incorporam a gama de cenários. Nesse caso, um desconto extra por fracasso é dupla contagem.
- **Ligar reinvestimento a g** reduz a sensibilidade espúria do TV a g ([D] p. 438).
- **Sensibilidade do APV** ao custo de falência e à probabilidade de default ([D] p. 587).

## 4. Passo a passo prático

1. **Matriz g_perp × WACC_perp** (por exemplo, ±1 p.p. em passos de 0,5), com RR = g/ROC recalculado em cada célula ([D] p. 438).
2. **Tornado** dos 3 a 5 inputs mais relevantes: os catalisadores ([P] p. 172).
3. **Cenários** (pessimista, base, otimista) com narrativa coerente entre as variáveis (macro, setor, empresa) ([P] p. 109–113, 172–174).
4. **Reverse engineering**: TIR ao preço atual e "o que o mercado está precificando" (g, margem e WACC implícitos) ([P] p. 145–147, 157–158).
5. **Faixa de preço justo** com o cenário-base como linha-mestra ([P] p. 175).
6. *(Opcional)* Simulação de Monte Carlo nos catalisadores. *Não é tratada nos trechos lidos.*

## 5. Erros comuns apontados pelos autores

- **"Cravar" um preço único** ([P] p. 97).
- **Fazer sensibilidade de tudo**, sem foco ([P] p. 175).
- **Sensibilizar g sem ajustar o reinvestimento**, o que exagera o efeito ([D] p. 438).
- **Cenários internamente inconsistentes** ([P] p. 172).
- **Achar que o mercado está sempre certo** quando o modelo diverge muito. Ou o contrário: Póvoa reconhece bolhas e efeito manada ([P] p. 157–158).

## 6. Onde concordam e onde divergem

| Ponto | Damodaran | Póvoa |
|---|---|---|
| Ênfase | Consistência g ↔ reinvestimento reduz a sensibilidade (p. 438) | Sensibilidade e cenários como ferramenta central (p. 104–113, 172–175) |
| Cenários e probabilidades | Fluxos esperados já ponderam os cenários (p. 445) | Prefere o cenário mais provável a uma média ponderada (p. 175) |
| Simulação | Não encontrei nos trechos citados **[não verificado no Cap. 5]** | Não trata |

## 7. Limites: o que está defasado ou é específico do Brasil

- Taxas dos exemplos de [P] (15–26%) refletem o Brasil de 2012.
- Ferramentas de simulação (Monte Carlo) não são tratadas nos trechos lidos **[NÃO VERIFICADO]**.

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. **Saídas obrigatórias por valuation**: (a) matriz g × WACC na perpetuidade; (b) tornado dos 3 catalisadores; (c) três cenários com narrativa; (d) TIR implícita ao preço atual.
2. **Comunicação**: preço justo em **faixa** (pessimista, base, otimista), com o cenário-base em destaque.
3. **Probabilidades dos cenários**: mostrar, mas sem fazer a média ponderada o "preço-alvo" (posição de Póvoa) **[a decidir]**.

## 9. Dúvidas abertas para você decidir

1. Valor central = cenário-base (Póvoa) ou média ponderada pelas probabilidades?
2. Incluir Monte Carlo em alguma valuation?
3. Amplitude padrão da matriz: ±1 p.p. ou ±2 p.p.?
