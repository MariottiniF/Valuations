# Fichamento 10: Do lucro ao fluxo de caixa: capex, depreciação, itens "não caixa", reinvestimento

**Fontes**
- **[D]** Damodaran (2002), Cap. 10 "From Earnings to Cash Flows", "Reinvestment Needs": capex líquido, normalização, despesas capitalizadas, aquisições e capital de giro (PDF p. 353–369).
- **[P]** Póvoa (2012), Cap. 5: "Abrindo o fluxo de caixa para o acionista" (p. 136–142), "Abrindo o fluxo de caixa para a firma" (p. 150–156) e "A questão da depreciação e dos itens que 'não são caixa'" (p. 163–166). Cap. 2 para o capital de giro (tema 05).

---

## 1. Conceito central

O fluxo de caixa livre é o lucro **depois do reinvestimento** necessário para crescer. O reinvestimento tem dois componentes: o **capex líquido** (capex − D&A) e a **variação do capital de giro não caixa** ([D] p. 353; [P] p. 138). Damodaran amplia o capex para incluir **aquisições** e **despesas de natureza de capital** (P&D, treinamento) e insiste em **normalizar** itens irregulares ([D] p. 353–360). Póvoa enfatiza que a D&A só afeta o caixa pelo **benefício fiscal**, e que apresentar o **investimento líquido** (bruto − depreciação) revela quanto a empresa investe além da reposição, base do teste de crescimento ([P] p. 163–165). Itens contábeis sem caixa (provisões, impairment) voltam ao fluxo ([P] p. 165–166).

## 2. Fórmulas

**FCFF** ([D] p. 341, 353; [P] p. 151)
`FCFF = EBIT(1−t) − (Capex − D&A) − ΔCG não caixa (+ itens sem efeito caixa, como provisões e impairment)`

**Capex líquido ajustado por P&D** ([D] p. 355–357)
`Capex aj. = Capex + P&D corrente`; `D&A aj. = D&A + amortização do ativo de pesquisa`
`Capex líquido aj. = (Capex − D&A) + P&D − amortização`
O ajuste no EBIT(1−t) é **igual** ao ajuste no capex líquido, então **o FCFF não muda**. Muda a medida de lucro e de reinvestimento, e por isso ROC e crescimento ([D] p. 357). Amgen: (438 − 212) + 845 − 398 = **673** ✔.

**Normalização** ([D] p. 353–355)
- Média do capex de 4 a 5 anos **com a D&A do ano corrente**, porque a D&A é mais estável e o benefício fiscal é o atual.
- Ou capex/D&A médio do setor, possivelmente de empresas no mesmo estágio de vida.
- Reliance: média do capex − D&A corrente = 21.666 − 12.784 = **8.882** ✔. *O texto escreve "21,166" (p. 355), mas a média dos 4 anos é 21.666, e só esse valor fecha a conta de 8.882.*

**Aquisições** ([D] p. 357–360): entram no capex, normalizadas (aquisição de 100 a cada 5 anos → ~20 por ano), **pagas em caixa ou em ações**.

**Capital de giro não caixa** ([D] p. 361–363)
`CG não caixa = (ativo circulante − caixa e aplicações) − (passivo circulante − dívida onerosa de curto prazo)`.
Projeção: `ΔCG_t = (CG/Receita) × ΔReceita_t`. Escolhas para a Gap: % da receita corrente (3,44%), % marginal (15,06%), média histórica (4,5%) e média do setor (7,54%) ([D] p. 364–366).

**Investimento líquido** ([P] p. 165)
`Investimento líquido = investimento bruto − depreciação`. No FCFE à Póvoa, ponderado pela fração de capital próprio £ (tema 11).

**Benefício fiscal da depreciação** ([P] p. 164–165): EBITDA 10, D&A 5, IR 30% → LL 3,5 → **LL + D&A = 8,5 = EBITDA − 1,5 de IR**. "O único efeito da depreciação no fluxo de caixa é a geração de um benefício fiscal."

## 3. Premissas e escolhas dos autores

