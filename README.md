# Dashboard de Análise de E-commerce

Projeto desenvolvido durante o curso de **Profissão: Analista de Dados**, da EBAC.

O objetivo do projeto é desenvolver uma aplicação utilizando **Dash e Plotly** para visualização e análise exploratória de dados de produtos de e-commerce.

## Objetivo

Criar um dashboard capaz de apresentar diferentes análises sobre os produtos disponíveis no conjunto de dados, permitindo visualizar informações relacionadas a:

- Preços;
- Quantidade de produtos;
- Quantidade vendida;
- Avaliações;
- Notas;
- Marcas;
- Gênero dos produtos;
- Correlação entre variáveis.

## Tecnologias utilizadas

- Python
- Pandas
- Plotly
- Dash
- Statsmodels

## Análises realizadas

O dashboard apresenta 7 visualizações:

### 1. Distribuição dos Preços

Histograma utilizado para visualizar a distribuição dos preços dos produtos.

### 2. Preço x Quantidade Vendida

Gráfico de dispersão utilizado para analisar a relação entre o preço dos produtos e a quantidade vendida.

### 3. Correlação entre Variáveis

Mapa de calor utilizado para visualizar a correlação entre:

- Nota;
- Número de avaliações;
- Desconto;
- Preço;
- Quantidade vendida.

### 4. Top 10 Marcas

Gráfico de barras apresentando as 10 marcas com maior quantidade de produtos no conjunto de dados.

### 5. Distribuição por Gênero

Gráfico de pizza mostrando a distribuição dos produtos por gênero.

### 6. Distribuição das Notas

Gráfico utilizado para visualizar a distribuição das avaliações dos produtos.

### 7. Avaliações x Quantidade Vendida

Gráfico de dispersão com linha de regressão para analisar a relação entre o número de avaliações e a quantidade vendida.

## Tratamento dos dados

Antes da criação dos gráficos, algumas categorias da variável `Gênero` foram padronizadas.

Foram realizadas as seguintes substituições:

- `roupa para gordinha pluss P ao 52` → `Feminino`
- `Sem gênero infantil` → `Sem gênero`
- `Unissex` → `Sem gênero`

## Estrutura do projeto

```text
ecommerce-dash/
│
├── app.py
├── ecommerce_estatistica.csv
├── requirements.txt
└── README.md
```

## Como executar o projeto

### 1. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Acesse a pasta do projeto

```bash
cd ecommerce-dash
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação

```bash
python app.py
```

### 5. Acesse o dashboard

Após iniciar a aplicação, acesse no navegador:

```text
http://127.0.0.1:8050/
```
## Aprendizados

Neste projeto foram praticados conceitos de:

- Manipulação de dados com Pandas;
- Criação de visualizações com Plotly;
- Construção de dashboards com Dash;
- Organização de código utilizando funções;
- Análise exploratória de dados;
- Correlação entre variáveis;
- Visualização de relações entre variáveis;
- Utilização de linha de regressão em gráficos.

## Próximos passos

Como evolução futura do projeto, pretendo adicionar:

- Melhorias no layout e design do dashboard;
- Filtros interativos;
- Indicadores e métricas;
- Maior interatividade entre os gráficos;
- Novas análises;
- Melhor organização visual das informações.

Projeto desenvolvido para fins acadêmicos e de aprendizado em Análise de Dados.