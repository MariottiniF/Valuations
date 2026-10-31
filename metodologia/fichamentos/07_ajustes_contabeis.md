# Fichamento 07: Ajustes ao lucro e ao balanço: itens não recorrentes, leasing, P&D, provisões, normalização de resultado

**Fontes**
- **[D]** Damodaran (2002), Cap. 9 "Measuring Earnings": balanço financeiro (PDF p. 311); atualização do lucro, LTM (p. 312–313, Ariba); classificação das despesas (p. 313–314); capitalização de P&D (p. 315–319, Amgen); capitalização de outras despesas operacionais, SG&A (p. 319–322); arrendamentos operacionais como dívida (p. 323–325, Gap); outros compromissos fixos (p. 325); lucros gerenciados (p. 326–330); itens extraordinários, recorrentes e incomuns (p. 330–336, Xerox); sinais de alerta (p. 336–338); resumo (p. 338).
- **[P]** Póvoa (2012), Cap. 3: P&D (p. 72–74, Pfizer, IBM/Lotus); marketing (AOL, p. 74–75); leasing operacional × financeiro (p. 79); impairment (p. 79–81); deemed cost (p. 82–83); instrumentos financeiros e variação cambial (p. 83–86); ajuste de avaliação patrimonial (p. 86–87); stock options e lucro diluído (p. 88–89); ágio (p. 89); depreciação (p. 89–90); equivalência patrimonial (p. 90–91); consequências na comparação pós-IFRS (p. 93–94). Cap. 2, PDD (p. 20).

---

## 1. Conceito central

O lucro contábil não é a base adequada para projetar. Antes de projetar, o analista deve deixá-lo **atualizado, corretamente classificado e normalizado** ([D] p. 311–312). Damodaran aponta dois erros de classificação comuns: **despesas de capital tratadas como operacionais** (P&D e, em parte, marketing e treinamento), que subestimam o capital e distorcem o lucro; e **despesas financeiras tratadas como operacionais** (arrendamentos operacionais), que escondem dívida ([D] p. 313–314). Além disso, o lucro de base deve refletir só as **operações continuadas**, sem itens realmente únicos, mas incluindo os "não recorrentes" que se repetem ([D] p. 330–331). Póvoa mostra que, no Brasil, o IFRS trouxe novas fontes de ruído (impairment, ajuste de avaliação patrimonial, variação cambial fora do resultado, fim da amortização do ágio, depreciação livre) que o analista precisa padronizar para comparar séries e empresas ([P] p. 93–94).

## 2. Fórmulas

**Capitalização de P&D** ([D] p. 315–316)
- `Ativo de pesquisa = Σ R&D_t × (vida − idade)/vida` (amortização linear). Com vida de 5 anos: 1/5 do gasto de 4 anos atrás, 2/5 do de 3 anos, … e 100% do ano corrente.
- `EBIT ajustado = EBIT + R&D do ano − amortização do ativo de pesquisa`
- `LL ajustado = LL + R&D do ano − amortização` (sem ajuste de IR, porque o P&D é integralmente dedutível; ver nota 1 da p. 316).
- `PL (e capital) ajustado = PL (capital) + ativo de pesquisa`.
- **Amgen, 2000** ✔: EBIT 1.549 + 845 − 398 = **1.996**; LL 1.139 + 845 − 398 = **1.586**; PL de 1999 3.024 + 2.909 = **5.933**; capital 3.347 + 2.909 = **6.256** ([D] p. 317–318). Os retornos caem bastante após o ajuste, efeito típico de empresas com P&D alto e retornos altos ([D] p. 319).

**Outras despesas de capital (SG&A, marketing, treinamento)** ([D] p. 320–321): mesmo procedimento, **só com evidência forte** de que o benefício dura vários períodos (cliente da Amazon que permanece; CDs da AOL).

**Arrendamento operacional como dívida** ([D] p. 323–324)
- `Dívida ajustada = dívida + VP(compromissos de arrendamento)`, descontados ao custo da dívida **antes** do IR.
- `EBIT ajustado = EBIT + despesa de arrendamento − depreciação do ativo arrendado`; **ou**, aproximado: `EBIT + VP(arrendamentos) × kd antes do IR`.
- **Gap, 2001** ✔: dívida 1.560 + 5.714 = **7.274**; depreciação 5.714/13 ≈ 440; EBIT 1.365 + 706 − 440 = **1.631**; aproximação: 1.365 + 5.714 × 7% = **1.765**.
- Compromissos fixos não canceláveis e não ligados a desempenho (por exemplo, contrato de atleta) também são dívida ([D] p. 325).

