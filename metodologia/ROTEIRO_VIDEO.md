# Regras para roteiros de vídeo

Valem para todo roteiro feito a partir de um valuation do canal. Decidido em 31/10/2026.

## 1. Nada de códigos internos na fala

As falas **não citam** os códigos das decisões e regras (D1 a D12, C1 a C3), nem números de tema ou fichamento. Cada escolha é explicada pelo **porquê**, em linguagem de vídeo. O espectador não conhece o `DECISOES.md`; o que convence é a razão, não o número da regra.

- Errado: "Pela D2, o arrendamento é dívida."
- Certo: "Trato o arrendamento como dívida porque alugar um caminhão por cinco anos é, na prática, financiar a compra dele."

A regra vale também para gráficos e tabelas que aparecem na tela. Os códigos só podem aparecer nas notas de produção do roteiro (ficha técnica, "antes de gravar"), que não vão ao ar.

## 2. Debt e Equity por extenso

Nunca usar "D", "E", "D/E" ou "D/(D+E)", nem na fala nem na tela. Escrever **Debt**, **Equity**, **Debt/Equity** e **Debt / (Debt + Equity)**. Na fala: "a relação Debt sobre Equity".

## 3. Como explicar cada decisão sem citar o código

| Código | Explicação para usar na fala |
|---|---|
| D1 (caixa fora do EV) | O caixa parado não roda a operação; ele é somado só no fim, na passagem do valor da empresa para o valor da ação. Pelo mesmo motivo, fica fora do Debt usado no WACC |
| D2 (IFRS 16) | Alugar um ativo por anos é, na prática, financiar a compra dele; por isso o arrendamento entra como dívida, e o EBITDA usado é o pós-IFRS 16, para não contar o aluguel duas vezes |
| D3 (perpetuidade) | No longo prazo, retorno acima do custo de capital atrai concorrentes que derrubam o retorno, e nenhuma empresa cresce para sempre acima da economia; por isso ROIC = WACC e crescimento igual ao da economia |
| D3a (ROIC > WACC) | Só aceito retorno acima do custo para sempre quando a empresa tem uma vantagem que dá para nomear (marca, rede, licença, custo) e histórico de vários anos de ROIC acima do WACC |
| D4 (taxa livre de risco) | O valor de uma empresa vem de fluxos de décadas, então a referência é o título público mais longo disponível, o mesmo para toda a projeção |
| D5 (prêmio de risco) | O prêmio implícito de um trimestre oscila muito; o valor da empresa depende de décadas, então uso um prêmio de longo prazo e mostro o do trimestre como checagem |
| D6 (JCP) | O JCP é economia de imposto da empresa, não mudança no risco do acionista; por isso entra no fluxo de caixa, não na taxa de desconto |
| D8 (cíclicas) | Empresa cujo resultado sobe e desce com o ciclo é avaliada pela média de um ciclo inteiro, não pelo ano atual |
| D9 (múltiplos) | Múltiplo diz quanto o mercado paga por empresas parecidas, não quanto a empresa vale; serve de checagem, e nunca faço média entre DCF e múltiplos, porque a média esconde as premissas |
| D11 (WACC único) | Uso um só WACC do começo ao fim; fazer a taxa cair com o tempo é apostar numa melhora que a empresa não prometeu |
| D12 (pesos do WACC) | Os pesos de Debt e Equity são os de hoje, a mercado, a menos que a própria empresa divulgue uma meta concreta, com prazo, de mudar bastante a alavancagem; nesse caso, o WACC acompanha o plano divulgado |
| C2 (reinvestimento = g/ROIC) | Crescimento não sai de graça: quanto menor o retorno do capital novo, mais a empresa precisa investir para crescer o mesmo |
| C3 (tese de divergência) | Quando o preço justo fica mais de 30% longe do mercado, a diferença pode ser erro meu, então sou eu que preciso explicar por que o mercado estaria errado |

## 4. Formato das cenas

Cada cena numerada traz: (a) a fala, em tom de conversa e frases curtas; (b) o tipo da cena: "dados", "contexto" ou "mista"; (c) o gráfico ou tabela na tela, com nome do arquivo, ou "nenhum"; (d) a imagem de apoio, com descrição em português e prompt em inglês para o gerador de imagem, em estilo ilustração limpa e escura, 16:9; (e) a duração estimada.

Imagens de apoio: sem texto, números, logotipos, marcas ou rostos de pessoas reais. Sugerem o tema de forma sutil. Nas cenas de dados, a imagem é discreta, para funcionar como fundo do gráfico.
