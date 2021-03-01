import os

from bokeh.plotting import figure, show
from bokeh.resources import CDN
from bokeh.embed import file_html

from DjangoRoot.GUI.settings import SOURCE_DIR
from ML_Model.pandas_convert import DataConverter


def plot_number_of_rooms_vs_price():
    converter = DataConverter(data_file=os.path.join(SOURCE_DIR, 'ML_Model/raw_data.json'))
    df = converter.convert_json_to_pandas()
    x = list(df["Broj soba"])
    y = list(df['Cijena'])

    # create a new plot with a title and axis labels
    p = figure(title="How number of rooms affects the price?", x_axis_label="Number of rooms", y_axis_label="Price")

    # add a line renderer with legend and line thickness
    p.circle(x, y, size=5, color="navy", alpha=0.5)

    # show the results
    html = file_html(p, CDN, "number_of_rooms_vs_price")
    filename = "../DjangoRoot/search/templates/search/number_of_rooms_vs_price.html"
    with open(filename, 'w') as f:
        f.write(html)


plot_number_of_rooms_vs_price()
