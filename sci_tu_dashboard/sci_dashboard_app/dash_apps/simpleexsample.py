# import os
# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# import pandas as pd
# import cdata.mysql as mod
# import plotly.graph_objs as go

# cnxn = mod.connect(
#     "User = admin;Password = admin;Database = sci_dashboard_database;Server = MySQL80 ;Port = 3306;")

# df = pd.read_sql(
#     "SELECT 'Room', 'status' FROM Report , cnxn)
# app_name = 'dash-mysqldataplot'

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = DjangoDash('SimpleExample', external_stylesheets=external_stylesheets)

# app.title = 'CData + Dash'
# trace = go.Bar(x=df.status, y=df.room, name='ShipName')

# app.layout = html.Div(children=[html.H1("CData Extension + Dash", style={'textAlign': 'center'}),
#                                 dcc.Graph(
#     id='example-graph',
#     figure={
#         'data': [trace],
#         'layout':
#         go.Layout(title='MySQL Orders Data', barmode='stack')
#     })
# ], className="container")

# # if __name__ == '__main__':
# # app.run_server(debug=True)

# import plotly.express as px
# df = px.data.gapminder().query("year==2007")
# fig = px.scatter_geo(df, locations="iso_alpha", color="continent",
#                      hover_name="country", size="pop",
#                      projection="natural earth")
# fig.show()