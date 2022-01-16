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

df_region = pd.read_excel(DATA_PATH.joinpath("2021_region.xlsx"),sheet_name= 'Data',header=0)  # GregorySmith Kaggle
df_country = pd.read_excel(DATA_PATH.joinpath("2021_country.xlsx"),sheet_name= 'Data',header=0)
region_codebook_df = pd.read_excel(DATA_PATH.joinpath("region_allyears.xlsx"),sheet_name= 'Codebook',header=0)
country_codebook_df = pd.read_excel(DATA_PATH.joinpath("country_allyears.xlsx"),sheet_name= 'Codebook',header=0)

regions = df_region.region.unique()
countrys = df_country.subregion.unique()

region_codebook2021 = region_codebook_df.query('Wave == "all" | Wave == "wave 2"')
country_codebook2021 = country_codebook_df.query('Wave == "all" | Wave == "wave 2"')

covidc =  country_codebook2021.query(" `Category theme` == 'covid' | `Category theme`==''")
democ =  country_codebook2021.query(" `Category theme` == 'demographics' | `Category theme`==''")
naac =  country_codebook2021.query(" `Category theme` == 'norms, access, and agency' | `Category theme`==''")
tcwc =  country_codebook2021.query(" `Category theme` == 'time spent, care, and work' | `Category theme`==''")

covidr =  region_codebook2021.query(" `Category theme` == 'covid' | `Category theme`==''")
demor =  region_codebook2021.query(" `Category theme` == 'demographics' | `Category theme`==''")
naar =  region_codebook2021.query(" `Category theme` == 'norms, access, and agency' | `Category theme`==''")
tcwr =  region_codebook2021.query(" `Category theme` == 'time spent, care, and work' | `Category theme`==''")
def generate_covr_graph(id):

    return dcc.Graph(id='covr21-{}'.format(str(id)))

def generate_demor_graph(id):

    return dcc.Graph(id='demor21-{}'.format(str(id)))
def generate_naar_graph(id):

    return dcc.Graph(id='naar21-{}'.format(str(id)))
def generate_tcwr_graph(id):

    return dcc.Graph(id='tcwr21-{}'.format(str(id)))
##################################################"
# "
def generate_covc_graph(id):

    return dcc.Graph(id='covc21-{}'.format(str(id)))

def generate_democ_graph(id):

    return dcc.Graph(id='democ21-{}'.format(str(id)))
def generate_naac_graph(id):

    return dcc.Graph(id='naac21-{}'.format(str(id)))
def generate_tcwc_graph(id):

    return dcc.Graph(id='tcwc21-{}'.format(str(id)))


region_row = html.Div([
    dbc.Row([
        dbc.Col(html.Div([html.H5("Region:")]) ,width = {"offset": 1}),
        dbc.Col( dcc.Dropdown(
        id="regions_dropdown",
        options=[{"label": x, "value": x} for x in regions],
        value=regions[0],
        clearable=False,
    ), width={"size": 3}, ),
        dbc.Col(dbc.Button(
            "Ok", id="region_button", className="me-2", n_clicks=0
        ))]),
    
    html.Div(
    [
        dbc.Button(
            "Demographics",
            id="demor_collap21_btn",
            className="mb-3",
            color="primary",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(dbc.CardBody(html.Div(children=[
                dbc.Row(children=[
                    generate_demor_graph(i) for i in range(0,len(demor['Parameter or Survey Question'].str.strip().unique()))
        ]),
            ]))),
            id="demor_collap21",
            is_open=False,
        ),
    ]
),

    html.Div(
    [
        dbc.Button(
            "Covid",
            id="covr_collap21_btn",
            className="mb-3",
            color="primary",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(dbc.CardBody(html.Div(children=[
                dbc.Row(children=[
                    generate_covr_graph(i) for i in range(0,len(covidr['Parameter or Survey Question'].str.strip().unique()))
        ]),
            ]))),
            id="covr_collap21",
            is_open=False,
        ),
    ]
),

    html.Div(
    [
        dbc.Button(
            "Norms, Access, and Agency",
            id="naar_collap21_btn",
            className="mb-3",
            color="primary",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(dbc.CardBody(html.Div(children=[
                dbc.Row(children=[
                    generate_naar_graph(i) for i in range(0,len(naar['Parameter or Survey Question'].str.strip().unique()))
        ]),
            ]))),
            id="naar_collap21",
            is_open=False,
        ),
    ]
),
    html.Div(
    [
        dbc.Button(
            "Time spent, Care, and work",
            id="tcwr_collap21_btn",
            className="mb-3",
            color="primary",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(html.Div(children=[
                dbc.Row(children=[
                    generate_tcwr_graph(i) for i in range(0,len(tcwr['Parameter or Survey Question'].str.strip().unique()))
        ]),
            ])),
            id="tcwr_collap21",
            is_open=False,
        ),
    ]
)
])


