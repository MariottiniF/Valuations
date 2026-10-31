# Fichamento 11: FCFF × FCFE × dividendos (definição, quando usar cada um, conversão)

**Fontes**
- **[D]** Damodaran (2002), Cap. 13 "Dividend Discount Models" (PDF p. 450–486; ver também o tema 39). Cap. 14 "Free Cashflow to Equity Discount Models": definição de FCFE, δ, FCFE × dividendos, razões para a diferença, crescimento do FCFE e FCFE × DDM (p. 487–529). Cap. 15, FCFF, Tab. 15.1 e firma × acionista (p. 533–560).
- **[P]** Póvoa (2012), Cap. 5 "Fluxo de Caixa para o Acionista × Fluxo de Caixa para a Firma" (p. 131–175).

---

## 1. Conceito central

Há três formas de avaliar o capital próprio: **dividendos** (o que é pago), **FCFE** (o que **poderia** ser pago depois de reinvestimento e serviço da dívida) e **FCFF** (o caixa antes da dívida, para todos os financiadores, menos a dívida no fim) ([D] p. 487–489, 533–534; [P] p. 132–134). O FCFE é descontado pelo **Ke** e dá o valor das ações. O FCFF é descontado pelo **WACC** e dá o valor da firma; subtraindo a dívida, chega-se às ações ([P] p. 134; [D] p. 537). Com hipóteses consistentes, os métodos levam ao mesmo valor ([D] p. 559–560; [P] p. 166). A escolha prática depende da **estrutura de capital**: estável favorece o FCFE ou o DDM; em mudança, o FCFF ([D] p. 542, 559; [P] p. 166–167).

## 2. Fórmulas

**FCFE (completo)** ([D] p. 488–489)
`FCFE = LL − (Capex − D&A) − ΔCG − (div. pref. + emissão de pref.) + (novas dívidas − amortizações)`

**FCFE com mix de financiamento fixo δ** ([D] p. 488–489)
`FCFE = LL − (Capex − D&A)(1 − δ) − ΔCG(1 − δ)`, com δ = fração do reinvestimento financiada por dívida (fixa em **valor contábil**, nota 1).
Equivalente em [P]: `FCFE = LL − £ × (investimento líquido) − £ × ΔCG + itens sem caixa − partes estatutárias`, com £ = E/(D+E) = 1 − δ ([P] p. 137–138).
Exemplo da química de [P]: LL × 1,1^10 × 1,07 = 208; investimento líquido 60 × 0,6 = 36; ΔCG 6,2; estatutárias 52 → FCFE perpétuo = **114** → TV = 114/(0,165 − 0,07) ≈ 1.198 → VP = **229** (÷1,18^10). Valor justo de 319,9 mi = R$ 31,99/ação, contra R$ 25 (upside de 28%) ([P] p. 139–142) ✔ nos itens verificáveis.

**FCFF** ([D] p. 533–534)
`FCFF = EBIT(1−t) + D&A − Capex − ΔCG = FCFE + juros(1−t) + amortizações − novas dívidas + div. pref.`

**Conversão de [P]** (p. 167–168)
`FCFF = FCFE + juros(1−t) − (1−£)(inv. líquido) − (1−£)ΔCG − novas dívidas + amortizações`

**Equivalência firma × acionista (perpétua, sem crescimento)** ([D] p. 559–560)
EBIT 166,67; t 40%; E 600 a Ke 13,87%; D 400 a Kd 7% → WACC 10% → firma 1.000 → equity **600**. LL = (166,67 − 28) × 0,6 = 83,2 → 83,2/0,1387 = **600**.

**Crescimento do FCFE** ([D] p. 497): use a **taxa de reinvestimento do acionista** × ROE (de ativos operacionais), não a retenção × ROE, porque o FCFE supõe que o excedente é pago.

**Razão caixa devolvido / FCFE** ([D] p. 492): `(dividendos + recompras)/FCFE`. Média NYSE em 1998: 51,55%.

## 3. Premissas e escolhas dos autores

- **Quando usar cada um**
  - **DDM**: empresas que pagam o que podem, ou investidor minoritário sem poder de mudar a política de dividendos ([D] Cap. 13; Cap. 14, p. 529).
  - **FCFE**: estrutura de capital estável; para aquisições ou com chance de mudança de controle, o FCFE é melhor que o DDM ([D] p. 529). Póvoa: empresas maduras, líderes de mercado ([P] p. 167).
  - **FCFF**: alavancagem alta ou em mudança, porque projetar emissões e amortizações vira um pesadelo ([D] p. 542, 559; [P] p. 166–167). "Na prática, os analistas usam [o FCFF] com muito mais frequência", porque no Brasil estruturas de capital definidas são a exceção ([P] p. 167).
