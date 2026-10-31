# Fichamento 34: "Múltiplo justo": derivar o múltiplo a partir do DCF

**Fontes**
- **[D]** Damodaran (2002), Cap. 17, testes analíticos (PDF p. 647–649); Cap. 18, P/L pelos fundamentos (p. 662–669), PEG (p. 685–690), EV/EBITDA (p. 704–708); Cap. 19, P/VP pelos fundamentos (p. 723–729), valor/capital (p. 748–752); Cap. 20, P/Receita e EV/Receita pelos fundamentos (p. 763–768).
- **[P]** Póvoa (2012), Cap. 9: "A ideia do múltiplo justo" (p. 299–302); P/VP justo (p. 302–308); P/L justo (p. 313–318); EV/EBITDA justo (p. 326–329); P/Receita (p. 331–338) e EV/Receita (p. 338–341).

---

## 1. Conceito central

Todo múltiplo é um DCF comprimido. Dividindo a fórmula de valor (Gordon ou estágios) pela variável do denominador, obtém-se o múltiplo **justificado pelos fundamentos** da própria empresa ([D] p. 647–648; [P] p. 299–300). Isso cria a ponte entre DCF e múltiplos: se os dois forem feitos com as mesmas premissas, **não podem divergir muito**. Póvoa chama de "falsa dicotomia" a ideia de que DCF e múltiplos são métodos alternativos e critica relatórios que fazem média ponderada entre métodos com resultados discrepantes ([P] p. 299–300).

## 2. Fórmulas (empresa estável, um estágio)

Com FCFE ≈ dividendos ([D] p. 648; [P] p. 300–303):
- **P/L** = `payout × (1 + g)/(Ke − g)` → depende de payout (+), g (+), Ke (−).
- **P/VP** = `ROE × payout × (1 + g)/(Ke − g)`; com `g = ROE × (1 − payout)`: **P/VP = (ROE − g)/(Ke − g)** ([D] Cap. 19, p. 724–725). **ROE > Ke ↔ P/VP > 1.**
- **P/Receita** = `margem líquida × payout × (1 + g)/(Ke − g)` ([D] Cap. 20, p. 764; [P] p. 332).
- **EV/Capital** = `(ROC − g)/(WACC − g)` ([D] Cap. 19, p. 751).
- **EV/Receita** = `margem operacional após IR × (1 − RR) × (1 + g)/(WACC − g)` ([D] Cap. 20, p. 767).
- **EV/EBITDA**: depende de alíquota, D&A/EBITDA, reinvestimento/EBITDA, WACC e g ([D] Cap. 18, p. 707–708; [P] p. 326).
- **Estágios**: soma do VP do alto crescimento com o VP do valor terminal, tudo dividido pela variável ([D] p. 663; [P] p. 300–301).

**Exemplos de [P] recalculados**
- **Média ponderada criticada** ([P] p. 300) ✔: 0,4 × 50 + 0,35 × 43 + 0,25 × 61 = **R$ 50,30**. "Muito bonito para marketing, pobre tecnicamente."
- **Retenção necessária** ([P] p. 305) ✔: A (ROE 15%, payout 20%) cresce 0,8 × 0,15 = 12%. B (ROE 13%) precisa reter 0,12/0,13 = 92,3%, ou seja, payout ≈ **8%**.
- **P/VP têxtil** ([P] p. 306–307): o livro chega a **3,31** (0,24 + 0,31 + 2,76). **Ressalvas**: (i) o texto diz retenção de 95%, mas calcula `0,42 × (1 − 0,15) = 36,9%`; depois cita 39,9% (= 0,42 × 0,95), uma inconsistência interna. (ii) o termo de variação do ROE (−28,6%) é aplicado como **taxa de crescimento** durante os três anos da fase moderada, mas pela fórmula de [D] (Cap. 11, p. 407) ele só vale no **ano** em que o ROE muda. (iii) **Não consegui reproduzir 3,31**: refazendo ano a ano pelo PL (lucro = ROE × PL inicial), obtive ≈ **6,3**; usando o método de taxas do livro, 3,4 a 3,8. *Use o exemplo pelo raciocínio, não pelo número.*
- **P/L justo da construtora** ([P] p. 315–316): Ke = 10% + 0,8 × 6,5% = **15,2%** ✔; com benefício do JCP, 15,2 × (1 − 0,0555) = **14,4%** ✔; P/L justo = **19,8**. A fragilidade apontada pelo próprio autor: ROE perpétuo de 32%, muito acima do Ke.

