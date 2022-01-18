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

df_regionall = pd.read_excel(DATA_PATH.joinpath("region_allyears.xlsx"),sheet_name= 'Data',header=0)  # GregorySmith Kaggle
df_countryall = pd.read_excel(DATA_PATH.joinpath("country_allyears.xlsx"),sheet_name= 'Data',header=0)

df_region = df_regionall.query('Year == 2020')
df_country = df_countryall.query('Year == 2020')


region_codebook_df = pd.read_excel(DATA_PATH.joinpath("region_allyears.xlsx"),sheet_name= 'Codebook',header=0)
country_codebook_df = pd.read_excel(DATA_PATH.joinpath("country_allyears.xlsx"),sheet_name= 'Codebook',header=0)

regions = df_region.Region.unique()
countrys = df_country.Subregion.unique()

region_codebook2020 = region_codebook_df.query('Wave == "all" | Wave == "wave 1"')
country_codebook2020 = country_codebook_df.query('Wave == "all" | Wave == "wave 1"')

covidc =  country_codebook2020.query(" `Category theme` == 'covid'")
democ =  country_codebook2020.query(" `Category theme` == 'demographics' & Variable != 'Gender'")
naac =  country_codebook2020.query(" `Category theme` == 'norms, access, and agency'")
tcwc =  country_codebook2020.query(" `Category theme` == 'time spent, care, and work'")

covidr =  region_codebook2020.query(" `Category theme` == 'covid'")
demor =  region_codebook2020.query(" `Category theme` == 'demographics'")
naar =  region_codebook2020.query(" `Category theme` == 'norms, access, and agency'")
tcwr =  region_codebook2020.query(" `Category theme` == 'time spent, care, and work'")
def generate_covr_graph(id):

    return dcc.Graph(id='covr-{}'.format(str(id)))

def generate_demor_graph(id):

    return dcc.Graph(id='demor-{}'.format(str(id)))
def generate_naar_graph(id):

    return dcc.Graph(id='naar-{}'.format(str(id)))
def generate_tcwr_graph(id):

    return dcc.Graph(id='tcwr-{}'.format(str(id)))
##################################################"
# "
def generate_covc_graph(id):

    return dcc.Graph(id='covc-{}'.format(str(id)))

def generate_democ_graph(id):

    return dcc.Graph(id='democ-{}'.format(str(id)))
def generate_naac_graph(id):

    return dcc.Graph(id='naac-{}'.format(str(id)))
def generate_tcwc_graph(id):

    return dcc.Graph(id='tcwc-{}'.format(str(id)))


region_row = html.Div([
    dbc.Row([
        dbc.Col(html.Div([html.H5("Region :")])),
        dbc.Col( 
            dcc.Dropdown(
                id="regions_dropdown",
                options=[{"label": x, "value": x} for x in regions],
                value=regions[0],
                clearable=False,
            )
        ),
    ], className="dim_dropdown"),
    
    html.Div([
        dbc.Button(
            "Demographics",
            id="demor_collap_btn",
            className="mb-3 cat-btn",
            color="primary",
            n_clicks=0,
        ),

        dbc.Button(
            "Covid",
            id="covr_collap_btn",
            className="mb-3 cat-btn",
            color="primary",
            n_clicks=0,
        ),

        dbc.Button(
            "Norms, Access, and Agency",
            id="naar_collap_btn",
            className="mb-3 cat-btn",
            color="primary",
            n_clicks=0,
        ),

        dbc.Button(
            "Time spent, Care, and work",
            id="tcwr_collap_btn",
            className="mb-3 cat-btn",
            color="primary",
            n_clicks=0,
        ),

    ],className="div_btns",
),


    html.Div(
    [

        dbc.Collapse(
            dbc.Card(dbc.CardBody(html.Div(children=[
                html.H2("Demographics"),
                dbc.Row(children=[
                    generate_demor_graph(i) for i in range(0,len(demor['[old] Parameter or Survey Question'].str.strip().unique()))
            ]),
            ]))),
            id="demor_collap",
            is_open=False,
        ),
        
        dbc.Collapse(
            dbc.Card(dbc.CardBody(html.Div(children=[
                html.H2("Covid"),
                dbc.Row(children=[
                    generate_covr_graph(i) for i in range(0,len(covidr['[old] Parameter or Survey Question'].str.strip().unique()))
        ]),
            ]))),
            id="covr_collap",
            is_open=False,
        ),

        dbc.Collapse(
            dbc.Card(dbc.CardBody(html.Div(children=[
                html.H2("Norms, Access, and Agency"),
                dbc.Row(children=[
                    generate_naar_graph(i) for i in range(0,len(naar['[old] Parameter or Survey Question'].str.strip().unique()))
            ]),
            ]))),
            id="naar_collap",
            is_open=False,
        ),

        dbc.Collapse(
            dbc.Card(html.Div(children=[
                html.H2("Time spent, Care, and work"),
                dbc.Row(children=[
                    generate_tcwr_graph(i) for i in range(0,len(tcwr['[old] Parameter or Survey Question'].str.strip().unique()))
            ]),
            ])),
            id="tcwr_collap",
            is_open=False,
        ),
    ]
),

],className="containner",)


