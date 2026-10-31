# Fichamento 24: Estrutura de capital ótima: verdades e mitos

**Fontes**
- **[D]** Damodaran (2002), Cap. 15, "The Effect of Leverage on Firm Value", "Cost of Capital and Optimal Leverage", Ilustração 15.7 (Boeing), "Default Risk, Operating Income and Optimal Leverage", "APV and Financial Leverage" e Ilustração 15.8 (PDF p. 566–588). Cap. 8 para o Hamada (p. 265).
- **[P]** Póvoa (2012), Cap. 7 "Estrutura de capital ótima – verdades e mitos" (p. 255–268). Cap. 6, p. 240–243.

---

## 1. Conceito central

À medida que a empresa troca capital próprio por dívida, o WACC cai no começo, porque a dívida é mais barata e tem benefício fiscal. Depois volta a subir, porque o Ke (via beta) e o Kd (via rating) aumentam. A **estrutura ótima** é a que **maximiza o valor da firma**. Ela só coincide com o ponto de WACC mínimo se o resultado operacional não depender da alavancagem ([D] p. 566–567, 583; [P] p. 256, 260–261). Damodaran mostra como calcular esse ponto. Póvoa enfatiza os **limites práticos**: crédito restrito, a média do setor como âncora, previsibilidade do resultado e juro real alto no Brasil ([P] p. 260, 264–267).

## 2. Fórmulas

**Beta em função da alavancagem** (Hamada) ([D] p. 569; [P] p. 240)
`βL = βu × [1 + (1 − t) D/E]`
Com beta da dívida: `βL = βu × [1 + (1−t) D/E] − βD × (1−t) D/E` ([D] p. 572).

**Rating sintético por nível de dívida** ([D] p. 572–577)
Para cada D/(D+E): dívida em US$ = índice × (D+E) atual → juros → ICR = EBIT/juros → rating → Kd. É preciso iterar, porque os juros dependem do rating ([D] p. 576).

**Alíquota efetiva quando juros > EBIT** ([D] p. 577–578)
`t efetiva = t × EBIT / juros` (o benefício fica limitado ao EBIT).

**Ganho de valor ao ir para o ótimo (perpetuidade)** ([D] p. 581)
`g implícito = (V × WACC − FCFF) / (V + FCFF)`, depois `V novo = FCFF(1+g)/(WACC novo − g)`. Boeing: de 40.789 para 40.990 (+US$ 201 mi; +0,62% no preço) ([D] p. 581–582).

**APV para o ótimo** ([D] p. 584–587)
`V alavancada = V desalavancada + t × D − P(default) × custo de falência × V desalavancada`

**Exemplo de Póvoa** ([P] p. 261–262): logística, βu = 0,52, Rf 10%, prêmio 6,5%, IR 30%, com JCP.
- Antes: D/E 0,40, rating A1 (spread 1,05%) → β 0,67, Ke 13,53%, Kd(1−t) 7,74%, **WACC 11,87%** ✔.
- Depois de quadruplicar a dívida: D/E 1,6, rating Ba1 (spread 4,6%) → β 1,10, Ke 16,21%, Kd(1−t) 10,22%, **WACC 12,53%** ✔.
- *O texto escreve "10% + 1,05% × (1 – 0,30)" com parênteses trocados; a conta certa é (10% + 1,05%) × 0,7.*

## 3. Premissas e escolhas dos autores

- **Por que a dívida é mais barata** ([P] p. 257–258): (a) o credor recebe em qualquer cenário; (b) o prêmio do capital próprio = prêmio da dívida + um adicional de renda variável sempre positivo; (c) o benefício fiscal dos juros (~30% sobre o total) supera o do JCP (~5,55%).
- **Disciplina e conflitos de agência** ([P] p. 258–259): a dívida disciplina o gestor. Há conflitos entre gestor e acionista (mitigados por stock options e participação nos resultados) e entre acionista e credor (mitigados por covenants e conversíveis).
- **O mito reescrito** ([P] p. 259): dívida é problema quando o retorno do investimento fica **permanentemente** abaixo do custo da dívida. Na dose certa, a dívida cria valor, mas é custo fixo e precisa de fonte de pagamento.
- **Hipóteses do método do WACC** ([D] p. 569–570): a mudança é feita por **recapitalização** (dívida para recomprar ações, ou o contrário), com o lado do ativo fixo; o resultado operacional não muda com o rating. Toda a dívida existente é **refinanciada** ao novo custo, o que evita transferência de riqueza entre credores e acionistas ([D] p. 577).
- **Resultado do caso Boeing** ([D] p. 578–582): WACC desalavancado de 9,79%, mínimo de 9,16% com 30% de dívida, contra 9,17% no nível atual de 20%. O ganho de ir ao ótimo é **desprezível** (+0,62%). O ótimo não muda quando a dívida carrega beta (Tab. 15.17, p. 579–580).
- **Custos indiretos de falência** ([D] p. 563–564, 583): podem chegar a 25–30% do valor (Shapiro e Titman), e o resultado operacional cai com o rebaixamento. Por isso o ótimo é o de **valor máximo**, não o de WACC mínimo.
- **APV** ([D] p. 584–588): também chega a um ótimo de 20–30% para a Boeing, mas é **muito sensível** à probabilidade de default e ao custo de falência (30% assumido). Quem ignora o custo de falência conclui que o ótimo é 100% dívida.
- **Limites práticos ([P])**:
  - O crédito é limitado e as agências olham o prazo da dívida, não a perpetuidade (p. 260).
  - **A média do setor é um sinalizador**: uma empresa muito acima da média pagará um prêmio adicional ("o dinheiro é covarde") (p. 265–266).
  - **Previsibilidade**: empresas maduras se alavancam mais; startups e cíclicas, menos (p. 266–267).
  - **Brasil**: juro real alto e prazos curtos fazem a empresa "quebrar antes de atingir a perpetuidade". A questão vira análise de **crédito** (p. 264).
  - Exemplo de dados: D/(D+E) mediano das companhias abertas brasileiras de 0,17 (2006), 0,20 (2009) e 0,25 (2012) (p. 264–265, Tab. 7.1).