**Itens extraordinários** ([D] p. 330–331), quatro tipos:
1. Realmente únicos → excluir.
2. Não anuais mas periódicos (reestruturação a cada 3 anos) → **anualizar** (1,5 bi a cada 3 anos = 0,5 bi/ano de despesa) ✔.
3. Anuais e voláteis → **média**.
4. Anuais com sinal alternado (variação cambial) → ignorar.

**Diluição por stock options** ([P] p. 88) ✔: 5 mi de lucro sobre 1 mi de ações = R$ 5/ação; com 100 mil novas ações a R$ 25, cai para 5/1,1 = **R$ 4,55**.

**PDD** ([P] Cap. 2, p. 20): provisão por inadimplência histórica e reversão quando a perda efetiva é menor (tema 04).

## 3. Premissas e escolhas dos autores

- **Atualize o lucro** ([D] p. 312): use os últimos 12 meses (LTM) somando 4 trimestres, sobretudo em empresas que mudam rápido. Itens que só saem no relatório anual (opções) ficam com o último anual ou são estimados.
- **Vida amortizável do P&D** ([D] p. 315): longa em farmacêuticas (aprovação demorada), curta em software.
- **Capitalizar SG&A com ceticismo** ([D] p. 320). Póvoa mostra o lado oposto do mesmo dilema: se AOL/Time Warner pudessem "inchar" o balanço com intangíveis em 2000, a bolha teria sido maior. Neste caso, a contabilidade conservadora tinha razão ([P] p. 75).
- **IBM/Lotus** ([P] p. 74): a IBM lançou como despesa 50% dos US$ 3,5 bi pagos, ou seja, reconheceu que metade do preço era P&D em andamento.
- **Leasing no IFRS (versão de 2012)** ([P] p. 79): leasing financeiro (com opção de compra) vai ao balanço do arrendatário; o operacional continua como aluguel na DRE. *Isso foi superado pelo IFRS 16 / CPC 06 (R2), em vigor desde 2019, que leva quase todos os arrendamentos ao balanço* **[NÃO VERIFICADO nos livros]**. Ou seja, o ajuste da Gap em [D] hoje já vem pronto no balanço, mas é preciso decidir como tratá-lo (ver seção 8).
- **Impairment** ([P] p. 79–81): teste ao menos anual nos ativos operacionais; a perda vai ao resultado e pode ser revertida (exceto ágio **[NÃO VERIFICADO em P]**). Não é a "velha reavaliação", que foi mal usada para inflar PL e melhorar indicadores de endividamento.
- **Deemed cost e ajuste de avaliação patrimonial** ([P] p. 82–87): ajustes de valor em ativos fora da operação vão ao PL, não ao resultado. Isso deixa o lucro menos volátil, mas o analista precisa acompanhar o AAP.
- **Variação cambial da dívida** ([P] p. 83–86): conforme a classificação (negociação, disponível, mantida até o vencimento), a mesma perda cambial vai ao resultado, ao PL ou só aparece no vencimento. *Note o exemplo de [P]: "no final de 2026, o mundo entra em crise e o dólar dispara para R$ 4" é uma hipótese didática do autor, não um dado.* O analista deve acompanhar o principal em moeda estrangeira independentemente da contabilização.
- **Ágio** ([P] p. 89): goodwill (valor interno) × mais-valia (valor externo). O IFRS acaba com a amortização societária (só impairment), mas a amortização fiscal continua, o que explica incorporações para aproveitar o benefício fiscal.
- **Depreciação** ([P] p. 89–90): o IFRS permite o ritmo "real" e um valor residual; a contabilidade fiscal segue a tabela antiga. Isso cria **diferenças entre empresas** para o mesmo ativo.
- **Equivalência patrimonial** ([P] p. 90–91): agora pelo critério subjetivo de "influência significativa" (presumida a partir de 20%).
- **Lucros gerenciados** ([D] p. 326–329): empresas que batem a estimativa por centavos todo trimestre (Microsoft: 39 de 40 trimestres na década de 1990). O mercado reage com estimativas "sussurradas" (Intel, 1997: LPA de 2,10 acima da estimativa de 2,06, mas a ação caiu porque o "sussurro" era 2,15).

## 4. Passo a passo prático (normalização)

