# Lista de fichamentos — Damodaran + Póvoa

**Livros**
- **[D]** Aswath Damodaran, *Investment Valuation*, 2ª ed., Wiley, 2002 (35 capítulos). Páginas citadas = **páginas do PDF** (a numeração do sumário do PDF).
- **[P]** Alexandre Póvoa, *Valuation: Como Precificar Ações*, Elsevier, 2012 (11 capítulos). Páginas citadas = **páginas impressas do livro** (o índice do PDF do leitor pode estar deslocado por causa das páginas iniciais).

**Legenda de prioridade**
- ★ Essencial: alimenta direto a `METODOLOGIA.md` (DCF de empresas listadas)
- ◐ Complementar: útil, mas não decide o método
- ○ Fora do escopo atual do canal (guardar para depois)

**Aviso de edição:** o Damodaran que você tem é a **2ª edição (2002)**. Tudo sobre prêmio de risco, taxa livre de risco, mercados emergentes e crise financeira está defasado. Use o [D] para a lógica e a teoria, e o [P] (2012, Brasil) para a aplicação local. Para números atuais, o `MACRO.md` manda.

---

## PARTE A — Fichamentos por TEMA (recomendado)

Um fichamento por tema, cruzando os dois livros. É o formato que vira `notas/TEMA.md` no repositório. Sugestão de nome de arquivo entre parênteses.

### Bloco 1 — Fundamentos e escolha do método
| # | Tema | [D] | [P] | Prior. |
|---|---|---|---|---|
| 01 | Filosofia do valuation: viés, subjetividade, mitos, preço × valor (`filosofia_vieses.md`) | Cap. 1 (p. 3–14) | Cap. 1 (p. 1–14), inclui "jargões famosos" | ★ |
| 02 | Abordagens: DCF, valuation relativa, opções (contingent claims); quando usar cada uma (`abordagens.md`) | Cap. 2 (p. 16–36) | Cap. 1 (escolas) e Cap. 4 (p. 95–99) | ★ |
| 03 | Eficiência de mercado e o que implica para quem faz valuation (`eficiencia_mercado.md`) | Cap. 6 (p. 152–210) | Cap. 1 | ◐ |

### Bloco 2 — Demonstrações contábeis e qualidade dos dados (etapas de coleta e entendimento)
| # | Tema | [D] | [P] | Prior. |
|---|---|---|---|---|
| 04 | Leitura de balanço, DRE e DFC; regras contábeis relevantes ao valuation (`contabilidade_base.md`) | Cap. 3 (p. 37–80) | Cap. 2 (p. 15–39) | ★ |
| 05 | Capital de giro e variação da necessidade de capital de giro (NCG): fórmula correta, erros comuns (`capital_de_giro.md`) | Cap. 10 | Cap. 2 (p. 26–36) | ★ |
| 06 | Indicadores: liquidez, giro, margens, retorno, endividamento, alavancagem; análise horizontal e vertical (`indicadores.md`) | Cap. 3 | Cap. 2 (p. 40–64) | ★ |
| 07 | Ajustes ao lucro e ao balanço: itens não recorrentes, leasing, P&D, provisões, normalização de resultado (`ajustes_contabeis.md`) | Cap. 9 (p. 311–340) | Cap. 3 (impairment, ágio, depreciação, equivalência) | ★ |
| 08 | Intangíveis e IFRS: impacto na leitura de balanço e nos modelos (`intangiveis_ifrs.md`) | Cap. 9, Cap. 27 | Cap. 3 (p. 69–94) | ◐ |

### Bloco 3 — Fluxo de caixa (etapa de modelo)
| # | Tema | [D] | [P] | Prior. |
|---|---|---|---|---|
| 09 | Lucro operacional, EBIT(1–t), alíquota efetiva × marginal, tratamento de impostos (`impostos_ebit.md`) | Cap. 9 e 10 | Cap. 5 (p. 158–163) | ★ |
| 10 | Do lucro ao fluxo de caixa: capex, depreciação e itens "não caixa", reinvestimento (`reinvestimento.md`) | Cap. 10 (p. 341–372) | Cap. 5 (p. 163–166) | ★ |
| 11 | FCFF × FCFE × dividendos: definição, quando usar cada um, como converter um no outro (`fcff_fcfe.md`) | Cap. 13, 14, 15 | Cap. 5 (p. 131–176) | ★ |
| 12 | Por que projetar caixa e não lucro; sunk cost; erros típicos de projeção (`projecao_fluxo.md`) | Cap. 10 | Cap. 4 (p. 96–104, 118) | ★ |
| 13 | Número de estágios de projeção e fases de crescimento (`estagios.md`) | Cap. 11 (p. 373–424) | Cap. 4 (p. 113–118) | ★ |

