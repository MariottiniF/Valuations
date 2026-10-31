# Fichamento 20 — Beta

**Fontes**
- **[D]** Damodaran, *Investment Valuation*, 2ª ed. (2002), Cap. 8 "Estimating Risk Parameters and Costs of Financing". Páginas = **páginas do PDF** (o capítulo começa na p. 246).
- **[P]** Póvoa, *Valuation: Como Precificar Ações* (2012), Cap. 6 "Taxa de desconto, um toque de arte na valuation". Páginas = **páginas impressas** (no PDF do leitor, página impressa = página do PDF − 22).

Trechos lidos: [D] p. 246–279; [P] p. 193–206 e 229–231.

---

## 1. Conceito central

O beta mede quanto do risco de uma ação **não pode ser eliminado com diversificação**, ou seja, a sensibilidade do retorno da ação ao retorno da carteira de mercado. No CAPM, é o único parâmetro próprio da empresa no custo do capital próprio ([D] p. 247; [P] p. 195–196). Os dois autores chegam à mesma conclusão: o beta de regressão de uma única empresa é ruidoso e enviesado demais para ser usado direto, e o melhor estimador é o **bottom-up beta**. Ele parte do beta desalavancado médio do setor e o realavanca com a estrutura de capital da própria empresa ([D] p. 261, 279; [P] p. 197–203).

## 2. Fórmulas

**CAPM (custo do capital próprio)**
`Ke = Rf + β × (Rm − Rf)`, em que Rf = taxa livre de risco, β = beta da ação e (Rm − Rf) = prêmio de risco de mercado ([D] p. 247; [P] p. 206).

**Beta de regressão**
`Rj = a + b × Rm`, com `b = Cov(Rj, Rm) / Var(Rm)`. Rj = retorno da ação no período (preço mais dividendos); Rm = retorno do índice; a = intercepto; b = beta ([D] p. 248; [P] p. 193–194).

**Alfa de Jensen (desempenho passado, não previsão)**
Compare o intercepto `a` com `Rf × (1 − β)`. Se `a > Rf(1−β)`, a ação superou o CAPM no período; se for menor, ficou abaixo ([D] p. 248–249; [P] p. 229–230). O teste contra zero só vale se a regressão usar **retornos em excesso** sobre Rf ([D] p. 248, notas 2 e 3).

**Intervalo de confiança do beta**
`β ± 1 erro-padrão` cobre ~67% dos casos, e `β ± 2 erros-padrão` cobre ~95% ([D] p. 252). Póvoa usa 1,96 desvios para 95% ([P] p. 198).

**Beta ajustado (Bloomberg)**
`β ajustado = 0,67 × β bruto + 0,33 × 1,00`. Esse ajuste puxa todo beta em direção a 1 ([D] p. 252–253).

**Grau de alavancagem operacional**
`GAO = %Δ lucro operacional / %Δ receita` ([D] p. 264; ideia equivalente em [P] p. 199).

**Hamada: alavancar e desalavancar** (supõe beta da dívida = 0)
`βL = βu × [1 + (1 − t) × D/E]`
βL = beta alavancado (do acionista); βu = beta desalavancado (dos ativos); t = alíquota de IR; D/E = dívida sobre patrimônio **a valor de mercado** ([D] p. 265; [P] p. 200–201, onde βu aparece como "βd").
Variantes em [D] p. 265, nota 8: sem impostos, `βL = βu × (1 + D/E)`; com beta da dívida βD, `βL = βu × [1 + (1−t)D/E] − βD × (1−t)D/E`.

**Beta de empresa com vários negócios**
`βu firma = Σ βu negócio j × peso de valor j`. O peso vem do valor de cada negócio; na falta dele, use lucro operacional ou receita ([D] p. 268).

**Erro-padrão do bottom-up beta**
`EP bottom-up ≈ EP médio dos comparáveis / √n`, supondo erros não correlacionados entre as empresas ([D] p. 268). Póvoa cita a mesma regra ([P] p. 198), mas a fórmula dele está numa imagem que não saiu na extração de texto **[NÃO VERIFICADO no PDF de P]**.

**Beta do negócio, sem a alavancagem operacional**
`β negócio = βu / (1 + Custos fixos / Custos variáveis)`. Aqui não entra imposto, porque os custos fixos e os variáveis são ambos dedutíveis ([D] p. 271).

## 3. Premissas e escolhas dos autores

