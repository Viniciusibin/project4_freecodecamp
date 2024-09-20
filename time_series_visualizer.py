import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Função para importar e limpar os dados
def import_and_clean_data():
    # Importar os dados
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

    # Limpar os dados: Remover os valores fora do intervalo de 2.5% superior e inferior
    df = df[(df['value'] >= df['value'].quantile(0.025)) &
            (df['value'] <= df['value'].quantile(0.975))]

    return df

# Função para desenhar gráfico de linha
def draw_line_plot():
    df = import_and_clean_data()

    # Desenhar o gráfico de linha
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df.index, df['value'], color='r', linewidth=1)

    # Adicionar título e rótulos
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Salvar a figura
    fig.savefig('line_plot.png')
    return fig

# Função para desenhar gráfico de barras
def draw_bar_plot():
    df = import_and_clean_data()

    # Preparar os dados para o gráfico de barras
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    # Agrupar por ano e mês, calculando a média das visualizações diárias
    df_bar = df_bar.groupby(['year', 'month']).mean().unstack()

    # Criar o gráfico de barras
    fig = df_bar.plot(kind='bar', figsize=(10, 6)).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.title('Average daily page views for each month grouped by year')
    plt.legend(title='Months')

    # Salvar a figura
    fig.savefig('bar_plot.png')
    return fig

# Função para desenhar boxplots
def draw_box_plot():
    df = import_and_clean_data()

    # Preparar os dados para os boxplots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')

    # Desenhar os boxplots
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # Gráfico de caixa por ano
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Gráfico de caixa por mês
    sns.boxplot(x='month', y='value', data=df_box, order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Salvar a figura
    fig.savefig('box_plot.png')
    return fig