### Bloco 4 — Crescimento e retorno
| # | Tema | [D] | [P] | Prior. |
|---|---|---|---|---|
| 14 | Estimativa de crescimento: histórico, analistas, fundamentos (g = reinvestimento × ROIC) (`crescimento.md`) | Cap. 11 | Cap. 8 (p. 269–290) | ★ |
| 15 | Teste de consistência de crescimento (curto prazo e perpetuidade); capacidade ociosa e depreciação (`consistencia_crescimento.md`) | Cap. 11 e 12 | Cap. 8 (p. 271–290) | ★ |
| 16 | ROIC, ROE e criação de valor: o retorno como motor do valor (`roic_criacao_valor.md`) | Cap. 11, 31, 32 | Cap. 8 (p. 282–290) e Cap. 10 (EVA, p. 379–395) | ★ |

### Bloco 5 — Taxa de desconto (etapa de WACC)
| # | Tema | [D] | [P] | Prior. |
|---|---|---|---|---|
| 17 | Risco e retorno: CAPM, APT e modelos multifatoriais (`risco_modelos.md`) | Cap. 4 (p. 81–120) | Cap. 6 (p. 179–186) | ★ |
| 18 | Taxa livre de risco: o que usar, risco-país, "ativo livre de risco existe?", dólar × real (`taxa_livre_risco.md`) | Cap. 7 (p. 211–245) | Cap. 6 (p. 186–193, 227–229) | ★ |
| 19 | Prêmio de risco de mercado: histórico × implícito, mercados emergentes (`premio_risco.md`) | Cap. 7 | Cap. 6 (p. 206–210, 250–254) | ★ |
| 20 | Beta: regressão, bottom-up, desalavancar e realavancar, alfa da regressão (`beta.md`) | Cap. 8 (p. 246–280) | Cap. 6 (p. 193–206, 229–231) | ★ |
| 21 | Custo da dívida: rating, spread, empréstimos subsidiados (BNDES), benefício fiscal (`custo_divida.md`) | Cap. 8 | Cap. 6 (p. 231–245) | ★ |
| 22 | JCP (juros sobre capital próprio): vantagem tributária brasileira (`jcp.md`) | — | Cap. 6 (p. 210–212) | ★ |
| 23 | WACC e estrutura de capital: pesos a valor de mercado × alvo, circularidade (`wacc.md`) | Cap. 8 e 15 (p. 533–592) | Cap. 6 (p. 231–245) e Cap. 7 | ★ |
| 24 | Estrutura de capital ótima: verdades e mitos do endividamento (`estrutura_capital.md`) | Cap. 8 e 15 | Cap. 7 (p. 255–268) | ◐ |
| 25 | Taxa de desconto variando no tempo: "escadinha" no WACC, pré-perpetuidade × perpetuidade (`taxa_variavel.md`) | Cap. 8, 12, 15 | Cap. 6 (p. 217–227, 245) | ★ |
| 26 | Taxa de desconto para empresas com receita no exterior (`receita_exterior.md`) | Cap. 7, 8 | Cap. 6 (p. 246–250) | ★ |
| 27 | Taxa de desconto e prêmio de risco implícitos ("fazer a conta ao contrário") (`taxa_implicita.md`) | Cap. 7 | Cap. 6 (p. 250–254) | ◐ |
| 28 | Método APV como alternativa ao WACC (`apv.md`) | Cap. 15 | — | ◐ |

### Bloco 6 — Valor terminal e valor por ação (etapa de modelo e sensibilidade)
| # | Tema | [D] | [P] | Prior. |
|---|---|---|---|---|
| 29 | Valor terminal: Gordon, múltiplo de saída, liquidação; premissas de estabilidade; normalização de margem e reinvestimento na perpetuidade (`valor_terminal.md`) | Cap. 12 (p. 425–449) | Cap. 4 (p. 119–125), Cap. 8 (p. 271–276) | ★ |
| 30 | Do valor da firma ao valor por ação: dívida líquida, caixa, minoritários, participações, opções e ações diluídas (`ev_para_equity.md`) | Cap. 16 (p. 593–636) | Cap. 3 (diluição, p. 88), Cap. 10 (caixa, p. 355–361) | ★ |
| 31 | Valor do caixa: caixa excedente, caixa operacional, desconto de caixa preso (`valor_caixa.md`) | Cap. 16 | Cap. 10 (p. 355–361) | ◐ |
| 32 | Análise de sensibilidade (g × taxa de desconto), cenários, simulação (`sensibilidade_cenarios.md`) | Cap. 2, 5, 16 | Cap. 4 (p. 104–113), Cap. 5 (p. 172–176) | ★ |

