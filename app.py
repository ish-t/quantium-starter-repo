from dash import Dash, html, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv("./out/output.csv")

regions = df["region"].unique()

app.layout = html.Div(children=[
    html.H1("Pink Morsel Data",id="title"),
    dcc.Graph(id="pink-morsel-line-graph"),
    html.Div(id="regions",children=[
    html.H2('Regions'),
    dcc.RadioItems(
        regions,
        "north",
        id="region-radio"
    )
])

])

@callback(
    Output("pink-morsel-line-graph", "figure"),
    Input("region-radio", "value")
)
def graph_region_update(selected_region):

    #filter dataframe by region
    df_regions = df[df["region"] == selected_region]
    #create new line graph
    fig = px.line(df_regions, x="date", y="sales", title="Pink Morsel Sales by Date")
    #return new line graph
    return fig

if __name__ == "__main__":
    app.run(debug=True)