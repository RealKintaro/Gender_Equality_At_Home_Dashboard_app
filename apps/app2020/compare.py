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

df_regionnames = pd.read_excel(DATA_PATH.joinpath("2020_region.xlsx"),sheet_name= 'Data',header=0)  # GregorySmith Kaggle
df_countrynames = pd.read_excel(DATA_PATH.joinpath("2020_country.xlsx"),sheet_name= 'Data',header=0)

df_region = df_regionall.query('Year == 2020')
df_country = df_countryall.query('Year == 2020')


region_codebook_df = pd.read_excel(DATA_PATH.joinpath("region_allyears.xlsx"),sheet_name= 'Codebook',header=0)
country_codebook_df = pd.read_excel(DATA_PATH.joinpath("country_allyears.xlsx"),sheet_name= 'Codebook',header=0)

regions = df_regionnames.Region.unique()
countrys = df_countrynames.Country.unique()

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

region_row = html.Div([
    dbc.Row([
        dbc.Col(html.Div([html.H5("Region 1 :")])),
        dbc.Col( 
            dcc.Dropdown(
                id="region1_dropdown",
                options=[{"label": x, "value": x} for x in regions],
                value=regions[0],
                clearable=False,
            )
        ),
        dbc.Col(html.Div([html.H5("Region 2 :")])),
        dbc.Col( 
            dcc.Dropdown(
                id="region2_dropdown",
                options=[{"label": x, "value": x} for x in regions],
                value=regions[1],
                clearable=False,
            )
        ),
    ], className="dim_dropdown reg1_reg2"),

    html.Div([
        dbc.Button(
            "Demographics",
            id="demor_collapcom_btn",
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
            id="naar_collapcom_btn",
            className="mb-3 cat-btn",
            color="primary",
            n_clicks=0,
        ),

        dbc.Button(
            "Time spent, Care, and work",
            id="tcwr_collapcom_btn",
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
                            id='demorquestion20-radio',
                            options=[{'label': k, 'value': k} for k in demor['[old] Parameter or Survey Question'].unique()],
                            value=demor['[old] Parameter or Survey Question'].unique()[0],
                            clearable = False
                        ),     
                    ]),
                    dbc.Row(children=[
                        dbc.Col([
                            html.H3('Region 1'),
                            dcc.Graph(id='demorquestion20-graph1'),
                        ],className='plot_div',),

                        dbc.Col([
                            html.H3('Region 2'),
                            dcc.Graph(id='demorquestion20-graph2')
                        ],className='plot_div',),
                    ],className='plots_containner',)
                ])
            )),
            id="demor_collapcom",
            is_open=False,
        ),
        
        dbc.Collapse(
            dbc.Card(dbc.CardBody(
                html.Div(children=[
                    html.H2("Covid"),
                    dbc.Row(children=[
                        dcc.Dropdown(
                            id='covrquestion20-radio',
                            options=[{'label': k, 'value': k} for k in covidr['[old] Parameter or Survey Question'].unique()],
                            value=covidr['[old] Parameter or Survey Question'].unique()[0],
                            clearable = False
                        ),     
                    ]),
                    dbc.Row(children=[
                        dbc.Col([
                            html.H3('Region 1'),
                            dcc.Graph(id='covrquestion20-graph1')
                        ],className='plot_div',),
                        dbc.Col([
                            html.H3('Region 2'),
                            dcc.Graph(id='covrquestion20-graph2')
                        ],className='plot_div',),
                    ],className='plots_containner',)
                ])
            )),
            id="covr_collapcom",
            is_open=False,
        ),

        dbc.Collapse(
            dbc.Card(dbc.CardBody(

                html.Div(children=[
                    html.H2("Norms, Access, and Agency"),
                    dbc.Row(children=[
                        dcc.Dropdown(
                            id='naarquestion20-radio',
                            options=[{'label': k, 'value': k} for k in naar['[old] Parameter or Survey Question'].unique()],
                            value=naar['[old] Parameter or Survey Question'].unique()[0],
                            clearable = False
                        ),     
                    ]),
                    dbc.Row(children=[
                        dbc.Col([
                            html.H3('Region 1'),
                            dcc.Graph(id='naarquestion20-graph1')
                        ],className='plot_div',),
                        dbc.Col([
                            html.H3('Region 2'),
                            dcc.Graph(id='naarquestion20-graph2')
                        ],className='plot_div',),
                    ],className='plots_containner',)
                ])
            )),
            id="naar_collapcom",
            is_open=False,
        ),

        dbc.Collapse(
            dbc.Card(

                html.Div(children=[
                    html.H2("Time spent, Care, and work"),
                    dbc.Row(children=[
                        dcc.Dropdown(
                            id='tcwrquestion20-radio',
                            options=[{'label': k, 'value': k} for k in tcwr['[old] Parameter or Survey Question'].unique()],
                            value=naar['[old] Parameter or Survey Question'].unique()[0],
                            clearable = False
                        ),     
                    ]),
                    dbc.Row(children=[
                        dbc.Col([
                            html.H3('Region 1'),
                            dcc.Graph(id='tcwrquestion20-graph1')
                        ],className='plot_div',),
                        dbc.Col([
                            html.H3('Region 2'),
                            dcc.Graph(id='tcwrquestion20-graph2')
                        ],className='plot_div',),
                    ],className='plots_containner',)
                ])
                
            ),
            id="tcwr_collapcom",
            is_open=False,
        ),
    ],className="aaaaaaaaaaa",
),

],className="containner",)

