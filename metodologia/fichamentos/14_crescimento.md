# Fichamento 14: Estimativa de crescimento (histórico, analistas, fundamentos)

**Fontes**
- **[D]** Damodaran (2002), Cap. 11 "Estimating Growth" (PDF p. 373–424): crescimento histórico (p. 374–388), estimativas de analistas (p. 388–394), fundamentos do crescimento (p. 394–410), crescimento de receita, margens e *sales-to-capital* (p. 410–419), aspectos qualitativos (p. 419–421) e resumo (p. 421–422).
- **[P]** Póvoa (2012), Cap. 8 "Taxa de crescimento: a busca da consistência" (p. 269–289).

---

## 1. Conceito central

Há três fontes de crescimento: **o passado**, **os analistas** e **os fundamentos**. Damodaran mostra que o crescimento passado tem pouco poder preditivo ("Higgledy Piggledy Growth", correlação média ~0,02, Little, 1960) e que os analistas só são melhores no curtíssimo prazo ([D] p. 383–384, 391–392). A forma **mais sólida** é tornar o crescimento **endógeno**, função de **quanto** a empresa reinveste e **com que retorno**: `g = taxa de reinvestimento × retorno` ([D] p. 394, 402, 421–422). Póvoa adota a mesma lógica: o lucro operacional só cresce com **mais investimento** ou **mais eficiência** (ROC maior) ([P] p. 271).

## 2. Fórmulas

**Crescimento do LPA** ([D] p. 395; [P] p. 281)
`g_LPA = b × ROE`, com b = índice de retenção = 1 − payout (sem emissão de ações).

**Crescimento do lucro líquido** ([D] p. 396)
`Reinvestimento do acionista = Capex − D&A + ΔCG − (novas dívidas − amortizações)`
`Taxa de reinvestimento do acionista = reinvestimento do acionista / LL` (pode passar de 100%)
`g_LL = taxa de reinvestimento do acionista × ROE`

**ROE e alavancagem** ([D] p. 397–398; [P] p. 283)
`ROE = ROC + (D/E) × [ROC − i(1 − t)]`, com D/E, i e ROC **contábeis**.
`g = b × {ROC + (D/E)[ROC − i(1−t)]}`

**Crescimento do lucro operacional** ([D] p. 402; [P] p. 271)
`g_EBIT(1−t) = taxa de reinvestimento × ROC`
`Taxa de reinvestimento = (Capex − D&A + ΔCG não caixa) / EBIT(1−t)`; `ROC = EBIT(1−t) / capital investido (contábil)`
Variante DuPont de [P] (p. 272): `g = reinvestimento × margem operacional × giro do ativo`.

**Crescimento com retorno variável** ([D] p. 400, 407–408; [P] p. 277–278)
`g = ROC_t × reinvestimento + (ROC_t − ROC_{t−1}) / ROC_{t−1}` (o segundo termo é o "crescimento por eficiência" sobre o estoque de capital).
- [D] Con Ed: ROE de 11,63% → 13%, b = 29,96% → g de um ano = 0,13 × 0,2996 + (0,13 − 0,1163)/0,1163 ≈ 15,7%, depois 3,89% ([D] p. 400–401).
- [P] Fertilizantes: 2012: 0,415 × 0,20 + 0,50 = **+58,3%**; 2013: 0,326 × 0,05 − 0,75 = **−73,4%** ([P] p. 277–279) ✔.
- *Erro de digitação em [D] p. 407:* o denominador do segundo termo aparece como ROC_t, mas o exemplo (10% → 11% = +10%) e a versão do ROE (p. 400) usam ROC_{t−1}.

**ROE marginal** ([D] p. 399): `ROE marginal = ΔLL_t / ΔPL_{t−1}`. Reliance: média de 19,43%, marginal de 35,54%.

**Empresa com prejuízo: crescimento pela receita** ([D] p. 410–418)
Receita (g decrescente com o tamanho) × margem-alvo (margem dos maduros do setor, convergindo) → EBIT. Reinvestimento = ΔReceita / (vendas/capital). Checagem: o ROC implícito em cada ano deve convergir para a média do setor.
Tamanho de mercado: `Receita_10 = mercado × (1+g_mercado)^10 × fatia` → g composto. Exemplo: varejo de brinquedos, 70 bi × 1,03¹⁰ × 5% = 4,703 bi → 46,98% a.a. ([D] p. 415).

## 3. Premissas e escolhas dos autores