country_row = html.Div([
    dbc.Row([
        dbc.Col(html.Div([html.H5("Country :")])),
            dbc.Col( dcc.Dropdown(
                id="countrys_dropdown",
                options=[{"label": x, "value": x} for x in countrys],
                value=countrys[0],
                clearable=False,
            )),
    ], className="dim_dropdown"),
    
    html.Div([
        dbc.Button(
            "Demographics",
            id="democ_collap_btn",
            className="mb-3 cat-btn",
            n_clicks=0,
        ),

        dbc.Button(
            "Covid",
            id="covc_collap_btn",
            className="mb-3 cat-btn",
            color="primary",
            n_clicks=0,
        ),

        dbc.Button(
            "Norms, Access, and Agency",
            id="naac_collap_btn",
            className="mb-3 cat-btn",
            color="primary",
            n_clicks=0,
        ),

        dbc.Button(
            "Time spent, Care, and work",
            id="tcwc_collap_btn",
            className="mb-3 cat-btn",
            color="primary",
            n_clicks=0,
        ),

    ],className="div_btns",
),



    html.Div(
    [

        dbc.Collapse(
            dbc.Card(dbc.CardBody(html.Div(children=[
                html.H2("Demographics"),
                dbc.Row(children=[
                    generate_democ_graph(i) for i in range(0,len(democ['[old] Parameter or Survey Question'].str.strip().unique()))
                ]),
            ]))),
            id="democ_collap",
            is_open=False,
        ),

        dbc.Collapse(
            dbc.Card(dbc.CardBody(html.Div(children=[
                html.H2("Covid"),
                dbc.Row(children=[
                    
                    generate_covc_graph(i) for i in range(0,len(covidc['[old] Parameter or Survey Question'].str.strip().unique()))
                ]),
            ]))),
            id="covc_collap",
            is_open=False,
        ),

        dbc.Collapse(
            dbc.Card(dbc.CardBody(html.Div(children=[
                html.H2("Norms, Access, and Agency"),
                dbc.Row(children=[
                    generate_naac_graph(i) for i in range(0,len(naac['[old] Parameter or Survey Question'].str.strip().unique()))
                ]),
            ]))),
            id="naac_collap",
            is_open=False,
        ),

        dbc.Collapse(
            dbc.Card(html.Div(children=[
                html.H2("Time spent, Care, and work"),
                dbc.Row(children=[
                    generate_tcwc_graph(i) for i in range(0,len(tcwc['[old] Parameter or Survey Question'].str.strip().unique()))
                ]),
            ])),
            id="tcwc_collap",
            is_open=False,
        ),

    ]
),


],className="containner",)

layout = html.Div([
    html.H3(
        'Survey on Gender Equality at Home YEAR : 2020', 
        style={"textAlign": "center"},
    ),
    html.Div(
        id='countent', 
        children=[

        ], className="row"),
],className="head_title")



@app.callback(Output('countent', 'children'),
              [Input('session', 'data')],
              )
def display_pagerows(data):
    if data.get('mode') == 1:
        return region_row
    if data.get('mode') == 2:
        return country_row

@app.callback(
    Output("demor_collap", "is_open"),
    [Input("demor_collap_btn", "n_clicks")],
    [State("demor_collap", "is_open")],
)
def toggle_demor_collap(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("covr_collap", "is_open"),
    [Input("covr_collap_btn", "n_clicks")],
    [State("covr_collap", "is_open")],
)
def toggle_covr_collap(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("naar_collap", "is_open"),
    [Input("naar_collap_btn", "n_clicks")],
    [State("naar_collap", "is_open")],
)
def toggle_naar_collap(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("tcwr_collap", "is_open"),
    [Input("tcwr_collap_btn", "n_clicks")],
    [State("tcwr_collap", "is_open")],
)
def toggle_tcwr_collap(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    [Output('covr-{}'.format(i), 'figure') for i in range(0,len(covidr['[old] Parameter or Survey Question'].str.strip().unique()))],
    [Input("covr_collap_btn", "n_clicks")],
    [Input("regions_dropdown", "value")]
)
def covidr_content(n_clicks,region):
    i=0
    mask1 = []
    figlist = []
    for q in covidr['[old] Parameter or Survey Question'].str.strip().unique():
        mask = df_region["Region"] == region
        test= covidr["Wave"].where(covidr['[old] Parameter or Survey Question'] == q).unique()
        if 'wave 1' in test:
                query = covidr['Variable Name'].where(covidr['[old] Parameter or Survey Question'] == q)
                query.dropna(inplace=True)
                mask1.append(query.values)
        elif 'all' in test:
                query = covidr['Variable Name'].where(covidr['[old] Parameter or Survey Question'] == q)
                query.dropna(inplace=True)
                mask1.append(query.values)
        
        fig =  px.bar(df_region[mask], x="Gender", y= mask1[i], 
                barmode="group",title= q)
        i+=1
        figlist.append(fig)
    
    return figlist

