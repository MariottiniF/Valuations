# Fichamento 31: Valor do caixa (caixa excedente, caixa operacional, desconto de caixa "preso")

**Fontes**
- **[D]** Damodaran (2002), Cap. 16, "Cash and Near Cash Investments", "Operating Cash Requirements", "Consolidated × Separate Valuation", "Should you ever discount cash?", Ilustrações 16.1 a 16.4 (PDF p. 593–606). Cap. 10, capital de giro sem caixa (p. 361–362). Cap. 14, FCFE × acúmulo de caixa (p. 496–497, 521–522).
- **[P]** Póvoa (2012), Cap. 10, "O valor do caixa: simplesmente caixa!" (p. 355–361).

---

## 1. Conceito central

**Caixa é caixa**: R$ 1 milhão aplicado com liquidez vale R$ 1 milhão ([P] p. 355). Por isso, os dois autores recomendam **separar** o caixa e as aplicações dos ativos operacionais, avaliar a operação como se não houvesse caixa e **somar** o caixa no fim ([D] p. 595–596; [P] p. 356). Misturar o rendimento do caixa no fluxo e descontá-lo à taxa da operação **reduz artificialmente** o valor do caixa ([D] p. 597; [P] p. 356). Só se justifica um desconto quando o caixa rende abaixo do mercado ou quando há expectativa de **mau uso** pela gestão ([D] p. 598–599).

## 2. Fórmulas

**Beta consolidado com caixa** ([D] p. 595–596)
`β_firma = β_operacional × w_op + β_caixa × w_caixa` (β_caixa ≈ 0).
Exemplo 16.1: operação de 1.200 (β = 1), caixa de 200 → β = 0,8571 → Ke = 9,21%; LL total = 120 + 9 = 129 → 129/0,0921 = **1.400**. Separado: 120/0,10 = 1.200 + 200 = **1.400**. Erro: 129/0,10 = 1.290 (perda de 110 = caixa avaliado a 90).

**Caixa aplicado abaixo do mercado** ([D] p. 598): 200 × 3% / 4,5% = **133,33** (perda de 66,67 em relação ao valor de face).

**Desconto por mau uso esperado** ([D] p. 599)
`Desconto = Δprobabilidade de aquisição ruim × sobrepreço esperado`. Exemplo: 30% × 50 = **15** → caixa vale 185.

**Póvoa: beta sem caixa** ([P] p. 359–361)
`β_total = w_caixa × 0 + (1 − w_caixa) × β_sem caixa` → `β_sem caixa = β_total/(1 − w_caixa)`. Exemplo: 1,47/0,8 = **1,84** ✔.
Alternativa: βu_sem caixa = βu_total/(1 − w) = 0,8/0,8 = 1,0 → realavancado com D/E 1,2 e t 30% = 1,84.

**Exemplo de [P]** (caixa como "projeto") (p. 355–356): 10 × 1,095¹² = 29,7; ÷ 1,1535¹² = **5,4**, um "desconto ilógico" de 46%.

## 3. Premissas e escolhas dos autores

- **Caixa operacional × excedente** ([D] p. 594): o caixa necessário para operar entra no capital de giro. O que rende uma taxa justa e excede a necessidade é somado. Varejo pequeno em mercado emergente (muitas transações em dinheiro) pode precisar de caixa operacional relevante.
- **O caixa não entra no capital de giro não caixa** ([D] Cap. 10, p. 361): ele rende uma taxa justa e é avaliado à parte.
- **Avaliação separada × consolidada** ([D] p. 594–597): a consolidada (DDM, FCFE com receita financeira) exige um beta ponderado que muda à medida que a proporção de caixa muda. A separada é mais segura.
- **No FCFE separado** ([D] p. 596; [P] p. 358): retire a receita financeira do lucro, use o beta da operação e some o caixa no fim.
- **Limiar de Póvoa** ([P] p. 356–358): se caixa e aplicações de curto prazo forem < 20% do ativo, basta somar o caixa. Se forem > 20% e de forma **consistente** no tempo, recalcule o beta sem o caixa, porque o caixa alto reduz o risco percebido ("triplo benefício": valor, receita financeira e amortecimento do risco). Em 2012, menos de 10% das abertas brasileiras passavam de 20%.
- **No FCFF** ([P] p. 360): Póvoa só ajusta o Ke e não tenta mexer no Kd ("é muito difícil estimar"). Também não tira o caixa do D/E na realavancagem, por falta de dados seguros ([P] p. 361).
- **FCFE e acúmulo de caixa** ([D] Cap. 14, p. 496–497, 521–522): o FCFE supõe que o excedente é pago. Se a empresa acumula caixa e investe mal (aquisições caras), o DDM pode dar menos que o FCFE.
- **Empresas "punidas" por acumular caixa** ([D] p. 599, 604): depende do histórico da gestão. A Microsoft, com histórico impecável, não era descontada em 2000.

