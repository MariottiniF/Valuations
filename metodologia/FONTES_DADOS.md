# Fontes de dados: como buscar os parâmetros em cada valuation

Este procedimento diz **onde buscar** cada parâmetro numérico usado no WACC e no cenário macro ([`PROCEDIMENTO_WACC.md`](PROCEDIMENTO_WACC.md), [`DECISOES.md`](DECISOES.md)), **como pedir a busca** e **o que registrar**. Ele existe para que nenhum parâmetro entre na planilha "de memória": todo número tem uma fonte, uma data e um link, verificáveis por qualquer pessoa que leia o material do vídeo.

## Princípio geral

1. **Nunca usar um número de treinamento do modelo sem confirmar.** Taxas de juros, prêmios de risco, alíquotas e tabelas de Damodaran mudam com frequência; o que "parece certo" pode estar desatualizado em meses ou anos.
2. **Buscar no momento da valuation**, não reaproveitar um número antigo sem checar a data.
3. **Registrar sempre**: valor, data de referência, fonte (nome + link). Esse registro vai num bloco **"Fontes de dados"** no fim de cada relatório/planilha, no mesmo padrão dos "Fontes" dos fichamentos.
4. **Dois níveis de atualização**:
   - **Cenário macro do canal** (C1): revisão **trimestral**, guardada em [`MACRO.md`](MACRO.md) (modelo na seção 5 abaixo). Todas as valuations do trimestre usam os mesmos números.
   - **Parâmetros específicos da empresa** (beta do setor, spread de crédito, CRP do país): buscados **a cada valuation**, porque podem mudar entre uma empresa e outra mesmo no mesmo trimestre (setor, rating, país).
5. **Se a fonte primária não responder ou não existir**: usar a fonte alternativa listada; se nenhuma responder, marcar o campo como `[NÃO VERIFICADO — fonte indisponível em <data>]` e seguir com o último valor confiável conhecido, destacando no vídeo que é uma estimativa.

## Como pedir a busca (para quem está operando o Claude)

Ao montar uma valuation, peça explicitamente a atualização dos parâmetros, por exemplo:

> "Antes de montar o WACC, busque a NTN-B atual, o IPCA esperado de longo prazo do Focus e o prêmio implícito do Ibovespa. Registre fonte e data."

O Claude deve usar busca na web (WebSearch) para localizar a página atual e, quando precisar abrir um link específico (uma tabela do Tesouro Direto, uma página do Damodaran Online), usar WebFetch sobre o link encontrado. Arquivos `.xls`/`.xlsx` (comuns no site de Damodaran) às vezes não podem ser lidos diretamente; nesse caso, buscar o valor citado em alguma página ou notícia que o reproduza, ou pedir para a pessoa baixar e anexar o arquivo.

---

## 1. Parâmetros do Brasil