@app.callback(
    [Output('demor-{}'.format(i), 'figure') for i in range(0,len(demor['[old] Parameter or Survey Question'].str.strip().unique()))],
    [Input("demor_collap_btn", "n_clicks")],
    [Input("regions_dropdown", "value")]
)
def demor_content(n_clicks,region):
    i=0
    mask1 = []
    figlist = []
    for q in demor['[old] Parameter or Survey Question'].str.strip().unique():
        mask = df_region["Region"] == region
        test= demor["Wave"].where(demor['[old] Parameter or Survey Question'] == q).unique()
        if 'wave 1' in test:
                query = demor['Variable Name'].where(demor['[old] Parameter or Survey Question'] == q)
                query.dropna(inplace=True)
                mask1.append(query.values)
        elif 'all' in test:
                query = demor['Variable Name'].where(demor['[old] Parameter or Survey Question'] == q)
                query.dropna(inplace=True)
                mask1.append(query.values)
        if len(mask1[i]) != 0:
            fig =  px.bar(df_region[mask], x="Gender", y= mask1[i], 
                barmode="group",title= q)
            figlist.append(fig)
        i+=1
        
    
    return figlist       
@app.callback(
    [Output('naar-{}'.format(i), 'figure') for i in range(0,len(naar['[old] Parameter or Survey Question'].str.strip().unique()))],
    [Input("naar_collap_btn", "n_clicks")],
    [Input("regions_dropdown", "value")])
def naar_content(n_clicks,region):
    i=0
    mask1 = []
    figlist = []
    for q in naar['[old] Parameter or Survey Question'].str.strip().unique():
        mask = df_region["Region"] == region
        test= naar["Wave"].where(naar['[old] Parameter or Survey Question'] == q).unique()
        if 'wave 1' in test:
                query = naar['Variable Name'].where(naar['[old] Parameter or Survey Question'] == q)
                query.dropna(inplace=True)
                mask1.append(query.values)
        elif 'all' in test:
                query = naar['Variable Name'].where(naar['[old] Parameter or Survey Question'] == q)
                query.dropna(inplace=True)
                mask1.append(query.values)
        
        fig =  px.bar(df_region[mask], x="Gender", y= mask1[i], 
                barmode="group",title= q)
        i+=1
        figlist.append(fig)
    
    return figlist 

@app.callback(
    [Output('tcwr-{}'.format(i), 'figure') for i in range(0,len(tcwr['[old] Parameter or Survey Question'].str.strip().unique()))],
    [Input("tcwr_collap_btn", "n_clicks")],
    [Input("regions_dropdown", "value")])
def tcwr_content(n_clicks,region):
    i=0
    mask1 = []
    figlist = []
    for q in tcwr['[old] Parameter or Survey Question'].str.strip().unique():
        mask = df_region["Region"] == region
        test= tcwr["Wave"].where(tcwr['[old] Parameter or Survey Question'] == q).unique()
        if 'wave 1' in test:
                query = tcwr['Variable Name'].where(tcwr['[old] Parameter or Survey Question'] == q)
                query.dropna(inplace=True)
                mask1.append(query.values)
        elif 'all' in test:
                query = tcwr['Variable Name'].where(tcwr['[old] Parameter or Survey Question'] == q)
                query.dropna(inplace=True)
                mask1.append(query.values)
        
        fig =  px.bar(df_region[mask], x="Gender", y= mask1[i], 
                barmode="group",title= q)
        i+=1
        figlist.append(fig)
    
    return figlist



@app.callback(
    [Output('covc-{}'.format(i), 'figure') for i in range(0,len(covidc['[old] Parameter or Survey Question'].str.strip().unique()))],
    [Input("covc_collap_btn", "n_clicks")],
    [Input("countrys_dropdown", "value")]
)
def covidc_content(n_clicks,Country):
    i=0
    mask1 = []
    figlist = []
    for q in covidc['[old] Parameter or Survey Question'].str.strip().unique():
        mask = df_country["Subregion"] == Country
        test= covidc["Wave"].where(covidc['[old] Parameter or Survey Question'] == q).unique()
        if 'wave 1' in test:
                query = covidc['Variable'].where(covidc['[old] Parameter or Survey Question'] == q)
                query.dropna(inplace=True)
                mask1.append(query.values)
        elif 'all' in test:
                query = covidc['Variable'].where(covidc['[old] Parameter or Survey Question'] == q)
                query.dropna(inplace=True)
                mask1.append(query.values)
        
        fig =  px.bar(df_country[mask], x="Gender", y= mask1[i], 
                barmode="group",title= q)
        i+=1
        figlist.append(fig)
    
    return figlist

