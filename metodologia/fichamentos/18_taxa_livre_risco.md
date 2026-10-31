# Fichamento 18: Taxa livre de risco

**Fontes**
- **[D]** Damodaran, *Investment Valuation*, 2ª ed. (2002), Cap. 7 "Riskless Rates and Risk Premiums", seção "The Risk Free Rate" (PDF p. 211–216) e conclusão (p. 243). Uso também o Cap. 8, Ilustração 8.9 (p. 281–283), sobre a conversão de moeda.
- **[P]** Póvoa, *Valuation: Como Precificar Ações* (2012), Cap. 6: "Regras básicas" (p. 179–180), "Ativo livre de risco, será que isso existe?" (p. 186–193), "Taxa de desconto para o acionista na teoria e na prática" (p. 212–216), "Taxa de desconto pré-perpetuidade" (p. 217–220), "Taxa de desconto na fase da perpetuidade" (p. 220–227) e "Transformação do retorno do ativo livre de risco em dólares para uma taxa em reais" (p. 227–229).

Páginas de [D] são as do PDF. Páginas de [P] são as impressas.

---

## 1. Conceito central

A taxa livre de risco é a base de todo modelo de risco e retorno. O ativo que a define precisa ter retorno efetivo **igual ao esperado**. Para isso, não pode haver **risco de default** nem **risco de reinvestimento** ([D] p. 211–212). Póvoa acrescenta uma terceira condição, a ausência de risco de oscilação da taxa de juros, mas reconhece que ela é inútil na prática: um título pós-fixado não informa a taxa para descontar o fluxo ([P] p. 186–188). Na prática, os dois autores usam o **título público longo na mesma moeda e no mesmo regime (nominal ou real) do fluxo de caixa**. Para o investidor brasileiro em reais, Póvoa escolhe a **NTN-B** ([P] p. 191).

## 2. Fórmulas

**Paridade de juros (taxa local a partir do câmbio a termo)** ([D] p. 215–216)
`Forward_t = Spot × [(1 + i_local) / (1 + i_US$)]^t`
O exemplo da Tailândia (spot 38,10; forward de 10 anos 61,36; Treasury 5%) dá i_baht = 10,12% a.a. ✔ (recalculado).

**Taxa local quando o próprio governo tem risco de default** ([D] p. 216)
`Rf local = taxa do título do governo em moeda local − spread de default do rating soberano`. Exemplo: Índia 12% − 2% (rating A) = 10%.

**Conversão de um custo em dólar para moeda local pelo diferencial de inflação** ([D] p. 232, 282)
`K_local = (1 + K_US$) × (1 + π_local)/(1 + π_US) − 1`

**Rf nominal em reais a partir da NTN-B** ([P] p. 185, 191)
`Rf ≈ IPCA esperado de longo prazo + cupom real da NTN-B` (Póvoa soma em vez de compor). Exemplo: 4,5% + 5,8% = 10,3% a.a. (início de 2012).

**Rf em dólares para ativo brasileiro** ([P] p. 192–193, 212)
`Rf US$ Brasil = Treasury 10 anos + risco-Brasil (EMBI)`. Exemplo: 2,3% + 1,6% = 3,9% a.a. no fim de 2011.

## 3. Premissas e escolhas dos autores

- **Princípio da consistência**. A moeda e o regime (nominal ou real) da taxa livre de risco vêm da moeda e do regime do **fluxo de caixa**, não do país-sede da empresa ([D] p. 213; [P] p. 179–180). Póvoa estende a regra a firma × firma e acionista × acionista: FCFF com WACC, FCFE com Ke ([P] p. 180).
- **Duração.** O purista usaria uma taxa zero cupom para cada ano. O compromisso prático é casar a duração do título com a duração dos fluxos; em valuation de empresa, que dura para sempre, isso leva ao título longo ([D] p. 212–213, nota 2). Se a curva for muito inclinada, vale usar taxas por ano ([D] p. 212).
- **Taxa real.** Damodaran aponta os títulos indexados à inflação como fonte da taxa real. Onde eles não existem, há dois argumentos: (i) com capital livre, a taxa real é igual em todos os países; (ii) com atrito, a taxa real de longo prazo tende ao crescimento real de longo prazo da economia ([D] p. 214–215).
- **Mercados sem ativo livre de default.** Damodaran propõe três saídas: a taxa das maiores e mais seguras empresas locais menos ~0,5% (nota 3), a paridade de juros com o câmbio a termo, ou o título do governo menos o spread de default ([D] p. 215–216).
- **Escolha de título no Brasil** ([P] p. 188–191):
  - LFT: ideal na teoria (bullet e pós), mas não fornece taxa, então é descartada.
  - LTN: prazo curto (menos de 10 anos).
  - NTN-F: tem risco de reinvestimento e carrega **prêmio de prefixação**. Em 2011 rendia ~1,2 p.p. acima da NTN-B de prazo parecido ([P] p. 189–190).
  - NTN-C (IGP-M): pouco líquida e sem emissão desde 2006.
  - **NTN-B (IPCA + cupom): a escolhida.** O prêmio de carregamento é menor e a meta de inflação torna a expectativa de IPCA mais estável ([P] p. 190–191).
