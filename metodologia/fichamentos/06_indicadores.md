# Fichamento 06: Indicadores financeiros (liquidez, atividade, rentabilidade, endividamento) e sua relação com o valuation

**Fontes**
- **[D]** Damodaran (2002), Cap. 3: ROA e ROC (PDF p. 59–60), decomposição margem × giro (p. 60), ROE e sua decomposição pela alavancagem (p. 61–63), medidas de risco: liquidez corrente e seca (p. 63–66), cobertura de juros e de encargos fixos, FCO/capex (p. 67–68), índices de endividamento e variantes (p. 69–71).
- **[P]** Póvoa (2012), Cap. 2: indicadores de liquidez, atividade e ciclo de caixa, margens (p. 40–52); ROA e ROE (p. 53–54); Sistema DuPont (p. 55); endividamento financeiro, cobertura de juros, "o fantasma das dívidas" (p. 56–59); Basileia e multiplicador de capital de terceiros, imobilização do PL (p. 60–61); análise combinada (p. 62–63); análise horizontal e vertical (p. 64).

---

## 1. Conceito central

Indicadores são **diagnóstico**, não valuation. Eles servem para entender o histórico e calibrar as premissas da projeção: margem, giro do capital (reinvestimento), retorno sobre o capital (criação de valor), risco de liquidez e de alavancagem (custo da dívida, rating sintético). Os dois autores destacam que **retorno = margem × giro** ([D] p. 60; [P] p. 55), e que o retorno só tem significado **comparado ao custo de capital** ([P] p. 53; [D] p. 60–61). Os indicadores devem ser comparados **dentro do mesmo setor**, para não comparar "maçãs com bananas" ([P] p. 54).

## 2. Fórmulas

**Rentabilidade**
- **ROA** ([P] p. 53): `Lucro operacional × (1 − t) / Ativo médio`. [D] (p. 59): `EBIT(1 − t)/Ativo total` ou `(LL + juros × (1 − t))/Ativo`.
- **ROC** ([D] p. 59): `EBIT(1 − t)/(dívida contábil + PL contábil)`. Melhor que o ROA quando há muito passivo circulante ou passivo sem juros.
- **DuPont** ([D] p. 60; [P] p. 55): `ROC = margem operacional após IR × giro do capital`; `ROE = margem líquida × giro do PL` ([P]).
- **ROE e alavancagem** ([D] p. 61–63): `ROE = ROC + D/E × [ROC − i × (1 − t)]`, com i = taxa contábil de juros. Alavancagem eleva o ROE só se ROC > custo da dívida após IR.
- *Nota de [P] p. 55*: "(1 − t)" não é uma alíquota marginal, mas a dedução de **todos os impostos pagos** ainda não computados. Ver o alerta do tema 09 sobre benefício fiscal dos juros.

**Liquidez** ([D] p. 65–66; [P] p. 40–45): corrente = AC/PC; seca = (AC − estoques)/PC; [P] usa também solvência de caixa e liquidez geral.

**Atividade** ([P] p. 46–50): PMR, PME, PMP; **ciclo de caixa = PMR + PME − PMP**. Exemplo de [P]: 91 + 37 − 31 = **97 dias** ✔.

**Endividamento** ([P] p. 56–58; [D] p. 69–71)
- [P] exemplo da empresa de alimentos (2002) ✔: `EF = Dívida/(Dívida + PL) = 17.500/22.600 = 77,4%`; capital próprio = 22,6%; dívida de CP = 2.000/17.500 = 11,4%.
- **Cobertura de juros** ([D] p. 67; [P] p. 58): EBIT/despesa de juros. [P] ✔: 3.260/(6.000 − 200) = 56,2%, ou seja, o operacional cobre só metade dos juros (2002, dívida em dólar).
- **FCO/capex** ([D] p. 68): `FCO = EBIT(1 − t) − ΔCG`, porque cobertura de juros ignora o capex necessário.
- **D/E a mercado** ([D] p. 70): a variante relevante para o custo de capital.
- **Bancos** ([P] p. 60): Índice de Basileia, mínimo de 8% pelo Comitê e de 11% pelo Banco Central à época; multiplicador de capital de terceiros = ativo total/dívida (26.100/17.500 = 1,5 ✔).

## 3. Premissas e escolhas dos autores

