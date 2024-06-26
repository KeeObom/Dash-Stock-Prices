import pandas as pd

# Load data
df =pd.read_csv('data/stockdata2.csv', index_col=0, parse_dates=True)
df.index = pd.to_datetime(df['Date'])

# THE DASH APP
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px

# Initialise the app
app = dash.Dash(__name__)

# Creates a list of dictionaries, which have the keys 'label'and 'value'
def get_options(list_stocks):
    dict_list = []
    for i in list_stocks:
        dict_list.append({'label': i, 'value': i})

    return dict_list


# Define the app
app.layout = html.Div()


app.layout = html.Div(children=[
    html.Div(className='row',  # Define the row element
             children=[
                 html.Div(className='four columns div-user-controls',
                          children=[
                              html.H2('Dash - STOCK PRICES'),
                              html.P('''Visualising time series with Plotly - Dash'''),
                              html.P('''Pick one or more stocks from the dropdown below.'''),
                              html.Div(className='div-for-dropdown',
                                       children=[
                                           dcc.Dropdown(id='stockselector',
                                                        options=get_options(df['stock'].unique()),
                                                        multi=True,
                                                        value=[df['stock'].sort_values()[0]],
                                                        style={'backgroundColor': '#1E1E1E'},
                                                        className='stockselector')
                                       ],
                                       style={'color': '1E1E1E'})
                          ]),  # Define the left element
                 html.Div(className='eight columns div-for-charts bg-grey',
                          children=[
                              dcc.Graph(id='timeseries',
                                        config={'displayModeBar': False},
                                        animate=True,
                                        figure=px.line(df,
                                                       x='Date',
                                                       y='value',
                                                       color='stock',
                                                       template='plotly_dark').update_layout(
                                                           {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                                            'paper_bgcolor': 'rgba(0, 0, 0, 0)'}
                                                       ))
                          ])
             ])
])

# app.layout = html.Div(children=[
#     html.Div(className='row', # Define the row element
#              children=[
#                  html.Div(className='four columns div-user-controls',
#                           children = [
#                                 html.H2('Dash - STOCK PRICES'),
#                                 html.P('''Visualising time series with Plotly - Dash'''),
#                                 html.P('''Pick one or more stocks from the dropdown below.''')
#                             ]), # Define the left element
#                  html.Div(className='eight columns div-for-charts bg-grey',
#                           children = [
#                               dcc.Graph(id='timeseries',
#                                         config={'displayModeBar': False},
#                                         animate=True,
#                                         figure=px.line(df,
#                                                        x='Date',
#                                                        y='value',
#                                                        color='stock',
#                                                        template='plotly_dark').update_layout(
#                                                            {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
#                                                             'paper_bgcolor': 'rgba(0, 0, 0, 0)'}
#                                                        ))]
#                                                        )
#                           ]) # Define the right element
#              ])




# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)