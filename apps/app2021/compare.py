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

df_regionnames = pd.read_excel(DATA_PATH.joinpath("2021_region.xlsx"),sheet_name= 'Data',header=0)  # GregorySmith Kaggle
df_countrynames = pd.read_excel(DATA_PATH.joinpath("2021_country.xlsx"),sheet_name= 'Data',header=0)

df_region = df_regionall.query('Year == 2021')
df_country = df_countryall.query('Year == 2021')


region_codebook_df = pd.read_excel(DATA_PATH.joinpath("region_allyears.xlsx"),sheet_name= 'Codebook',header=0)
country_codebook_df = pd.read_excel(DATA_PATH.joinpath("country_allyears.xlsx"),sheet_name= 'Codebook',header=0)

regions = df_regionnames.region.unique()
countrys = df_countrynames.subregion.unique()

region_codebook2020 = region_codebook_df.query('Wave == "all" | Wave == "wave 2"')
country_codebook2020 = country_codebook_df.query('Wave == "all" | Wave == "wave 2"')


covidc =  country_codebook2020.query(" `Category theme` == 'covid'")
democ =  country_codebook2020.query(" `Category theme` == 'demographics' & Variable != 'Gender'")
naac =  country_codebook2020.query(" `Category theme` == 'norms, access, and agency'")
tcwc =  country_codebook2020.query(" `Category theme` == 'time spent, care, and work'")


covidr =  region_codebook2020.query(" `Category theme` == 'covid'")
demor =  region_codebook2020.query(" `Category theme` == 'demographics'")
naar =  region_codebook2020.query(" `Category theme` == 'norms, access, and agency'")
tcwr =  region_codebook2020.query(" `Category theme` == 'time spent, care, and work'")