- **Retorno contra custo de capital** ([P] p. 53; [D] p. 61): ROA/ROC contra WACC; ROE contra Ke. É o elo com o tema 16.
- **Valores médios ou de início de período** ([D] p. 59): Damodaran mostra os dois; para retorno sobre investimento, o capital **do início** do período é o mais coerente (ver tema 16). [P] usa ativo e PL **médios**.
- **ROE como payback é ingênuo** ([P] p. 54): ROE de 25% sugere "4 anos de payback" só sob a hipótese irrealista de manter o ritmo.
- **Dívida não é vilã** ([P] p. 59): alavancagem bem usada cria valor; o problema é dívida cara, curta ou descasada da moeda.
- **Liquidez corrente alta não é virtude** ([D] p. 65): pode indicar capital de giro mal administrado; e o índice muda com movimentos iguais de AC e PC.
- **Análise combinada** ([P] p. 62–63): olhar os indicadores em conjunto (exemplo Bradesco, Ultrapar e Sadia em 2002: setores diferentes chegam a retornos semelhantes por combinações diferentes de margem e giro, p. 55).
- **Análise horizontal e vertical** ([P] p. 64): vertical = cada linha como % da receita (base 100); horizontal = evolução no tempo. Ajudam a localizar a origem de mudanças de margem.

## 4. Passo a passo prático

1. Calcule, para 5 anos: margem bruta, EBIT, líquida; giro do capital investido; ROIC (tema 16); ROE; ciclo de caixa; dívida líquida/EBITDA; EBIT/juros; dívida de CP/dívida total; % em moeda estrangeira.
2. Faça a análise vertical da DRE e a horizontal do BP.
3. Compare cada indicador com a mediana do setor.
4. Decomponha o ROIC em margem × giro para saber **de onde** vem o retorno e qual premissa da projeção é mais sensível.
5. Use a cobertura de juros para o **rating sintético** e o spread (tema 21).
6. Use os indicadores como premissas: margem-alvo, giro (receita/capital) → reinvestimento (tema 10), NCG/receita (tema 05).

## 5. Erros comuns apontados pelos autores

- **Comparar setores diferentes** ([P] p. 54).
- **Olhar o ROE sem a alavancagem** ([D] p. 61–63): ROE alto pode ser só dívida.
- **Achar que liquidez alta é sempre boa** ([D] p. 65).
- **Cobertura de juros sem capex** ([D] p. 67–68).
- **Ver dívida como mal em si** ([P] p. 59).

## 6. Onde concordam e onde divergem

**Concordam**: retorno = margem × giro; comparar com o custo de capital; comparar dentro do setor.

| Ponto | Damodaran | Póvoa |
|---|---|---|
| Base do retorno | Capital investido (dívida + PL), de preferência do início do período | Ativo e PL médios |
| ROE | Decomposto por ROC e alavancagem | Margem líquida × giro do PL |
| Endividamento | D/E a valor de mercado é o relevante | Indicadores contábeis; exemplo com dívida em dólar |
| Bancos | Não trata aqui | Índice de Basileia |
| Análise horizontal/vertical | Não trata | Trata (p. 64) |

## 7. Limites: o que está defasado ou é específico do Brasil

- Exemplos de 1998 ([D]) e 2002 ([P]). Os mínimos de Basileia citados em [P] foram alterados por Basileia III **[NÃO VERIFICADO aqui]**.
- No Brasil, o indicador de mercado mais usado é **dívida líquida/EBITDA** (covenants), que nenhum dos dois livros destaca aqui.
- Com o IFRS 16, EBITDA e dívida incluem arrendamentos: padronize "com" ou "sem" IFRS 16 em toda a série (tema 07).
- Variação cambial da dívida em dólar distorce cobertura e ROE (exemplo 2002 de [P]).

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. **Painel padrão de indicadores** (10 itens do passo 1), 5 anos, com a mediana do setor.
2. **ROIC = margem × giro** sempre apresentado no vídeo, com o WACC ao lado.
3. **Rating sintético** pela cobertura de juros (tema 21).
4. Declarar se os números são pré ou pós IFRS 16.

## 9. Dúvidas abertas para você decidir

1. Capital do início ou médio no ROIC? (sugestão: início, conforme [D]; ver tema 16)
2. Incluir dívida líquida/EBITDA no painel, apesar de não estar nos livros?
3. Painel separado para bancos (Basileia, ROE, eficiência)?
