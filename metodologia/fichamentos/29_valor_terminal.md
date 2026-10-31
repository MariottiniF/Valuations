# Fichamento 29: Valor terminal (Gordon, múltiplo de saída, liquidação; premissas de estabilidade)

**Fontes**
- **[D]** Damodaran (2002), Cap. 12 "Closure in Valuation: Estimating Terminal Value" (PDF p. 425–449). Cap. 15, condições do modelo estável (p. 537–538).
- **[P]** Póvoa (2012), Cap. 4, "Perpetuidade – o período mais importante da valuation…" (p. 119–125) e exemplos de estágios (p. 99–100, 105, 114–118). Cap. 8, consistência na perpetuidade (p. 271–276). Cap. 6, taxa na perpetuidade (p. 220–227).

---

## 1. Conceito central

Como não dá para projetar fluxos para sempre, a valuation é "fechada" com um **valor terminal (TV)** no fim do período explícito ([D] p. 425). Há três formas: **liquidação** (vida finita), **múltiplo de saída** e **crescimento perpétuo** (Gordon) ([D] p. 425–427). Damodaran sustenta que só a liquidação e o crescimento estável são **consistentes** com o DCF, porque o múltiplo de comparáveis transforma o DCF em valuation relativa ([D] p. 427). O TV costuma ser a maior parte do valor: em média 60% e frequentemente mais de 50% segundo [P] (p. 119), e por isso merece mais atenção do que os analistas costumam dar ([P] p. 119). Isso é natural, porque o retorno de quem compra uma ação vem em boa parte da venda futura ([D] p. 448).

## 2. Fórmulas

**Valor com TV** ([D] p. 425)
`Valor = Σ_{t=1}^{n} CF_t/(1+k)^t + TV_n/(1+k)^n`

**Gordon (firma e acionista)** ([D] p. 427–428; [P] p. 99)
`TV_n (firma) = FCFF_{n+1} / (WACC_{n+1} − g)`; `TV_n (equity) = FCFE_{n+1} / (Ke_{n+1} − g)`.
Póvoa escreve `FC_n(1 + g_p) / [(r_p − g_p)(1 + r)^n]` ([P] p. 99).

**TV com reinvestimento coerente** ([D] p. 437–438)
`TV = EBIT_{n+1}(1−t)(1 − g/ROC) / (WACC − g)`. Se ROC = WACC: `TV = EBIT_{n+1}(1−t)/WACC` (g é irrelevante).

**Liquidação** ([D] p. 426)
(a) Contábil corrigido: `VL = Ativo contábil_n × (1 + π)^idade média`. Exemplo: 2 bi × 1,03⁵ = 2,319 bi.
(b) Poder de geração: VP dos fluxos dos ativos. Exemplo: 400 mi por 15 anos a 10% = 3,042 bi.
Para o acionista, subtraia a dívida do ano n.

**Múltiplo** ([D] p. 427): `TV = múltiplo × variável_n`. Exemplo: 2 × 6 bi de receita = 12 bi.

**g negativo** ([D] p. 430): `100/(0,10 − (−0,05)) = 633` (setores em extinção).

**Ajuste de sobrevivência** ([D] p. 446)
`Valor ajustado = DCF × (1 − p) + valor de venda forçada × p`. Exemplo: 1.000 × 0,8 + 500 × 0,2 = 900.
*Cash-burn* = caixa / |EBITDA| ([D] p. 445).

**Exemplos de [P]** ✔
- Cervejaria (8 anos + perpetuidade, r = 20% e r_p = 15%, g_p = 3%): TV a valor presente = 33,543 mi, ou ~41% de 81,947 ([P] p. 105).
- Fax (2 estágios): 24,02 + 37,38 = 61,4 mi, 61% no TV ([P] p. 116–117).
- Informática (3 estágios): 277,4 + 297,68 + 629,22 = 1.204,3 mi, 52,3% no TV ([P] p. 118).
- **Laticínio** (p. 126–127): *a soma está errada no livro.* −8,264 + 0,683 + 4,515 + 4,665 + 30,615 = **32,214** (o livro dá 31,532). Valor justo = **42,214**, não 41,532.