region_row = html.Div([
    dbc.Row([
        dbc.Col(html.Div([html.H5("Region 1 :")])),
        dbc.Col( 
            dcc.Dropdown(
                id="region1_dropdown21",
                options=[{"label": x, "value": x} for x in regions],
                value=regions[0],
                clearable=False,
            )
        ),
        dbc.Col(html.Div([html.H5("Region 2 :")])),
        dbc.Col( 
            dcc.Dropdown(
                id="region2_dropdown21",
                options=[{"label": x, "value": x} for x in regions],
                value=regions[1],
                clearable=False,
            )
        ),
    ], className="dim_dropdown"),

    html.Div([
        dbc.Button(
            "Demographics",
            id="demor_collapcom_btn21",
            className="mb-3 cat-btn",
            color="primary",
            n_clicks=0,
        ),

        dbc.Button(
            "Covid",
            id="covr_collapcom_btn",
            className="mb-3 cat-btn",
            color="primary",
            n_clicks=0,
        ),

        dbc.Button(
            "Norms, Access, and Agency",
            id="naar_collapcom_btn21",
            className="mb-3 cat-btn",
            color="primary",
            n_clicks=0,
        ),

        dbc.Button(
            "Time spent, Care, and work",
            id="tcwr_collapcom_btn21",
            className="mb-3 cat-btn",
            color="primary",
            n_clicks=0,
        ),

    ],className="div_btns",
),


    html.Div(
    [

        dbc.Collapse(
            dbc.Card(dbc.CardBody(
                html.Div(children=[
                    html.H2("Demographics"),
                    dbc.Row(children=[
                        dcc.Dropdown(
                            id='demorquestion21-radio',
                            options=[{'label': k, 'value': k} for k in demor['Parameter or Survey Question'].unique()],
                            value=demor['Parameter or Survey Question'].unique()[0],
                            clearable = False
                        ),     
                    ]),
                    dbc.Row(children=[
                        dbc.Col([
                            html.H3('Region 1'),
                            dcc.Graph(id='demorquestion21-graph1')
                        ]),
                        dbc.Col([
                            html.H3('Region 2'),
                            dcc.Graph(id='demorquestion21-graph2')
                        ]),
                    ])
                ])
            )),
            id="demor_collapcom21",
            is_open=False,
        ),
        
        dbc.Collapse(
            dbc.Card(dbc.CardBody(
                html.Div(children=[
                    html.H2("Covid"),
                    dbc.Row(children=[
                        dcc.Dropdown(
                            id='covrquestion21-radio',
                            options=[{'label': k, 'value': k} for k in covidr['Parameter or Survey Question'].unique()],
                            value=covidr['Parameter or Survey Question'].unique()[0],
                            clearable = False
                        ),     
                    ]),
                    dbc.Row(children=[
                        dbc.Col([
                            html.H3('Region 1'),
                            dcc.Graph(id='covrquestion21-graph1')
                        ]),
                        dbc.Col([
                            html.H3('Region 2'),
                            dcc.Graph(id='covrquestion21-graph2')
                        ]),
                    ])
                ])
            )),
            id="covr_collapcom21",
            is_open=False,
        ),

        dbc.Collapse(
            dbc.Card(dbc.CardBody(

                html.Div(children=[
                    html.H2("Norms, Access, and Agency"),
                    dbc.Row(children=[
                        dcc.Dropdown(
                            id='naarquestion21-radio',
                            options=[{'label': k, 'value': k} for k in naar['Parameter or Survey Question'].unique()],
                            value=naar['Parameter or Survey Question'].unique()[0],
                            clearable = False
                        ),     
                    ]),
                    dbc.Row(children=[
                        dbc.Col([
                            html.H3('Region 1'),
                            dcc.Graph(id='naarquestion21-graph1')
                        ]),
                        dbc.Col([
                            html.H3('Region 2'),
                            dcc.Graph(id='naarquestion21-graph2')
                        ]),
                    ])
                ])
            )),
            id="naar_collapcom21",
            is_open=False,
        ),

        dbc.Collapse(
            dbc.Card(

                html.Div(children=[
                    html.H2("Time spent, Care, and work"),
                    dbc.Row(children=[
                        dcc.Dropdown(
                            id='tcwrquestion21-radio',
                            options=[{'label': k, 'value': k} for k in tcwr['Parameter or Survey Question'].unique()],
                            value=naar['Parameter or Survey Question'].unique()[0],
                            clearable = False
                        ),     
                    ]),
                    dbc.Row(children=[
                        dbc.Col([
                            html.H3('Region 1'),
                            dcc.Graph(id='tcwrquestion21-graph1')
                        ]),
                        dbc.Col([
                            html.H3('Region 2'),
                            dcc.Graph(id='tcwrquestion21-graph2')
                        ]),
                    ])
                ])
                
            ),
            id="tcwr_collapcom21",
            is_open=False,
        ),
    ]
),

],className="containner",)