### Bloco 7 — Valuation relativa (checagem cruzada do DCF)
| # | Tema | [D] | [P] | Prior. |
|---|---|---|---|---|
| 33 | Princípios da valuation relativa: padronização, comparáveis, controle de variáveis (`relativa_principios.md`) | Cap. 17 (p. 637–658) | Cap. 9 (p. 291–299) | ★ |
| 34 | "Múltiplo justo": derivar o múltiplo a partir do DCF (`multiplo_justo.md`) | Cap. 17–20 | Cap. 9 (p. 299–302) | ★ |
| 35 | Múltiplos de lucro: P/L, PEG, EV/EBITDA, polêmica do caixa no EV (`multiplos_lucro.md`) | Cap. 18 (p. 659–717) | Cap. 9 (p. 313–331) | ★ |
| 36 | Múltiplos de patrimônio: P/VP e P/VP × ROE (`multiplos_vp.md`) | Cap. 19 (p. 718–759) | Cap. 9 (p. 302–313) | ◐ |
| 37 | Múltiplos de receita e setoriais: P/Receita, EV/Receita (`multiplos_receita.md`) | Cap. 20 (p. 760–801) | Cap. 9 (p. 331–342) | ◐ |

### Bloco 8 — Tópicos especiais
| # | Tema | [D] | [P] | Prior. |
|---|---|---|---|---|
| 38 | Macro e valor: efeito de juros, câmbio e inflação nas projeções (`macro_efeitos.md`) | Cap. 7 e 12 | Cap. 10 (p. 365–379) | ★ |
| 39 | Dividendos: o "mito dos dividendos" e o DDM (`dividendos.md`) | Cap. 13 (p. 450–486) | Cap. 10 (p. 410–420) | ◐ |
| 40 | Controle, liquidez e empresas fechadas (`controle_liquidez.md`) | Cap. 16, 24, 25 | Cap. 10 (p. 346–355, 396–407) | ◐ |
| 41 | Marca, P&D e marketing no valor (`marca_pd.md`) | Cap. 27, 22 | Cap. 10 (p. 361–365, 407–410) | ◐ |
| 42 | EVA, CFROI e outras métricas de criação de valor (`eva.md`) | Cap. 32 (p. 1221–1255) | Cap. 10 (p. 379–396) | ◐ |
| 43 | Limites da teoria: crise de 2008, quando o modelo falha (`limites_teoria.md`) | Cap. 1, 35 | Cap. 10 (p. 420–424) | ◐ |
| 44 | Empresas financeiras (bancos, seguradoras): a regra do DCF muda (`financeiras.md`) | Cap. 21 (p. 802–846) | — | ○ (banco está fora da 1ª empresa) |
| 45 | Prejuízo, cíclicas e start-ups: normalização e valuation com earnings negativos (`prejuizo_ciclicas.md`) | Cap. 22, 23 | — | ◐ (útil para cíclicas) |
| 46 | Fusões e aquisições, sinergias (`ma.md`) | Cap. 25 (p. 969–1027) | — | ○ |
| 47 | Opções reais (`opcoes_reais.md`) | Cap. 5, 28, 29, 30 | Cap. 11 (p. 425–452) | ○ |
| 48 | Imóveis, outros ativos, títulos e futuros (`outros_ativos.md`) | Cap. 26, 27, 33, 34 | — | ○ |

---

## PARTE B — Fichamentos por CAPÍTULO (alternativa, mais fácil de conferir)

Use se preferir resumir capítulo a capítulo (um arquivo por capítulo). Depois você pode consolidar por tema.

