import dash_core_components as dcc
import dash_html_components as html
from django_plotly_dash import DjangoDash

from dash.dependencies import Input, Output

from sensors.models import SensorData

app = DjangoDash('SimpleExample')

all_options = {
    'Option 1': ['Temperature', 'Air Pressure', u'Accumulated PPT.'],
    'Option 2': [u'Accumulated PPT.', 'Humidity', 'Dust Concerntration'],
    'All': ['Temperature', 'Air Pressure', 'Dust Concerntration', u'Accumulated PPT.', 'Radiation Illuminance', 'Humidity', 'Solar Radiations']
}

field_data = {
    'Air Pressure': {'x': list(SensorData.objects.values_list('Date', flat=True)), 'y': list(SensorData.objects.values_list('Air_Pressure', flat=True))},
    'Accumulated PPT.': {'x': list(SensorData.objects.values_list('Date', flat=True)), 'y': list(SensorData.objects.values_list('Accumulated_PPT', flat=True))},
    'Temperature': {'x': list(SensorData.objects.values_list('Date', flat=True)), 'y': list(SensorData.objects.values_list('Air_Temperature', flat=True))},
    'Dust Concerntration': {'x': list(SensorData.objects.values_list('Date', flat=True)), 'y': list(SensorData.objects.values_list('Dust_Concentration', flat=True))},
    'Radiation Illuminance': {'x': list(SensorData.objects.values_list('Date', flat=True)), 'y': list(SensorData.objects.values_list('Radiation_Illuminance', flat=True))},
    'Humidity': {'x': list(SensorData.objects.values_list('Date', flat=True)), 'y': list(SensorData.objects.values_list('Humidity', flat=True))},
    'Solar Radiation': {'x': list(SensorData.objects.values_list('Date', flat=True)), 'y': list(SensorData.objects.values_list('Solar_Radiation', flat=True))}
}

# Boostrap CSS.
app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})

app.layout = html.Div(
    html.Div([
        html.Div([
            html.Img(
                src="http://test.fulcrumanalytics.com/wp-content/uploads/2015/10/Fulcrum-logo_840X144.png",
                className='three columns',
                style={
                    'height': '14%',
                    'width': '14%',
                    'float': 'right',
                    'position': 'relative',
                    'margin-top': 20,
                    'margin-right': 20
                },
            ),
            html.Div(children='''
                            History in graphical representations:
                            ''',
                     className='nine columns')
        ], className="row"),

        html.Div(
            [
                html.Div(
                    [
                        html.P('Choose Parameters:'),
                        dcc.Checklist(
                            id='Fields',
                            value=['Temperature'],
                            labelStyle={'display': 'inline-block'}
                        ),
                    ],
                    className='six columns',
                    style={'margin-top': '10'}
                ),
                html.Div(
                    [
                        html.P('Select Items:'),
                        dcc.RadioItems(
                            id='Item',
                            options=[{'label': k, 'value': k} for k in all_options.keys()],
                            value='All',
                            labelStyle={'display': 'inline-block'}
                        ),
                    ],
                    className='six columns',
                    style={'margin-top': '10'}
                )
            ], className="row"
        ),

        html.Div([
            html.Div([
                dcc.Graph(
                    id='graph'
                )
            ], className='six columns'),
            html.Div([
                dcc.Graph(
                    id='graph-2'
                )
            ], className="six columns")
        ], className="row")
    ], className='ten columns offset-by-one')
)


@app.callback(
    Output('Fields', 'options'),
    [Input('Item', 'value')])
def set_Fields_options(selected_item):
    return [{'label': i, 'value': i} for i in all_options[selected_item]]


@app.callback(
    Output('graph', 'figure'),
    [Input('Fields', 'value')])
def update_graph_src(selector):
    data = []
    for field in selector:
        data.append({'x': field_data[field]['x'], 'y': field_data[field]['y'],
                     'type': 'bar', 'name': field})
    figure = {
        'data': data,
        'layout': {
            'title': 'Bar Graph',
            'xaxis': dict(
                title='x Axis',
                rangeselector=dict(
                    buttons=list([
                        dict(count=1,
                             label="1m",
                             step="month",
                             stepmode="backward"),
                        dict(count=6,
                             label="6m",
                             step="month",
                             stepmode="backward"),
                        dict(count=1,
                             label="YTD",
                             step="year",
                             stepmode="todate"),
                        dict(count=1,
                             label="1y",
                             step="year",
                             stepmode="backward"),
                        dict(step="all")
                    ])
                ),
                rangeslider=dict(
                    visible=True
                ),
                type="date",
                titlefont=dict(
                    family='Courier New, monospace',
                    size=20,
                    color='#7f7f7f'
                )),
            'yaxis': dict(
                title='y Axis',
                titlefont=dict(
                    family='Helvetica, monospace',
                    size=20,
                    color='#7f7f7f'
                ))
        }
    }
    return figure


@app.callback(
    Output('graph-2', 'figure'),
    [Input('Fields', 'value')])
def update_graph_src(selector):
    data = []
    for field in selector:
        data.append({'x': field_data[field]['x'], 'y': field_data[field]['y'],
                     'type': 'line', 'name': field})
    figure = {
        'data': data,
        'layout': {
            'title': 'Scatter-Line Graph',
            'xaxis': dict(
                title='x Axis',
                rangeselector=dict(
                    buttons=list([
                        dict(count=1,
                             label="1m",
                             step="month",
                             stepmode="backward"),
                        dict(count=6,
                             label="6m",
                             step="month",
                             stepmode="backward"),
                        dict(count=1,
                             label="YTD",
                             step="year",
                             stepmode="todate"),
                        dict(count=1,
                             label="1y",
                             step="year",
                             stepmode="backward"),
                        dict(step="all")
                    ])
                ),
                rangeslider=dict(
                    visible=True
                ),
                type="date",
                titlefont=dict(
                    family='Courier New, monospace',
                    size=20,
                    color='#7f7f7f'
                )),
            'yaxis': dict(
                title='y Axis',
                titlefont=dict(
                    family='Helvetica, monospace',
                    size=20,
                    color='#7f7f7f'
                ))
        }
    }
    return figure
