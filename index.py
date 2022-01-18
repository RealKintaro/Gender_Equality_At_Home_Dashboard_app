from typing import Text
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output , State
from dash.exceptions import PreventUpdate
import pathlib

from app import app , server
from apps.app2020 import index as index2020
from apps.app2020 import compare as compare2020
from apps.app2021 import index as index2021
from apps.app2021 import compare as compare2021


app.config.suppress_callback_exceptions=True

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

    html.Div(
        className="banner",
        style={'backgroundColor': '#242a44', 'padding': '2em 0', 'marging': '0'},
        children=[
            html.H3(
                children='DASHBOARD',
                style={'textAlign': 'center', 'color': 'white'}
            ),
            html.H2(
                children='Survey on Gender Equality at Home',
                style={'textAlign': 'center', 'color': 'white'}
            ),
            html.H3(
                children='Explore the country and region-level data from the 2020 and 2021 waves of the Survey on Gender Equality at Home.',
                style={'textAlign': 'center', 'color': 'white', 'font-weight': 'bold'}
            ),   
        ],
    ),
    
    html.Div(id='page-content page-content-select', children=[
        dbc.Row([
            html.Label(style={'font-weight': 'bold','font-size': '1.2em'}, children=['Select the survey year *']),
            dbc.Col( dcc.RadioItems(
                id='year_index',
                options=[{'label': ' 2020', 'value': 2020 }, {'label': ' 2021', 'value': 2021 }],
            ), width={"size": 3}, ),
        ], className="row1"),

        dbc.Row([
            html.Label(style={'font-weight': 'bold','font-size': '1.2em'}, children=['Select country or region *']),
            dbc.Col( dcc.RadioItems(
                id='mode',
                options=[{'label': ' By Region', 'value': 1 } , {'label': ' By Country', 'value': 2 }],
            ), width={"size": 3}, ),
        ], className="row2"),

        dbc.Row([
            dbc.Col( 
                dbc.Button(
                    "Show by all Questions",
                    id="all_questions",
                    className="mb-3 cat-btn",
                    color="primary",
                    n_clicks=0,
                ), width={"size": 3},
            ),
        ], className="row1"),
        dbc.Row([
            dbc.Col( 
                dbc.Button(
                    "Compare by region/country",
                    id="compare",
                    className="mb-3 cat-btn",
                    color="primary",
                    n_clicks=0,
                ), width={"size": 3}, 
            ),
        ] , className="row2")
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
              [Input('all_questions', 'n_clicks')],
              [Input('compare', 'n_clicks')],
              [Input('mode', 'value')],
              State('session', 'data'))
def session_store(year_index,ball,bcomp,mode,data):
    if ball:
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
    if bcomp:
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
            path='/apps/2020/compare'
        if year_index == 2021:
            path='/apps/2021/compare'

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
    if pathname == '/apps/2020/compare':
        return compare2020.layout
    if pathname == '/apps/2021/compare':
        return compare2021.layout
    else:
        return "404 Page Error! Please choose a link"


if __name__ == '__main__':
    app.run_server(debug=False)