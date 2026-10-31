# Fichamento 15: Teste de consistência do crescimento (curto prazo e perpetuidade); capacidade ociosa e depreciação

**Fontes**
- **[D]** Damodaran (2002), Cap. 11, fundamentos do crescimento, ROC variável e reinvestimento negativo (PDF p. 401–410). Cap. 12, "Constraints on Stable Growth", "Can the stable growth rate be negative?", "Reinvestment and Retention Ratios", Ilustração 12.2 e "Closing Thoughts" (p. 428–440, 447–448). Cap. 15, condições do modelo estável (p. 537–538).
- **[P]** Póvoa (2012), Cap. 8: "O teste da consistência na perpetuidade" (p. 271–276), "O teste da consistência no curto prazo" (p. 276–279), "A questão da capacidade ociosa" (p. 279), "A questão da depreciação" (p. 280–281) e "O crescimento do lucro líquido" (p. 281–282).

---

## 1. Conceito central

O crescimento projetado precisa ser **compatível** com o reinvestimento e com o retorno projetados. Na **perpetuidade** há limites: g ≤ crescimento nominal da economia (na moeda do fluxo), e o reinvestimento tem de ser **g/ROC**, porque sem investimento não há crescimento perpétuo ([D] p. 428–430, 437; [P] p. 271–276). No **curto prazo**, qualquer crescimento é possível, mas ele se decompõe em reinvestimento × ROC **mais** o ganho ou a perda de produtividade sobre o capital existente ([P] p. 276–279; [D] p. 400, 407). Os dois mostram que, com **ROC = WACC** na perpetuidade, **g não altera o valor** ([D] p. 438).

## 2. Fórmulas

**Perpetuidade**
- `g_estável ≤ g nominal da economia` (moeda e inflação do fluxo). Regra prática: **g ≤ Rf** ([D] p. 429–430).
- `Reinvestimento_estável = g / ROC_estável` ([D] p. 437; [P] p. 274).
- `Retenção_estável = g / ROE_estável` (DDM); `reinvestimento do acionista = g / ROE` (FCFE) ([D] p. 437).
- `TV = EBIT_{n+1}(1−t)(1 − g/ROC) / (WACC − g)`. Se **ROC = WACC**: `TV = EBIT_{n+1}(1−t) / WACC`, e o valor independe de g ([D] p. 438).

**Curto prazo** ([P] p. 277–278; [D] p. 407)
`g_EBIT(1−t),t = RR_t × ROC_t + (ROC_t − ROC_{t−1}) / ROC_{t−1}`

**Ajuste de depreciação fiscal ≠ real (pré-IFRS)** ([P] p. 280–281): investimento líquido = investimento bruto − depreciação fiscal, mais um termo de correção. *A fórmula completa está numa imagem que não saiu no texto extraído [NÃO VERIFICADO].*

**Exemplo de consistência de [P]** (siderúrgica madura, p. 272–275) ✔
EBIT(1−t) = 200; ΔCG = 60 (6% da Δreceita de 1 bi); investimento físico líquido = 0; ROC = WACC = 15%; g proposto = 7,5%.
- Sem teste: FCFF = 140 → TV = 140 × 1,075 / (0,15 − 0,075) = **2.006,7**.
- Hipótese 1 (manter o investimento): g possível = (60/200) × 15% = **4,5%** → TV = 140 × 1,045 / 0,105 = **1.393** (−30,6%).
- Hipótese 2 (manter g = 7,5%): RR necessário = 0,075/0,15 = **50%** → reinvestimento de 100 → FCFF = 100 → TV = 100 × 1,075 / 0,075 = **1.433,3** (−28,6%).
- *Erro de digitação em [P] p. 274:* "Taxa de Reinvestimento necessária… = 0,075"; o correto é 0,50, como a linha seguinte usa.

**Exemplo de [D]** (Alloy Mills, p. 439–440): ROC 20% e RR 50% → g = 10% por 5 anos, depois g = 5%. Com ROC estável de 20% (RR = 25%), a empresa vale 1.825. Com ROC estável de 10% (RR = 50%), vale 1.300. Com ROC de 10% e g de 4% ou 0%, o valor fica inalterado (TV menor, mas FCF do ano 5 maior). *Inconsistência em [D] p. 440:* o texto diz que "o valor da firma permanece em US$ 1.600 milhões", mas os cálculos mostram US$ 1.300 milhões.

## 3. Premissas e escolhas dos autores