### [D] Damodaran, *Investment Valuation* 2ª ed.
| Cap. | Título | PDF pág. | Prior. |
|---|---|---|---|
| 1 | Introduction to Valuation | 3 | ★ |
| 2 | Approaches to Valuation | 16 | ★ |
| 3 | Understanding Financial Statements | 37 | ★ |
| 4 | The Basics of Risk | 81 | ★ |
| 5 | Option Pricing Theory and Models | 121 | ○ |
| 6 | Market Efficiency: Theory and Models | 152 | ◐ |
| 7 | Riskless Rates and Risk Premiums | 211 | ★ |
| 8 | Estimating Risk Parameters and Costs of Financing | 246 | ★ |
| 9 | Measuring Earnings | 311 | ★ |
| 10 | From Earnings to Cash Flows | 341 | ★ |
| 11 | Estimating Growth | 373 | ★ |
| 12 | Closure in Valuation: Estimating Terminal Value | 425 | ★ |
| 13 | Dividend Discount Models | 450 | ◐ |
| 14 | Free Cashflow to Equity Models | 487 | ★ |
| 15 | Firm Valuation: Cost of Capital and APV Approaches | 533 | ★ |
| 16 | Estimating Equity Value Per Share | 593 | ★ |
| 17 | Fundamental Principles of Relative Valuation | 637 | ★ |
| 18 | Earnings Multiples | 659 | ★ |
| 19 | Book Value Multiples | 718 | ◐ |
| 20 | Revenue and Sector-Specific Multiples | 760 | ◐ |
| 21 | Valuing Financial Service Firms | 802 | ○ |
| 22 | Valuing Firms with Negative Earnings | 847 | ◐ |
| 23 | Valuing Young and Start-up Firms | 891 | ○ |
| 24 | Valuing Private Firms | 928 | ○ |
| 25 | Acquisitions and Takeovers | 969 | ○ |
| 26 | Valuing Real Estate | 1028 | ○ |
| 27 | Valuing Other Assets | 1067 | ○ |
| 28 | The Option to Delay and Valuation Implications | 1090 | ○ |
| 29 | The Option to Expand and Abandon | 1124 | ○ |
| 30 | Valuing Equity in Distressed Firms | 1155 | ○ |
| 31 | Value Enhancement: A Discounted Cashflow Framework | 1176 | ◐ |
| 32 | Value Enhancement: EVA, CFROI and Other Tools | 1221 | ◐ |
| 33 | Valuing Bonds | 1256 | ○ |
| 34 | Valuing Forward and Futures Contracts | 1308 | ○ |
| 35 | Overview and Conclusions | 1338 | ◐ |

### [P] Póvoa, *Valuation: Como Precificar Ações*
| Cap. | Título | Pág. | Prior. |
|---|---|---|---|
| 1 | Valuation, a arte de precificar (escolas, top-down × bottom-up, jargões) | 1 | ★ |
| 2 | Contabilidade e análise de balanço (NCG, indicadores) | 15 | ★ |
| 3 | Ativos intangíveis e IFRS no Brasil | 69 | ◐ |
| 4 | O fluxo de caixa descontado (mitos, sensibilidade, estágios, perpetuidade) | 95 | ★ |
| 5 | Fluxo de caixa para o acionista × para a firma (FCFE × FCFF, impostos) | 131 | ★ |
| 6 | Taxa de desconto (CAPM, beta, risco-país, JCP, rating, WACC) | 177 | ★ |
| 7 | Estrutura de capital ótima: verdades e mitos | 255 | ◐ |
| 8 | Taxa de crescimento: a busca da consistência | 269 | ★ |
| 9 | Valuation relativa: o uso indiscriminado dos múltiplos | 291 | ★ |
| 10 | Tópicos em valuation (controle, caixa, marca, juros/câmbio/inflação, EVA, dividendos, crise de 2008) | 345 | ★ |
| 11 | Opções reais | 425 | ○ |

---

## PARTE C — Prompt-modelo para pedir cada fichamento

Cole no Projeto "Método e Bibliografia", trocando `[TEMA]` e as fontes:

```
Faça o fichamento do tema [TEMA] com base em [Damodaran, Cap. X] e [Póvoa, Cap. Y].

Regras:
1. Escreva com as suas palavras. Não transcreva trechos longos (no máximo uma frase curta entre aspas, quando indispensável).
2. Cite livro, capítulo e página em cada ideia. Se não tiver o texto à mão, marque "[NÃO VERIFICADO]".
3. Não invente número, fórmula nem citação. Se o livro não trata do ponto, diga isso.
4. Entregue em Markdown, com estas seções:
   - Conceito central (3 a 5 linhas)
   - Fórmulas (com definição de cada variável)
   - Premissas e escolhas do autor (e por que ele as faz)
   - Passo a passo prático
   - Erros comuns apontados pelo autor
   - Onde Damodaran e Póvoa concordam e onde divergem
   - Limites: o que está defasado (Damodaran é de 2002) ou é específico do Brasil
   - Aplicação ao canal: o que isso muda ou confirma na METODOLOGIA.md
     (apenas sugestão; não altere o arquivo)
   - Dúvidas abertas para eu decidir
```

---

## Ordem sugerida (para começar)

1. 20 (beta), 18 (taxa livre de risco), 19 (prêmio de risco), 21 (custo da dívida), 23 (WACC): fecham a etapa que mais pesa no resultado.
2. 29 (valor terminal), 14 e 15 (crescimento e consistência), 16 (ROIC).
3. 09 a 13 (fluxo de caixa) e 30 (do EV para o preço por ação).
4. 04 a 07 (contabilidade e ajustes) e 32 (sensibilidade).
5. 33 a 35 (múltiplos como checagem) e 38 (macro).
6. Os demais, na ordem do interesse.
