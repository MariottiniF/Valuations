# Fichamento 02: Abordagens (DCF, valuation relativa, opções/contingent claims): quando usar cada uma

**Fontes**
- **[D]** Damodaran (2002), Cap. 2 "Approaches to Valuation": DCF (equity, firma, APV; fluxo total × excesso de retorno; limites), valuation relativa, modelos baseados em ativos e contingent claims (PDF p. 16–34).
- **[P]** Póvoa (2012), Cap. 1, escolas e análise fundamentalista (p. 4–10). Cap. 4, mitos do FCD, simplicidade e casos complicados (p. 96–99, 125–129). Cap. 9 para múltiplos (tema 33). Cap. 11 para opções reais (tema 47).

---

## 1. Conceito central

Há três abordagens ([D] p. 16): (1) **DCF**, o valor presente dos fluxos esperados à taxa do risco; (2) **valuation relativa**, o preço de "comparáveis" padronizado por uma variável (lucro, VP, receita); (3) **contingent claims**, modelos de opções para ativos com payoff contingente (patentes, reservas, equity de empresa em dificuldade). Damodaran argumenta que o **DCF é a base de todas**: fazer múltiplos direito exige entender os fundamentos do DCF, e opções começam de um DCF ([D] p. 16). Póvoa considera o FCD "o mais completo" e afirma que múltiplos bem feitos embutem as mesmas variáveis ([P] p. 96–97).

## 2. Fórmulas

**DCF** ([D] p. 17): `Valor = Σ CF_t/(1+r)^t`
- Equity: `Σ CF_equity/(1+Ke)^t` (o DDM é caso particular) ([D] p. 18–19).
- Firma: `Σ CF_firma/(1+WACC)^t` ([D] p. 19).
- **APV**: `Valor = firma 100% equity + VP benefícios fiscais − custo esperado de falência` ([D] p. 19). *O livro imprime "+ Expected Bankruptcy Costs" na p. 19. O sinal correto é **menos**, como o Cap. 15 deixa claro (p. 565).*

**Descasamento de fluxo e taxa** ([D] p. 19–21): FCFE a WACC **superestima** o equity (+175 no exemplo); FCFF a Ke **subestima** a firma (−260).

**Excesso de retorno** ([D] p. 22): `Valor = capital investido + VP(excesso de retorno)`. Exemplo: investimento de 100, fluxo de 12 perpétuo e custo de 10% → 12/0,10 = 120 = 100 + (12 − 10)/0,10 ✔. Base do EVA (tema 42).

## 3. Premissas e escolhas dos autores

- **Valor intrínseco** ([D] p. 17–18): o valor que um analista "onisciente" atribuiria. Supõe que os preços se desviam do valor e **convergem** com o tempo.
- **Três caminhos no DCF** (equity, firma e APV) dão o mesmo valor com hipóteses consistentes ([D] p. 19).
- **Teste simples** ([D] p. 21): fluxo depois de juros e principal é equity (Ke); antes deles, é firma (WACC).
- **Onde o DCF "sofre"** ([D] p. 22–25; [P] p. 125–129): empresas em dificuldade, cíclicas, com ativos não utilizados, com patentes ou opções de produto, em reestruturação, em aquisições (sinergia, controle) e fechadas (risco). Todos têm adaptação possível: o desafio é estender o arcabouço, não abandoná-lo.
- **Valuation relativa** ([D] p. 25–30):
  - Supõe que o mercado acerta **na média** e erra em ações individuais, e que essas correções são mais rápidas ([D] p. 26).
  - Duas vertentes: múltiplos **derivados de fundamentos** (equivalentes ao DCF) × **comparáveis** (cross-section ou série histórica).
  - Fácil de manipular: a escolha dos comparáveis muda a média. No exemplo de software de 1992, o P/L médio de 24 vira 27 tirando as duas menores ([D] p. 28–29).
  - Herda os **erros do mercado**: se o setor inteiro estiver caro, a avaliação fica cara ([D] p. 30).
- **Modelos baseados em ativos** (liquidação, custo de reposição) não são uma quarta abordagem, porque dependem das outras para estimar os valores ([D] p. 30).
- **Contingent claims** ([D] p. 30–33): o DCF subestima ativos com payoff contingente (reserva não desenvolvida). Limitações: em opções longas sobre ativos não negociados, variância e valor do ativo têm de ser estimados, com erro grande.
- **Póvoa** ([P] p. 4–10): a escola fundamentalista busca o valor intrínseco a partir de fundamentos macro, setoriais e da empresa; a escola gráfica e técnica é auxiliar (efeito manada). Top-down e bottom-up são complementares.

## 4. Passo a passo prático (escolha da abordagem)

1. **Padrão: DCF de FCFF** para empresas não financeiras com fluxos estimáveis.
2. **Bancos e seguradoras**: FCFE, DDM ou excesso de retorno (tema 44).
3. **Checagem cruzada obrigatória**: múltiplos de comparáveis e o "múltiplo justo" derivado do DCF (temas 33 a 35).
4. **Ativos com opcionalidade relevante** (reservas não desenvolvidas, patentes, licenças): avaliar à parte, com cenários ou opções reais, e somar (tema 47).
5. **Vida finita** (concessões): DCF com liquidação ou valor residual no fim (tema 29).

## 5. Erros comuns apontados pelos autores

- **Descasar fluxo e taxa** ([D] p. 19–21).
- **Escolher comparáveis para confirmar um viés** ([D] p. 28–29).
- **Usar múltiplos como "atalho" sem entender os fundamentos** ([D] p. 16; [P] p. 97).
- **Abandonar o DCF em empresas difíceis** em vez de adaptá-lo ([D] p. 25).

## 6. Onde concordam e onde divergem

**Concordam**: o DCF é a abordagem mais completa; múltiplos dependem dos mesmos fundamentos; opções para casos específicos.

| Ponto | Damodaran | Póvoa |
|---|---|---|
| Taxonomia | DCF, relativa e contingent claims (p. 16) | Escola gráfica × fundamentalista; top-down × bottom-up (Cap. 1) |
| Excesso de retorno | Modelo equivalente ao DCF (base do EVA) (p. 22) | EVA no Cap. 10 (tema 42) |
| Valuation relativa | Mercado certo na média, errado no individual (p. 26) | "Uso indiscriminado dos múltiplos" (título do Cap. 9) |

## 7. Limites: o que está defasado ou é específico do Brasil

- Os exemplos (software em 1992) estão datados.
- No Brasil, a escassez de comparáveis listados por setor dificulta a valuation relativa e o bottom-up beta. Muitas vezes é preciso recorrer a pares globais (tema 20).

## 8. Aplicação ao canal (sugestões para a `METODOLOGIA.md`)

1. **Hierarquia**: (1) DCF de FCFF como método principal; (2) múltiplos como checagem e "o que o preço implica"; (3) opções e cenários para ativos contingentes.
2. **Regra de comunicação**: o vídeo apresenta o DCF e mostra os múltiplos implícitos no preço justo contra os do setor.
3. **Tabela de decisão por tipo de empresa** (não financeira madura, crescimento, cíclica, financeira, concessão, holding) com a abordagem recomendada.

## 9. Dúvidas abertas para você decidir

1. Usar o modelo de excesso de retorno (EVA) como apresentação alternativa em algum caso?
2. Incluir opções reais nos vídeos ou só no material de apoio?
