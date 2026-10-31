# Fichamento 30: Do valor da firma ao valor por ação (dívida, caixa, minoritários, participações, opções, ações diluídas)

**Fontes**
- **[D]** Damodaran (2002), Cap. 16 "Estimating Equity Value per Share": ativos não operacionais, caixa, títulos, participações em outras empresas, ativos não utilizados, fundos de pensão, direitos não acionários, opções e ações com voto diferente (PDF p. 593–634). Cap. 8, dívida bruta × líquida (p. 295–296). Cap. 15, dívida líquida (p. 555–557).
- **[P]** Póvoa (2012), Cap. 3, "O fim do mistério das stock options – o lucro por ação diluído" (p. 88–89). Cap. 10, "O valor do caixa: simplesmente caixa!" (p. 355–361). Cap. 4, ativos não operacionais (p. 126–127). Cap. 5, valor da firma × de mercado (p. 134, 155–156).

---

## 1. Conceito central

O DCF de FCFF dá o **valor dos ativos operacionais**. Para chegar ao **valor por ação**: (1) **some** os ativos não operacionais (caixa excedente, títulos, participações em outras empresas, ativos não utilizados, superávit de pensão após impostos); (2) **subtraia** os direitos de não acionistas (dívida, incluindo leasing, preferenciais, minoritários, contingências, déficit de pensão, impostos diferidos); (3) **subtraia o valor das opções** de empregados e divida pelas ações **primárias**; (4) se houver classes com direitos diferentes, reparta o valor entre elas ([D] p. 593, 617–633). Póvoa: `valor da firma − dívida total = valor de mercado`. Ativos não operacionais são avaliados à parte e somados ([P] p. 134, 126–127).

## 2. Fórmulas

**Ponte geral** ([D] p. 617; [P] p. 134)
`Equity = VP(ativos operacionais) + caixa e títulos + participações (a valor justo) + ativos não operacionais − dívida (inclusive leasing) − preferenciais − minoritários (a valor justo) − contingências esperadas − déficit de pensão e saúde − VP dos impostos diferidos`

**Regra de consistência** ([D] p. 617): a dívida subtraída deve ser **pelo menos** a usada no WACC. Se o leasing entrou no WACC, ele também é subtraído.

**Contingências** ([D] p. 617–618): `probabilidade × valor esperado` (a valor presente se o pagamento for futuro). Exemplo: 10% × 1 bi = 100 mi.

**Imposto diferido** ([D] p. 618): trate-o como dívida que vence quando o crescimento se estabilizar. Desconte-o até lá.

**Pensão superavitária** ([D] p. 616): some o excedente **após impostos** (nos EUA, 50%: 1 bi → 500 mi).

**Participações em outras empresas** ([D] p. 609–614)
- **A melhor forma**: avaliar cada participação separadamente e somar a fração detida.
- Se a subsidiária é consolidada, **retire** a receita, os ativos e a dívida dela antes de avaliar a controladora.
- O minoritário contábil está a **valor contábil**, não justo, e por isso subtraí-lo no consolidado é impreciso (Segovia: 1.529 separado contra 1.605 consolidado).
- Participação em empresa fechada: múltiplo P/VP do setor × valor contábil ([D] p. 610–611).

**Preferencial** ([D] nota 9, p. 617): `valor = dividendo preferencial / custo da preferencial`.

**Opções de empregados** ([D] p. 621–631)
1. Ações totalmente diluídas: subestima o valor, porque ignora o preço de exercício e o valor no tempo.
2. Exercício futuro esperado: circular, pouco útil.
3. **Treasury stock**: `(Equity + nº opções × preço de exercício)/(ações + opções)`. Superestima o valor, porque ignora o valor no tempo.
4. **A recomendada**: `(Equity − valor das opções por modelo)/ações primárias`, com ajuste de vesting, impostos e circularidade do preço.