- **Defeitos do FCFF** ([D] p. 542–543): é um fluxo hipotético; pode esconder risco de sobrevivência (FCFF positivo com FCFE negativo); o índice de dívida constante implica emissões futuras.
- **Por que dividendos ≠ FCFE** ([D] p. 492–496): desejo de estabilidade, investimentos futuros, impostos, sinalização, construção de "impérios" pela gestão e colchão de caixa.
- **FCFE > DDM** quando o excesso de caixa é aplicado abaixo do custo ou em aquisições ruins; **FCFE < DDM** quando os dividendos superam o FCFE e há emissões (custos de emissão, sobrealavancagem, racionamento de capital) ([D] p. 521–522). O FCFE supõe **que não há acúmulo de caixa** e crescimento só de ativos operacionais ([D] p. 496–497).
- **Erro clássico no FCFE** ([P] p. 137): supor que todo o investimento é bancado por capital próprio. Isso subestima o valor; use £.
- **Dividendos no FCFE** ([P] p. 135–136): **não** subtraia dividendos (mínimos ou discricionários), porque eles voltam ao acionista. Subtraia o que vai para terceiros (participações estatutárias).
- **"Upside de 0%" não é ganho zero**: o investidor recebe o retorno exigido (Ke). Não compare o upside com a renda fixa, que já está no Ke ([P] p. 143–144). Não há prazo para a convergência; o "12 meses" é convenção comercial ([P] p. 144–145).
- **TIR do fluxo ao preço de mercado** ([P] p. 145–147): ao preço de R$ 25, a TIR implícita sobe para 20,9% nos anos 1 a 10 (com a perpetuidade mantida em 16,5%), ou para 20,7% na perpetuidade (com 18% mantido no explícito). É a forma correta de comparar o retorno esperado com o exigido (tema 27).
- **Valor da firma × pesos iniciais** ([P] p. 156): Póvoa checa se o E/(D+E) resultante (87,5%) bate com o usado (90%). É uma checagem de circularidade (tema 23).

## 4. Passo a passo prático

1. **Diagnóstico**: a estrutura de capital vai mudar? Sim → FCFF. Não, e a empresa paga o que pode → DDM ou FCFE. Não, e paga menos do que pode → FCFE.
2. **FCFF**: EBIT(1−t) − capex líquido − ΔCG → desconte a WACC_t (acumulado) → + caixa e ativos não operacionais − dívida − minoritários → equity (tema 30).
3. **FCFE**: LL − (1−δ)(capex líquido + ΔCG) − participações estatutárias → desconte a Ke → + caixa excedente (se não estiver no LL) → equity.
4. **Checagem**: rode os dois (FCFF e FCFE) em empresas estáveis. Diferenças grandes indicam incoerência (pesos, juros, itens não operacionais) ([D] p. 559–560).
5. Compare **dividendos + recompras com o FCFE** histórico para entender a política de distribuição.

## 5. Erros comuns apontados pelos autores

- **Descontar o FCFE pelo WACC** ou o FCFF pelo Ke ([P] p. 134; [D] p. 534).
- **Financiar 100% do investimento com capital próprio no FCFE** ([P] p. 137).
- **Subtrair dividendos do FCFE** ([P] p. 136).
- **Usar retenção × ROE como crescimento do FCFE** ([D] p. 497).
- **Esperar que FCFF e FCFE coincidam com pesos de mercado de uma empresa mal precificada** ([D] p. 560).
- **Esquecer que o FCFF pode esconder um problema de solvência** ([D] p. 542).

**Inconsistência no exemplo de [P] (p. 168–170)**: no FCFE da empresa de entretenimento, o livro pondera o investimento por £ = 0,8 (supondo 20% financiado por dívida) **e** soma as novas dívidas (+3) **e** a emissão de ações (+3), chegando a FCFE = 7,8.
- Somar as emissões depois de já ponderar por £ **conta o financiamento duas vezes**.
- Emissão de ações **não é fluxo para o acionista**; é um aporte dele.
- O FCFF final (3,11) está correto: EBIT(1−t) = 4 + 1,61 = 5,61, menos 1, 0,5 e 1 (estatutárias) = 3,11.
- O FCFE coerente seria 4 − 1 − 0,5 + 3 (dívida nova) − 1 = **4,5** (versão completa) ou 4 − 0,8 − 0,4 − 1 = **1,8** (versão com £, sem somar a dívida).
- *Esta é uma análise minha; confira no livro.*

## 6. Onde concordam e onde divergem

**Concordam**: FCFE ↔ Ke, FCFF ↔ WACC; FCFF quando a estrutura muda; FCFE com mix de financiamento fixo; equivalência teórica.

| Ponto | Damodaran | Póvoa |
|---|---|---|
| DDM | Modelo próprio (Cap. 13), útil para minoritários | "Mito dos dividendos" (tema 39); não usa o DDM como principal |
| Crescimento do FCFE | Reinvestimento do acionista × ROE operacional (p. 497) | Não detalha nesse capítulo |
| Participações estatutárias | Não trata | Subtraídas do fluxo (p. 135) |
| Preferência prática | FCFF para alavancagem em mudança; FCFE para controle | FCFF na maioria dos casos no Brasil (p. 167) |

## 7. Limites: o que está defasado ou é específico do Brasil

- **Dividendo mínimo obrigatório de 25%** (Lei 6.404/76) e **participações estatutárias** são específicos do Brasil ([P] p. 135–136).
- **Tributação de dividendos**: os livros supõem isenção (regra brasileira desde 1996). Mudanças recentes ou propostas de tributar dividendos **não estão nos livros [NÃO VERIFICADO aqui]**.
- Exemplos de 1989–2001 (Home Depot, Boeing, Coca) e de 2012 (P).

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. **Método principal: FCFF a WACC.**
2. **FCFE como checagem** em empresas com estrutura estável, com δ = dívida-alvo/(dívida + PL) em valor contábil.
3. **Bancos e seguradoras**: FCFE ou DDM obrigatórios (tema 44).
4. **Participações estatutárias** sempre no fluxo.
5. Mostrar a **TIR implícita ao preço atual** em cada vídeo, comparada com o Ke ou o WACC (temas 27 e 32).

## 9. Dúvidas abertas para você decidir

1. FCFE como checagem obrigatória ou opcional?
2. Usar o DDM em algum caso (por exemplo, utilities com payout alto e estável)?
3. Recompras de ações entram como dividendo na análise de política de distribuição?