- **Os três determinantes do beta** são o tipo de negócio (ciclicidade e quanto o produto é discricionário), a alavancagem operacional e a alavancagem financeira ([D] p. 263–265). Póvoa usa ciclicidade, alavancagem operacional e "diferenciação/especialização" para agrupar empresas, e trata a alavancagem financeira como o quarto fator, o que distingue empresas do mesmo grupo ([P] p. 199–200).
- **Por que bottom-up.** Uma média de muitos betas tem erro-padrão bem menor. O método também acompanha mudanças de mix de negócios e de dívida, inclusive antes que aconteçam, e dispensa histórico de preço da empresa ([D] p. 268–269, 279; [P] p. 198–199).
- **Ordem do cálculo ([D]).** Primeiro tire a média dos betas e dos D/E dos comparáveis, depois desalavanque. Desalavancar cada beta errado antes "compõe o erro" ([D] p. 268). Póvoa diz que as duas ordens chegam ao mesmo resultado, mas só porque ele pondera por valor de mercado ([P] p. 203).
- **Média dos comparáveis.** [D] prefere a **média simples**: a ponderada por valor anula o ganho de erro-padrão quando há uma ou duas gigantes na amostra ([D] p. 270–271). [P] usa a **média ponderada por valor de mercado** "garantindo representatividade às maiores companhias" ([P] p. 201).
- **Excluir a própria empresa da amostra.** Em teoria, sim. Com 15 a 20 comparáveis ou mais, faz pouca diferença ([D] p. 271).
- **Alíquota.** No exemplo da Vans, [D] desalavanca com a alíquota **efetiva média** dos comparáveis e realavanca com a **marginal** da empresa ([D] p. 271–272). [P] usa uma alíquota única hipotética de 30% ([P] p. 202).
- **Os betas "viajam" entre países.** Usar o mesmo beta setorial para empresas de países diferentes é aceitável, porque o risco-país entra no prêmio e não no beta. A exceção é um produto discricionário num mercado e essencial em outro (telefonia em emergentes), caso em que só valem comparáveis emergentes ([D] p. 275–276).
- **Beta contábil** (regredir lucros contra lucros): [D] praticamente nunca usa. Lucro é suavizado, depende de critério contábil e tem poucas observações ([D] p. 278–279). [P] não trata do tema nesses trechos.

## 4. Passo a passo prático (síntese das duas fontes)

1. **Defina os negócios** da empresa. Se forem vários, separe por segmento e estime o valor de cada um ([D] p. 268, 273–274).
2. **Monte a amostra de comparáveis** por negócio. Equilibre a semelhança com o tamanho da amostra: com poucas empresas, amplie o setor ou a geografia ([D] p. 270, 275; [P] p. 205).
3. **Obtenha os betas de regressão dos comparáveis.** Um beta de serviço é aceitável; erros de índices diferentes tendem a se compensar numa amostra grande ([D] p. 270). Se for rodar a regressão:
   - janela: [D] cita 5 anos como padrão (Bloomberg usa 2) ([D] p. 254); [P] recomenda **3 anos, com até 6 em setores maduros** ([P] p. 197);
   - intervalo: **mensal** nos dois. Retornos diários e semanais têm viés de não negociação, pior em ações ilíquidas ([D] p. 254–255; [P] p. 197–198);
   - índice: o do investidor marginal ([D] p. 254–255); no Brasil, Ibovespa ou IBX, sabendo que são concentrados ([P] p. 193, 198).
4. **Calcule o D/E médio dos comparáveis a valor de mercado** e a alíquota.
5. **Desalavanque** a média: `βu = β médio / [1 + (1−t) D/E médio]`.
6. *(Opcional)* **Ajuste pela alavancagem operacional** se ela variar muito no setor ([D] p. 271–272).
7. **Pondere os βu** pelos pesos de valor dos negócios da empresa ([D] p. 268).
8. **Realavanque** com o D/E **atual, ou o D/E-alvo** da empresa, a valor de mercado. Se a estrutura de capital for mudar ao longo da projeção, calcule um beta por ano ([D] p. 269; [P] p. 202).
9. **Faça a checagem de sanidade** contra o beta de regressão da própria empresa e o erro-padrão dele. Uma diferença grande pede explicação (exemplos da Distribuidora do Norte e da do Centro-Oeste, [P] p. 202–203).