**Opções futuras** ([D] p. 630–631): estime o valor das concessões futuras como % da receita ou do EBIT e trate-o como **despesa operacional** (ou capital), sem contar em dobro o que já está nas margens.

**Classes de ações com voto diferente** ([D] p. 631–633)
- Ad hoc: valor total ÷ (ações sem voto + ações com voto × 1,10). Exemplo: 500/(25 + 25 × 1,1) = 9,52 sem voto e 10,48 com voto. Evidência de prêmio de voto: 5,44% (Lease, McConnell e Mikkelson, 1983).
- Pelo valor do controle: `sem voto = valor status quo / (todas as ações)`; `com voto = sem voto + (valor ótimo − status quo) / ações com voto`. Exemplo: 40 + (1.200 − 800)/10 = **80**.

**LPA diluído (IFRS)** ([P] p. 88–89): básico (ações em circulação) × diluído (inclui conversíveis e opções, mesmo fora do dinheiro). Exemplo: 100 mil opções exercidas a R$ 25 com a ação a R$ 50 → o LPA vai de 5,00 para 4,55.

## 3. Premissas e escolhas dos autores

- **Caixa: separar, não consolidar** ([D] p. 594–597; [P] p. 355–356). Descontar o rendimento do caixa ao Ke **destrói valor artificialmente**. [D]: caixa de 200 vira 90 se descontado a 10%. [P]: R$ 10 mi vira 5,4 se tratado como um "projeto" a 15,35%.
- **Caixa operacional** vai para o capital de giro, e só o excedente é somado ([D] p. 594).
- **Quando descontar o caixa** ([D] p. 598–599): (1) caixa aplicado abaixo da taxa de mercado (200 a 3% com Rf de 4,5% → vale 133,33); (2) gestão com histórico de aquisições ruins. Exemplo: +30% de probabilidade × 50 de sobrepreço = desconto de 15.
- **Títulos negociáveis** ([D] p. 600–606): some o valor de mercado (ou o valor de mercado menos o IR sobre ganho de capital, em liquidação); em geral, sem prêmio nem desconto. Exceção: fundos fechados com gestão abaixo ou acima do mercado.
- **Transparência** ([D] p. 614–615): estruturas societárias opacas tendem a ser subavaliadas.
- **Dívidas futuras não são subtraídas hoje** ([D] p. 618–619): o equity é um valor corrente.
- **Dívida bruta × líquida** ([D] Cap. 8, p. 296; Cap. 15, p. 555–557): se usar dívida líquida em todo o modelo, **não some o caixa** no fim. A dívida líquida negativa deve ser zerada e o excesso de caixa somado.
- **Caixa e beta ([P] p. 357–361)**: se caixa e aplicações de curto prazo passarem de **20% do ativo** de forma consistente, recalcule o beta **sem o caixa**: `β_sem caixa = β_total / (1 − w_caixa)`. Exemplo: 1,47/0,8 = **1,84** ✔. Retire as receitas financeiras do FCFE e some o caixa no fim.

## 4. Passo a passo prático

1. **Valor dos ativos operacionais** (FCFF a WACC).
2. **+ Caixa excedente** (caixa total − caixa operacional mínimo) e aplicações a valor justo.
3. **+ Participações**: coligadas e investidas a valor de mercado (se listadas) ou avaliadas à parte. Se consolidadas, avaliar a subsidiária separadamente e trocar o minoritário contábil pelo **valor justo** da fatia de terceiros.
4. **+ Ativos não operacionais** (imóveis não usados, créditos fiscais monetizáveis, depósitos judiciais recuperáveis) a valor de mercado ([P] p. 126–127).
5. **− Dívida bruta** (empréstimos, debêntures, arrendamentos IFRS 16, preferenciais resgatáveis).
6. **− Provisões e contingências** prováveis, a valor presente (trabalhistas, fiscais, cíveis); **− déficit atuarial**; **− imposto diferido passivo** (descontado).
7. **− Valor das opções e planos de ações** (modelo de opções) ou, na falta de dados, treasury stock.
8. **÷ Ações em circulação**, sem ações em tesouraria.
9. **Classes ON × PN**: decida se aplica prêmio de voto ou de controle (temas 40 e 22); por padrão, valor igual por ação, com a diferença explicada.

