# Fichamento 48: Imóveis, outros ativos, títulos e futuros

> **Profundidade reduzida (○)**: baseado nos resumos dos capítulos e, no Cap. 27, no trecho sobre marcas e licenças. Exemplos não recalculados, exceto onde indicado.

**Fontes**
- **[D]** Damodaran (2002): Cap. 26 "Valuing Real Estate" (PDF p. 1028–1066; resumo p. 1063); Cap. 27 "Valuing Other Assets" (p. 1067–1089): franquias (p. 1068–1075), consultório dentário (p. 1075–1077), restaurante (p. 1077–1079), "key person" (p. 1079), marcas, direitos e licenças (p. 1080–1082), arte e colecionáveis (p. 1083–1089); Cap. 33 "Valuing Bonds" (p. 1256–1307; resumo p. 1303); Cap. 34 "Valuing Forward and Futures Contracts" (p. 1308–1337; resumo p. 1334).
- **[P]** Póvoa (2012): não há capítulos específicos.

---

## 1. Conceito central

Todos os ativos, financeiros ou reais, **podem ser avaliados pelos mesmos princípios**: VP dos fluxos esperados à taxa que reflete o risco, ou comparação com ativos semelhantes ([D] Cap. 27, p. 1067; Cap. 26, p. 1063). As diferenças são práticas:
- **Imóveis** não são negociados com frequência, o que dificulta estimar risco e taxa e encontrar comparáveis ([D] p. 1063).
- **Títulos** valem o VP dos cupons e do principal, à taxa livre de risco mais prêmios de prazo e de crédito. Cláusulas especiais (conversão, call, put) são opções ([D] p. 1303).
- **Futuros e termos** derivam do ativo-objeto por **arbitragem**: juros, custo de armazenagem e rendimento do ativo ligam o preço futuro ao à vista ([D] p. 1334).
- **Direitos com prazo** (marcas licenciadas, direitos autorais) não têm valor terminal ([D] p. 1080; tema 41).
- **Arte e colecionáveis** não geram caixa; o valor vem do preço que outros pagarão ([D] p. 1083 em diante).

## 2. Fórmulas

- **Título** ([D] p. 1303): `P = Σ cupom/(1 + r)^t + face/(1 + r)^n`, com r = Rf + prêmio de prazo + prêmio de default.
- **Futuro** ([D] p. 1334): `F = S × (1 + r − y)^t + custos de armazenagem` (forma geral da relação de arbitragem).
- **Franquia** ([D] p. 1072, exemplo) ✔: Ke = 8% + 1,25 × 5,5% = **14,88%**; WACC = 14,88% × 0,5 + 10% × (1 − 0,4) × 0,5 = **10,44%**.
- **Restaurante** ([D] p. 1079) ✔: Ke = 8% + 0,7 × 5,5% = **11,85%**; WACC = 11,85% × 0,9 + 9% × 0,6 × 0,1 = **11,20%**.

## 3. Premissas e escolhas dos autores

- **Imóveis** ([D] Cap. 26): o beta por regressão de índices de imóveis é pouco confiável (os índices são suavizados por avaliações); fluxo de aluguel menos custos e vacância; valor terminal pela venda.
- **"Key person"** ([D] p. 1079): em negócios pequenos, o valor depende de uma pessoa; avalie com e sem ela.
- **Títulos com opções** ([D] p. 1303): cláusulas que favorecem o comprador aumentam o valor (conversão, put); as que favorecem o emissor reduzem (call).
- **Futuros** ([D] p. 1334): limites de preço, ajuste diário (marking to market) e opções de entrega afetam o preço.

## 4. Passo a passo prático (uso no canal)

1. **Imóveis em balanço** (shoppings, lajes, terrenos): avaliar pelo NOI e cap rate de mercado, ou pelo DCF do aluguel, e somar como ativo não operacional quando não fizerem parte da operação (tema 31).
2. **Debêntures e dívida** a valor de mercado no WACC (temas 21 e 23).
3. **Curvas futuras de commodities** (petróleo, minério, celulose) na fase explícita das cíclicas (tema 45).

## 5. Erros comuns apontados pelos autores

- Usar betas de índices suavizados para imóveis ([D] Cap. 26).
- Dar valor terminal a direitos com prazo ([D] p. 1080).
- Ignorar as opções embutidas em títulos ([D] p. 1303).

## 6. Onde concordam e onde divergem

Póvoa não trata esses ativos; não há divergência a registrar.

## 7. Limites: o que está defasado ou é específico do Brasil

- No Brasil: FIIs como referência de cap rate; títulos públicos (NTN-B, LTN, LFT) e debêntures incentivadas (isenção de IR para pessoa física) **[fora dos livros]**.

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. Ativos imobiliários não operacionais avaliados à parte, com cap rate declarado.
2. Curva futura como insumo das cíclicas, convergindo para o preço normalizado.

## 9. Dúvidas abertas para você decidir

1. Fonte de cap rates (FIIs, laudos, transações)?
2. Aprofundar algum destes capítulos?
