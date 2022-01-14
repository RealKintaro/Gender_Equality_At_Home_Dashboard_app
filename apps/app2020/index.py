import imp
from dash import dcc
from dash import html
from dash.dependencies import Input, Output , State
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import pathlib
from app import app,server

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../../datasets").resolve()

df_region = pd.read_excel(DATA_PATH.joinpath("2020_region.xlsx"),sheet_name= 'Data',header=0)  # GregorySmith Kaggle
df_country = pd.read_excel(DATA_PATH.joinpath("2020_country.xlsx"),sheet_name= 'Data',header=0)
regions = df_region.Region.unique()
countrys = df_country.Country.unique()


region_row = dbc.Row([
        dbc.Col(html.Div([html.H5("Region:")]) ,width = {"offset": 1}),
        dbc.Col( dcc.Dropdown(
        id="regions_dropdown",
        options=[{"label": x, "value": x} for x in regions],
        value=regions[0],
        clearable=False,
    ), width={"size": 3}, ),
        dbc.Col(dbc.Button(
            "Ok", id="region_button", className="me-2", n_clicks=0
        ))])
country_row = dbc.Row([
    dbc.Col(html.Div([html.H5("Country:")]) ,width = {"offset": 1} ),

        dbc.Col( dcc.Dropdown(
        id="countrys_dropdown",
        options=[{"label": x, "value": x} for x in countrys],
        value=countrys[0],
        clearable=False,
    ), width={"size": 3},),
    dbc.Col(dbc.Button(
            "Ok", id="country_button", className="me-2", n_clicks=0
        ),),
])

layout = html.Div([
    html.H1('Survey on Gender Equality at Home YEAR: 2020', style={"textAlign": "center"}),
    html.H3('Choose by'),

    html.Div(id='countent', children=[


        ], className="row")

])

@app.callback(Output('countent', 'children'),
              [Input('session', 'data')],
              )
def display_pagerows(data):
    if data.get('mode') == 1:
        return region_row
    if data.get('mode') == 2:
        return country_row