country_row = html.Div([
    dbc.Row([
        dbc.Col(
            html.Div([html.H5("Country 1 :")])),
            dbc.Col( dcc.Dropdown(
                id="country1_dropdown21",
                options=[{"label": x, "value": x} for x in countrys],
                value=countrys[0],
                clearable=False,
            )),
        dbc.Col(
            html.Div([html.H5("Country 2 :")])),
            dbc.Col( dcc.Dropdown(
                id="country2_dropdown21",
                options=[{"label": x, "value": x} for x in countrys],
                value=countrys[3],
                clearable=False,
            )),
    ], className="dim_dropdown"),
    
        html.Div([
        dbc.Button(
            "Demographics",
            id="democ_collapcom_btn21",
            className="mb-3 cat-btn",
            n_clicks=0,
        ),

        dbc.Button(
            "Covid",
            id="covc_collapcom_btn21",
            className="mb-3 cat-btn",
            color="primary",
            n_clicks=0,
        ),

        dbc.Button(
            "Norms, Access, and Agency",
            id="naac_collapcom_btn21",
            className="mb-3 cat-btn",
            color="primary",
            n_clicks=0,
        ),

        dbc.Button(
            "Time spent, Care, and work",
            id="tcwc_collapcom_btn21",
            className="mb-3 cat-btn",
            color="primary",
            n_clicks=0,
        ),

    ],className="div_btns",
),



    html.Div(
    [

        dbc.Collapse(
            dbc.Card(dbc.CardBody(

                html.Div(children=[
                    html.H2("Demographics"),
                    dbc.Row(children=[
                        dcc.Dropdown(
                            id='democquestion21-radio',
                            options=[{'label': k, 'value': k} for k in democ['Parameter or Survey Question'].unique()],
                            value=democ['Parameter or Survey Question'].unique()[0],
                            clearable = False
                        ),     
                    ]),
                    dbc.Row(children=[
                        dbc.Col([
                            html.H3('Country 1'),
                            dcc.Graph(id='democquestion21-graph1')
                        ]),
                        dbc.Col([
                            html.H3('Country 2'),
                            dcc.Graph(id='democquestion21-graph2')
                        ]),
                    ])
                ])

            )),
            id="democ_collapcom21",
            is_open=False,
        ),

        dbc.Collapse(
            dbc.Card(dbc.CardBody(

                html.Div(children=[
                    html.H2("Covid"),
                    dbc.Row(children=[
                        dcc.Dropdown(
                            id='covcquestion21-radio',
                            options=[{'label': k, 'value': k} for k in covidc['Parameter or Survey Question'].unique()],
                            value=covidc['Parameter or Survey Question'].unique()[0],
                            clearable = False
                        ),     
                    ]),
                    dbc.Row(children=[
                        dbc.Col([
                            html.H3('Country 1'),
                            dcc.Graph(id='covcquestion21-graph1')
                        ]),
                        dbc.Col([
                            html.H3('Country 2'),
                            dcc.Graph(id='covcquestion21-graph2')
                        ]),
                    ])
                ])

            )),
            id="covc_collapcom21",
            is_open=False,
        ),

        dbc.Collapse(
            dbc.Card(dbc.CardBody(

                html.Div(children=[
                    html.H2("Norms, Access, and Agency"),
                    dbc.Row(children=[
                        dcc.Dropdown(
                            id='naacquestion21-radio',
                            options=[{'label': k, 'value': k} for k in naac['Parameter or Survey Question'].unique()],
                            value=naac['Parameter or Survey Question'].unique()[0],
                            clearable = False
                        ),     
                    ]),
                    dbc.Row(children=[
                        dbc.Col([
                            html.H3('Country 1'),
                            dcc.Graph(id='naacquestion21-graph1')
                        ]),
                        dbc.Col([
                            html.H3('Country 2'),
                            dcc.Graph(id='naacquestion21-graph2')
                        ]),
                    ])
                ])

            )),
            id="naac_collapcom21",
            is_open=False,
        ),

        dbc.Collapse(
            dbc.Card(

                html.Div(children=[
                    html.H2("Time spent, Care, and work"),
                    dbc.Row(children=[
                        dcc.Dropdown(
                            id='tcwcquestion21-radio',
                            options=[{'label': k, 'value': k} for k in tcwc['Parameter or Survey Question'].unique()],
                            value=tcwc['Parameter or Survey Question'].unique()[0],
                            clearable = False
                        ),     
                    ]),
                    dbc.Row(children=[
                        dbc.Col([
                            html.H3('Country 1'),
                            dcc.Graph(id='tcwcquestion21-graph1')
                        ]),
                        dbc.Col([
                            html.H3('Country 2'),
                            dcc.Graph(id='tcwcquestion21-graph2')
                        ]),
                    ])
                ])

            ),
            id="tcwc_collapcom21",
            is_open=False,
        ),

    ]

),


],className="containner",)

layout = html.Div([
    html.H3(
        'Survey on Gender Equality at Home YEAR : 2020 Compare mode', 
        style={"textAlign": "center"},
    ),
    html.Div(
        id='countentcomp21', 
        children=[

        ], className="row"),
],className="head_title")


##################################################################