## 5. Erros comuns apontados pelos autores

- **Descontar o caixa a uma taxa de ativo arriscado** ([D] p. 597; [P] p. 356).
- **Subtrair a dívida líquida e também somar o caixa** (dupla contagem) ([D] p. 555).
- **Subtrair o minoritário a valor contábil** ([D] p. 610, 614).
- **Esquecer o leasing** que entrou no WACC ([D] p. 617).
- **Usar ações totalmente diluídas** como forma de "tratar" as opções ([D] p. 621–622).
- **Contar as opções futuras em dobro** (já nas margens e de novo como despesa) ([D] p. 631).
- **Subtrair as dívidas futuras implícitas** na estrutura-alvo ([D] p. 618–619).

## 6. Onde concordam e onde divergem

**Concordam**: caixa à parte e pelo valor de face; ativos não operacionais somados a mercado; a diluição por opções reduz o valor por ação.

| Ponto | Damodaran | Póvoa |
|---|---|---|
| Caixa e risco | O beta deve refletir só os ativos operacionais (p. 595) | Recalcula o beta só se caixa > 20% do ativo (p. 357–361) |
| Opções | Modelo de opções (p. 625–631) | Discute o LPA diluído (p. 88–89) |
| Participações | Avaliar cada uma (p. 609–614) | Não detalha nos trechos lidos |
| Classes de ações | Prêmio de voto (p. 631–633) | Controle no Cap. 10 (tema 40) |

## 7. Limites: o que está defasado ou é específico do Brasil

- **IFRS 16**: arrendamentos já são passivo. Use o passivo de arrendamento como dívida, coerente com o EBITDA pós-IFRS 16.
- **Brasil**: provisões para contingências (trabalhistas e fiscais) e **depósitos judiciais** são relevantes. Créditos tributários (PIS/COFINS, ICMS) podem ser ativos não operacionais. *Não estão nos livros.*
- **ON × PN e tag along** (Lei 6.404, art. 254-A; regulamentos do Novo Mercado): afetam o prêmio de voto. *Fora dos livros.*
- **Tabela 10.3 de [P]** (p. 357): diz "2012", mas lista empresas que não existiam mais com esse nome naquele ano (por exemplo, Unibanco Holdings, Tele Centro-Oeste Celular). Provavelmente os dados são mais antigos **[inferência minha]**.
- **[D] p. 603** traz uma nota de revisão esquecida ("[NOTE: I removed this sentence…]").

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. **Tabela-ponte padrão** em todo vídeo: EV operacional → + caixa → + participações → − dívida bruta (com leasing) → − minoritários a valor justo → − contingências → equity → ÷ ações = preço justo.
2. **Caixa operacional mínimo** = X% da receita (definido por setor), e só o excedente é somado.
3. **Minoritários a valor justo**: múltiplo P/L ou P/VP da subsidiária, ou DCF da subsidiária quando relevante. Nunca o valor contábil, se for material.
4. **Contingências**: somar as prováveis, com análise das possíveis quando forem materiais.
5. **Opções**: treasury stock por padrão; modelo de opções se a diluição passar de 2%.
6. **ON/PN**: valor igual por padrão. Mostre o prêmio histórico de mercado como informação.

## 9. Dúvidas abertas para você decidir

1. Caixa operacional mínimo: % da receita fixo, por setor ou zero?
2. Contingências "possíveis" (não provisionadas): ignorar, ponderar por probabilidade ou só citar?
3. Prêmio de ON sobre PN: aplicar ou não?
4. Depósitos judiciais: somar como ativo?
