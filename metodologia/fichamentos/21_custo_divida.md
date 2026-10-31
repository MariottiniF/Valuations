# Fichamento 21: Custo da dívida

**Fontes**
- **[D]** Damodaran (2002), Cap. 7, "Default Spreads on Bonds" (PDF p. 239–243), e Cap. 8, "Calculating the Cost of Debt", "Estimating a Tax Rate", "Cost of Debt for an Emerging Market firm", "Hybrid Securities", "What is debt?", "Operating leases", "Market value of debt" e "Gross versus net debt" (PDF p. 284–297).
- **[P]** Póvoa (2012), Cap. 6: "Taxa de desconto para a firma" (p. 231–237), "Agência de rating…" (p. 237–240), "Por que, quando elevamos o endividamento, o custo de capital próprio também aumenta?" (p. 240–243) e "BNDES" (p. 243–245).

---

## 1. Conceito central

O custo da dívida é a taxa **corrente** a que a empresa conseguiria tomar emprestado hoje, a longo prazo, e não a taxa histórica dos contratos ([D] p. 284; [P] p. 234–235). Ele depende de três coisas: a taxa livre de risco, o **spread de default** da empresa (medido pelo rating, real ou sintético) e o **benefício fiscal** dos juros ([D] p. 284). No Brasil, Póvoa acrescenta o problema da **dívida subsidiada (BNDES)**: ela vale no período explícito, mas não deve ser perpetuada ([P] p. 243–245).

## 2. Fórmulas

**Custo da dívida após impostos** ([D] p. 284; [P] p. 232)
`Kd(1−t) = Kd × (1 − t)`, com t = **alíquota marginal** ([D] p. 287).

**Custo da dívida antes de impostos** ([D] p. 285–286)
`Kd = Rf + spread de default (do rating)`

**Empresa de mercado emergente (versão conservadora)** ([D] p. 289)
`Kd = Rf (US$) + spread de default do país + spread de default da empresa (rating sintético)`. Exemplo da Embraer: 5% + 5,37% + 0,75% = 11,12%; após impostos (33%) = 7,45% ([D] p. 289).

**Taxa soberana e taxa corporativa** ([P] p. 238)
`Taxa soberana = Rf + spread soberano`; `taxa corporativa = taxa soberana + spread corporativo`. O rating do país funciona, em geral, como teto para o das empresas.

**Rating sintético pela cobertura de juros** ([D] p. 285–286)
`ICR = EBIT / despesa de juros` → rating → spread. As tabelas 8.5 (empresas pequenas) e 8.6 (grandes) dão as faixas. Exemplo: Boeing com ICR 1.720/453 = 3,80 → A− (tabela de grandes) → spread de 2% ([D] p. 288).

**ICR ajustado para leasing operacional** ([D] p. 293)
`ICR mod. = (EBIT + despesa de leasing) / (juros + despesa de leasing)`

**Valor de mercado da dívida contábil** ([D] p. 295)
Trate toda a dívida como um único título: cupom = despesa de juros, prazo = prazo médio ponderado, descontado a Kd corrente. Exemplo: US$1 bi, juros de 60, 6 anos, Kd 7,5% → US$930 mi ✔.

**Valor presente do leasing operacional** ([D] p. 292–294): VP dos compromissos futuros a Kd pré-impostos. Fora dos EUA, use uma anuidade da despesa corrente por 8 a 10 anos.

**Preferencial (perpétua)** ([D] p. 290): `kps = dividendo preferencial / preço`.

**Dívida mista BNDES + mercado ([P] p. 244)**
`Kd(1−t) = (w_BNDES × Kd_BNDES + w_mercado × Kd_mercado) × (1 − t)`. Exemplo: (0,25 × 7,5% + 0,75 × 13,5%) × 0,7 = 8,40% ✔. Após o rebaixamento: (0,25 × 7,5% + 0,75 × 14%) × 0,7 = 8,66% ✔. Na perpetuidade: 14% × 0,7 = 9,80% ([P] p. 245).

## 3. Premissas e escolhas dos autores