- **Capex irregular** ([D] p. 353–354): normalize pela média histórica ou pela média do setor (capex/D&A). Para empresas com pouca história ou mix de negócios em mudança, use a média do setor.
- **Aquisições no capex** ([D] p. 357–360): Cisco tinha 80% do reinvestimento em aquisições. **Se ignorar as aquisições, ignore também o crescimento que elas trazem** (erro comum: extrapolar o crescimento histórico por aquisições sem projetar o custo delas). Ignorar só é neutro se as aquisições forem a preço justo (VPL zero).
- **Capital de giro sem caixa e sem dívida** ([D] p. 361–362): o caixa rende uma taxa justa e é avaliado à parte. Exceção: caixa operacional necessário (sistema bancário precário). A dívida de curto prazo vai para o WACC.
- **ΔCG negativa** ([D] p. 366–368): é possível por alguns anos (ganho de eficiência), depois volta ao % da receita. Capital de giro **negativo** (Walmart, Dell) pode ser sustentado, mas tem custo (perda de descontos de fornecedor, risco percebido). No longo prazo, não suponha que ele fique cada vez mais negativo.
- **Detalhar ou agregar o CG**: agregar costuma ser mais fácil e preciso, salvo quando os itens se comportam de formas muito diferentes ([D] p. 364).
- **Depreciação pós-IFRS** ([P] p. 165): reflete o desgaste real e pode ter valor residual. A amortização de ágio saiu do balanço societário, mas segue dedutível no fiscal (o benefício continua; não há mais linha a "devolver").
- **Provisões** ([P] p. 166): o aumento de provisão reduz o lucro sem caixa e volta ao fluxo. Só gera benefício fiscal quando a perda se realiza.
- **Impairment** ([P] p. 166): não é caixa e volta ao fluxo.
- **Itens obrigatórios não destinados ao acionista** ([P] p. 135–136): partes beneficiárias e estatutárias (até 10% do lucro para administradores) **reduzem o fluxo**, salvo para um comprador de controle que possa revogá-las. O dividendo mínimo obrigatório (25%) **não** reduz o fluxo, porque volta ao acionista.

## 4. Passo a passo prático

1. Capex histórico de 5 anos, mais aquisições (caixa e ações), mais P&D capitalizado (se adotado).
2. D&A do ano corrente, mais a amortização do ativo de pesquisa.
3. Capex líquido normalizado = capex médio − D&A corrente, ou capex/D&A do setor × D&A.
4. CG não caixa histórico como % da receita (corrente, marginal, média, setor). Escolha e justifique.
5. Projete o ΔCG = % × ΔReceita. Se houver ganho de eficiência, convirja para o % alvo em 3 a 5 anos.
6. Some as provisões e o impairment ao fluxo. Subtraia as participações estatutárias.
7. **Checagem cruzada**: reinvestimento/EBIT(1−t) = taxa de reinvestimento, coerente com g/ROC (tema 15).

## 5. Erros comuns apontados pelos autores

- **Usar o capex de um único ano** (alto ou baixo demais) ([D] p. 353–354).
- **Normalizar o capex e também a D&A** quando a D&A não é volátil ([D] p. 354).
- **Extrapolar o crescimento de aquisições sem projetar aquisições** ([D] p. 360).
- **Incluir caixa e dívida de curto prazo no capital de giro** ([D] p. 361–362).
- **Projetar a variação de CG do último ano crescendo com o lucro** (é volátil demais) ([D] p. 365).
- **ΔCG negativa perpétua** ([D] p. 366–368).
- **Achar que a depreciação "é caixa" em si mesma**: ela vale só pelo benefício fiscal ([P] p. 164–165).
- **Esquecer as partes estatutárias** ([P] p. 135).

## 6. Onde concordam e onde divergem

**Concordam**: investimento líquido = bruto − D&A; ΔCG ligado à receita; itens sem caixa voltam ao fluxo.

| Ponto | Damodaran | Póvoa |
|---|---|---|
| Aquisições | Entram no capex (caixa e ações) (p. 357–360) | Não trata nesse capítulo |
| P&D e marketing | Capitaliza (FCFF igual, ROC e g diferentes) (p. 355–357) | Despesa; reflete no crescimento (Cap. 4, p. 102) |
| Normalização do capex | Média ou setor (p. 353–355) | Investimento a partir do plano da empresa e do histórico (p. 171) |
| Partes estatutárias | Não trata | Reduzem o fluxo (p. 135) |

## 7. Limites: o que está defasado ou é específico do Brasil

- **IFRS 16**: arrendamentos no balanço. Os pagamentos de arrendamento deixam de ser despesa operacional e viram amortização e juros. É preciso decidir se o "capex" inclui os novos direitos de uso (tema 07). *Não está nos livros.*
- **Partes beneficiárias** foram extintas para companhias abertas, mas as **participações estatutárias** de administradores continuam ([P] p. 135).
- Exemplos (Gap, Reliance, Cisco) de 1999–2000.

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. Capex de partida = **média de 5 anos** do capex mais aquisições, comparada com capex/D&A do setor.
2. CG não caixa como **% da receita**, com o percentual escolhido justificado (média de 3 a 5 anos, por padrão).
3. **Linha separada para aquisições** em empresas consolidadoras, coerente com o crescimento projetado.
4. Participações estatutárias e de empregados (PLR acima do usual) **dentro** do fluxo.
5. Mostrar a **taxa de reinvestimento** e o **ROC implícito** em cada ano (tema 14).

## 9. Dúvidas abertas para você decidir

1. Capitalizar P&D e marketing (Damodaran) nas empresas em que são relevantes, ou manter como despesa (Póvoa)?
2. Tratar o direito de uso do IFRS 16 como capex?
3. Janela de normalização: 3 ou 5 anos?