@app.callback(
    [Output('democ-{}'.format(i), 'figure') for i in range(0,len(democ['[old] Parameter or Survey Question'].str.strip().unique()))],
    [Input("democ_collap_btn", "n_clicks")],
    [Input("countrys_dropdown", "value")]
)
def democ_content(n_clicks,country):
    i=0
    mask1 = []
    figlist = []
    for q in democ['[old] Parameter or Survey Question'].str.strip().unique():
        mask = df_country["Subregion"] == country
        test= democ["Wave"].where(democ['[old] Parameter or Survey Question'] == q).unique()
        if 'wave 1' in test:
                query = democ['Variable'].where(democ['[old] Parameter or Survey Question'] == q)
                query.dropna(inplace=True)
                mask1.append(query.values)
        elif 'all' in test:
                query = democ['Variable'].where(democ['[old] Parameter or Survey Question'] == q)
                query.dropna(inplace=True)
                mask1.append(query.values)
        if len(mask1[i]) != 0:
            fig =  px.bar(df_country[mask], x="Gender", y= mask1[i], 
                barmode="group",title= q)
            figlist.append(fig)
        i+=1
        
    
    return figlist       
@app.callback(
    [Output('naac-{}'.format(i), 'figure') for i in range(0,len(naac['[old] Parameter or Survey Question'].str.strip().unique()))],
    [Input("naac_collap_btn", "n_clicks")],
    [Input("countrys_dropdown", "value")])
def naac_content(n_clicks,country):
    i=0
    mask1 = []
    figlist = []
    for q in naac['[old] Parameter or Survey Question'].str.strip().unique():
        mask = df_country["Subregion"] == country
        test= naac["Wave"].where(naac['[old] Parameter or Survey Question'] == q).unique()
        if 'wave 1' in test:
                query = naac['Variable'].where(naac['[old] Parameter or Survey Question'] == q)
                query.dropna(inplace=True)
                mask1.append(query.values)
        elif 'all' in test:
                query = naac['Variable'].where(naac['[old] Parameter or Survey Question'] == q)
                query.dropna(inplace=True)
                mask1.append(query.values)
        
        fig =  px.bar(df_country[mask], x="Gender", y= mask1[i], 
                barmode="group",title= q)
        i+=1
        figlist.append(fig)
    
    return figlist 

@app.callback(
    [Output('tcwc-{}'.format(i), 'figure') for i in range(0,len(tcwc['[old] Parameter or Survey Question'].str.strip().unique()))],
    [Input("tcwc_collap_btn", "n_clicks")],
    [Input("countrys_dropdown", "value")])
def tcwc_content(n_clicks,country):
    i=0
    mask1 = []
    figlist = []
    for q in tcwc['[old] Parameter or Survey Question'].str.strip().unique():
        mask = df_country["Subregion"] == country
        test= tcwc["Wave"].where(tcwc['[old] Parameter or Survey Question'] == q).unique()
        if 'wave 1' in test:
                query = tcwc['Variable'].where(tcwc['[old] Parameter or Survey Question'] == q)
                query.dropna(inplace=True)
                mask1.append(query.values)
        elif 'all' in test:
                query = tcwc['Variable'].where(tcwc['[old] Parameter or Survey Question'] == q)
                query.dropna(inplace=True)
                mask1.append(query.values)
        
        fig =  px.bar(df_country[mask], x="Gender", y= mask1[i], 
                barmode="group",title= q)
        i+=1
        figlist.append(fig)
    
    return figlist

@app.callback(
    Output("democ_collap", "is_open"),
    [Input("democ_collap_btn", "n_clicks")],
    [State("democ_collap", "is_open")],
)
def toggle_democ_collap(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("covc_collap", "is_open"),
    [Input("covc_collap_btn", "n_clicks")],
    [State("covc_collap", "is_open")],
)
def toggle_covc_collap(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("naac_collap", "is_open"),
    [Input("naac_collap_btn", "n_clicks")],
    [State("naac_collap", "is_open")],
)
def toggle_naac_collap(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("tcwc_collap", "is_open"),
    [Input("tcwc_collap_btn", "n_clicks")],
    [State("tcwc_collap", "is_open")],
)
def toggle_democ_collap(n, is_open):
    if n:
        return not is_open
    return is_open