- **Histórico** ([D] p. 374–388): use a média **geométrica**; a receita é mais persistente que o lucro (p. 385); cuidado com o tamanho (Cisco não manteria 86,57% a.a.; p. 386–387). Em empresas jovens, use o histórico só para o próximo ano ou dois, ano a ano, e olhe o crescimento do mercado (p. 387–388). Póvoa: quanto mais rápido o crescimento passado, menos provável que se repita. O histórico só serve para empresas **maduras** e estáveis (tamanho, estrutura de capital, setor e fatia) ([P] p. 270).
- **Analistas** ([D] p. 388–394): são melhores em 1 a 2 trimestres, mas não no longo prazo; usam muito o próprio histórico; projetam **LPA**, que cresce mais que o EBIT por causa da alavancagem, então é preciso ajustar para baixo. O peso deles cresce com informação recente, número de analistas, baixa dispersão e qualidade. "O segredo de uma boa valuation está em descobrir inconsistências entre as previsões dos analistas e os fundamentos" (p. 393–394).
- **Fundamentos** ([D] p. 402–403): reinvestimento e ROC devem ser **prospectivos**. Use médias (de 3 a 5 anos, somando valores e não médias de taxas, nota 5) quando o reinvestimento for irregular; ajuste o ROC para a média do setor se estiver muito acima dela; trate P&D e leasing como capex e dívida (Cap. 9).
- **Reinvestimento negativo** ([D] p. 406–407): em geral é temporário (capex irregular, capital de giro). Use a média. Se for capacidade ociosa, cresça por ganho de ROC e depois volte ao reinvestimento do setor ([P] p. 279). Se for liquidação gradual, g negativo é coerente.
- **ROC e ROE contábeis, não de mercado** ([P] p. 282–283): o lucro é uma "variável-estoque" de um ano, enquanto o valor de mercado é o valor presente de todos os fluxos. Dividir um pelo outro seria "maçã com banana".
- **Depreciação real × fiscal** ([P] p. 280–281): antes do IFRS, a depreciação fiscal distorcia o investimento líquido. Com IFRS, use a depreciação societária, que reflete a vida útil econômica.
- **Qualitativos** ([D] p. 419–421): gestão, marketing, marca e concorrência precisam aparecer em ROC, margem, giro ou reinvestimento. "If you cannot [quantify], you should remain skeptical" (p. 420).

## 4. Passo a passo prático

1. **Empresa lucrativa e madura**: calcule o ROC e o reinvestimento (média de 3 a 5 anos, somando valores) → g = RR × ROC. Compare com o histórico de receita e com o consenso.
2. **Empresa com ROC mudando**: some o termo de eficiência (ROC_t/ROC_{t−1} − 1) no ano da mudança ou distribua-o linearmente ([D] p. 409).
3. **Empresa com prejuízo ou em transição**: receita (tamanho de mercado e fatia) → margem convergindo para a margem dos maduros → reinvestimento por vendas/capital → checagem do ROC implícito ([D] p. 410–419).
4. **Para o acionista**: g_LPA = b × ROE, ou g_LL = reinvestimento do acionista × ROE. Decomponha o ROE (ROC, alavancagem, juros) para ver de onde vem o retorno ([D] p. 397–399; [P] p. 283–289).
5. **Sanidade**: receita no ano 10 contra o tamanho do mercado; ROC implícito contra o setor e o WACC.

## 5. Erros comuns apontados pelos autores

- **Extrapolar o crescimento passado**, principalmente de lucro e de empresas pequenas ou que cresceram muito ([D] p. 383–387; [P] p. 270).
- **Usar o consenso de LPA como crescimento do EBIT** ([D] p. 392).
- **Projetar crescimento sem reinvestimento**, ou reinvestimento sem retorno coerente ([P] p. 275–276; [D] p. 421–422).
- **Usar média aritmética** de taxas de crescimento voláteis ([D] p. 375–376).
- **Ignorar que o ROE alto pode vir de alavancagem, de resultado não operacional ou de imposto baixo** (Reliance, [D] p. 398–399).
- **Contar histórias** sem traduzi-las em números (Ashford a 60% a.a. "porque o mercado é enorme") ([D] p. 421).

## 6. Onde concordam e onde divergem

**Concordam**: g = reinvestimento × retorno; o histórico serve pouco; o ROC converge; ROE = ROC + alavancagem × spread; crescimento por eficiência no curto prazo.

| Ponto | Damodaran | Póvoa |
|---|---|---|
| Analistas | Discute a evidência e como ponderar (p. 388–394) | Não trata do consenso nesse capítulo |
| Empresa com prejuízo | Receita → margem → vendas/capital (p. 410–419) | Não trata nesse capítulo |
| Depreciação | Não discute o problema fiscal × real | Ajuste para pré-IFRS (p. 280–281) |
| ROE com mudança de alavancagem | Fórmula (p. 397–398) | Exemplos com ponto de equilíbrio de D/E e de juros (p. 284–289) |

## 7. Limites: o que está defasado ou é específico do Brasil

- Exemplos de empresas (Cisco, Commerce One, Ashford) e estudos (anos 1960 a 1990) são datados.
- **PIB potencial nominal de 7,5%** em [P] (p. 273, 276) é premissa de 2012 e precisa ser revista no `MACRO.md`.
- **IFRS**: o problema de depreciação de [P] (p. 280–281) já foi resolvido para as listadas. Ainda vale conferir a vida útil adotada.

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. **Crescimento sempre derivado** de reinvestimento × ROC (ou de vendas/capital), nunca digitado à mão.
2. Na planilha, cada ano mostra: g da receita, margem, EBIT(1−t), reinvestimento, capital investido, **ROC implícito** e RR. Isso dá transparência total.
3. Use **média de 3 a 5 anos** (somando valores) para reinvestimento e ROC de partida.
4. **Checagem cruzada** com o histórico de receita e com o consenso do mercado, comentando no vídeo de onde vêm as divergências ([D] p. 393–394).
5. Separe no vídeo a contribuição de **reinvestimento** e de **eficiência** para o crescimento ([P] p. 277–279).

## 9. Dúvidas abertas para você decidir

1. Ponto de partida do ROC: último ano, média de 3 a 5 anos ou média do setor?
2. Usar o consenso de mercado no período explícito curto (anos 1 e 2)?
3. Abordagem padrão: g = RR × ROC ou receita + margem + vendas/capital?
