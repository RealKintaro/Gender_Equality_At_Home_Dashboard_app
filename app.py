import dash

app = dash.Dash(__name__,suppress_callback_exceptions=False,
                        meta_tags=[{'name': 'viewport',
                                    'content': 'width=device-width, initial-scale=1.0'}]
                )
server = app.server