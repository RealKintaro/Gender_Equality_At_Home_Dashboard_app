from typing import Text
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from app import app , server
from apps.app2020 import index as index2020
from apps.app2021 import index as index2021



navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("2020", href='/apps/2020')),
        dbc.NavItem(dbc.NavLink("2021", href='/apps/2021')),
    ],
    brand="Survey on Gender Equality at Home",
    brand_href="/",
    color="primary",
    dark=True,
)

page = html.Div([html.H3("Survey on Gender Equality at Home")])

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content', children=[])
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return  index2020.layout
    if pathname == '/apps/2020':
        return index2020.layout
    if pathname == '/apps/2021':
        return index2021.layout
    else:
        return "404 Page Error! Please choose a link"


if __name__ == '__main__':
    app.run_server(debug=True)