- **Como modelar a mudança** ([P] p. 267–268): prefira o FCFF. Pergunte à empresa a estrutura de capital pretendida; na falta de resposta coerente, (i) mantenha a estrutura atual ou (ii) faça a convergência para a média do setor. Defina o ritmo da convergência até a perpetuidade. Quatro casos (bons ou maus projetos × alavancar ou desalavancar) e os instrumentos de cada um: dívida, payout, recompra, emissão, renegociação.

## 4. Passo a passo prático (análise de ótimo, [D])

1. Calcule o βu atual (desalavancando pelo D/E de mercado).
2. Para D/(D+E) de 0% a 90%: realavanque o beta → Ke; calcule dívida e juros → ICR → rating → Kd (iterando); ajuste a alíquota se os juros passarem do EBIT.
3. Calcule o WACC em cada nível e encontre o mínimo.
4. Verifique se o resultado operacional cairia com o rebaixamento. Se cair, maximize o **valor**, não minimize o WACC.
5. Para o valuation, **não suponha que a empresa vai ao ótimo** sem evidência. Use a estrutura pretendida declarada pela empresa ou a média do setor ([P] p. 267).

## 5. Erros comuns apontados pelos autores

- **"Dívida é sempre ruim"** ([P] p. 256) ou **"dívida é sempre boa"** (APV sem custo de falência) ([D] p. 565–566, 588).
- **Ignorar que Ke e Kd sobem com a alavancagem** ([D] p. 569; [P] p. 240–242, 261–262).
- **Supor que os valores de mercado não reagem**: Póvoa usa a notação t0 porque D/E não muda linearmente depois do anúncio ([P] p. 242–243, 263).
- **Justificar uma alavancagem excessiva pelos projetos novos**, quando os mesmos projetos poderiam ser financiados com um mix melhor ([P] p. 263).
- **Esquecer o efeito de imagem** do rebaixamento para grau especulativo: receita menor, marketing maior ([P] p. 263).

## 6. Onde concordam e onde divergem

**Concordam**: curva do WACC em "U"; Hamada; rating piora com a dívida; custos indiretos importam.

| Ponto | Damodaran | Póvoa |
|---|---|---|
| Ênfase | Calcular o ótimo (WACC ou APV) (p. 566–588) | Limites práticos e média do setor (p. 260–268) |
| Uso no valuation | Ganho de ir ao ótimo costuma ser pequeno (Boeing +0,6%) | Projetar convergência para a meta da empresa ou do setor |
| Brasil | Não trata | Juro real alto restringe a alavancagem; foco em crédito (p. 264) |

## 7. Limites: o que está defasado ou é específico do Brasil

- As tabelas de ICR e de spread (1999) e de default (Altman e Kishore, 1998) estão vencidas.
- A Tab. 7.1 de [P] (D/(D+E) por setor, 2012, Economática) está vencida.
- O JCP no Ke (tema 22) entra nas contas de Póvoa; veja as ressalvas.

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. **Não** modelar a ida ao "ótimo teórico" por padrão.
2. Estrutura-alvo da perpetuidade = **meta declarada pela empresa**, se crível pelo histórico, ou **mediana do setor** ([P] p. 267). Convergência linear durante o período explícito.
3. Em empresas muito alavancadas, rodar a **análise de crédito** (ICR, dívida/EBITDA, cronograma de amortização) **antes** do DCF, seguindo o alerta de Póvoa sobre "quebrar antes da perpetuidade".
4. Opcional para vídeos didáticos: mostrar a curva WACC × D/(D+E) da empresa (planilha no estilo `captstr.xls`).

## 9. Dúvidas abertas para você decidir

1. Estrutura-alvo: meta da empresa, mediana do setor ou a atual?
2. Incluir a análise de crédito como etapa obrigatória para empresas com dívida/EBITDA acima de X?
3. Mostrar a análise de ótimo nos vídeos ou só no material de apoio?
