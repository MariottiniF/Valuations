# Fichamento 42: EVA, CFROI e outras métricas de criação de valor

**Fontes**
- **[D]** Damodaran (2002), Cap. 32 "Value Enhancement: EVA, CFROI and Other Tools" (PDF p. 1221–1255): **lidos a introdução e o resumo** (p. 1221, 1251–1252); estrutura mapeada (EVA, ligação EVA ↔ DCF, EVA e crescimento, CFROI). Cap. 2, modelo de excesso de retorno (p. 22; tema 02).
- **[P]** Póvoa (2012), Cap. 10, "Economic value added" (p. 379–392): lucro econômico, exemplo de dois anos, alocação por segmento, terminologia e ajustes (full cost, P&D), EVA do acionista, MVA (p. 388–391); "Outras metodologias de valor" (p. 392–396): CFROI, TSR.

---

## 1. Conceito central

**Gerar valor = retorno sobre o investimento − custo do capital** ([P] p. 379). O EVA mede o excesso de retorno **em reais**: `capital investido × (ROIC − WACC)` ([P] p. 380). O conceito de lucro econômico é "mais do que secular"; o nome EVA é marca da Stern Stewart ([P] p. 380). O valor de uma empresa pode ser escrito como **capital investido + VP dos EVAs futuros**, o que é equivalente ao DCF se as premissas forem as mesmas ([D] Cap. 2, p. 22; Cap. 32). O **MVA** é o valor de mercado menos o capital investido e, no longo prazo, converge para o VP dos EVAs ([P] p. 388–389). O **CFROI** é uma TIR dos ativos existentes, comparada ao custo de capital real ([D] p. 1251; [P] p. 392). Damodaran alerta que a simplicidade das métricas permite **manipulação**: trocar crescimento futuro por EVA alto hoje, ou migrar para investimentos mais arriscados ([D] p. 1251).

## 2. Fórmulas

- **EVA** ([P] p. 380): `EVA = capital investido × (ROIC − WACC) = NOPAT − WACC × capital`.
- **EVA do acionista** ([P] p. 388): `PL × (ROE − Ke)`.
- **Valor pela ótica do EVA** ([D] Cap. 2, p. 22): `valor = capital investido + Σ VP(EVA_t)`. Exemplo do tema 02: 100 + (12 − 10)/0,10 = 120 ✔.
- **MVA** ([P] p. 388): `valor de mercado das ações + dívida − capital investido`. No longo prazo, MVA = VP dos EVAs (p. 389).
- **Exemplo de dois anos de [P]** (p. 379–380) ✔: NOPAT de 80 mil (ano 1) e 320 mil (ano 2); retorno acumulado de 40% sobre 1 mi; custo acumulado de 1,15² − 1 = 32,25% (*o livro escreve "1,152", ou seja, 1,15²*); lucro econômico = 1 mi × (0,40 − 0,3225) = **77,5 mil**.
- **ROI com passivo não oneroso** ([P] p. 385) ✔: com o mesmo lucro de 5 mi, a empresa A (capital oneroso de 13 mi) tem 38,5% e a B (15 mi) tem 33,3%. Fornecedores reduzem o capital investido.
- **Ajuste de P&D no EVA** ([P] p. 387): lucro ajustado = 100 + 20 − 6 − 2 + 0,6 = **112,6**; capital = 1.000 + (20 − 2) = 1.018; ROI = **11,1%** (contra 10% contábil) ✔. **Divergência com [D]**: [P] desconta o benefício fiscal do P&D devolvido (−6) e soma o da amortização (+0,6). [D] Cap. 9 (p. 316, nota 1) argumenta que, como o P&D é integralmente dedutível, **não se ajusta o imposto**: o resultado seria 100 + 20 − 2 = 118 e ROI de 11,6%. A escolha muda o ROIC; ver dúvidas.

## 3. Premissas e escolhas dos autores

- **Ajustes de "full cost"** ([P] p. 386): P&D, marketing e outros investimentos lançados como despesa voltam ao lucro e ao capital. A Stern Stewart propõe dezenas de ajustes; na prática, poucos são relevantes.
- **Terminologia** ([P] p. 383): NOPAT, NOPLAT e capital investido são os mesmos conceitos do DCF com outros nomes.
- **Alocação de capital por segmento** ([P] p. 381): o EVA por divisão mostra onde se cria e onde se destrói valor.
- **MVA** ([P] p. 389–391): bom como indicador de longo prazo; ruim para remunerar executivos no curto prazo (o mercado oscila). Rankings de EVA/MVA favorecem empresas grandes.
- **Manipulação** ([D] p. 1251–1252): os gestores podem melhorar o EVA de hoje com menos investimento (menos crescimento futuro) ou com projetos mais arriscados. Atrelar remuneração a uma métrica faz os gestores otimizarem a métrica, não o valor.
- **Compromisso da gestão** ([D] p. 1251): nenhum mecanismo funciona sem compromisso real com a maximização de valor.
- **CFROI e TSR** ([P] p. 392–394): CFROI relativiza o fluxo pelo investimento bruto; TSR mede retorno total ao acionista. Use o TSR comparando com o custo de capital e o risco.

## 4. Passo a passo prático (uso no canal)

1. Calcule o **spread ROIC − WACC** e o **EVA** histórico (5 anos) e projetado.
2. Mostre o valor como **capital investido + VP dos EVAs**. Deve bater com o DCF; se não bater, há inconsistência.
3. Use o EVA por segmento quando a empresa divulgar dados por segmento.
4. Não use EVA de um ano isolado para julgar a gestão.

## 5. Erros comuns apontados pelos autores

- **Achar que EVA é outro método** com resultado diferente do DCF ([P] p. 300, 389; [D] Cap. 2, p. 22).
- **EVA de curto prazo como meta** (troca crescimento por EVA atual) ([D] p. 1251).
- **Ignorar passivos não onerosos** no capital ([P] p. 385).
- **Rankings de EVA/MVA** sem ajustar por tamanho ([P] p. 391).

## 6. Onde concordam e onde divergem

**Concordam**: EVA = excesso de retorno × capital; equivalência com o DCF; ajustes de P&D.

| Ponto | Damodaran | Póvoa |
|---|---|---|
| Ênfase | Limites e manipulação das métricas | Mecânica e exemplos |
| **Imposto no ajuste de P&D** | Não ajusta (P&D já dedutível) | Desconta o benefício fiscal |
| CFROI | TIR dos ativos existentes, comparada ao custo real | Breve menção |

## 7. Limites: o que está defasado ou é específico do Brasil

- No Brasil, o JCP reduz o "custo" efetivo do capital próprio no EVA do acionista (tema 22).
- O IFRS 16 eleva o capital investido; mantenha a coerência com o WACC (tema 07).

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. Mostrar o **spread ROIC − WACC** e o **EVA** como leitura de criação de valor (gráfico do tema 16).
2. Reconciliação: valor do DCF = capital + VP dos EVAs (checagem interna, não precisa ir ao vídeo).
3. Não usar MVA ou TSR como critério de valuation.

## 9. Dúvidas abertas para você decidir

1. Ajuste de P&D: com ou sem efeito fiscal ([D] × [P])? Sugestão: sem, como [D], se o P&D for dedutível no ano.
2. Apresentar o EVA no vídeo ou só no material de apoio?