@app.callback(Output('countentcomp21', 'children'),
              [Input('session', 'data')],
              )
def display_pagerows(data):
    if data.get('mode') == 1:
        return region_row
    if data.get('mode') == 2:
        return country_row



##############################################################
@app.callback(
    Output("demor_collapcom21", "is_open"),
    [Input("demor_collapcom_btn21", "n_clicks")],
    [State("demor_collapcom21", "is_open")],
)
def toggle_demor_collapcom(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("covr_collapcom21", "is_open"),
    [Input("covr_collapcom_btn", "n_clicks")],
    [State("covr_collapcom21", "is_open")],
)
def toggle_covr_collapcom(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("naar_collapcom21", "is_open"),
    [Input("naar_collapcom_btn21", "n_clicks")],
    [State("naar_collapcom21", "is_open")],
)
def toggle_naar_collapcom(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("tcwr_collapcom21", "is_open"),
    [Input("tcwr_collapcom_btn21", "n_clicks")],
    [State("tcwr_collapcom21", "is_open")],
)
def toggle_tcwr_collapcom(n, is_open):
    if n:
        return not is_open
    return is_open
####################################################""
@app.callback(
    Output("democ_collapcom21", "is_open"),
    [Input("democ_collapcom_btn21", "n_clicks")],
    [State("democ_collapcom21", "is_open")],
)
def toggle_democ_collapcom(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("covc_collapcom21", "is_open"),
    [Input("covc_collapcom_btn21", "n_clicks")],
    [State("covc_collapcom21", "is_open")],
)
def toggle_covc_collapcom(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("naac_collapcom21", "is_open"),
    [Input("naac_collapcom_btn21", "n_clicks")],
    [State("naac_collapcom21", "is_open")],
)
def toggle_naac_collapcom(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("tcwc_collapcom21", "is_open"),
    [Input("tcwc_collapcom_btn21", "n_clicks")],
    [State("tcwc_collapcom21", "is_open")],
)
def toggle_democ_collapcom(n, is_open):
    if n:
        return not is_open
    return is_open

##############################################################"

@app.callback(
    Output('demorquestion21-graph1', 'figure'),
    [Input("demorquestion21-radio", "value")],
    [Input("region1_dropdown21", "value")]
)
def demor_content1(q,region):

    mask = df_region["Region"] == region
    mask1 = []
    
    query = demor['Variable Name'].where(demor['Parameter or Survey Question'] == q)
    query.dropna(inplace=True)
    mask1.append(query.values)
    
    if len(mask1) != 0:
            fig =  px.bar(df_region[mask], x="Gender", y= mask1[0], 
                barmode="group",title= q)
            return fig
    else:
            return

@app.callback(
    Output('demorquestion21-graph2', 'figure'),
    [Input("demorquestion21-radio", "value")],
    [Input("region2_dropdown21", "value")]
)
def demor_content2(q,region):

    mask = df_region["Region"] == region
    mask1 = []
    
    query = demor['Variable Name'].where(demor['Parameter or Survey Question'] == q)
    query.dropna(inplace=True)
    mask1.append(query.values)
    
    if len(mask1) != 0:
            fig =  px.bar(df_region[mask], x="Gender", y= mask1[0], 
                barmode="group",title= q)
            return fig
    else:
            return

###############################################################################""

@app.callback(
    Output('covrquestion21-graph1', 'figure'),
    [Input("covrquestion21-radio", "value")],
    [Input("region1_dropdown21", "value")]
)
def demor_content1(q,region):

    mask = df_region["Region"] == region
    mask1 = []
    
    query = covidr['Variable Name'].where(covidr['Parameter or Survey Question'] == q)
    query.dropna(inplace=True)
    mask1.append(query.values)
    
    if len(mask1) != 0:
            fig =  px.bar(df_region[mask], x="Gender", y= mask1[0], 
                barmode="group",title= q)
            return fig
    else:
            return