country_row = html.Div([
    dbc.Row([
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
]),
    
    html.Div(
    [
        dbc.Button(
            "Demographics",
            id="democ_collap21_btn",
            className="mb-3",
            color="primary",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(dbc.CardBody(html.Div(children=[
                dbc.Row(children=[
                    generate_democ_graph(i) for i in range(1,len(democ['Parameter or Survey Question'].str.strip().unique()))
        ]),
            ]))),
            id="democ_collap21",
            is_open=False,
        ),
    ]
),

    html.Div(
    [
        dbc.Button(
            "Covid",
            id="covc_collap21_btn",
            className="mb-3",
            color="primary",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(dbc.CardBody(html.Div(children=[
                dbc.Row(children=[
                    generate_covc_graph(i) for i in range(0,len(covidc['Parameter or Survey Question'].str.strip().unique()))
        ]),
            ]))),
            id="covc_collap21",
            is_open=False,
        ),
    ]
),

    html.Div(
    [
        dbc.Button(
            "Norms, Access, and Agency",
            id="naac_collap21_btn",
            className="mb-3",
            color="primary",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(dbc.CardBody(html.Div(children=[
                dbc.Row(children=[
                    generate_naac_graph(i) for i in range(0,len(naac['Parameter or Survey Question'].str.strip().unique()))
        ]),
            ]))),
            id="naac_collap21",
            is_open=False,
        ),
    ]
),
    html.Div(
    [
        dbc.Button(
            "Time spent, Care, and work",
            id="tcwc_collap21_btn",
            className="mb-3",
            color="primary",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(html.Div(children=[
                dbc.Row(children=[
                    generate_tcwc_graph(i) for i in range(0,len(tcwc['Parameter or Survey Question'].str.strip().unique()))
        ]),
            ])),
            id="tcwc_collap21",
            is_open=False,
        ),
    ]
)
])

layout = html.Div([
    html.H1('Survey on Gender Equality at Home YEAR: 2021', style={"textAlign": "center"}),

    html.Div(id='countent2021', children=[

        ], className="row"),

    

])



@app.callback(Output('countent2021', 'children'),
              [Input('session', 'data')],
              )
def display_pagerows(data):
    if data.get('mode') == 1:
        return region_row
    if data.get('mode') == 2:
        return country_row

@app.callback(
    Output("demor_collap21", "is_open"),
    [Input("demor_collap21_btn", "n_clicks")],
    [State("demor_collap21", "is_open")],
)
def toggle_demor_collap21(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("covr_collap21", "is_open"),
    [Input("covr_collap21_btn", "n_clicks")],
    [State("covr_collap21", "is_open")],
)
def toggle_covr_collap21(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("naar_collap21", "is_open"),
    [Input("naar_collap21_btn", "n_clicks")],
    [State("naar_collap21", "is_open")],
)
def toggle_naar_collap21(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("tcwr_collap21", "is_open"),
    [Input("tcwr_collap21_btn", "n_clicks")],
    [State("tcwr_collap21", "is_open")],
)
def toggle_tcwr_collap21(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    [Output('covr21-{}'.format(i), 'figure') for i in range(0,len(covidr['Parameter or Survey Question'].str.strip().unique()))],
    [Input("covr_collap21_btn", "n_clicks")],
    [Input("regions_dropdown", "value")]
)
def covidr_content(n_clicks,region):
    i=0
    mask1 = []
    figlist = []
    for q in covidr['Parameter or Survey Question'].str.strip().unique():
        mask = df_region["region"] == region

        query = covidr['Variable Name'].where(covidr['Parameter or Survey Question'] == q)
        query.dropna(inplace=True)
        mask1.append(query.values)

        
        fig =  px.bar(df_region[mask], x="gender", y= mask1[i], 
                barmode="group",title= q)
        i+=1
        figlist.append(fig)
    
    return figlist

@app.callback(
    [Output('demor21-{}'.format(i), 'figure') for i in range(0,len(demor['Parameter or Survey Question'].str.strip().unique()))],
    [Input("demor_collap21_btn", "n_clicks")],
    [Input("regions_dropdown", "value")]
)
def demor_content(n_clicks,region):
    i=0
    mask1 = []
    figlist = []
    for q in demor['Parameter or Survey Question'].str.strip().unique():
        mask = df_region["region"] == region
        query = demor['Variable Name'].where(demor['Parameter or Survey Question'] == q)
        query.dropna(inplace=True)
        mask1.append(query.values)

        if len(mask1[i]) != 0:
            fig =  px.bar(df_region[mask], x="gender", y= mask1[i], 
                barmode="group",title= q)
            figlist.append(fig)
        i+=1
        
    
    return figlist       
@app.callback(
    [Output('naar21-{}'.format(i), 'figure') for i in range(0,len(naar['Parameter or Survey Question'].str.strip().unique()))],
    [Input("naar_collap21_btn", "n_clicks")],
    [Input("regions_dropdown", "value")])
def naar_content(n_clicks,region):
    i=0
    mask1 = []
    figlist = []
    for q in naar['Parameter or Survey Question'].str.strip().unique():
        mask = df_region["region"] == region
        query = naar['Variable Name'].where(naar['Parameter or Survey Question'] == q)
        query.dropna(inplace=True)
        mask1.append(query.values)
        fig =  px.bar(df_region[mask], x="gender", y= mask1[i], 
                barmode="group",title= q)
        i+=1
        figlist.append(fig)
    
    return figlist 