country_row = html.Div([
    dbc.Row([
        dbc.Col(
            html.Div([html.H5("Country 1 :")])),
            dbc.Col( dcc.Dropdown(
                id="country1_dropdown",
                options=[{"label": x, "value": x} for x in countrys],
                value=countrys[0],
                clearable=False,
            )),
        dbc.Col(
            html.Div([html.H5("Country 2 :")])),
            dbc.Col( dcc.Dropdown(
                id="country2_dropdown",
                options=[{"label": x, "value": x} for x in countrys],
                value=countrys[5],
                clearable=False,
            )),
    ], className="dim_dropdown"),
    
        html.Div([
        dbc.Button(
            "Demographics",
            id="democ_collapcom_btn",
            className="mb-3 cat-btn",
            n_clicks=0,
        ),

        dbc.Button(
            "Covid",
            id="covc_collapcom_btn",
            className="mb-3 cat-btn",
            color="primary",
            n_clicks=0,
        ),

        dbc.Button(
            "Norms, Access, and Agency",
            id="naac_collapcom_btn",
            className="mb-3 cat-btn",
            color="primary",
            n_clicks=0,
        ),

        dbc.Button(
            "Time spent, Care, and work",
            id="tcwc_collapcom_btn",
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
                            id='democquestion20-radio',
                            options=[{'label': k, 'value': k} for k in democ['[old] Parameter or Survey Question'].unique()],
                            value=democ['[old] Parameter or Survey Question'].unique()[0],
                            clearable = False
                        ),     
                    ]),
                    dbc.Row(children=[
                        dbc.Col([
                            html.H3('Country 1'),
                            dcc.Graph(id='democquestion20-graph1')
                       ],className='plot_div',),
                        dbc.Col([
                            html.H3('Country 2'),
                            dcc.Graph(id='democquestion20-graph2')
                       ],className='plot_div',),
                    ],className='plots_containner',)
                ])

            )),
            id="democ_collapcom",
            is_open=False,
        ),

        dbc.Collapse(
            dbc.Card(dbc.CardBody(

                html.Div(children=[
                    html.H2("Covid"),
                    dbc.Row(children=[
                        dcc.Dropdown(
                            id='covcquestion20-radio',
                            options=[{'label': k, 'value': k} for k in covidc['[old] Parameter or Survey Question'].unique()],
                            value=covidc['[old] Parameter or Survey Question'].unique()[0],
                            clearable = False
                        ),     
                    ]),
                    dbc.Row(children=[
                        dbc.Col([
                            html.H3('Country 1'),
                            dcc.Graph(id='covcquestion20-graph1')
                        ],className='plot_div',),
                        dbc.Col([
                            html.H3('Country 2'),
                            dcc.Graph(id='covcquestion20-graph2')
                        ],className='plot_div',),
                    ],className='plots_containner',)
                ])

            )),
            id="covc_collapcom",
            is_open=False,
        ),

        dbc.Collapse(
            dbc.Card(dbc.CardBody(

                html.Div(children=[
                    html.H2("Norms, Access, and Agency"),
                    dbc.Row(children=[
                        dcc.Dropdown(
                            id='naacquestion20-radio',
                            options=[{'label': k, 'value': k} for k in naac['[old] Parameter or Survey Question'].unique()],
                            value=naac['[old] Parameter or Survey Question'].unique()[0],
                            clearable = False
                        ),     
                    ]),
                    dbc.Row(children=[
                        dbc.Col([
                            html.H3('Country 1'),
                            dcc.Graph(id='naacquestion20-graph1')
                        ],className='plot_div',),
                        dbc.Col([
                            html.H3('Country 2'),
                            dcc.Graph(id='naacquestion20-graph2')
                        ],className='plot_div',),
                    ],className='plots_containner',)
                ])

            )),
            id="naac_collapcom",
            is_open=False,
        ),

        dbc.Collapse(
            dbc.Card(

                html.Div(children=[
                    html.H2("Time spent, Care, and work"),
                    dbc.Row(children=[
                        dcc.Dropdown(
                            id='tcwcquestion20-radio',
                            options=[{'label': k, 'value': k} for k in tcwc['[old] Parameter or Survey Question'].unique()],
                            value=tcwc['[old] Parameter or Survey Question'].unique()[0],
                            clearable = False
                        ),     
                    ]),
                    dbc.Row(children=[
                        dbc.Col([
                            html.H3('Country 1'),
                            dcc.Graph(id='tcwcquestion20-graph1')
                        ],className='plot_div',),
                        dbc.Col([
                            html.H3('Country 2'),
                            dcc.Graph(id='tcwcquestion20-graph2')
                        ],className='plot_div',),
                    ],className='plots_containner',)
                ])
            ),
            id="tcwc_collapcom",
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
        id='countentcomp20', 
        children=[

        ], className="row"),
],className="head_title")