**Exemplos numéricos conferidos** (refiz as contas):
- Póvoa, distribuidoras ([P] p. 201–203): β setorial ponderado = 7.850/8.100 = 0,97; D/E do setor = 18.175/8.100 = 2,24; βu = 0,97 / (1 + 2,24 × 0,7) = 0,38; realavancado para a Norte (D/E 3,0) = 0,38 × 3,1 = **1,18 ≈ 1,2**, contra 0,7 pela regressão. ✔
- Damodaran, Boeing bottom-up ([D] p. 273–275): βu ponderado = 0,8774; βL = 0,8774 × (1 + 0,65 × 7,85/55,2) = **0,9585**, contra 0,56 pela regressão. ✔ *A fórmula impressa parece dividir por (55,2 + 7,85), mas o resultado só fecha com D/E = 7,85/55,2. Pode ser problema de diagramação do PDF.*

## 5. Erros comuns apontados pelos autores

- **Usar o beta de regressão sem olhar o erro-padrão.** O beta da Boeing (0,56, EP 0,23) vai de 0,10 a 1,02 com 95% de confiança ([D] p. 252). O exemplo de Póvoa vai de 0,22 a 2,18 ([P] p. 198).
- **Confiar num erro-padrão baixo quando o índice é dominado por uma ação.** É o caso da Nokia no HEX (75% do índice): a regressão é da ação contra ela mesma ([D] p. 256–257). Damodaran cita o Bovespa dominado pela Telebras ([D] p. 255–256); Póvoa trata da concentração do Ibovespa e do IBX ([P] p. 198).
- **Usar retornos diários ou semanais em ações ilíquidas.** O viés é para baixo ([D] p. 254–255; [P] p. 197–198). Exemplo: a Boeing tem beta 0,88 com dados semanais e 0,96 com mensais no mesmo período de 2 anos ([D] p. 254).
- **Usar uma janela longa depois de uma reestruturação** (fusões, mudança de dívida), porque a regressão mistura duas empresas diferentes ([D] p. 254, 260–261, 276; [P] p. 196).
- **Mudar o beta a cada oscilação de mercado.** Isso "sanciona" o mercado. Só mude quando a mudança for estrutural ([P] p. 205–206).
- **Restringir demais o grupo de comparáveis** até sobrarem uma ou duas empresas, o que elimina a vantagem estatística ([D] p. 270; [P] p. 205).
- **Desalavancar cada beta individual antes de tirar a média** ([D] p. 268).
- **Ler o alfa como previsão.** O alfa mede o passado e não diz que a ação é um bom investimento ([D] p. 252).
- **Comparar o intercepto com zero numa regressão de retornos brutos.** O teste correto é contra Rf(1−β) ([D] p. 248, nota 3).

## 6. Onde concordam e onde divergem

**Concordam**
- O beta de regressão individual é pouco confiável, e o bottom-up beta é o preferido ([D] p. 279; [P] p. 197–203).
- Os determinantes do beta são ciclicidade, alavancagem operacional e alavancagem financeira, com a fórmula de Hamada ([D] p. 263–265; [P] p. 199–201).
- Dados mensais e D/E a valor de mercado ([D] p. 254, 268; [P] p. 197, 201).
- O alfa se compara com Rf(1−β) ([D] p. 248–249; [P] p. 229–230).

**Divergem**
| Ponto | Damodaran | Póvoa |
|---|---|---|
| Média dos comparáveis | Simples, que minimiza o erro-padrão (p. 270–271) | Ponderada por valor de mercado (p. 201) |
| Janela da regressão | 5 anos é o usual (p. 254) | 3 anos, até 6 em setores maduros (p. 197) |
| Mudança estrutural | Use o bottom-up com o novo mix e o novo D/E (p. 276–277) | Encurte a regressão, por exemplo 1 ano com dados **diários** (p. 206) |
| Índice de referência | O do investidor marginal: global ou regional, se ele for diversificado (p. 254–255, 257–259) | Ibovespa ou IBX, sabendo que são concentrados (p. 193, 198) |
| Beta ajustado em direção a 1 | Descreve o ajuste da Bloomberg (p. 252–253) | Não trata nos trechos lidos |
| Alavancagem operacional | Ajuste quantitativo com o "beta do negócio" (p. 271–272) | Só qualitativo, para agrupar setores (p. 199) |
| Alíquota | Efetiva para desalavancar, marginal para realavancar (p. 271–272) | Alíquota única (p. 202) |