@app.callback(
    [Output('tcwr21-{}'.format(i), 'figure') for i in range(0,len(tcwr['Parameter or Survey Question'].str.strip().unique()))],
    [Input("tcwr_collap21_btn", "n_clicks")],
    [Input("regions_dropdown", "value")])
def tcwr_content(n_clicks,region):
    i=0
    mask1 = []
    figlist = []
    for q in tcwr['Parameter or Survey Question'].str.strip().unique():
        mask = df_region["region"] == region
        query = tcwr['Variable Name'].where(tcwr['Parameter or Survey Question'] == q)
        query.dropna(inplace=True)
        mask1.append(query.values)
        fig =  px.bar(df_region[mask], x="gender", y= mask1[i], 
                barmode="group",title= q)
        i+=1
        figlist.append(fig)
    
    return figlist

@app.callback(
    [Output('covc21-{}'.format(i), 'figure') for i in range(0,len(covidc['Parameter or Survey Question'].str.strip().unique()))],
    [Input("covc_collap21_btn", "n_clicks")],
    [Input("countrys_dropdown", "value")]
)
def covidc_content(n_clicks,Country):
    i=0
    mask1 = []
    figlist = []
    for q in covidc['Parameter or Survey Question'].str.strip().unique():
        mask = df_country["subregion"] == Country
        query = covidc['Variable'].where(covidc['Parameter or Survey Question'] == q)
        query.dropna(inplace=True)
        mask1.append(query.values)
        fig =  px.bar(df_country[mask], x="gender", y= mask1[i], 
                barmode="group",title= q)
        i+=1
        figlist.append(fig)
    
    return figlist

@app.callback(
    [Output('democ21-{}'.format(i), 'figure') for i in range(1,len(democ['Parameter or Survey Question'].str.strip().unique()))],
    [Input("democ_collap21_btn", "n_clicks")],
    [Input("countrys_dropdown", "value")]
)
def democ_content(n_clicks,country):
    i=0
    mask1 = []
    figlist = []
    for q in democ['Parameter or Survey Question'].str.strip().unique():
        mask = df_country["subregion"] == country
        query = democ['Variable'].where(democ['Parameter or Survey Question'] == q)
        query.dropna(inplace=True)
        mask1.append(query.values)

        if len(mask1[i]) != 0:
            fig =  px.bar(df_country[mask], x="gender", y= mask1[i], 
                barmode="group",title= q)
            figlist.append(fig)
        i+=1
        
    
    return figlist       
@app.callback(
    [Output('naac21-{}'.format(i), 'figure') for i in range(0,len(naac['Parameter or Survey Question'].str.strip().unique()))],
    [Input("naac_collap21_btn", "n_clicks")],
    [Input("countrys_dropdown", "value")])
def naac_content(n_clicks,country):
    i=0
    mask1 = []
    figlist = []
    for q in naac['Parameter or Survey Question'].str.strip().unique():
        mask = df_country["subregion"] == country
        query = naac['Variable'].where(naac['Parameter or Survey Question'] == q)
        query.dropna(inplace=True)
        mask1.append(query.values)   
        fig =  px.bar(df_country[mask], x="gender", y= mask1[i], 
                barmode="group",title= q)
        i+=1
        figlist.append(fig)
    
    return figlist 

@app.callback(
    [Output('tcwc21-{}'.format(i), 'figure') for i in range(0,len(tcwc['Parameter or Survey Question'].str.strip().unique()))],
    [Input("tcwc_collap21_btn", "n_clicks")],
    [Input("countrys_dropdown", "value")])
def tcwc_content(n_clicks,country):
    i=0
    mask1 = []
    figlist = []
    for q in tcwc['Parameter or Survey Question'].str.strip().unique():
        mask = df_country["subregion"] == country
        query = tcwc['Variable'].where(tcwc['Parameter or Survey Question'] == q)
        query.dropna(inplace=True)
        mask1.append(query.values)
        fig =  px.bar(df_country[mask], x="gender", y= mask1[i], 
                barmode="group",title= q)
        i+=1
        figlist.append(fig)
    
    return figlist

@app.callback(
    Output("democ_collap21", "is_open"),
    [Input("democ_collap21_btn", "n_clicks")],
    [State("democ_collap21", "is_open")],
)
def toggle_democ_collap21(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("covc_collap21", "is_open"),
    [Input("covc_collap21_btn", "n_clicks")],
    [State("covc_collap21", "is_open")],
)
def toggle_covc_collap21(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("naac_collap21", "is_open"),
    [Input("naac_collap21_btn", "n_clicks")],
    [State("naac_collap21", "is_open")],
)
def toggle_naac_collap21(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("tcwc_collap21", "is_open"),
    [Input("tcwc_collap21_btn", "n_clicks")],
    [State("tcwc_collap21", "is_open")],
)
def toggle_democ_collap21(n, is_open):
    if n:
        return not is_open
    return is_open