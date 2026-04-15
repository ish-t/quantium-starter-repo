from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv("./out/output.csv")

fig = px.line(df, x="date", y="sales", title="Pink Morsel Sales by Date")

app.layout = html.Div(children=[
    dcc.Graph(
        id='graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)