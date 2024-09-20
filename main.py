from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

# Executar as funções para gerar os gráficos
if __name__ == "__main__":
    # Gerar e salvar o gráfico de linha
    line_plot_figure = draw_line_plot()
    line_plot_figure.savefig('line_plot.png')

    # Gerar e salvar o gráfico de barras
    bar_plot_figure = draw_bar_plot()
    bar_plot_figure.savefig('bar_plot.png')

    # Gerar e salvar os boxplots
    box_plot_figure = draw_box_plot()
    box_plot_figure.savefig('box_plot.png')