##################################################################


@app.callback(Output('countentcomp20', 'children'),
              [Input('session', 'data')],
              )
def display_pagerows(data):
    if data.get('mode') == 1:
        return region_row
    if data.get('mode') == 2:
        return country_row



##############################################################
@app.callback(
    Output("demor_collapcom", "is_open"),
    [Input("demor_collapcom_btn", "n_clicks")],
    [State("demor_collapcom", "is_open")],
)
def toggle_demor_collapcom(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("covr_collapcom", "is_open"),
    [Input("covr_collapcom_btn", "n_clicks")],
    [State("covr_collapcom", "is_open")],
)
def toggle_covr_collapcom(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("naar_collapcom", "is_open"),
    [Input("naar_collapcom_btn", "n_clicks")],
    [State("naar_collapcom", "is_open")],
)
def toggle_naar_collapcom(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("tcwr_collapcom", "is_open"),
    [Input("tcwr_collapcom_btn", "n_clicks")],
    [State("tcwr_collapcom", "is_open")],
)
def toggle_tcwr_collapcom(n, is_open):
    if n:
        return not is_open
    return is_open
####################################################""
@app.callback(
    Output("democ_collapcom", "is_open"),
    [Input("democ_collapcom_btn", "n_clicks")],
    [State("democ_collapcom", "is_open")],
)
def toggle_democ_collapcom(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("covc_collapcom", "is_open"),
    [Input("covc_collapcom_btn", "n_clicks")],
    [State("covc_collapcom", "is_open")],
)
def toggle_covc_collapcom(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("naac_collapcom", "is_open"),
    [Input("naac_collapcom_btn", "n_clicks")],
    [State("naac_collapcom", "is_open")],
)
def toggle_naac_collapcom(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("tcwc_collapcom", "is_open"),
    [Input("tcwc_collapcom_btn", "n_clicks")],
    [State("tcwc_collapcom", "is_open")],
)
def toggle_democ_collapcom(n, is_open):
    if n:
        return not is_open
    return is_open

##############################################################"

@app.callback(
    Output('demorquestion20-graph1', 'figure'),
    [Input("demorquestion20-radio", "value")],
    [Input("region1_dropdown", "value")]
)
def demor_content1(q,region):

    mask = df_region["Region"] == region
    mask1 = []
    
    query = demor['Variable Name'].where(demor['[old] Parameter or Survey Question'] == q)
    query.dropna(inplace=True)
    mask1.append(query.values)
    
    if len(mask1) != 0:
            fig =  px.bar(df_region[mask], x="Gender", y= mask1[0], 
                barmode="group")
            return fig
    else:
            return

@app.callback(
    Output('demorquestion20-graph2', 'figure'),
    [Input("demorquestion20-radio", "value")],
    [Input("region2_dropdown", "value")]
)
def demor_content2(q,region):

    mask = df_region["Region"] == region
    mask1 = []
    
    query = demor['Variable Name'].where(demor['[old] Parameter or Survey Question'] == q)
    query.dropna(inplace=True)
    mask1.append(query.values)
    
    if len(mask1) != 0:
            fig =  px.bar(df_region[mask], x="Gender", y= mask1[0], 
                barmode="group")
            return fig
    else:
            return

