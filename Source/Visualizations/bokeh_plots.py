import os
import numpy as np
import pandas as pd
from bokeh.models import ColumnDataSource, HoverTool, NumeralTickFormatter

from bokeh.plotting import figure, show
from bokeh.resources import CDN
from bokeh.embed import file_html
import seaborn as sb
import matplotlib.pyplot as plt

from ML_Model.pandas_convert import DataConverter

converter = DataConverter(data_file='../ML_Model/raw_data.json')
df = converter.convert_json_to_pandas()
df_english = converter.english_translation(df)

def plot_number_of_rooms_vs_price():
    x = list(df["Broj soba"])
    y = list(df['Cijena'])

    p = figure(title="How number of rooms affects the price?", x_axis_label="Number of rooms", y_axis_label="Price")
    p.circle(x, y, size=5, color="navy", alpha=0.5)
    save_fig(p, 'number_of_rooms_vs_price')


def plot_number_of_area_indoor_vs_price():
    x = list(df["Stambena površina"])
    y = list(df["Cijena"])

    p = figure(title="How does the size of the house affect the price?", x_axis_label="Area indoor (in sq. meters)",
               y_axis_label="Price")
    p.circle(x, y, size=5, color="black", alpha=0.5)
    save_fig(p, 'area_indoor_vs_price')


def heat_map():
    df1 = df_english.iloc[:, 0:5]
    ax = plt.axes()
    sb.heatmap(df1.corr(), annot=True, cmap='magma', ax=ax)
    ax.set_title("Heatmap of dataset on housing prices in Croatia")
    plt.tight_layout()
    plt.savefig("../DjangoRoot/search/templates/search/heatmap.png", dpi=100, transparent=True)


def price_histogram():
    column = 'Cijena'  # Price
    hist, edges = np.histogram(df[column], bins=25)

    hist_df = pd.DataFrame({column: hist,
                            "left": edges[:-1],
                            "right": edges[1:]})
    hist_df["interval"] = ["%d to %d" % (left, right) for left,
                                                          right in zip(hist_df["left"], hist_df["right"])]

    src = ColumnDataSource(hist_df)
    plot = figure(plot_height=600, plot_width=600,
                  title="Price Histogram",
                  x_axis_label="Price",
                  y_axis_label="Count")

    plot.quad(bottom=0, top=column, left="left",
              right="right", source=src, fill_color='lightblue',
              line_color="black", fill_alpha=0.7,
              hover_fill_alpha=1.0, hover_fill_color='blue')

    hover = HoverTool(tooltips=[('Interval', '@interval'),
                                ('Count', str("@" + column))])
    plot.add_tools(hover)
    plot.xaxis[0].formatter = NumeralTickFormatter(format="0.0")
    save_fig(plot, name='price_histogram')


def save_fig(figure, name):
    html = file_html(figure, CDN, name)
    filename = "../DjangoRoot/search/templates/search/{}.html".format(name)
    with open(filename, 'w') as f:
        f.write(html)


def run_plotting():
    plot_number_of_rooms_vs_price()
    plot_number_of_area_indoor_vs_price()
    heat_map()
    price_histogram()

heat_map()