- **Prazo da NTN-B** ([P] p. 191). (A), a mais usada: uma só taxa, a NTN-B mais longa. (B), a preferida do autor: uma NTN-B com vencimento igual ao número de anos do período explícito e outra taxa, ajustada com parcimônia, para a perpetuidade.
- **Sem "escadinha" no Rf.** A taxa longa já é uma média das taxas curtas esperadas. Projetar queda de juros sobre ela é contar a mesma coisa duas vezes ([P] p. 217–219; exemplo do DI jan/14, p. 217).
- **Perpetuidade.** Não existe proxy de mercado para o "risco perpétuo". Póvoa admite ajuste de Rf e de prêmio na perpetuidade dentro de **±1 a 2 p.p.** em relação ao último ano explícito ([P] p. 220–227). O ajuste pode ser para cima: nos EUA de 2011, com Treasury a 1,8% e juro real negativo, ele sugere ~4% na perpetuidade (p. 224–226).
- **Investidor local × estrangeiro.** O estrangeiro vê como ativo livre de risco o título soberano emitido lá fora (Treasury + EMBI). O brasileiro vê a NTN-B. A diferença (~3,6 p.p. em 2012) vem do **"risco-fronteira"**: internalizar recursos numa moeda não conversível ([P] p. 213–215, 227–228).

## 4. Passo a passo prático

1. Defina a **moeda** (R$ ou US$) e o **regime** (nominal ou real) do fluxo de caixa ([D] p. 213; [P] p. 179).
2. Fluxo nominal em R$: pegue o **cupom real da NTN-B** e some (ou componha) a **expectativa de IPCA de longo prazo** ([P] p. 191).
   - Período explícito: NTN-B com vencimento próximo ao fim da projeção. Ou, na alternativa simples, a NTN-B mais longa ([P] p. 191).
   - Perpetuidade: parta da NTN-B mais longa e ajuste no máximo 1 a 2 p.p. se a taxa corrente parecer fora do equilíbrio ([P] p. 220–227).
3. Fluxo em US$: use a Treasury de 10 anos ([P] p. 192) ou o T-bond longo ([D] p. 213) **+ risco-país**, se o investidor relevante for estrangeiro.
4. **Não converta** Rf em US$ para R$ pelo diferencial de inflação e depois use essa taxa para o investidor local ([P] p. 227–229, ver seção 5).
5. Se precisar converter o custo de capital **inteiro** entre moedas, use o diferencial de inflação de forma multiplicativa ([D] p. 232, 282).
6. **Não faça "escadinha"** no Rf do período explícito ([P] p. 217–220).

## 5. Erros comuns apontados pelos autores

- **Usar a T-bill (curta) para descontar fluxos longos**, por causa do risco de reinvestimento ([D] p. 212, 243).
- **Usar taxa e fluxo em moedas ou regimes diferentes**, por exemplo fluxo em reais com Rf em dólar ([D] p. 213; [P] p. 179–180).
- **Usar como Rf um título soberano em dólar que já embute spread de default** (o C-Bond brasileiro, no exemplo) **e somar risco-país no prêmio**. É dupla contagem, piorada se o analista também aumenta o beta ou corta o fluxo (*haircut*) ([D] p. 229).
- **"Escadinha" decrescente no Rf** por convicção de que os juros vão cair ([P] p. 217).
- **Usar a NTN-B de 5 anos como taxa única de todo o fluxo, perpetuidade incluída** ([P] p. 224).
- **Fazer `Rf R$ = (Treasury + EMBI) + diferencial de inflação`** para o investidor local. Isso ignora o risco-fronteira e gera uma "taxa média" entre investidores que não existe. Em 2012 dava 6,6% contra 10,2% da NTN-B ([P] p. 227–229).
- **Tratar o soberano como livre de default em qualquer circunstância.** Contraexemplos: as LFTs com deságio em 2002 e o rebaixamento dos EUA em 2011 ([P] p. 186–188).