@app.callback(
    Output('covrquestion21-graph2', 'figure'),
    [Input("covrquestion21-radio", "value")],
    [Input("region2_dropdown21", "value")]
)
def demor_content2(q,region):

    mask = df_region["Region"] == region
    mask1 = []
    
    query = covidr['Variable Name'].where(covidr['Parameter or Survey Question'] == q)
    query.dropna(inplace=True)
    mask1.append(query.values)
    
    if len(mask1) != 0:
            fig =  px.bar(df_region[mask], x="Gender", y= mask1[0], 
                barmode="group",title= q)
            return fig
    else:
            return
###############################################################################""

@app.callback(
    Output('tcwrquestion21-graph1', 'figure'),
    [Input("tcwrquestion21-radio", "value")],
    [Input("region1_dropdown21", "value")]
)
def demor_content1(q,region):

    mask = df_region["Region"] == region
    mask1 = []
    
    query = tcwr['Variable Name'].where(tcwr['Parameter or Survey Question'] == q)
    query.dropna(inplace=True)
    mask1.append(query.values)
    
    if len(mask1) != 0:
            fig =  px.bar(df_region[mask], x="Gender", y= mask1[0], 
                barmode="group",title= q)
            return fig
    else:
            return

@app.callback(
    Output('tcwrquestion21-graph2', 'figure'),
    [Input("tcwrquestion21-radio", "value")],
    [Input("region2_dropdown21", "value")]
)
def demor_content2(q,region):

    mask = df_region["Region"] == region
    mask1 = []
    
    query = tcwr['Variable Name'].where(tcwr['Parameter or Survey Question'] == q)
    query.dropna(inplace=True)
    mask1.append(query.values)
    
    if len(mask1) != 0:
            fig =  px.bar(df_region[mask], x="Gender", y= mask1[0], 
                barmode="group",title= q)
            return fig
    else:
            return

###############################################################################""

@app.callback(
    Output('naarquestion21-graph1', 'figure'),
    [Input("naarquestion21-radio", "value")],
    [Input("region1_dropdown21", "value")]
)
def demor_content1(q,region):

    mask = df_region["Region"] == region
    mask1 = []
    
    query = naar['Variable Name'].where(naar['Parameter or Survey Question'] == q)
    query.dropna(inplace=True)
    mask1.append(query.values)
    
    if len(mask1) != 0:
            fig =  px.bar(df_region[mask], x="Gender", y= mask1[0], 
                barmode="group",title= q)
            return fig
    else:
            return

@app.callback(
    Output('naarquestion21-graph2', 'figure'),
    [Input("naarquestion21-radio", "value")],
    [Input("region2_dropdown21", "value")]
)
def demor_content2(q,region):

    mask = df_region["Region"] == region
    mask1 = []
    
    query = naar['Variable Name'].where(naar['Parameter or Survey Question'] == q)
    query.dropna(inplace=True)
    mask1.append(query.values)
    
    if len(mask1) != 0:
            fig =  px.bar(df_region[mask], x="Gender", y= mask1[0], 
                barmode="group",title= q)
            return fig
    else:
            return

##############################################################"

@app.callback(
    Output('democquestion21-graph1', 'figure'),
    [Input("democquestion21-radio", "value")],
    [Input("country1_dropdown21", "value")]
)
def democ_content1(q,country):

    mask = df_country["Subregion"] == country
    mask1 = []
    
    query = democ['Variable'].where(democ['Parameter or Survey Question'] == q)
    query.dropna(inplace=True)
    mask1.append(query.values)
    
    if len(mask1) != 0:
            fig =  px.bar(df_country[mask], x="Gender", y= mask1[0], 
                barmode="group",title= q)
            return fig
    else:
            return

@app.callback(
    Output('democquestion21-graph2', 'figure'),
    [Input("democquestion21-radio", "value")],
    [Input("country2_dropdown21", "value")]
)
def democ_content2(q,country):

    mask = df_country["Subregion"] == country
    mask1 = []
    
    query = democ['Variable'].where(democ['Parameter or Survey Question'] == q)
    query.dropna(inplace=True)
    mask1.append(query.values)
    
    if len(mask1) != 0:
            fig =  px.bar(df_country[mask], x="Gender", y= mask1[0], 
                barmode="group",title= q)
            return fig
    else:
            return

