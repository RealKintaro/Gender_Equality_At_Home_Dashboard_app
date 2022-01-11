import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__,suppress_callback_exceptions=False,
                        meta_tags=[{'name': 'viewport',
                                    'content': 'width=device-width, initial-scale=1.0'}],
                        external_stylesheets=[dbc.themes.BOOTSTRAP]
                )
server = app.server