# Procedimento de WACC por região: Brasil, Estados Unidos e Europa

Este procedimento define como montar o custo de capital conforme o país e a moeda da empresa avaliada. Para empresas dos EUA e da Europa, o método segue **Damodaran** (*Investment Valuation*, 2ª ed., Caps. 7, 8, 9 e 10, e a prática atual dos dados que ele publica). Para o Brasil, segue as decisões do canal (ver [`DECISOES.md`](DECISOES.md) e os fichamentos 18 a 26).

> **Regra de ouro (vale para as três regiões):** fluxo de caixa, taxa livre de risco, prêmio de risco, custo da dívida, inflação e crescimento perpétuo **na mesma moeda**. A moeda da valuation é a **moeda das demonstrações financeiras** da empresa. Nunca misturar uma taxa em R$ com um fluxo em US$, nem converter só o Rf.

---

## 0. Estrutura comum

```
WACC = Ke × E/(D + E) + Kd × (1 − t) × D/(D + E)
Ke   = Rf + β alavancado × ERP
β alavancado = βu × [1 + (1 − t) × D/E]          (Hamada, tema 20)
Kd   = Rf + spread de crédito (+ spread do país, quando aplicável)
```

- **Dívida** = empréstimos + títulos + passivo de arrendamento (decisão IFRS 16; ver a seção 4 para US GAAP).
- **WACC único** (D11): o mesmo WACC desconta o período explícito e a perpetuidade; sem *rolling WACC*.
- **Pesos** (critério em D12): classificar a empresa antes de montar o WACC, pelos últimos 5 exercícios (ou desde a abertura de capital, o que for menor) de Dívida Líquida/EBITDA — (a) **estável** (desvio-padrão ≤ 1,0x, sem meta divulgada) → pesos **atuais**; (b) **processo concreto de desalavancagem/alavancagem** (meta numérica com prazo, em guidance/covenant/fato relevante) → pesos da **estrutura-alvo divulgada**, um único conjunto para toda a projeção; (c) **estrutura futura incerta** (desvio-padrão > 1,0x sem meta, ou evento recente não representativo) → pesos **atuais** + sensibilidade obrigatória ao intervalo histórico. Em qualquer caso: equity a valor de mercado; dívida a valor de mercado quando houver títulos negociados, senão contábil.
- **Caixa**: fora do WACC e fora do beta. É somado na ponte EV → equity (decisão do caixa, como em [D]).
- **Perpetuidade**: ROIC = WACC (salvo casos especiais) e g = LTG, com **g ≤ Rf da moeda** (ver a seção 5).

---

## 1. Brasil (R$ nominal)

| Parâmetro | Regra | Fonte |
|---|---|---|
| Rf | NTN-B **atual**: `(1 + cupom real) × (1 + IPCA LP) − 1`. NTN-B **mais longa**, para toda a projeção (D11) | Tesouro / ANBIMA; IPCA do cenário macro |
| ERP | **Prêmio único em R$, de longo prazo**, sem somar risco-país (já está na NTN-B): média de vários anos do implícito do Ibovespa; sem série, proxy = prêmio maduro + (CRP − spread soberano). O implícito do trimestre é checagem. Mesmo ERP em toda a projeção (D11) | Cálculo do canal; Damodaran |
| β | Bottom-up: listadas brasileiras do setor; menos de ~10 → emergentes ou globais | Comparáveis; Damodaran (Emerging/Global) |
| Kd | Rf + spread das debêntures da empresa (ANBIMA); na falta, rating ou rating sintético via EBIT/juros | ANBIMA; tabela de Damodaran |
| t | **34%** marginal (IR + CSLL), salvo benefício documentado | Legislação |
| JCP | Benefício no **fluxo** (menos IR), **nunca** reduzindo o Ke | Decisão 4 |
| λ / risco-país | Não usar no padrão (só como sensibilidade) | Tema 26 |

---

## 2. Estados Unidos (US$ nominal)

| Parâmetro | Regra (Damodaran) | Fonte |
|---|---|---|
| Rf | **Treasury de 10 anos**, rendimento atual na data da valuation. Sem ajuste de default (EUA tratado como livre de risco em US$, tema 43) | US Treasury / FRED |
| ERP | **Prêmio implícito do S&P 500** do início do mês (o "mature market premium" de Damodaran) | Damodaran Online (ERP mensal) |
| Exposição internacional | Se a receita for relevante fora de mercados maduros: **ERP ponderado pela receita por país** = Σ (% receita país × (ERP maduro + CRP do país)) | Segmentos geográficos da empresa (10-K); CRP de Damodaran (`ctryprem`) |
| β | Bottom-up com o **βu do setor dos EUA corrigido pelo caixa** (Damodaran). Realavancar com D/E a mercado e t marginal | Damodaran (`betas` US) |
| Kd | (a) rendimento (YTM) dos títulos longos da empresa, se líquidos; (b) senão, **rating** S&P/Moody's → spread da tabela; (c) sem rating, **rating sintético** pelo índice de cobertura EBIT/juros (tabela de Damodaran, que separa empresas grandes e pequenas) | FINRA TRACE; agências; Damodaran (`ratings`) |
| t | **Marginal combinada** (federal 21% + estadual) para o benefício fiscal da dívida, pela tabela de Damodaran **[confirmar o valor vigente]**. No EBIT, alíquota efetiva convergindo para a marginal na perpetuidade | Damodaran (`countrytaxrates`) |
| Arrendamentos | **Ajuste obrigatório de US GAAP (ASC 842)**: ver a seção 4 | 10-K, notas de leases |
| Opções de ações | Avaliar as opções e RSUs em aberto e subtrair do equity (não usar só o número diluído) | 10-K; tema 30 |

