# Fichamento 09: Lucro operacional, EBIT(1−t), alíquota efetiva × marginal, tratamento de impostos

**Fontes**
- **[D]** Damodaran (2002), Cap. 10, "The Tax Effect": efetiva × marginal, multinacionais, efeito no valor (Ilustração 10.1), prejuízos fiscais (NOL), benefício fiscal do P&D, livros fiscais × societários e subsídios fiscais (PDF p. 341–353). Cap. 8, alíquota no custo da dívida (p. 287). Cap. 9 para o EBIT ajustado (tema 07).
- **[P]** Póvoa (2012), Cap. 5, "Impostos, como tratar na valuation e o caso específico do EBIT (1 – t) no FCFF" (p. 158–163) e "A questão da depreciação…" (p. 163–166).

---

## 1. Conceito central

O FCFF parte do **lucro operacional depois dos impostos que a empresa pagaria sem dívida**, EBIT(1−t) ([D] p. 341; [P] p. 162–163). A alíquota é a grande questão. A **efetiva** (imposto pago/lucro antes do IR) pode ficar muito abaixo da **marginal** (alíquota sobre o último real de lucro) por diferimentos, créditos, incentivos e diferenças entre livros fiscais e societários ([D] p. 342–343). Damodaran admite começar pela efetiva, mas exige **convergir para a marginal**, principalmente na perpetuidade, porque nenhuma das causas da diferença dura para sempre ([D] p. 344). Póvoa recomenda a **efetiva** e manter a carga tributária corrente em todo o fluxo, com uma regra rígida: **benefícios fiscais só até o fim do prazo legal** ([P] p. 159–162).

## 2. Fórmulas

**Alíquota efetiva** ([D] p. 342): `t efetiva = impostos devidos / lucro tributável`.

**EBIT(1−t) no FCFF**
- [D]: `EBIT × (1 − t)`, com t convergindo para a marginal ([D] p. 344).
- [P]: `EBIT − IR efetivamente pago` (o IR calculado depois do resultado financeiro). No exemplo da papelaria, a alíquota efetiva sobre o EBIT é 3/18 = **16,7%** contra 30% marginal, porque o resultado financeiro negativo reduz o IR ([P] p. 162–163).

**Prejuízo fiscal acumulado (NOL)** ([D] p. 347–349)
(1) Alíquota **zero** enquanto o NOL protege o lucro, subindo depois para a marginal. **Isso também vale para o Kd(1−t) no WACC.**
(2) Alternativa: valor sem NOL + t × NOL. É imprecisa, porque supõe que a economia é garantida e imediata.

**Benefício fiscal de despesas capitalizadas (P&D)** ([D] p. 349–351)
`EBIT(1−t) ajustado = EBIT(1−t) + P&D corrente − amortização do ativo de pesquisa`
Exemplo da Amgen: 1.549 × 0,65 + 845 − 398 = **1.454** ✔.

**Passivo fiscal diferido** ([D] p. 346): ao usar a marginal, subtraia o VP dos impostos diferidos a pagar. Exemplo: 50/ano por 4 anos a 9% = **161,99** ✔.

**Prejuízo compensável** ([P] p. 158–159): prejuízo de 1 mi → crédito de 0,3 mi. Lucro de 3 mi no ano seguinte → IR de 0,6 mi, alíquota efetiva de 20%.

**Subsídio fiscal** ([D] p. 352; [P] p. 160–162): avalie a empresa **sem** o benefício e some o **VP do benefício durante o prazo legal**, a uma taxa apropriada ao risco do benefício. Exemplo de [P] (sapatos, região isenta): 36% do valor viria da isenção perpétua (121 × 89 mi).

## 3. Premissas e escolhas dos autores

- **Por que efetiva ≠ marginal** ([D] p. 343): (1) livros fiscais × societários (depreciação acelerada no fiscal); (2) créditos fiscais; (3) diferimento; (4) alíquotas escalonadas.
- **Multinacionais** ([D] p. 343–344): (a) média ponderada das marginais pela renda de cada país; (b) marginal do país-sede (supõe repatriação); (c) **a mais segura**: alíquota separada para cada fluxo de renda.
- **Efeito no valor** ([D] p. 345–347, Convoy): efetiva para sempre → valor mais alto (supõe que o diferido nunca será pago); marginal para sempre (e subtrair o diferido) → mais baixo; **combinação** (efetiva por 5 anos, marginal no TV, VP do diferido acumulado subtraído) → intermediário. Valores do exemplo: 1.956,94 − 161,99 = 1.794,96 (marginal); 2.111,12 − 167,45 = 1.943,67 (combinado).
- **Lucro líquido também carrega a alíquota de hoje** ([D] p. 344): no FCFE, se o LL atual tem imposto baixo por planejamento, a projeção precisa ajustar.
- **Livros fiscais**: se fosse possível escolher, Damodaran avaliaria pelo livro fiscal ([D] p. 351–352).
- **Póvoa sobre a projeção da carga** ([P] p. 159–160): não "adivinhar" mudanças tributárias. Mantenha a carga corrente; na perpetuidade há algum espaço, mas é um exercício "praticamente de adivinhação". **Isenções legais** (Zona Franca, regiões incentivadas) só até o fim do prazo legal, eventualmente como um estágio intermediário de N anos ([P] p. 160–162).
- **Impostos sobre faturamento** (PIS/COFINS, ICMS) entram na receita líquida; o IR e a CSLL incidem sobre o lucro ([P] p. 158).

