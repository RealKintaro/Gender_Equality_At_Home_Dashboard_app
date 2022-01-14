from typing import Text
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output , State
from dash.exceptions import PreventUpdate
import pathlib

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

layout = html.Div([
    html.Div(id= 'page-content', children=[
    dbc.Row([
        dbc.Col( dcc.RadioItems(
        id='year_index',
        options=[{'label': 2020, 'value': 2020 } , {'label': 2021, 'value': 2021 }],
    ), width={"size": 3}, ),
        
    dbc.Col( dcc.RadioItems(
        id='mode',
        options=[{'label': 'By Region', 'value': 1 } , {'label': 'By Country', 'value': 2 }],
    ), width={"size": 3}, ),
    ]),
        ], className="row")

])


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    dcc.Store(id='session', storage_type='session'),
    html.Div(id= 'page-content', children=[
    dbc.Row([
        dbc.Col( dcc.RadioItems(
        id='year_index',
        options=[{'label': 2020, 'value': 2020 } , {'label': 2021, 'value': 2021 }],
    ), width={"size": 3}, ),
        
    dbc.Col( dcc.RadioItems(
        id='mode',
        options=[{'label': 'By Region', 'value': 1 } , {'label': 'By Country', 'value': 2 }],
    ), width={"size": 3}, ),
    ]),
        ], className="row")

])

@app.callback([Output('session', 'data'),Output('url', 'pathname')],
              [Input('year_index', 'value')],
              [Input('mode', 'value')],
              State('session', 'data'))
def session_store(year_index,mode,data):
    if year_index is None:
            # prevent the None callbacks is important with the store component.
            # you don't want to update the store for nothing.
            raise PreventUpdate
    if mode is None:
            # prevent the None callbacks is important with the store component.
            # you don't want to update the store for nothing.
            raise PreventUpdate
    data = data or {'year': 0}
    data = data or {'mode': 0}
    path ='/'
    data['year'] = year_index
    data['mode'] = mode
    if year_index == 2020:
        path='/apps/2020'
    if year_index == 2021:
        path='/apps/2021'

    return [data,path]



@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return layout 
    if pathname == '/apps/2020':
        return index2020.layout
    if pathname == '/apps/2021':
        return index2021.layout
    else:
        return "404 Page Error! Please choose a link"


if __name__ == '__main__':
    app.run_server(debug=True)