# Fichamento 37: Múltiplos de receita e setoriais: P/Receita, EV/Receita

**Fontes**
- **[D]** Damodaran (2002), Cap. 20 "Revenue Multiples and Sector-Specific Multiples" (PDF p. 760–801): definição (p. 761); distribuição (p. 762); P/Receita pelos fundamentos (p. 763–766); EV/Receita (p. 767–768); margem e estratégia de preços, nota sobre marca (p. 777–779); descasamentos (p. 780–782); regressões no setor e no mercado (p. 783–788); receita futura (p. 789); múltiplos setoriais: motivos, limites, definições, valor por cliente (p. 790–797); resumo (p. 798). *Lido: estrutura, fórmulas e resumo; exemplos intermediários apenas mapeados.*
- **[P]** Póvoa (2012), Cap. 9: P/Receita, "múltiplo híbrido" (p. 331–338); EV/Receita (p. 338–341); múltiplos técnicos (p. 341–342, apenas mapeado).

---

## 1. Conceito central

Os múltiplos de receita são **menos afetados pela contabilidade** e existem mesmo para empresas com prejuízo ([D] p. 760, 798). Mas o determinante dominante é a **margem**: líquida para o P/Receita, operacional para o EV/Receita ([D] p. 764, 767; [P] p. 332–333). Por isso, comparar P/Receita sem olhar a margem é comparar empresas diferentes. O **P/Receita é inconsistente**: preço do acionista sobre receita da firma. Com alavancagens diferentes, o múltiplo distorce. O **EV/Receita** é a versão coerente ([P] p. 331, 338; [D] p. 761). Múltiplos **setoriais** (por cliente, assinante, tonelada) só valem com hipóteses fortes sobre operação e crescimento ([D] p. 790–798).

## 2. Fórmulas

- **Definições** ([D] p. 761): `P/Receita = valor de mercado do equity/receita`; `EV/Receita = (equity + dívida − caixa)/receita`.
- **P/Receita estável** ([D] p. 764; [P] p. 332): `margem líquida × payout × (1 + g)/(Ke − g)`.
- **EV/Receita estável** ([D] p. 767): `margem operacional após IR × (1 − RR) × (1 + g)/(WACC − g)`.
- **Regressão de [P] para o Brasil** (p. 333): `P/Receita = 0,8639 + 0,0364 × margem líquida` (margem em pontos percentuais). Exemplo: margem de 20 → 0,8639 + 0,728 = **1,59** (cálculo próprio a partir da equação do livro).
- **Regressão setorial** ([D] p. 784): `EV/Receita = a + b × margem operacional após IR`.
- **Valor por cliente** ([D] p. 793–795): VP do fluxo esperado de cada cliente ao longo da sua vida; base dos múltiplos por assinante.
- **Exemplo de supermercado** ([P] p. 339–340) ✔: margem operacional após IR de 4,9% × giro do ativo de 3 = ROC de **14,7%**.

## 3. Premissas e escolhas dos autores

- **Estratégia de preço** ([D] p. 777–779; [P] p. 334–338): reduzir preço (margem) para vender mais (giro) muda o múltiplo de receita. O valor depende da combinação margem × giro, não de um dos dois. [P] mostra isso com uma joalheria que escolhe entre manter margem alta e baixar preços (ROE de alto crescimento = 0,4 × 1,2 = **48%** ✔, p. 336).
- **Marca** ([D] p. 779): a marca aparece como margem maior; valor da marca ≈ diferença de valor entre a empresa com sua margem e com a margem de uma empresa genérica (tema 41).
- **Descasamentos** ([D] p. 780–782): margem baixa com múltiplo alto (cara) e o contrário (barata). [P] faz um screening com P/Receita < 1 e margem líquida > 20% (Tab. 9.4, p. 334).
- **Múltiplos setoriais** ([D] p. 790–797): populares em setores novos (internet em 2000: valor por visitante ou assinante). Limites: não se comparam com outros setores, e supõem que cada cliente gera o mesmo fluxo.
- **Receita futura** ([D] p. 789): para empresas jovens, aplicar o múltiplo de receita a uma receita de daqui a alguns anos e trazer a VP.

## 4. Passo a passo prático

1. Use múltiplos de receita para **empresas com prejuízo** ou margem deprimida temporariamente, e como checagem em varejo.
2. Prefira **EV/Receita** a P/Receita.
3. Sempre mostre ao lado a **margem operacional** (atual e normalizada) dos pares.
4. Para setoriais (EV por assinante, por tonelada, por MW), confira o valor por unidade implícito no DCF.

## 5. Erros comuns apontados pelos autores

- **Usar P/Receita** com alavancagens diferentes ([P] p. 331; [D] p. 761).
- **Comparar múltiplos de receita sem a margem** ([D] p. 798).
- **Múltiplos setoriais sem hipóteses explícitas** ([D] p. 790–798).

## 6. Onde concordam e onde divergem

**Concordam**: a margem é o determinante principal; EV/Receita é mais coerente; regressões margem × múltiplo.

| Ponto | Damodaran | Póvoa |
|---|---|---|
| Setoriais | Analisa e define valor por cliente | Mapeado como "múltiplos técnicos" (p. 341–342), não lido em detalhe |
| Exemplos | Varejo e tecnologia nos EUA | Joalheria, supermercado; regressão Brasil |

## 7. Limites: o que está defasado ou é específico do Brasil

- A regressão de [P] é de outra época; refazer com dados atuais.
- Setoriais comuns no Brasil: EV/capacidade (MW) em energia, EV/km em rodovias, EV/tonelada em siderurgia e celulose, EV/cliente em telecom e saneamento. **Não estão nos livros**.

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. EV/Receita só como checagem (varejo, empresas com margem deprimida).
2. Setoriais: mostrar o valor por unidade implícito no DCF contra transações recentes, quando houver.

## 9. Dúvidas abertas para você decidir

1. Quais múltiplos setoriais padronizar por setor?
2. Incluir transações de M&A como referência de EV por unidade?