- **Hierarquia de fontes** ([D] p. 284–286): (1) yield de títulos líquidos da empresa; (2) rating da agência + spread típico; (3) sem rating, use empréstimos recentes ou **rating sintético**.
- **Simplicidade > precisão**: Damodaran prefere o ICR isolado a escores multivariados como o Z de Altman, porque é mais fácil de explicar ([D] p. 286–287).
- **Spreads variam** com o prazo (maiores nos vencimentos longos e nos ratings baixos) e com o ciclo (sobem em recessão) e por isso precisam ser reestimados periodicamente ([D] p. 241–243; [P] p. 238, 240).
- **Alíquota marginal, não efetiva**: os juros economizam imposto na margem. Sem lucro tributável, não há benefício no ano ([D] p. 287). *Póvoa usa no WACC a "alíquota média de imposto de renda" ([P] p. 232) e, nos exemplos, 30%.*
- **O que é dívida** ([D] p. 292): só passivos **onerosos**, de curto e de longo prazo, **+ leasing operacional capitalizado**. Fornecedores ficam de fora.
- **Valor de mercado da dívida**: preferido pelos dois. Póvoa observa que, no Brasil, o mercado secundário de dívida privada é ilíquido e por isso se usa o contábil como proxy ([P] p. 231). Quando o rating piora, o valor de mercado da dívida cai, e o WACC sobe "por duas fontes" (Tabelas 6.6 e 6.7, [P] p. 235–237). Exemplo: debênture de 10% com 8 anos restantes, reprecificada a 15% → 77,6% do valor de face ✔ ([P] p. 236–237).
- **Dívida bruta × líquida** ([D] p. 295–296): é mais seguro trabalhar com a bruta e somar o caixa. Se usar a líquida, use-a de ponta a ponta (beta, ICR, pesos) e não some o caixa no fim. A dívida líquida **superestima o valor de empresas arriscadas**, porque supõe que caixa e dívida têm risco igual.
- **Risco-país na dívida**: a visão conservadora diz que a empresa não toma mais barato que o próprio país. O contra-argumento é que a empresa pode ser mais segura que o país, por exemplo a Embraer com receita em dólar ([D] p. 289; [P] p. 238–239).
- **Juros altos e ICR**: num país de juros altos o ICR tende a ser menor para o mesmo risco. Ajuste a tabela ou recalcule os juros em US$ ([D] p. 288–289).
- **Ratings, apesar das falhas**: continuam a referência, por causa dos limites regulatórios de investidores institucionais e da falta de alternativa ([P] p. 237–238). Tabela 6.8 de [P] (p. 239): equivalência S&P/Moody's/Fitch com spreads soberanos e corporativos em US$ no início de 2012, adaptada de Damodaran.
- **BNDES no período explícito**: o subsídio pode ser "rolado" ao mesmo custo mesmo depois de um rebaixamento. **Na perpetuidade, deve ser substituído por dívida a mercado**, porque subsídio é temporário por definição ([P] p. 244–245).
- **Híbridos**: separe a conversível em dívida (o título "puro") e capital (a opção) ([D] p. 291). Exemplo da Amazon: US$ 811 mi de dívida e US$ 439 mi de capital.

## 4. Passo a passo prático

1. **Liste a dívida onerosa** (curto e longo prazo, inclusive debêntures e BNDES) e o leasing ([D] p. 292). *No IFRS 16 o leasing já aparece no balanço; ver seção 7.*
2. **Encontre o spread**: títulos líquidos → rating de agência → rating sintético pelo ICR ([D] p. 284–286).
3. **Monte Kd pré-impostos** = Rf (na mesma moeda) + spread. Em US$, decida se soma o spread soberano ([D] p. 289).
4. **Separe a dívida subsidiada**: custo contratual no período explícito; a mercado na perpetuidade ([P] p. 244–245).
5. **Aplique (1 − t marginal)**, verificando se haverá lucro tributável ([D] p. 287).
6. **Converta a dívida contábil para valor de mercado** se o custo corrente for muito diferente do cupom ([D] p. 295–297), ou use o contábil como proxy por falta de mercado secundário ([P] p. 231).
7. Leve o resultado ao WACC (tema 23).