## 3. Premissas e escolhas dos autores

- **FCFE = dividendos é frágil** ([P] p. 301–302): há muitos motivos para reter caixa (oportunidades, ciclo, custos fixos, desalavancagem, NCG, má gestão). Por isso, o múltiplo justo funciona melhor em **empresas maduras** e em múltiplos em que o payout pesa menos (P/VP, dominado pelo ROE). Para o P/L, melhor usar FCFE/lucro.
- **EV/EBITDA justo não precisa da hipótese de payout** ([P] p. 329), por ser um múltiplo da firma.
- **Cada múltiplo tem sua variável dominante** ([D] p. 649): P/VP pelo ROE, P/Receita pela margem.
- **Duas aplicações** ([D] Cap. 18, p. 669): (a) comparar o múltiplo de mercado com o justo da própria empresa; (b) inverter: que g ou ROE o múltiplo atual implica (temas 27 e 32).

## 4. Passo a passo prático

1. Do DCF, extraia o **EV/EBITDA, P/L e P/VP implícitos** no preço justo (valor justo ÷ EBITDA/lucro/PL projetado do ano 1).
2. Compare com o **múltiplo atual** da ação e com a **mediana dos pares** (tema 33).
3. Se o múltiplo justo estiver muito acima dos pares, verifique qual premissa explica (ROIC perpétuo, g, WACC).
4. Faça o inverso: qual g perpétuo ou ROIC o preço atual implica?

## 5. Erros comuns apontados pelos autores

- **Média ponderada entre métodos** com resultados inconsistentes ([P] p. 300).
- **Supor FCFE = dividendos** em empresas em crescimento ([P] p. 301–302).
- **Ignorar a variável dominante** (P/VP alto com ROE baixo) ([D] Cap. 19, p. 755).
- **ROE ou ROIC perpétuos muito acima do custo de capital** sem vantagem durável ([P] p. 307, 316).

## 6. Onde concordam e onde divergem

**Concordam**: o múltiplo justo deriva do DCF; métodos consistentes geram valores próximos; P/VP depende do spread ROE − Ke.

| Ponto | Damodaran | Póvoa |
|---|---|---|
| Base do fluxo | FCFE ou dividendos; FCFF para múltiplos da firma | Dividendos como proxy, com ressalvas |
| Uso | Comparação e regressões em toda a amostra | Exemplos numéricos por empresa |
| EV/EBITDA | Derivação com reinvestimento e D&A | Exemplo de dois estágios (p. 327–329) |

## 7. Limites: o que está defasado ou é específico do Brasil

- No Brasil, o JCP altera o Ke efetivo e o payout (tema 22). [P] reduz o Ke pelo benefício do JCP (p. 315), escolha a decidir (tema 22).
- Exemplos com taxa livre de risco de 10% e prêmio de 6,5% ([P]) são da época.

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. **Saída obrigatória do DCF**: EV/EBITDA, P/L e P/VP implícitos no preço justo, em tabela ao lado dos pares.
2. **Proibido** fazer média ponderada entre métodos.
3. Mostrar sempre o **g e o ROIC implícitos** no preço atual.

## 9. Dúvidas abertas para você decidir

1. Mostrar no vídeo a fórmula P/VP = (ROE − g)/(Ke − g) como intuição?
2. Qual múltiplo implícito destacar como principal (EV/EBITDA ou P/L)?