###############################################################################""

@app.callback(
    Output('covrquestion20-graph1', 'figure'),
    [Input("covrquestion20-radio", "value")],
    [Input("region1_dropdown", "value")]
)
def demor_content1(q,region):

    mask = df_region["Region"] == region
    mask1 = []
    
    query = covidr['Variable Name'].where(covidr['[old] Parameter or Survey Question'] == q)
    query.dropna(inplace=True)
    mask1.append(query.values)
    
    if len(mask1) != 0:
            fig =  px.bar(df_region[mask], x="Gender", y= mask1[0], 
                barmode="group")
            return fig
    else:
            return

@app.callback(
    Output('covrquestion20-graph2', 'figure'),
    [Input("covrquestion20-radio", "value")],
    [Input("region2_dropdown", "value")]
)
def demor_content2(q,region):

    mask = df_region["Region"] == region
    mask1 = []
    
    query = covidr['Variable Name'].where(covidr['[old] Parameter or Survey Question'] == q)
    query.dropna(inplace=True)
    mask1.append(query.values)
    
    if len(mask1) != 0:
            fig =  px.bar(df_region[mask], x="Gender", y= mask1[0], 
                barmode="group")
            return fig
    else:
            return
###############################################################################""

@app.callback(
    Output('tcwrquestion20-graph1', 'figure'),
    [Input("tcwrquestion20-radio", "value")],
    [Input("region1_dropdown", "value")]
)
def demor_content1(q,region):

    mask = df_region["Region"] == region
    mask1 = []
    
    query = tcwr['Variable Name'].where(tcwr['[old] Parameter or Survey Question'] == q)
    query.dropna(inplace=True)
    mask1.append(query.values)
    
    if len(mask1) != 0:
            fig =  px.bar(df_region[mask], x="Gender", y= mask1[0], 
                barmode="group")
            return fig
    else:
            return

@app.callback(
    Output('tcwrquestion20-graph2', 'figure'),
    [Input("tcwrquestion20-radio", "value")],
    [Input("region2_dropdown", "value")]
)
def demor_content2(q,region):

    mask = df_region["Region"] == region
    mask1 = []
    
    query = tcwr['Variable Name'].where(tcwr['[old] Parameter or Survey Question'] == q)
    query.dropna(inplace=True)
    mask1.append(query.values)
    
    if len(mask1) != 0:
            fig =  px.bar(df_region[mask], x="Gender", y= mask1[0], 
                barmode="group")
            return fig
    else:
            return

###############################################################################""

@app.callback(
    Output('naarquestion20-graph1', 'figure'),
    [Input("naarquestion20-radio", "value")],
    [Input("region1_dropdown", "value")]
)
def demor_content1(q,region):

    mask = df_region["Region"] == region
    mask1 = []
    
    query = naar['Variable Name'].where(naar['[old] Parameter or Survey Question'] == q)
    query.dropna(inplace=True)
    mask1.append(query.values)
    
    if len(mask1) != 0:
            fig =  px.bar(df_region[mask], x="Gender", y= mask1[0], 
                barmode="group")
            return fig
    else:
            return

@app.callback(
    Output('naarquestion20-graph2', 'figure'),
    [Input("naarquestion20-radio", "value")],
    [Input("region2_dropdown", "value")]
)
def demor_content2(q,region):

    mask = df_region["Region"] == region
    mask1 = []
    
    query = naar['Variable Name'].where(naar['[old] Parameter or Survey Question'] == q)
    query.dropna(inplace=True)
    mask1.append(query.values)
    
    if len(mask1) != 0:
            fig =  px.bar(df_region[mask], x="Gender", y= mask1[0], 
                barmode="group")
            return fig
    else:
            return

##############################################################"

@app.callback(
    Output('democquestion20-graph1', 'figure'),
    [Input("democquestion20-radio", "value")],
    [Input("country1_dropdown", "value")]
)
def democ_content1(q,country):

    mask = df_country["Subregion"] == country
    mask1 = []
    
    query = democ['Variable'].where(democ['[old] Parameter or Survey Question'] == q)
    query.dropna(inplace=True)
    mask1.append(query.values)
    
    if len(mask1) != 0:
            fig =  px.bar(df_country[mask], x="Gender", y= mask1[0], 
                barmode="group")
            return fig
    else:
            return