## 3. Premissas e escolhas dos autores

- **Características da firma estável** ([D] p. 434–437):
  - **Beta** perto de 1; no máximo 1,2 (dois terços das empresas dos EUA estão entre 0,8 e 1,2). Commodities com beta baixo podem mantê-lo se continuarem no mesmo negócio (p. 434–435).
  - **ROC**: ROC = WACC é o "puro", mas Damodaran prefere a **média do setor** (p. 435, 442).
  - **Dívida**: maior em firmas maduras, ou a média do setor; depende da disposição da gestão (p. 435–436).
  - **Reinvestimento** = g/ROC; retenção = g/ROE (p. 436–437).
- **Características da perpetuidade ([P] p. 119–125)**:
  1. **ROC ≈ WACC e ROE ≈ Ke**: a concorrência elimina o spread. Exceções: qualidade e marca (Apple), tamanho (bancos brasileiros) e serviços pouco intensivos em capital (Lojas Americanas). **Barreiras legais e protecionismo não justificam spread perpétuo** (caso Cobra) (p. 119–121). Intangíveis não contabilizados explicam parte do ROC alto. Exemplo da Renner: para levar o ROI de 23% a 15%, o capital teria de ir de 7,8 para 12 bi, o que implica uma marca de ~2,1 bi a valor presente, ~26% do valor de mercado de 8 bi (p. 121–122).
  2. **PIB potencial como balizador**, não como teto rígido: setores diferem e exportadoras seguem outros PIBs. Mas sustentar mais de 9% num PIB de 7,5% "parece inconsistente" (p. 123–124). Póvoa usava 7,5% nominal para o Brasil (3,5% real + 4% de inflação).
  3. **Não perpetuar benefícios fiscais e subsídios** (Zona Franca, BNDES) (p. 124).
  4. **Estrutura de capital possível, não ideal** (p. 125).
- **Duração do alto crescimento** ([D] p. 430–434): tamanho (empresas pequenas têm mais espaço), crescimento e excesso de retorno atuais (momento) e, acima de tudo, **vantagens competitivas e barreiras de entrada**. Exemplos: Con Ed (já estável), P&G (5 anos), Amgen (10 anos, patentes). "Competitive Advantage Period" e MICAP, o período implícito no preço (p. 433–434).
- **Teto de g** ([D] p. 428–430): ≤ crescimento da economia na moeda e no regime da valuation; **g ≤ Rf** como regra prática; uma multinacional pode ter g 0,5–1 p.p. maior. Empresas maduras podem crescer abaixo da economia.
- **Taxa na perpetuidade** ([P] p. 220–227): é permitido ajustar o Rf e o prêmio com parcimônia, até ±2 p.p. (tema 25).
- **"O TV é manipulável"** ([D] p. 448): só quando o analista usa múltiplos ou viola g ≤ economia e reinvestimento coerente. O que mais move o valor não é g, e sim o **excesso de retorno perpétuo**.
- **Sobrevivência** ([D] p. 444–447): para firmas com ativos sólidos, descontar a não sobrevivência é contar o risco duas vezes. Para firmas jovens, sem caixa, ajuste por probabilidade de falência se os fluxos esperados não a refletirem.

## 4. Passo a passo prático