## 6. Onde concordam e onde divergem

**Concordam**
- O título público longo é a melhor aproximação ([D] p. 213; [P] p. 191–192).
- A consistência entre moeda e inflação do fluxo e da taxa é inegociável ([D] p. 213–214; [P] p. 179–180).

**Divergem ou se complementam**
| Ponto | Damodaran | Póvoa |
|---|---|---|
| Título de referência | T-bond longo dos EUA, sem detalhar o Brasil | NTN-B, com a análise de cada título público brasileiro (p. 188–191) |
| Rf ao longo do tempo | Pode haver taxa por ano se a curva for muito inclinada (p. 212) | Período explícito sem escadinha; ajuste só na perpetuidade (p. 217–227) |
| Investidor relevante | O marginal, com o risco-país no prêmio (Cap. 7) | Cada investidor tem seu Rf: local (NTN-B) × estrangeiro (Treasury + EMBI) (p. 213–216) |
| Conversão de moeda | Converte o **custo de capital** pelo diferencial de inflação (p. 232, 282) | Critica a conversão do **Rf** para o investidor local por causa do risco-fronteira (p. 227–229) |

*Nota:* as duas conversões não se contradizem por completo. Damodaran converte o custo de capital de um investidor que é **o mesmo** nas duas moedas. Póvoa critica usar o Rf do estrangeiro como se fosse o do brasileiro.

## 7. Limites: o que está defasado ou é específico do Brasil

- **Números**: Treasury de 5% e títulos da Tailândia e da Índia ([D], 2000–2001); NTN-B a IPCA + 5,5–5,9% e IPCA de 4,5% ([P], 2011–2012). **São todos ilustrativos e estão vencidos.** Use o `MACRO.md`.
- **Inconsistência interna em [P]**: a NTN-B 2050 aparece a IPCA + 5,8% (p. 185, p. 222), IPCA + 5,9% (p. 191, onde a conta usa 5,8%) e IPCA + 5,6% (p. 221). Parecem ser datas ou cotações diferentes, mas o texto não diz.
- **Meta de inflação**: Póvoa usa 4,5% (a meta de 2012). A meta vigente é outra e precisa ser conferida **[NÃO VERIFICADO aqui]**.
- **Prazos da NTN-B**: os vencimentos disponíveis mudaram desde 2012. Confira a curva atual.
- **EMBI e grau de investimento**: Póvoa escreve depois do grau de investimento de 2008, que o Brasil depois perdeu. Isso não está nos livros; confira o rating soberano atual **[NÃO VERIFICADO aqui]**.

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. **Moeda-base: R$ nominal**, com o investidor marginal local. Rf = cupom real da NTN-B + IPCA esperado de longo prazo (do `MACRO.md`).
2. **Composição, não soma**: `Rf = (1 + cupom real) × (1 + IPCA) − 1`. Póvoa soma; a diferença é pequena, mas a composição é a forma correta.
3. **Período explícito**: NTN-B com vencimento próximo ao fim da projeção (alternativa B de Póvoa). Registrar o vencimento e a data da cotação.
4. **Perpetuidade**: NTN-B mais longa. Qualquer ajuste fica limitado a ±1 p.p. e é justificado por escrito.
5. **Nunca** "escadinha" no Rf. **Nunca** Rf em US$ + diferencial de inflação para o investidor local.
6. Se fizer valuation em US$ (por exemplo, para comparar com pares globais), monte a taxa inteira em US$ e converta o resultado, nunca só o Rf.

## 9. Dúvidas abertas para você decidir

1. Uma taxa única (NTN-B mais longa) ou duas taxas (explícito × perpetuidade)?
2. Fonte e data padrão da expectativa de IPCA de longo prazo: Focus, meta ou inflação implícita (NTN-F × NTN-B)?
3. O canal vai publicar alguma valuation em US$? Se sim, qual a fonte do risco-país?
4. Aceita o ajuste de perpetuidade de Póvoa (até ±2 p.p.) ou prefere zero de ajuste por transparência?