###############################################################################""

@app.callback(
    Output('covcquestion21-graph1', 'figure'),
    [Input("covcquestion21-radio", "value")],
    [Input("country1_dropdown21", "value")]
)
def covc_content1(q,country):

    mask = df_country["Subregion"] == country
    mask1 = []
    
    query = covidc['Variable'].where(covidc['Parameter or Survey Question'] == q)
    query.dropna(inplace=True)
    mask1.append(query.values)
    
    if len(mask1) != 0:
            fig =  px.bar(df_country[mask], x="Gender", y= mask1[0], 
                barmode="group",title= q)
            return fig
    else:
            return

@app.callback(
    Output('covcquestion21-graph2', 'figure'),
    [Input("covcquestion21-radio", "value")],
    [Input("country2_dropdown21", "value")]
)
def covc_content2(q,country):

    mask = df_country["Subregion"] == country
    mask1 = []
    
    query = covidc['Variable'].where(covidc['Parameter or Survey Question'] == q)
    query.dropna(inplace=True)
    mask1.append(query.values)
    
    if len(mask1) != 0:
            fig =  px.bar(df_country[mask], x="Gender", y= mask1[0], 
                barmode="group",title= q)
            return fig
    else:
            return
###############################################################################""

@app.callback(
    Output('tcwcquestion21-graph1', 'figure'),
    [Input("tcwcquestion21-radio", "value")],
    [Input("country1_dropdown21", "value")]
)
def tcwc_content1(q,country):

    mask = df_country["Subregion"] == country
    mask1 = []
    
    query = tcwc['Variable'].where(tcwc['Parameter or Survey Question'] == q)
    query.dropna(inplace=True)
    mask1.append(query.values)
    
    if len(mask1) != 0:
            fig =  px.bar(df_country[mask], x="Gender", y= mask1[0], 
                barmode="group",title= q)
            return fig
    else:
            return

@app.callback(
    Output('tcwcquestion21-graph2', 'figure'),
    [Input("tcwcquestion21-radio", "value")],
    [Input("country2_dropdown21", "value")]
)
def tcwc_content2(q,country):

    mask = df_country["Subregion"] == country
    mask1 = []
    
    query = tcwc['Variable'].where(tcwc['Parameter or Survey Question'] == q)
    query.dropna(inplace=True)
    mask1.append(query.values)
    
    if len(mask1) != 0:
            fig =  px.bar(df_country[mask], x="Gender", y= mask1[0], 
                barmode="group",title= q)
            return fig
    else:
            return

###############################################################################""

@app.callback(
    Output('naacquestion21-graph1', 'figure'),
    [Input("naacquestion21-radio", "value")],
    [Input("country1_dropdown21", "value")]
)
def naac_content1(q,country):

    mask = df_country["Subregion"] == country
    mask1 = []
    
    query = naac['Variable'].where(naac['Parameter or Survey Question'] == q)
    query.dropna(inplace=True)
    mask1.append(query.values)
    
    if len(mask1) != 0:
            fig =  px.bar(df_country[mask], x="Gender", y= mask1[0], 
                barmode="group",title= q)
            return fig
    else:
            return

@app.callback(
    Output('naacquestion21-graph2', 'figure'),
    [Input("naacquestion21-radio", "value")],
    [Input("country2_dropdown21", "value")]
)
def naac_content2(q,country):

    mask = df_country["Subregion"] == country
    mask1 = []
    
    query = naac['Variable'].where(naac['Parameter or Survey Question'] == q)
    query.dropna(inplace=True)
    mask1.append(query.values)
    
    if len(mask1) != 0:
            fig =  px.bar(df_country[mask], x="Gender", y= mask1[0], 
                barmode="group",title= q)
            return fig
    else:
            return