import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from dash import no_update

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.layout = dbc.Container(
    dbc.Row(
        dbc.Col(
            [
                dbc.Card(
                    [
                        html.H2('Hello from docker dash!',className='card-title'),
                        
                        html.Div(id='output'),
                        dbc.Input(id='input',placeholder='Type here...'),


                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Col(html.Img(src='https://picsum.photos/500',alt='random-image-1',width=500),width=6),
                                dbc.Col(html.Img(src='https://picsum.photos/500',alt='random-image-2',width=500),width=6)
                            ]
                        ),
                        
                        html.Br(),
                        dcc.Graph(
                            id='graph',
                            figure={
                                'data': [
                                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montréal'},
                                ],
                                'layout': {
                                    'title': 'Dash Data Visualization',
                                }
                            }
                        ),
                    ], # end card children
                    body=True
                ) # end card
            ], # end col children
        ), # end col
        justify='center'
    ) # end row
) # end container


@app.callback(
    Output('output','children'),
    [Input('input','value')]
)
def output(value):
    return value


if __name__ == "__main__":
    app.run_server(
        debug=True,
        port=8050,
        host='0.0.0.0'
    )