| Parâmetro | Fonte primária | Como buscar | Fonte alternativa |
|---|---|---|---|
| **NTN-B (taxa real)** | Tesouro Transparente / Tesouro Direto — "Preços e Taxas dos Títulos Públicos" | Buscar "Tesouro Direto NTN-B taxa hoje" e abrir a tabela de preços e taxas do dia | ANBIMA — "Estrutura a Termo de Taxas de Juros" (ETTJ) |
| **IPCA esperado (curto e longo prazo)** | Banco Central — Boletim Focus (relatório semanal de expectativas de mercado) | Buscar "Boletim Focus Banco Central IPCA expectativas" e localizar a mediana para os próximos anos e para "longo prazo" (acima de 5 anos) | FGV IBRE (projeções de inflação) |
| **PIB real potencial (longo prazo)** | Banco Central — Boletim Focus (seção de PIB) | Buscar "Boletim Focus PIB longo prazo" | FMI — World Economic Outlook (crescimento potencial do Brasil); IFI/Senado |
| **Selic / DI (curva de juros)** | B3 — curva de DI futuro | Buscar "curva DI futuro B3 hoje" | Banco Central — Copom (meta Selic) |
| **Câmbio (PTAX)** | Banco Central — cotação PTAX | Buscar "PTAX hoje Banco Central" | B3 — dólar futuro |
| **Prêmio implícito do Ibovespa (ERP Brasil)** | **Calculado pelo canal**, não é um dado pronto (ver fichamento 19 e 27) | Buscar os insumos: dividend yield projetado do Ibovespa, crescimento esperado dos lucros e o preço atual do índice; aplicar a fórmula do prêmio implícito | Damodaran Online, como checagem: ERP maduro (EUA) + CRP do Brasil (ver seção 2) |
| **Spread de crédito de debêntures** | ANBIMA — "Taxas Indicativas de Debêntures" | Buscar "ANBIMA taxas indicativas debêntures [nome da empresa]" | Rating da empresa (S&P, Moody's, Fitch, local) → tabela de spread por rating |
| **Alíquota de IR + CSLL** | Legislação vigente (Receita Federal) | Buscar "alíquota IRPJ CSLL vigente" para confirmar os 34% (ou o valor setorial, se houver regime especial) | — |
| **Tributação de dividendos/JCP** | Legislação vigente (Receita Federal / Lei em vigor) | Buscar "tributação dividendos JCP Brasil lei vigente [ano]" antes de citar qualquer alíquota no vídeo | — |

## 2. Parâmetros globais (EUA e Europa) — Damodaran Online

Site principal: **pages.stern.nyu.edu/~adamodar/New_Home_Page/data.html** (a página "Data" do site pessoal de Aswath Damodaran na NYU Stern). É a fonte usada no [`PROCEDIMENTO_WACC.md`](PROCEDIMENTO_WACC.md). Os arquivos são atualizados em janeiro de cada ano (dados anuais) e mensalmente (prêmio implícito).

| Parâmetro | Onde está no site | Como buscar | Observação |
|---|---|---|---|
| **ERP implícito do S&P 500 (maduro)** | Página "Implied Equity Risk Premiums" / planilha de prêmios mensais | Buscar "Damodaran implied equity risk premium current" | Atualizado todo mês; usar o valor do mês mais recente disponível |
| **Country Risk Premium (CRP) por país** | Planilha "Country Default Spreads and Risk Premiums" (`ctryprem`) | Buscar "Damodaran country risk premium [país]" | Atualizado poucas vezes por ano |
| **Betas por setor (US, Europe, Global, Emerging Markets)** | Planilha "Betas by Sector" (`betas`) | Buscar "Damodaran betas by sector [US/Europe/Global] [setor]" | Escolher a região certa (US, Europe, Emerging, Global) |
| **Spreads por rating / rating sintético** | Página "Ratings, Interest Coverage Ratios and Default Spreads" | Buscar "Damodaran default spread by rating" e, para empresas sem rating, "Damodaran synthetic rating interest coverage" | Há tabelas separadas para empresas grandes e pequenas/arriscadas |
| **Alíquotas marginais de IR por país** | Planilha "Tax Rates by Country" (`countrytaxrates`) | Buscar "Damodaran marginal tax rate by country [ano]" | Confirmar o ano mais recente publicado |
| **WACC médio por setor** | Planilha "Cost of Capital by Sector" | Buscar "Damodaran cost of capital by industry [região]" | Usado só como checagem de sanidade (passo 8 do procedimento de WACC) |

## 3. Taxas livres de risco específicas (EUA e Europa)

| Parâmetro | Fonte primária | Como buscar |
|---|---|---|
| **Treasury dos EUA de 10 anos** | U.S. Department of the Treasury (Daily Treasury Par Yield Curve) | Buscar "US Treasury 10 year yield today" |
| **Bund alemão de 10 anos** | Bundesbank / mercado (Refinitiv, Bloomberg, ou agregadores como investing.com) | Buscar "German 10 year bund yield today" |
| **Gilt do Reino Unido de 10 anos** | UK Debt Management Office (DMO) | Buscar "UK 10 year gilt yield today" |
| **Spread de default soberano (países não Aaa)** | Damodaran (`ctryprem`) ou agências (S&P, Moody's, Fitch) | Buscar "Damodaran default spread [país]" ou "[país] sovereign rating S&P" |

## 4. Dados específicos de cada empresa (não "globais")

Buscados sempre, empresa por empresa, no momento da valuation:

- **Rating de crédito da empresa** (se houver): agência local (Fitch Brasil, Moody's Brasil, S&P Brasil) ou internacional. Buscar "rating [empresa] Fitch/Moody's/S&P".
- **Títulos/debêntures da empresa negociados**: ANBIMA (Brasil) ou FINRA TRACE (EUA, títulos corporativos).
- **Segmentação geográfica de receita** (para CRP ponderado, Procedimento WACC seção 2–3): relatório anual / 10-K / Formulário de Referência da própria empresa.
- **Opções e RSUs em aberto** (empresas dos EUA): nota de "stock-based compensation" do 10-K.

## 5. Modelo do `MACRO.md` (cenário macro trimestral do canal)

Criar/atualizar este arquivo a cada revisão trimestral, com o seguinte formato:

```markdown
# Cenário macro do canal — [trimestre/ano]

Atualizado em: [data]

## Brasil
- NTN-B mais longa (Rf de toda a projeção, D11): [X]% real — fonte: Tesouro Direto, [data]
- IPCA esperado longo prazo: [X]% a.a. — fonte: Focus/BCB, [data]
- PIB real potencial longo prazo: [X]% a.a. — fonte: Focus/BCB, [data]
- g nominal (perpetuidade, R$) = (1+IPCA)×(1+PIB real) − 1 = [X]%
- Prêmio implícito do Ibovespa do trimestre: [X]% — cálculo do canal, [data], memória de cálculo em [link/anexo] (entra na série)
- ERP de longo prazo (usado no WACC, D5/D11): [X]% — média da série / proxy, [data]
- Câmbio PTAX: R$ [X]/US$ — fonte: BCB, [data]

## EUA
- Treasury 10 anos: [X]% — fonte: US Treasury, [data]
- ERP implícito S&P 500: [X]% — fonte: Damodaran, [mês/ano]
- Alíquota marginal: [X]% — fonte: Damodaran `countrytaxrates`, [ano]

## Europa (zona do euro)
- Bund 10 anos: [X]% — fonte: Bundesbank/mercado, [data]
- ERP maduro: [X]% (igual ao dos EUA, premissa de Damodaran)
- Alíquota marginal: depende do país sede — fonte: Damodaran `countrytaxrates`, [ano]
```

## 6. O que fazer quando a fonte falhar

- **Página indisponível ou bloqueada**: tentar a fonte alternativa da tabela correspondente.
- **Arquivo `.xls`/`.xlsx` não pôde ser lido**: buscar o valor citado em alguma notícia, relatório de análise ou página HTML que reproduza a tabela; se não encontrar, pedir para a pessoa baixar o arquivo e anexá-lo à conversa.
- **Nenhuma fonte responde**: usar o último valor confiável já registrado em algum `MACRO.md` anterior, marcando `[NÃO VERIFICADO — fonte indisponível em <data>]` no relatório, e revisar na próxima atualização trimestral.
- **Dúvida entre duas fontes com valores diferentes**: registrar ambos e explicar no vídeo qual foi usado e por quê (nunca escolher em silêncio).