## 4. Passo a passo prático

1. Calcule a **alíquota efetiva histórica** (3 a 5 anos) e entenda a diferença para a **marginal** (34% no Brasil, IRPJ + CSLL, lucro real): JCP, incentivos (SUDENE/SUDAM), diferidos, prejuízos fiscais.
2. **Período explícito**: alíquota projetada conforme cada causa (prazo do incentivo, consumo do NOL, JCP se tratado no fluxo).
3. **Perpetuidade**: **alíquota marginal**, sem incentivos temporários ([D] p. 344; [P] p. 160–162).
4. **NOL**: projete o consumo ano a ano (alíquota zero → marginal) e aplique a mesma alíquota no Kd(1−t) ([D] p. 347).
5. **Diferido**: se a projeção usa a marginal, considere o VP dos diferidos passivos a pagar ([D] p. 346).
6. **EBIT(1−t)**: aplique t sobre o EBIT (método de [D]), não o IR pago depois do resultado financeiro. O benefício fiscal dos juros já está no WACC (tema 23).

## 5. Erros comuns apontados pelos autores

- **Usar a alíquota efetiva baixa para sempre** ([D] p. 344).
- **Perpetuar isenções e incentivos** ([P] p. 160–162; [D] p. 352).
- **Somar t × NOL** como se a economia fosse garantida e imediata ([D] p. 348).
- **Esquecer o benefício fiscal do P&D** ao capitalizá-lo ([D] p. 349).
- **Dar benefício fiscal à dívida em anos sem lucro tributável** ([D] p. 347; Cap. 8, p. 287).

## 6. Onde concordam e onde divergem

**Concordam**: não perpetuar benefícios fiscais; o IR é custo que destrói valor; prejuízos compensáveis reduzem a alíquota no curto prazo.

| Ponto | Damodaran | Póvoa |
|---|---|---|
| Alíquota | Efetiva no início → **marginal**, obrigatória no TV (p. 344) | **Efetiva**, mantida constante (p. 159–160) |
| EBIT(1−t) | EBIT × (1 − t) | EBIT − IR pago (inclui o efeito do resultado financeiro) (p. 162–163) |
| Subsídios | Valor separado, com taxa própria (p. 352) | Até o prazo legal; estágio intermediário (p. 162) |

*Atenção*: o método de [P] para o EBIT(1−t) mistura o benefício fiscal dos juros (o resultado financeiro negativo reduz o IR) com o fluxo operacional. No FCFF descontado a WACC com Kd(1−t), isso **conta o benefício fiscal duas vezes** ([D] Cap. 15, p. 534). É uma análise minha, que precisa ser conferida no exemplo completo da Tab. 5.9, cujos números não saíram na extração.

*Erro de texto em [P] p. 162*: no exemplo dos sapatos, o livro diz que a empresa "valeria 60% a menos" sem isenção (89 contra 121). A diferença é de −26% (ou +36% no sentido inverso), não 60%.

## 7. Limites: o que está defasado ou é específico do Brasil

- **Reforma tributária (EC 132/2023)**: a substituição de PIS/COFINS/ICMS/ISS por CBS/IBS, com transição a partir de 2026, afeta a receita líquida e os créditos. **Não está nos livros [NÃO VERIFICADO aqui]**.
- **IRPJ 25% + CSLL 9% = 34%** (lucro real) e as alíquotas de CSLL de setores específicos (bancos) também não estão nos livros.
- **Compensação de prejuízos** no Brasil é limitada a 30% do lucro real por ano, sem prazo. *Não está nos livros; é a regra usual, a confirmar.* O exemplo de [P] (até 3 anos) é hipotético.
- O JCP como benefício fiscal está no tema 22.
- A "Lei do Bem" (P&D) e outros incentivos têm regras próprias.

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. **t marginal de 34%** na perpetuidade. No explícito, a efetiva justificada item a item, convergindo para 34%.
2. **EBIT(1−t) = EBIT × (1 − t)**, sem usar o IR pago depois dos juros.
3. **Incentivos regionais**: tabela com o prazo legal de cada benefício e o VP do benefício mostrado em separado.
4. **Prejuízo fiscal**: projetar o consumo com a trava de 30% e aplicar t = 0 no Kd(1−t) enquanto houver compensação.
5. Acompanhar a transição da reforma tributária no `MACRO.md`.

## 9. Dúvidas abertas para você decidir

1. Alíquota no explícito: efetiva histórica com convergência ou marginal desde o ano 1?
2. Como tratar incentivos renováveis historicamente (Zona Franca): só até o prazo legal ou com um cenário de renovação?
3. Modelar a reforma tributária em todas as empresas ou só onde o impacto for relevante?