- **Limites do g estável** ([D] p. 428–430): (1) empresa doméstica × multinacional (até +0,5–1 p.p. para a multinacional); (2) nominal × real; (3) moeda: em moeda de inflação alta, o g nominal é maior. Empresas maduras podem e até devem crescer **abaixo** da economia.
- **g negativo** é legítimo para setores em extinção, como uma liquidação parcial a cada ano (máquinas de escrever, defesa no pós-Guerra Fria) ([D] p. 430).
- **Excesso de retorno na perpetuidade**: ROC = WACC é o "puro", mas Damodaran prefere mover o ROC para a **média do setor**, porque vantagens competitivas não somem de uma vez ([D] p. 435, 442). Póvoa: no longo prazo o ROC tende a um equilíbrio "próximo ao seu WACC" ([P] p. 271).
- **Crescimento acima do PIB** na perpetuidade não fere a teoria, já que o PIB é uma média de setores. Mas 12% nominais perpétuos dobrariam a fatia da empresa na economia em 17 anos. Empresas de tecnologia pedem **mais anos explícitos**, não um g perpétuo alto ([P] p. 275–276).
- **Qual hipótese usar** ([P] p. 275): é preferível fixar o g pelo PIB potencial (Hipótese 2) e ajustar o investimento, porque o plano de investimento declarado pela empresa muda com o tempo.
- **Capacidade ociosa** ([P] p. 279): no curto prazo, a empresa pode crescer com reinvestimento negativo, compensado pelo aumento do ROC (diluição de custo fixo). No longo prazo, o investimento líquido volta a ser necessário. [D] (p. 406–407) diz o mesmo: superinvestimento passado permite viver dele por um tempo; depois, volte ao reinvestimento do setor.
- **Depreciação** ([P] p. 280–281): com o IFRS, a depreciação societária reflete a vida útil real. O problema da depreciação fiscal some para quem converge totalmente.
- **Lucro líquido** ([P] p. 281–282): na perpetuidade, `g_LL = b × ROE`, e a taxa de reinvestimento vem direto da retenção.
- **Crítica comum ao DCF** ([D] p. 447–448): "o valor terminal é grande demais e manipulável". Damodaran responde que ele é grande porque o retorno vem da venda futura, e que só é manipulável se o analista usar múltiplos ou violar as duas regras: g ≤ economia e reinvestir para crescer.

## 4. Passo a passo prático (checklist de consistência)

**Perpetuidade**
1. g ≤ PIB nominal de longo prazo na moeda do fluxo, e g ≤ Rf ([D] p. 429–430).
2. Defina o ROC estável: entre o WACC e a média do setor ([D] p. 435).
3. Reinvestimento = g / ROC estável. Recalcule o FCFF do ano n+1 ([D] p. 437; [P] p. 274).
4. Beta estável entre 0,8 e 1,2; D/(D+E) maduro ([D] p. 434–436).
5. ΔCG não negativo na perpetuidade ([D] p. 538).
6. Teste: se ROC = WACC, o g não deve mudar o valor. Se mudar muito, há excesso de retorno embutido e ele precisa ser justificado.

**Curto prazo**
7. Decomponha o crescimento anual do EBIT(1−t) em RR × ROC + Δeficiência ([P] p. 277–278).
8. Desconfie de reinvestimento negativo persistente sem uma explicação (capacidade ociosa) ([P] p. 279; [D] p. 406).
9. Confirme a política de depreciação com a área de RI ([P] p. 280).

## 5. Erros comuns apontados pelos autores

- **"Na perpetuidade, investimento = depreciação, capital de giro zero e g = 7%"**: crescimento sem investimento ([P] p. 275–276).
- **"g nominal de 12% na perpetuidade"** ([P] p. 275–276).
- **g estável acima do Rf ou da economia** ([D] p. 428–430).
- **Reinvestimento na perpetuidade não ligado a g** ([D] p. 437–438; Cap. 15, p. 538).
- **ΔCG negativa perpétua**, que levaria o capital de giro a −∞ ([D] p. 538, nota 2).
- **Manipular o valor terminal com múltiplos** ([D] p. 448; tema 29).

## 6. Onde concordam e onde divergem

**Concordam**: RR = g/ROC na perpetuidade; g limitado pela economia; o ROC converge; decomposição do curto prazo com termo de eficiência.

| Ponto | Damodaran | Póvoa |
|---|---|---|
| ROC na perpetuidade | Média do setor (com algum excesso de retorno) (p. 435, 442) | "Próximo ao WACC" (p. 271), sem se fixar nisso |
| Teto de g | ≤ economia e ≤ Rf (p. 429–430) | PIB potencial como referência; "moderadamente acima" é aceitável (p. 276) |
| Hipótese preferida | Liga RR a g (p. 437) | Fixa g pelo PIB e ajusta o investimento (Hipótese 2) (p. 275) |
| Depreciação | Não discute | Ajuste fiscal × real (p. 280–281) |

## 7. Limites: o que está defasado ou é específico do Brasil

- PIB potencial nominal brasileiro de 7,5% a.a. ([P] p. 273, 276), premissa de 2012: **revisar no `MACRO.md`**.
- O ajuste de depreciação pré-IFRS é obsoleto para companhias abertas brasileiras (IFRS obrigatório desde 2010) **[conferir exceções]**.
- No Brasil, com inflação maior que nos EUA, o g nominal em R$ é naturalmente maior que em US$ (lógica de [D] p. 429).

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. **Regras duras na planilha**: (a) g_perp ≤ min(PIB nominal LP, Rf); (b) RR_perp = g/ROC_perp, calculado e não digitado; (c) ΔCG_perp ≥ 0; (d) beta_perp entre 0,8 e 1,2.
2. **Mostrar sempre o "teste ROC = WACC"**: valor terminal com ROC_perp = WACC ao lado do valor-base. A diferença é o **valor do excesso de retorno perpétuo**, e é ela que precisa ser defendida no vídeo.
3. **Decomposição do crescimento** no período explícito (reinvestimento × eficiência), como no exemplo dos fertilizantes de [P].
4. Para empresas com capacidade ociosa, documentar até quando o reinvestimento baixo é sustentável.

## 9. Dúvidas abertas para você decidir

1. ROC na perpetuidade: igual ao WACC (conservador), média do setor ou um meio-termo?
2. Teto de g: PIB nominal, Rf ou o menor dos dois?
3. Publicar o "valor do excesso de retorno perpétuo" como linha separada?
