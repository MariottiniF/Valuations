# Fichamento 13: Número de estágios de projeção e fases de crescimento

**Fontes**
- **[D]** Damodaran (2002), Cap. 12, "Length of the High Growth Period", "Competitive Advantage Period" e "The Transition to Stable Growth" (PDF p. 430–444). Cap. 15, exemplos de 2 e 3 estágios (Gap, Amgen, Embraer, p. 543–555).
- **[P]** Póvoa (2012), Cap. 4, "Quantos estágios devemos usar para projetar um fluxo de caixa descontado corretamente?" (p. 113–118) e casos complicados (p. 125–129).

---

## 1. Conceito central

Um **estágio** é um período em que a empresa tem características semelhantes de crescimento, retorno, risco e reinvestimento ([P] p. 113). Quanto mais jovem a empresa, mais estágios até a perpetuidade ([P] p. 113–114). Damodaran organiza a escolha em três padrões: **dois estágios** (alto crescimento e depois estável, de forma abrupta), **três estágios** (alto, transição gradual, estável) e **n estágios** (mudança ano a ano). A escolha depende de **quão alto é o crescimento atual** e de **quanto os fundamentos precisam mudar** ([D] p. 443).

## 2. Fórmulas

**Anuidade crescente** (estágio de crescimento) ([P] p. 115–116)
`VP = FC₀(1+g)/(r−g) × [1 − ((1+g)/(1+r))^n]`, válida também com g > r ([P] p. 118).

**Perpetuidade após n anos** ([P] p. 116)
`VP = [FC_n(1+g_p)/(r_p − g_p)] / (1+r)^n`

**Exemplos de [P]** (recalculados) ✔
- 1 estágio (peças de ventilador): FC = 3,5; g = 5%; r = 15% (p. 114–115).
- 2 estágios (fax): FC₀ = 6,3; g = 7,5% por 5 anos com r = 18%; g_p = 4% com r_p = 15% → 24,02 + 37,38 = **61,4** (p. 115–117).
- 3 estágios (informática): FC₀ = 40; 30% por 5 anos, 12% por 5 anos, 4% depois; r = 17% e r_p = 13% → 277,40 + 297,68 + 629,22 = **1.204,30** (p. 117–118).

**Transição linear** ([D] p. 550, 554): no estágio 2, g, RR, beta, D/(D+E) e Kd vão em incrementos lineares dos valores do alto crescimento até os estáveis.

## 3. Premissas e escolhas dos autores

- **Horizonte do período explícito ([P] p. 113–114)**: um bom analista projeta com competência ~**5 anos**, com cenários. A partir do 6º ano a subjetividade cresce "exponencialmente". Nos exemplos do livro, Póvoa usa **7 a 8 anos** antes da perpetuidade. Empresas nascentes pedem mais anos, o que gera um "ciclo vicioso": menos certezas para prazos maiores.
- **Quando usar cada modelo**
  - **1 estágio**: empresa já madura (estrutura de capital, produtividade e crescimento) ([P] p. 114).
  - **2 estágios**: crescimento moderado, para que o salto não seja dramático. Ainda há ajustes de estrutura e de dividendos ([D] p. 443; [P] p. 114).
  - **3 estágios**: crescimento alto. A transição ajusta o crescimento **e também** risco, ROC e reinvestimento ([D] p. 443; [P] p. 114).
  - **n estágios ou 4+**: empresas muito jovens ou com margem negativa ([D] p. 443). "A criatividade é livre", mas o ganho marginal de mais variáveis é decrescente ([P] p. 114).
- **Duração do alto crescimento** ([D] p. 430–433): tamanho e mercado potencial; momento (crescimento e excesso de retorno atuais); **vantagens competitivas** (o fator mais crítico) e qualidade da gestão. É uma escolha subjetiva (P&G 5 anos, Amgen e Coca 10 anos).
- **Crescimento baixo ainda pode exigir transição** ([D] p. 444): uma empresa crescendo 4% com ROC de 20% e beta de 1,5 precisa de transição para ROC e beta sustentáveis. Também pode haver crescimento "extraordinário" **abaixo** do estável no início, por exemplo 2% por 5 anos e depois 5%.
- **Sunk cost** ([P] p. 118–119): fluxos negativos passados não entram. Só importam os efeitos futuros (por exemplo, juros da dívida contraída).

## 4. Passo a passo prático

1. Diagnostique a empresa: crescimento atual × economia; ROC × WACC; beta × 1; estrutura de capital × alvo.
2. Se tudo já estiver próximo do estável: **1 estágio**.
3. Se o crescimento for moderado e os fundamentos estiverem perto do estável: **2 estágios** (explícito de 5 a 10 anos + perpetuidade).
4. Se o crescimento for alto ou os fundamentos estiverem longe do estável: **3 estágios** (alto, transição linear de 5 anos, estável).
5. Para empresa jovem ou com margem negativa: **n estágios**, com receita, margem e vendas/capital ano a ano (tema 14).
6. Em todos os casos, a transição move juntos g, RR (g/ROC), beta, D/(D+E) e Kd.

## 5. Erros comuns apontados pelos autores

- **Saltar de crescimento muito alto direto para a perpetuidade** sem transição de risco e retorno ([D] p. 443).
- **Achar que crescimento baixo dispensa transição** quando ROC e beta ainda não estão em equilíbrio ([D] p. 444).
- **Excesso de estágios e variáveis** sem ganho de informação ([P] p. 97, 114).
- **Incluir fluxos passados (sunk cost)** ([P] p. 118).

## 6. Onde concordam e onde divergem

**Concordam**: o número de estágios depende do estágio de vida da empresa; a transição é gradual para quem cresce rápido; há limite de previsibilidade.

| Ponto | Damodaran | Póvoa |
|---|---|---|
| Critério principal | Nível do crescimento e distância dos fundamentos ao estável (p. 443–444) | Maturidade da empresa; previsibilidade de ~5 anos (p. 113–114) |
| Duração do alto crescimento | Vantagem competitiva, tamanho, momento (p. 430–433) | Não detalha critérios; usa 7 a 8 anos nos exemplos |
| Transição | Linear em todos os parâmetros (p. 550, 554) | Taxas de crescimento decrescentes por estágio (p. 114) |

## 7. Limites: o que está defasado ou é específico do Brasil

- Os exemplos são ilustrativos. A regra dos "5 anos de previsibilidade" de [P] é opinião do autor, sem evidência apresentada.
- As taxas dos exemplos de [P] (r = 13–20%) refletem o juro brasileiro de 2012.

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. **Padrão: 3 estágios.** Anos 1 a 5 explícitos detalhados, anos 6 a 10 de transição linear e perpetuidade. Usar **2 estágios** (5 anos + perpetuidade) para empresas maduras como utilities reguladas e bancos grandes.
2. Na transição, interpolar **todos** os parâmetros (g, ROC, RR, beta, D/(D+E), Kd), não só o g.
3. Justificar no vídeo a **duração do alto crescimento** com base em vantagem competitiva, tamanho de mercado e momento.

## 9. Dúvidas abertas para você decidir

1. Padrão de 3 estágios (5 + 5 + perpetuidade) ou 2 estágios (10 + perpetuidade)?
2. Um único horizonte para todas as empresas ou um por setor?
