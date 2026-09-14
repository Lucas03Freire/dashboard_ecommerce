import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

# 1. CARREGAMENTO E TRATAMENTO DOS DADOS

df = pd.read_csv('ecommerce_estatistica.csv')

# Padroniza categorias inconsistentes de gênero
df['Gênero'] = df['Gênero'].replace({
    'roupa para gordinha pluss P ao 52': 'Feminino',
    'Sem gênero infantil': 'Sem gênero',
    'Unissex': 'Sem gênero'
})

# 2. CRIAÇÃO DOS GRÁFICOS

# Gráfico 1 - Histograma de Preços
def cria_histograma(df):

    fig = px.histogram(
        df,
        x='Preço',
        nbins=50,
        title='Distribuição dos Preços dos Produtos'
    )

    fig.update_layout(
        xaxis_title='Preço',
        yaxis_title='Quantidade de Produtos',
        bargap=0.08  # Espaço entre as barras
    )
    return fig

# Gráfico 2 - Dispersão Preço x Quantidade Vendida
def cria_dispersao(df):

    fig = px.scatter(
        df,
        x='Preço',
        y='Qtd_Vendidos_Cod',
        opacity=0.5,
        title='Relação entre Preço e Quantidade Vendida'
    )

    fig.update_layout(
        xaxis_title='Preço',
        yaxis_title='Quantidade Vendida'
    )
    return fig

# Gráfico 3 - Mapa de Calor
def cria_heatmap(df):

    corr = df[
        ['Nota', 'N_Avaliações', 'Desconto', 'Preço', 'Qtd_Vendidos_Cod']
    ].corr()

    fig = px.imshow(
        corr,
        text_auto='.2f',
        title='Mapa de Calor - Correlação entre Variáveis do E-commerce'
    )
    return fig

# Gráfico 4 - Top 10 Marcas
def cria_barras_marcas(df):

    marcas = (
        df['Marca']
        .value_counts()
        .head(10)
        .reset_index()
    )
    marcas.columns = ['Marca', 'Quantidade']

    fig = px.bar(
        marcas,
        x='Marca',
        y='Quantidade',
        title='Top 10 Marcas com Maior Número de Produtos'
    )

    fig.update_layout(
        xaxis_title='Marca',
        yaxis_title='Quantidade de Produtos'
    )
    return fig

# Gráfico 5 - Pizza por Gênero
def cria_pizza_genero(df):
    
    genero = df['Gênero'].value_counts().reset_index()
    genero.columns = ['Gênero', 'Quantidade']

    fig = px.pie(
        genero,
        names='Gênero',
        values='Quantidade',
        title='Distribuição dos Produtos por Gênero'
    )
    return fig

# Gráfico 6 - Densidade das Notas
def cria_densidade(df):
    
    fig = px.histogram(
        df,
        x='Nota',
        marginal='rug',
        histnorm='density',
        title='Distribuição da Nota dos Produtos',
    )

    fig.update_layout(
        xaxis_title='Nota',
        yaxis_title='Densidade',
        bargap = 0.08  # Espaço entre as barras
    )
    return fig

# Gráfico 7 - Regressão Avaliações x Vendas
def cria_regressao(df):

    fig = px.scatter(
        df,
        x='N_Avaliações',
        y='Qtd_Vendidos_Cod',
        trendline='ols',
        opacity=0.5,
        title='Relação entre Número de Avaliações e Quantidade Vendida'
    )

    fig.update_layout(
        xaxis_title='Número de Avaliações',
        yaxis_title='Quantidade Vendida'
    )
    return fig

# 3. CRIAÇÃO DO DASHBOARD

def cria_app():
    
    app = Dash(__name__)

    # Cria os gráficos
    fig1 = cria_histograma(df)
    fig2 = cria_dispersao(df)
    fig3 = cria_heatmap(df)
    fig4 = cria_barras_marcas(df)
    fig5 = cria_pizza_genero(df)
    fig6 = cria_densidade(df)
    fig7 = cria_regressao(df)

    # Layout do Dashboard
    app.layout = html.Div([
        html.H1(
            'Dashboard de Análise de E-commerce',
            style={
                'textAlign': 'center',
                'marginTop': '30px'
            }
        ),

        html.P(
            'Análise exploratória dos dados de produtos de e-commerce.',
            style = {
                'textAlign': 'center',
                'marginTop': '30px'
            }
        ),

        html.H2('Distribuição dos Preços'),
        dcc.Graph(figure=fig1),

        html.H2('Preço x Quantidade Vendida'),
        dcc.Graph(figure=fig2),

        html.H2('Correlação entre Variáveis'),
        dcc.Graph(figure=fig3),

        html.H2('Top 10 Marcas'),
        dcc.Graph(figure=fig4),

        html.H2('Distribuição por Gênero'),
        dcc.Graph(figure=fig5),

        html.H2('Distribuição das Notas'),
        dcc.Graph(figure=fig6),

        html.H2('Avaliações x Quantidade Vendida'),
        dcc.Graph(figure=fig7)
    ])
    return app

# 4. EXECUÇÃO DA APLICAÇÃO

if __name__ == '__main__':
    app = cria_app()
    app.run(debug=True, port=8050)
