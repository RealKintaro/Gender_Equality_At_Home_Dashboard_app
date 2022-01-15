import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib
from app import app

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../../datasets").resolve()

df = pd.read_excel(DATA_PATH.joinpath("2020_region.xlsx"),sheet_name= 'Data',header=0)  # GregorySmith Kaggle

regions = df.Region.unique()

layout = html.Div([
    html.H1('Survey on Gender Equality at Home', style={"textAlign": "center"}),

    html.Div([

    html.Div([
        dcc.Dropdown(
        id="dropdown",
        options=[{"label": x, "value": x} for x in regions],
        value=regions[0],
        clearable=False,
    ),
    
    dcc.Graph(id="bar-chart"),

    html.Hr(),

    dcc.RadioItems(
        id='region-radio',
        options=[{'label': k, 'value': k} for k in regions],
        
    ),
    dcc.Graph(id="bar-chart1"),

        ], className="row")

        ]),

    dcc.Graph(id='my-bar', figure={}),
])

@app.callback(
   Output("bar-chart", "figure"),
   [Input("dropdown", "value")]
)
def update_bar_chart(region):
    mask = df["Region"] == region
    fig = px.bar(df[mask], x="Gender", y=["a1_agree","a1_neutral","a1_disagree"], 
                barmode="group",title="A.1. How much do you agree or disagree with the following statement? “Men and women should have equal opportunities (e.g. in education, jobs, household decision-making).")
    return fig

@app.callback(
   Output("bar-chart1", "figure"),
   [Input("region-radio", "value")]
)
def update_bar_chart1(region):
    mask = df["Region"] == region
    fig = px.bar(df[mask], x="Gender", y=["a3_yes","a3_no","a1_agree","a1_neutral","a1_disagree"], 
                barmode="group",title="A.3.  Last week, did you do any work for pay, do any kind of business, farming or other activity to generate income, even if only for one hour? ")
        
    return fig