1. Decida se a empresa é **going concern** (Gordon) ou de **vida finita** (liquidação: concessões, minas, projetos).
2. Defina **quando** ela fica estável: tamanho, vantagem competitiva, patentes ou concessões ([D] p. 430–434).
3. Defina os parâmetros estáveis: g (≤ PIB nominal e ≤ Rf), ROC (WACC ↔ setor), beta (0,8–1,2), D/(D+E) maduro, alíquota sem benefícios temporários e Kd sem subsídio.
4. Calcule o FCFF_{n+1} = EBIT_n(1+g)(1−t) × (1 − g/ROC).
5. TV = FCFF_{n+1}/(WACC_estável − g), descontado pelo **fator acumulado** do período explícito.
6. **Checagens**: % do TV no valor total; TV implícito como múltiplo (EV/EBITDA_{n+1}) contra os múltiplos de maduros do setor, **só como sanidade** ([D] p. 427); TV com ROC = WACC; sensibilidade de g × WACC (tema 32).
7. Se houver risco relevante de falência não refletido nos fluxos, aplique o ajuste de sobrevivência ([D] p. 446).

## 5. Erros comuns apontados pelos autores

- **TV por múltiplo de comparáveis atuais**, que mistura valuation relativa com DCF ([D] p. 427, 448).
- **g perpétuo acima da economia** (por exemplo, 12% num PIB de 7,5%) ([P] p. 123; [D] p. 428).
- **Crescer sem reinvestir** ([D] p. 437; [P] Cap. 8, p. 275–276).
- **Beta, ROC e dívida de fase de alto crescimento na perpetuidade** ([D] p. 434–436).
- **Perpetuar subsídios, incentivos fiscais e barreiras legais** ([P] p. 120–121, 124).
- **Dedicar só 10% do tempo à perpetuidade** quando ela responde por ~60% do valor ([P] p. 119).
- **Descontar a sobrevivência duas vezes** em empresas sólidas ([D] p. 446).

## 6. Onde concordam e onde divergem

**Concordam**: Gordon com parâmetros de firma madura; g limitado pela economia; ROC convergente; perpetuidade como a parte mais importante; não perpetuar vantagens artificiais.

| Ponto | Damodaran | Póvoa |
|---|---|---|
| Múltiplo de saída | Inconsistente com o DCF (p. 427) | Não discute nesse capítulo |
| ROC perpétuo | Média do setor (p. 435) | ≈ WACC, salvo exceções justificadas (marca, tamanho, serviços) (p. 119–122) |
| Teto de g | ≤ economia e ≤ Rf (p. 428–430) | PIB como "balizador, não teto"; >9% num PIB de 7,5% é inconsistente (p. 123–124) |
| Beta perpétuo | → 0,8–1,2 (p. 434) | Mantém o beta do último ano explícito (Cap. 6, p. 221–223) |
| Liquidação e sobrevivência | Trata (p. 426, 444–447) | Não trata nesse capítulo |

## 7. Limites: o que está defasado ou é específico do Brasil

- PIB potencial nominal de 7,5% e inflação de 4% ([P] p. 123) são premissas de 2012 e precisam ser revisadas no `MACRO.md`.
- Exemplos de Lojas Americanas (ROE de 30–80% em 2002–2011), Renner e Apple em 2012: históricos.
- Estudos de probabilidade de default (Altman) citados em [D] são antigos.

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. **Método padrão: Gordon** com parâmetros estáveis explícitos. **Liquidação** para empresas de vida finita (concessões com prazo, mineração com reserva definida).
2. **Múltiplo de saída: nunca como método**, só como linha de sanidade ("o TV implica EV/EBITDA de X×, contra Y× de maduros do setor").
3. Regras: g ≤ min(PIB nominal LP, Rf); RR = g/ROC; beta entre 0,8 e 1,2; sem subsídios ou incentivos com prazo.
4. Mostrar no vídeo: **% do valor no TV**, o **valor com ROC = WACC** e a **matriz g × WACC**.
5. Para concessões, a perpetuidade só entra com hipótese explícita de renovação, tratada como cenário.

## 9. Dúvidas abertas para você decidir

1. ROC perpétuo: WACC, média do setor ou intermediário?
2. Beta perpétuo: convergir para 1 ou manter?
3. Para concessões: liquidação no fim do contrato ou cenário com renovação?
4. Limite máximo aceitável de % do valor no TV antes de exigir mais anos explícitos?