@app.callback(
    Output('democquestion20-graph2', 'figure'),
    [Input("democquestion20-radio", "value")],
    [Input("country2_dropdown", "value")]
)
def democ_content2(q,country):

    mask = df_country["Subregion"] == country
    mask1 = []
    
    query = democ['Variable'].where(democ['[old] Parameter or Survey Question'] == q)
    query.dropna(inplace=True)
    mask1.append(query.values)
    
    if len(mask1) != 0:
            fig =  px.bar(df_country[mask], x="Gender", y= mask1[0], 
                barmode="group")
            return fig
    else:
            return

###############################################################################""

@app.callback(
    Output('covcquestion20-graph1', 'figure'),
    [Input("covcquestion20-radio", "value")],
    [Input("country1_dropdown", "value")]
)
def covc_content1(q,country):

    mask = df_country["Subregion"] == country
    mask1 = []
    
    query = covidc['Variable'].where(covidc['[old] Parameter or Survey Question'] == q)
    query.dropna(inplace=True)
    mask1.append(query.values)
    
    if len(mask1) != 0:
            fig =  px.bar(df_country[mask], x="Gender", y= mask1[0], 
                barmode="group")
            return fig
    else:
            return

@app.callback(
    Output('covcquestion20-graph2', 'figure'),
    [Input("covcquestion20-radio", "value")],
    [Input("country2_dropdown", "value")]
)
def covc_content2(q,country):

    mask = df_country["Subregion"] == country
    mask1 = []
    
    query = covidc['Variable'].where(covidc['[old] Parameter or Survey Question'] == q)
    query.dropna(inplace=True)
    mask1.append(query.values)
    
    if len(mask1) != 0:
            fig =  px.bar(df_country[mask], x="Gender", y= mask1[0], 
                barmode="group")
            return fig
    else:
            return
###############################################################################""

@app.callback(
    Output('tcwcquestion20-graph1', 'figure'),
    [Input("tcwcquestion20-radio", "value")],
    [Input("country1_dropdown", "value")]
)
def tcwc_content1(q,country):

    mask = df_country["Subregion"] == country
    mask1 = []
    
    query = tcwc['Variable'].where(tcwc['[old] Parameter or Survey Question'] == q)
    query.dropna(inplace=True)
    mask1.append(query.values)
    
    if len(mask1) != 0:
            fig =  px.bar(df_country[mask], x="Gender", y= mask1[0], 
                barmode="group")
            return fig
    else:
            return

@app.callback(
    Output('tcwcquestion20-graph2', 'figure'),
    [Input("tcwcquestion20-radio", "value")],
    [Input("country2_dropdown", "value")]
)
def tcwc_content2(q,country):

    mask = df_country["Subregion"] == country
    mask1 = []
    
    query = tcwc['Variable'].where(tcwc['[old] Parameter or Survey Question'] == q)
    query.dropna(inplace=True)
    mask1.append(query.values)
    
    if len(mask1) != 0:
            fig =  px.bar(df_country[mask], x="Gender", y= mask1[0], 
                barmode="group")
            return fig
    else:
            return

###############################################################################""

@app.callback(
    Output('naacquestion20-graph1', 'figure'),
    [Input("naacquestion20-radio", "value")],
    [Input("country1_dropdown", "value")]
)
def naac_content1(q,country):

    mask = df_country["Subregion"] == country
    mask1 = []
    
    query = naac['Variable'].where(naac['[old] Parameter or Survey Question'] == q)
    query.dropna(inplace=True)
    mask1.append(query.values)
    
    if len(mask1) != 0:
            fig =  px.bar(df_country[mask], x="Gender", y= mask1[0], 
                barmode="group")
            return fig
    else:
            return

@app.callback(
    Output('naacquestion20-graph2', 'figure'),
    [Input("naacquestion20-radio", "value")],
    [Input("country2_dropdown", "value")]
)
def naac_content2(q,country):

    mask = df_country["Subregion"] == country
    mask1 = []
    
    query = naac['Variable'].where(naac['[old] Parameter or Survey Question'] == q)
    query.dropna(inplace=True)
    mask1.append(query.values)
    
    if len(mask1) != 0:
            fig =  px.bar(df_country[mask], x="Gender", y= mask1[0], 
                barmode="group")
            return fig
    else:
            return