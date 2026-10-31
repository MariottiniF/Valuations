# Fichamento 38: Macro e valor: efeito de juros, câmbio e inflação nas projeções

**Fontes**
- **[D]** Damodaran (2002), Cap. 7, consistência de moeda na taxa livre de risco, real × nominal (PDF p. 212–214); Cap. 12, valor terminal: valuation nominal × real e moeda como limites do crescimento estável (p. 429). Temas 18 (Rf), 26 (receita no exterior) e 29 (valor terminal) já tratam dos detalhes.
- **[P]** Póvoa (2012), Cap. 10 "Tópicos em valuation": "O efeito dos juros no valor das companhias" (p. 365–368); "O efeito do câmbio" (p. 368–374); "O efeito da inflação" (p. 374–379).

---

## 1. Conceito central

Juros, câmbio e inflação afetam o valor por **três canais ao mesmo tempo**: o fluxo de caixa (receitas, custos, margens, dívida), a taxa de crescimento e a taxa de desconto ([P] p. 374). Por isso, os "mitos" de mercado que ligam uma variável macro diretamente à bolsa ("juro sobe, bolsa cai"; "desvalorização sempre sobe ações em reais"; "inflação é boa para a bolsa") não se sustentam como regra ([P] p. 365–368, 374). Do lado técnico, Damodaran insiste na **consistência**: fluxo e taxa na mesma moeda e no mesmo regime (nominal com nominal, real com real), e um crescimento estável que respeite a inflação da moeda usada ([D] Cap. 7, p. 213–214; Cap. 12, p. 429).

## 2. Fórmulas

- **Taxa nominal** ([D] Cap. 12, p. 429): `Rf nominal ≈ Rf real + inflação esperada` (Fisher; versão exata: (1 + real)(1 + inflação) − 1).
- **Crescimento estável** ([D] p. 429): em moeda de inflação alta, o g estável **inclui** a inflação; em valuation real, o g é real.
- **Paridade entre moedas**: com fluxos em R$ e em US$, o diferencial de inflação deve aparecer na taxa (ver tema 26; [D] Cap. 7, p. 213).

## 3. Premissas e escolhas dos autores

**Juros** ([P] p. 365–368)
- O que importa para os fluxos é o **juro longo**, que reflete as expectativas sobre a política monetária, não a Selic do dia (p. 366).
- Um corte de juros "forçado" pode **empinar a curva** (juros longos sobem com medo de inflação) e reduzir o valor (p. 366).
- Em estudo do autor, a correlação "juro sobe, bolsa cai" se confirmou em poucos ciclos (p. 367). Só **surpresas** de política monetária movem preços de forma consistente; um BC "atrás da curva" eleva os juros longos (p. 367).

**Câmbio** ([P] p. 368–374)
- O efeito depende da estrutura da empresa: receitas, custos e dívida em moeda estrangeira, e do hedge (p. 368–369).
- **Derivativos**: Aracruz e Sadia "quebraram" em 2008 com posições cambiais muito maiores que o hedge necessário (p. 369).
- Efeitos macro de valorização ou desvalorização excessiva: exportações, importados nas margens, atividade (p. 369–370).
- Três episódios analisados (p. 372–373): fim do câmbio controlado (1999), eleição de 2002 (BC "atrás da curva") e valorização de 2004–2008 (com commodities em alta compensando o câmbio).
- **Conclusão** (p. 374): é falso que variações cambiais tenham efeito direto na bolsa; atuam por fluxo, crescimento e taxa.

**Inflação** ([P] p. 374–379)
- **Tese "positiva"** (p. 374–375): ações como ativo real, abrigo contra a inflação.
- **Tese "negativa"** (p. 375–377): ilusão de valores nominais; margens que crescem "de mentira" quando os preços sobem e os custos de reposição vêm depois (exemplo de 2011–2012, p. 376–377); depreciação a custo histórico subestimada; IR sobre lucro inflacionário; Ke nominal maior.
- **Conclusão** (p. 377): fluxo menor e taxa maior **destroem valor**. Inflação alta tende a ser negativa.

**Consistência** ([D] Cap. 7, p. 213–214)
- Com inflação alta e instável, a valuation **real** pode ser mais confiável (p. 214).
- Valuations em moedas diferentes dão o mesmo valor se a paridade de poder de compra valer (p. 213).

## 4. Passo a passo prático

1. **Moeda e regime**: canal em R$ nominal (padrão), com cenário macro explícito (IPCA, Selic, câmbio, PIB) por ano da projeção.
2. **Fluxos**: indexar receitas e custos conforme o contrato (IPCA, IGP-M, dólar, commodity). Separar parte dolarizada × parte em reais.
3. **Taxa**: Rf da curva NTN-B mais a inflação implícita ou o DI longo, coerente com o IPCA do cenário (tema 18).
4. **Dívida em moeda estrangeira**: projetar o principal e os juros com o câmbio do cenário, independentemente da contabilidade (tema 07).
5. **g perpétuo** em R$ nominal ≤ inflação de longo prazo + crescimento real da economia (tema 29).
6. **Sensibilidade**: câmbio ±20% e juros longos ±200 pb (tema 32).

## 5. Erros comuns apontados pelos autores

- **Mitos macro** de efeito direto ([P] p. 365, 368, 374).
- **Misturar fluxo nominal com taxa real** (ou o contrário) ([D] Cap. 12, p. 429).
- **Fluxo em reais com taxa em dólar** sem ajuste de inflação ([D] Cap. 7, p. 213).
- **Confundir margem nominal com real** em inflação alta ([P] p. 376–377).
- **Hedge que vira especulação** ([P] p. 369).

## 6. Onde concordam e onde divergem

**Concordam** (implicitamente): a macro age pelos componentes do DCF; consistência entre moeda e inflação.

| Ponto | Damodaran | Póvoa |
|---|---|---|
| Enfoque | Técnico: consistência de taxa, moeda e g | Empírico e histórico: mitos, episódios brasileiros |
| Inflação | Real × nominal; real em inflação alta | Efeitos reais em margens, depreciação, IR |
| Câmbio | Paridade entre moedas | Exposição, hedge, derivativos (2008) |

## 7. Limites: o que está defasado ou é específico do Brasil

- Episódios de [P] vão até 2012. Os ciclos posteriores (Selic de 2% em 2020 e de dois dígitos em 2022–2025) não estão no livro **[NÃO VERIFICADO aqui]**.
- No Brasil, contratos indexados ao IGP-M (aluguéis, energia antiga) e ao IPCA (concessões) exigem projeção dos dois índices.

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. **Cenário macro único do canal**, revisado periodicamente e usado em todas as empresas (fonte sugerida: Boletim Focus e curva de juros).
2. Valuation em **R$ nominal**; taxa e g coerentes com o IPCA do cenário.
3. Mapa de exposição por empresa: % da receita, custo e dívida em moeda estrangeira.
4. Sensibilidade padrão a câmbio e juros longos.

## 9. Dúvidas abertas para você decidir

1. Fonte do cenário macro (Focus, cenário próprio ou de um banco)?
2. Frequência de revisão do cenário.
3. Valuation real para algum setor (por exemplo, concessões indexadas ao IPCA)?
