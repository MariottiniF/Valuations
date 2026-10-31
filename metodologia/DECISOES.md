# Decisões metodológicas do canal

Registro das decisões tomadas a partir dos fichamentos ([`fichamentos/README.md`](fichamentos/README.md)). Cada decisão indica os temas que a fundamentam. Decidido em 31/10/2026.

## Decisões principais

| # | Decisão | Regra adotada | Temas |
|---|---|---|---|
| D1 | **Caixa no EV** | Como Damodaran: EV = equity + dívida bruta + arrendamentos + minoritários − caixa e aplicações − participações não consolidadas. EBITDA sem receita financeira e sem equivalência patrimonial | 30, 31, 35 |
| D2 | **IFRS 16** | Passivo de arrendamento **é dívida**; EBIT e EBITDA pós-IFRS 16. Varejo: registrar também o número pré-IFRS 16 para comparação com pares. Empresas em US GAAP: ajuste da seção 4 do [`PROCEDIMENTO_WACC.md`](PROCEDIMENTO_WACC.md) | 07, 21, 35 |
| D3 | **Perpetuidade** | **ROIC = WACC** e **g = LTG** (crescimento nominal de longo prazo da economia na moeda da valuation, com g ≤ Rf). Reinvestimento = g/ROIC | 15, 16, 29 |
| D3a | Casos especiais (ROIC > WACC) | Só com vantagem competitiva **nomeável** (marca, rede, regulação, custo) **e** histórico de ROIC acima do WACC por vários anos, com justificativa escrita no material do vídeo | 16, 29 |
| D4 | **Taxa livre de risco** | Brasil: **NTN-B atual** (vencimento compatível no explícito; a mais longa na perpetuidade). EUA e Europa: Damodaran (Treasury de 10 anos; Bund de 10 anos para €) | 18, 43 |
| D5 | **Prêmio de risco** | Brasil: prêmio único em R$, implícito do Ibovespa recalculado por trimestre; perpetuidade pela média de vários anos. EUA e Europa: ERP implícito do S&P 500 + CRP ponderado pela receita | 19, 26, 27 |
| D6 | **JCP** | Benefício no **fluxo** (menos IR), nunca no Ke | 22 |
| D7 | **Tributação de dividendos** | Valuation na perspectiva da empresa, antes do imposto do investidor. A nova tributação é comentada como efeito no retorno líquido da pessoa física (conferir a lei vigente antes de citar alíquotas) | 39 |
| D8 | **Cíclicas** | Margem e ROIC normalizados por 10 anos (ou um ciclo completo). Commodity: curva futura por 2 a 3 anos, convergindo para a média real de 10 a 15 anos. Sensibilidade ao preço da commodity obrigatória | 45 |
| D9 | **Múltiplos** | DCF = preço justo. Múltiplos só como checagem: tabela com múltiplos implícitos no preço justo × mediana dos pares. **Proibida** a média ponderada entre métodos | 02, 33, 34 |
| D10 | **WACC fora do Brasil** | Procedimento Damodaran para EUA e Europa: [`PROCEDIMENTO_WACC.md`](PROCEDIMENTO_WACC.md) | 17–26 |

## Regras complementares aceitas

| # | Regra | Temas |
|---|---|---|
| C1 | **Cenário macro único** do canal (IPCA, Selic, câmbio, PIB), revisado por trimestre com base no Focus e usado em todas as empresas | 38 |
| C2 | **Checklist obrigatório**: reinvestimento = g/ROIC; ΔNCG ≥ 0 na perpetuidade; regra do "uma vez só" no balanço; sinais de alerta do lucro (D p. 336–337) | 05, 07, 15 |
| C3 | **Tese de por que o mercado erra** sempre que o preço justo divergir do preço em mais de 30% (postura "cético cauteloso") | 01, 03 |

## Parâmetros a fixar

Estes valores dependem de dados da data da valuation e não foram fixados aqui:

- IPCA e PIB real de longo prazo para o LTG em R$ (cenário macro, C1).
- Prêmio implícito do Ibovespa do trimestre (D5).
- Alíquotas marginais dos EUA e dos países europeus (tabela de Damodaran, D10).
