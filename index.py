import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app , server
from apps.app2020 import index as index2020
from apps.app2021 import index as index2021
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('2020',href='/apps/2020'),
        dcc.Link('2021',href='/apps/2021')
    ], className="row"),
    html.Div(id='page-content', children=[])
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/2020':
        return index2020.layout
    if pathname == '/apps/2021':
        return index2021.layout
    else:
        return "404 Page Error! Please choose a link"


if __name__ == '__main__':
    app.run_server(debug=True)