## 4. Passo a passo prático

1. Separe o caixa e as aplicações de liquidez imediata.
2. Estime o **caixa operacional mínimo** (histórico do setor, % da receita) e trate-o como capital de giro.
3. O **caixa excedente** vai para a ponte EV → equity pelo valor de face (tema 30).
4. Se usar FCFE, retire a receita financeira do excedente.
5. Verifique se o **beta** dos comparáveis está "contaminado" por caixa alto. Se estiver, desalavanque também pelo caixa (`βu_op = βu / (1 − w_caixa)`), à maneira de [D] p. 595 e [P] p. 360.
6. Aplique um desconto só com justificativa: rendimento abaixo do mercado (caixa preso no exterior, restrições) ou histórico de desperdício ([D] p. 598–599).

## 5. Erros comuns apontados pelos autores

- **Descontar a receita financeira do caixa pelo Ke ou WACC da operação** ([D] p. 597; [P] p. 356).
- **Usar o beta de regressão (com caixa embutido) para avaliar só a operação** ([D] p. 595, nota 3; [P] p. 358–359).
- **Contar o caixa duas vezes**: na dívida líquida e somado de novo ([D] Cap. 15, p. 555).
- **Descontar o caixa por padrão**, sem evidência de mau uso ([D] p. 599, 604).

## 6. Onde concordam e onde divergem

**Concordam**: caixa à parte, pelo valor de face; descontar o caixa a uma taxa de risco é erro; o caixa reduz o beta observado.

| Ponto | Damodaran | Póvoa |
|---|---|---|
| Ajuste do beta | Sempre que relevante (beta da operação) (p. 595) | Só acima de 20% do ativo, com estabilidade (p. 357–358) |
| Desconto no caixa | Quando rende abaixo do mercado ou há mau uso esperado (p. 598–599) | Não discute desconto |
| Caixa operacional | Separa do excedente (p. 594) | Não distingue explicitamente |

## 7. Limites: o que está defasado ou é específico do Brasil

- No Brasil, aplicações em CDI rendem perto do Rf de curto prazo. **O caixa rende "taxa justa" na maioria das empresas.** Exceções: caixa retido em subsidiárias no exterior, caixa vinculado (garantias, depósitos judiciais).
- A Tab. 10.3 de [P] (p. 357) parece usar dados anteriores a 2012 **[inferência]**.

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. Caixa e aplicações **sempre separados** e somados pelo valor de face.
2. **Caixa operacional mínimo** definido por setor (por exemplo, 2% da receita no varejo) **[a calibrar]**.
3. **Caixa restrito** (garantias, vinculados) **não** é somado como excedente.
4. Para comparáveis com caixa alto, desalavancar o beta também pelo caixa (regra de Póvoa: acima de 20% do ativo).

## 9. Dúvidas abertas para você decidir

1. Valor do caixa operacional mínimo por setor?
2. Aplicar a regra de 20% de Póvoa ou ajustar o beta pelo caixa sempre?
3. Algum caso de desconto no caixa por governança (histórico de aquisições ruins)?