---

## 3. Europa (€, £, CHF etc.)

| Parâmetro | Regra (Damodaran) | Fonte |
|---|---|---|
| Moeda | Moeda das demonstrações (em geral €; £ para o Reino Unido; CHF para a Suíça) | Relatório anual |
| Rf em € | **Bund alemão de 10 anos**, para **qualquer** empresa da zona do euro (inclusive Itália, Espanha, Portugal). O título soberano desses países embute risco de default e não é livre de risco | Bundesbank / mercado |
| Rf fora do euro | Título soberano local de 10 anos **menos o spread de default do soberano** quando o rating for inferior a Aaa (ex.: Reino Unido) | Mercado; spread por rating em Damodaran (`ctryprem`) |
| ERP | **ERP maduro** (implícito do S&P 500) + **CRP** dos países onde a empresa opera, ponderado pela receita. Países Aaa: CRP = 0 | Damodaran (`ctryprem`); segmentos geográficos |
| β | Bottom-up com o **βu do setor na Europa** (ou Global, se a amostra for pequena), corrigido pelo caixa | Damodaran (`betas` Europe/Global) |
| Kd | YTM dos títulos da empresa, se líquidos; senão rating ou rating sintético → spread **+ spread de default do país sede** quando o país não for Aaa (como na planilha de custo de capital de Damodaran) | Agências; Damodaran |
| t | Alíquota marginal estatutária do país sede (tabela de Damodaran) **[confirmar o valor vigente]** | Damodaran (`countrytaxrates`) |
| Arrendamentos | IFRS 16: já no balanço, compatível com a decisão do canal; sem ajuste | Relatório anual |

---

## 4. Ajuste de arrendamentos para US GAAP (ASC 842)

No IFRS 16, o arrendamento vira depreciação + juros. No **US GAAP (ASC 842)**, o arrendamento **operacional** fica no balanço, mas a despesa continua **inteira no custo operacional** (linear). Para manter a decisão do canal (passivo de arrendamento como dívida, EBIT "pós-IFRS 16"), aplicar o ajuste de Damodaran (Cap. 9, p. 323–324, tema 07):

1. **Dívida** += passivo de arrendamento operacional (já no balanço).
2. **EBIT ajustado** = EBIT + despesa de arrendamento operacional − amortização do direito de uso.
   - Aproximação aceita: EBIT + passivo de arrendamento × Kd antes do IR.
3. **EBITDA ajustado** = EBITDA + despesa de arrendamento operacional.
4. Usar os mesmos EBIT e EBITDA ajustados nos múltiplos dos pares dos EUA.

Arrendamentos **financeiros** (finance leases) no US GAAP já seguem a lógica do IFRS 16: sem ajuste.

---

## 5. Crescimento perpétuo (LTG) por moeda

- **g = LTG** = crescimento **nominal** de longo prazo da economia, na moeda da valuation:
  - R$: `(1 + IPCA de longo prazo) × (1 + PIB real potencial) − 1`, do cenário macro do canal;
  - US$, €, £: inflação de longo prazo da moeda + crescimento real potencial.
- **Teto**: g ≤ Rf da mesma moeda (regra de Damodaran: nenhuma empresa cresce para sempre acima da economia, e o Rf é a proxy do crescimento nominal de longo prazo).
- Com **ROIC = WACC**, o g não altera o valor da perpetuidade, mas define o reinvestimento: `RR = g/ROIC`.

---

## 6. Passo a passo (empresa estrangeira)

1. Identifique a **moeda das demonstrações** e o **país sede**.
2. Baixe da Damodaran Online, **registrando a data**: ERP implícito do mês; tabela de CRP e de spreads de default por país; βu do setor (US, Europe ou Global); tabela de rating sintético; alíquotas marginais.
3. Rf: Treasury de 10 anos (US$), Bund de 10 anos (€) ou soberano local menos spread de default.
4. ERP: maduro + CRP ponderado pela receita por país (receita só em países maduros → CRP = 0).
5. β: bottom-up; realavancar com D/E a mercado (dívida incluindo arrendamentos) e t marginal.
6. Kd: YTM dos títulos, rating ou rating sintético; somar o spread do país sede quando ele não for Aaa (Europa).
7. US GAAP: aplicar o ajuste de arrendamentos da seção 4.
8. Monte o WACC, cheque contra o **WACC médio do setor** publicado por Damodaran para a região e explique diferenças > 1,5 p.p.
9. Valuation **na moeda local**. Se o canal mostrar o preço em R$ (BDR), converter **só o resultado final** pelo câmbio à vista e pela razão do BDR.

---

## 7. Erros a evitar

- Usar o BTP italiano ou o título espanhol como Rf em €.
- Somar o CRP do Brasil em uma empresa americana só porque o investidor é brasileiro.
- Usar a despesa de arrendamento do US GAAP no EBIT e, ao mesmo tempo, o passivo de arrendamento na dívida (contagem dupla).
- Calcular o WACC em US$ e descontar um fluxo em R$ (ou o contrário).
- Usar a alíquota efetiva no benefício fiscal da dívida (o correto é a marginal).
- Deixar de registrar a data dos dados de Damodaran (eles mudam todo mês ou todo ano).