## 5. Erros comuns apontados pelos autores

- **Usar a taxa histórica dos contratos** em vez da taxa corrente ([P] p. 234–235).
- **Usar a alíquota efetiva** no benefício fiscal ([D] p. 287).
- **Dar benefício fiscal a quem tem prejuízo** ([D] p. 287).
- **Incluir passivos não onerosos** (fornecedores) na dívida ([D] p. 292).
- **Esquecer o leasing operacional** ([D] p. 292–294).
- **Não ajustar o valor da dívida depois de um rebaixamento**: subir o custo e manter o valor (WACC sobe "por uma fonte") ou nem subir o custo (o erro mais grave) ([P] p. 235–237).
- **Misturar dívida líquida e bruta** ao longo da valuation ([D] p. 296).
- **Perpetuar o subsídio do BNDES** ([P] p. 244–245).

## 6. Onde concordam e onde divergem

**Concordam**: o custo é o corrente e não o histórico; rating → spread; valor de mercado de preferência; benefício fiscal pelos juros.

| Ponto | Damodaran | Póvoa |
|---|---|---|
| Alíquota | Marginal (p. 287) | "Média" (p. 232); exemplos com 30% |
| Sem rating | Rating sintético por ICR (p. 285–286) | Não detalha o sintético nos trechos lidos |
| Valor da dívida | Converte o contábil em mercado como um título (p. 295) | Contábil como proxy no Brasil (p. 231), mas defende reprecificar após mudança de rating (p. 235–237) |
| Dívida subsidiada | Não trata | Explícito: contratual; perpetuidade: a mercado (p. 243–245) |
| Leasing | Capitaliza (p. 292–294) | Não trata nos trechos lidos (ver tema 07) |

## 7. Limites: o que está defasado ou é específico do Brasil

- **Tabelas de spreads e ICR** ([D] 2000–2001; [P] 2012): vencidas. Damodaran atualiza essas tabelas periodicamente fora do livro **[NÃO VERIFICADO aqui]**.
- **Leasing**: desde o **IFRS 16 / CPC 06 (R2)** (2019), arrendamentos aparecem no balanço como passivo. O ajuste de Damodaran passa a ser, em boa parte, ler a nota do passivo de arrendamento. *Informação de fora dos livros.*
- **BNDES**: desde 2018, os novos contratos usam a **TLP** em vez da TJLP (Lei 13.483/2017), o que reduziu o subsídio. *Informação de fora dos livros; confira a regra vigente.*
- **Alíquota marginal no Brasil**: 34% (IRPJ 25% + CSLL 9%) é a referência usual para lucro real, mas não aparece nos livros. Confira regimes especiais (SUDENE/SUDAM, lucro presumido etc.).

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. Kd = Rf (NTN-B) + spread, de preferência pelas **debêntures da empresa negociadas no secundário** (taxa indicativa ANBIMA) e, na falta delas, pelo rating ou por um rating sintético via ICR.
2. Use **34%** como t marginal, salvo benefício fiscal documentado (e com prazo).
3. Dívida = empréstimos + debêntures + **passivo de arrendamento (IFRS 16)**, coerente com o EBITDA ou EBIT pós-IFRS 16 (ver tema 07).
4. **BNDES**: custo contratual no explícito e custo de mercado na perpetuidade.
5. Valor da dívida: contábil por padrão. Reprecifique quando o spread corrente diferir muito do contratual.
6. Defina **bruta ou líquida** uma única vez e mantenha em beta, pesos e ponte EV → equity (tema 30).

## 9. Dúvidas abertas para você decidir

1. Fonte padrão do spread: debêntures negociadas, rating ou ICR sintético?
2. Dívida bruta com o caixa somado, ou dívida líquida?
3. Benefícios fiscais regionais (SUDENE etc.) entram na alíquota? Até quando?
4. Somar algum "spread soberano" ao Kd em R$? Damodaran faz isso em US$; em R$, o Rf da NTN-B já o embute.