*Atenção:* a sugestão de Póvoa para mudança estrutural (dados diários, janela curta) contraria o alerta dele mesmo e o de Damodaran sobre viés de iliquidez. O bottom-up de Damodaran resolve o mesmo problema sem cair nesse viés.

## 7. Limites: o que está defasado ou é específico do Brasil

- **Números de [D] (2002):** todos os betas, D/E e exemplos (Boeing 1996–2000, Vans, Titan) são ilustrativos e vencidos. A Telebras, citada como dominante no Bovespa ([D] p. 255–256), já não existe nessa forma. Vale a lógica, não os valores.
- **Tabela setorial de [P] (início de 2012, Economática)** ([P] p. 204): βu de energia elétrica 0,32, telecom 0,34, comércio 0,45 etc. Está **defasada** e serve só de ordem de grandeza. Precisa ser recalculada com dados atuais.
- **Composição do Ibovespa/IBX:** a concentração setorial mudou desde 2012. O problema de índice concentrado continua valendo, mas qual setor domina precisa ser verificado na carteira atual **[NÃO VERIFICADO aqui]**.
- **Alíquota no Brasil:** os livros não fixam valor (Póvoa usa 30% hipotético). A alíquota marginal usual é 34% (IRPJ 25% + CSLL 9%), mas isso é informação de fora dos dois livros; confirme no `MACRO.md` ou na legislação vigente.
- **Dívida a valor de mercado no Brasil:** Póvoa observa que o mercado secundário de dívida privada é ilíquido e por isso se usa o **valor contábil** como proxy ([P] p. 231, no contexto do WACC). Isso afeta o D/E da fórmula de Hamada.
- **Moeda:** na prática se usa o mesmo beta para Ke em reais ou em dólares, e o que muda é Rf e o prêmio (inferência minha, não afirmação explícita dos trechos lidos). A discussão sobre "para quem" o fluxo é construído está em [P] p. 229 (o argumento começa antes, em trecho que não li) e pertence aos temas 18 e 19.

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`, sem alterar o arquivo)

1. **Padrão:** bottom-up beta. O beta de regressão da própria empresa serve só como checagem de sanidade, sempre reportado com o erro-padrão.
2. **Fixar a regressão dos comparáveis:** retornos mensais, com dividendos, sobre 3 a 5 anos. O índice precisa ser decidido (ver dúvidas abertas).
3. **Amostra de comparáveis:** primeiro listadas brasileiras do setor; se houver menos de ~10 empresas, ampliar para emergentes ou globais, usando o argumento de que "os betas viajam" ([D] p. 275–276). Registrar a regra de exceção para produtos discricionários.
4. **Desalavancar a média, não cada empresa** ([D] p. 268). Documentar se a média é simples ou ponderada (é uma escolha que muda o resultado).
5. **Realavancar com o D/E-alvo de longo prazo** na perpetuidade e com o D/E projetado ano a ano no período explícito, em ligação com o tema 25 ("escadinha" no WACC).
6. **Publicar em cada vídeo ou planilha** o βu do setor, o D/E usado, a alíquota e a amostra, para que o cálculo possa ser auditado.

## 9. Dúvidas abertas para você decidir

1. **Média simples ou ponderada** dos comparáveis? (Damodaran × Póvoa)
2. **Índice de regressão:** Ibovespa, IBX-100 ou um índice global (MSCI ACWI)? Depende de quem você supõe ser o investidor marginal.
3. **Janela:** 3 anos (Póvoa) ou 5 anos (Damodaran)?
4. **Aplicar o ajuste de Blume/Bloomberg** (0,67/0,33) ao beta final, ou não?
5. **Ajustar pela alavancagem operacional** (beta do negócio) só quando a estrutura de custos da empresa for muito diferente da do setor?
6. **Dívida no D/E:** valor contábil (prática brasileira, segundo Póvoa) ou valor de mercado quando houver debêntures negociadas?
7. **Alíquota para desalavancar:** efetiva média dos comparáveis ou marginal de 34%?

---
*Observações sobre as fontes:* em [D], há duas "Illustration 8.3" no capítulo (p. 266 e p. 271), um erro de numeração da edição. No exemplo da Vans, as contas dão βu ≈ 0,5078 e o livro mostra 0,5081, uma diferença de arredondamento. O próprio PDF traz uma nota de revisão esquecida sobre a média de custos fixos/variáveis (p. 271).