1. **LTM**: monte o resultado dos últimos 4 trimestres.
2. **Reclassifique** P&D (se relevante) e decida o tratamento de arrendamentos (seção 8).
3. **Liste os não recorrentes** dos últimos 5–10 anos e classifique em um dos 4 tipos de [D]. Anualize os periódicos.
4. **Retire do EBIT** o que é financeiro ou não operacional: variação cambial, resultado de equivalência (vai para participações no EV→equity, tema 30), ganhos de venda de ativos.
5. **Ajuste o impairment**: exclua do lucro de base, mas pergunte se ele sinaliza retornos menores (revise o ROIC projetado).
6. **Use o LPA diluído** e conte as opções em aberto (tema 30).
7. **Aplique o checklist de sinais de alerta** ([D] p. 336–337):
   - lucro crescendo muito mais que a receita, ano após ano;
   - encargos "não recorrentes" frequentes, cada ano com nome diferente;
   - despesas operacionais (% da receita) oscilando muito;
   - bater a estimativa por um centavo todo trimestre;
   - receita relevante de subsidiárias ou partes relacionadas;
   - mudanças frequentes de critério de estoque ou depreciação;
   - lucros "milagrosos" após aquisições;
   - capital de giro inchando junto com a receita (venda financiada ao próprio cliente).
   Nenhum isolado justifica cortar o lucro; vários juntos pedem mais escrutínio.

## 5. Erros comuns apontados pelos autores

- **Usar o último relatório anual** quando há dados trimestrais mais novos ([D] p. 312).
- **Ignorar não recorrentes que se repetem** ([D] p. 330).
- **Capitalizar marketing sem evidência** ([D] p. 320; [P] p. 75).
- **Ignorar arrendamentos e compromissos fixos** como dívida ([D] p. 323–325).
- **Confiar na variação cambial "fora do resultado"** ([P] p. 85–86).
- **Comparar empresas com critérios de depreciação ou equivalência diferentes** sem padronizar ([P] p. 90, 93–94).
- **Usar o LPA básico** quando há diluição relevante ([P] p. 88–89).

## 6. Onde concordam e onde divergem

**Concordam**: o P&D é investimento mal tratado pela contabilidade; o lucro de base deve ser normalizado; há margem de manobra contábil que o analista precisa desfazer.

| Ponto | Damodaran | Póvoa |
|---|---|---|
| P&D | Capitaliza com fórmula explícita (p. 315–319) | Aponta a distorção (Pfizer), sem método de capitalização |
| Marketing | Capitalizável com evidência e ceticismo | O conservadorismo protegeu do caso AOL |
| Leasing | VP dos compromissos como dívida (p. 323) | Descreve a regra do IFRS de 2012 (p. 79) |
| Não recorrentes | Taxonomia de 4 tipos (p. 330–331) | Foco no fim dos "resultados não operacionais" com o IFRS (p. 92–93) |
| Ênfase | US GAAP, manipulação de lucro | Transição brasileira ao IFRS |

## 7. Limites: o que está defasado ou é específico do Brasil

- **IFRS 16 (2019)**: arrendamentos já no balanço; o ajuste de [D] p. 323 muda de "fazer" para "decidir se mantém ou desfaz" **[NÃO VERIFICADO nos livros]**.
- **IFRS 9**: perda esperada substitui a PDD por perda histórica **[NÃO VERIFICADO nos livros]**.
- [P] Cap. 3 descreve o IFRS por volta de 2012: classificações de instrumentos financeiros mudaram com o IFRS 9.
- **Brasil**: JCP (tema 22), subvenções de ICMS (tratamento fiscal alterado em 2023–2024 **[NÃO VERIFICADO aqui]**), créditos extemporâneos de PIS/COFINS ("tese do século") geram lucros não recorrentes grandes e frequentes nos anos 2020; tratá-los como não recorrentes do tipo 1.
- **Hiperinflação** (Argentina, IAS 29) afeta as consolidadas com operações lá.

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. **Base**: EBIT LTM ajustado, com tabela de reconciliação "EBIT reportado → ajustado" no material de apoio.
2. **Arrendamentos (IFRS 16)**: escolha um padrão e use em tudo: (a) **com IFRS 16**: passivo de arrendamento na dívida, EBIT com depreciação do direito de uso e WACC com esse passivo; ou (b) **sem IFRS 16**: aluguel como despesa operacional e passivo fora da dívida. Sugestão: (a), alinhado com [D], mas com a coerência entre fluxo, EBITDA, dívida e múltiplos.
3. **P&D**: capitalizar só quando > 3% da receita (limite sugerido, não está nos livros), com vida declarada por setor.
4. **Não recorrentes**: aplicar a taxonomia de 4 tipos de [D]; créditos fiscais extemporâneos e ganhos de venda de ativos sempre excluídos.
5. **Checklist de sinais de alerta** de [D] p. 336–337 em toda empresa.
6. **LPA diluído** sempre.

## 9. Dúvidas abertas para você decidir

1. IFRS 16: incluir o passivo de arrendamento na dívida (padrão "a") ou não?
2. Limite de P&D/receita para capitalizar.
3. Impairment: só excluir, ou também rever o ROIC projetado?
4. Usar LTM ou o último exercício anual como base?
