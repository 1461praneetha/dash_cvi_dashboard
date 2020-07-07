import pandas as pd
pd.set_option('display.max_columns', None)
from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


data = pd.read_csv("../../../Downloads/covid_community_vulnerability-master/data/severe_cases_score_data.csv", dtype={'FIPS': str})
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

indicators_lst = ['Severe COVID Case Complications',
'covid_cases',
'Years of Potential Life Lost Rate',
'% Fair or Poor Health',
'% Smokers',
'% Adults with Obesity',
'% Adults with Diabetes',
'% 65 and over']


all_states = list(data.State.unique())
all_states.insert(0, "United States")


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


colors = {'Severe COVID Case Complications': ['#fdc1f6', '#ff385e'], 'covid_cases': ['#bdb4fe', '#0d0c54'],
 'Years of Potential Life Lost Rate': ['#bdb4fe', '#0d0c54'], '% Fair or Poor Health': ['#bdb4fe', '#0d0c54'],
'% Smokers': ['#bdb4fe', '#0d0c54'],
'% Adults with Obesity':['#bdb4fe', '#0d0c54'],
'% Adults with Diabetes':['#bdb4fe', '#0d0c54'],
'% 65 and over':['#bdb4fe', '#0d0c54'] }

index_range = {'Severe COVID Case Complications': (35, 65), 'covid_cases': (1, 500), 'Years of Potential Life Lost Rate': (5146, 11159),
'% Fair or Poor Health': (13.4, 22.6),
'% Smokers': (14.1, 21),
'% Adults with Obesity': (28, 38),
'% Adults with Diabetes':(8.2, 16),
'% 65 and over':(14.5, 23)}

fig1 = px.choropleth_mapbox(data, geojson=counties, locations=data.FIPS, color='Severe COVID Case Complications',
                           color_continuous_scale='Reds',
                           range_color=(0,100),
                           mapbox_style="carto-positron",
                           zoom=3.5, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.8,
                           labels={'score'}, hover_data= ['County', 'State']#, visible = True 
                          )

fig1.update_layout(coloraxis_showscale=False, title_text = 'score',
  	   	margin={"r":0,"t":0,"l":0,"b":20})

fig1.add_trace(go.Choroplethmapbox(geojson=counties, locations=data.FIPS, z=data['covid_cases'],
                           colorscale='Blues',
                           zmin=0,
                           zmax=100,
                           marker_line_width=0.1, marker_opacity=0.8, hovertext=indicators_lst, hoverinfo='all', showscale=False))#, hoverinfo='all'))#, coloraxis_showscale= False)

fig1.update_layout(coloraxis_showscale=False, title_text = 'cases',
 	   	margin={"r":0,"t":0,"l":0,"b":20})


	
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([
	html.Div([
		html.Div([
			html.Label('Choose State'),
			dcc.Dropdown(
				id = 'choose-state',
				options= [{'label': state, 'value': state} for state in all_states],
				value= 'United States'
)
],
	style={'width': '48%', 'display': 'inline-block'}),

	html.Div([
		html.Label('Indicator'),
		dcc.Dropdown(
            id='choose-indicator',
            options=[{'label': i, 'value': i} for i in indicators_lst],
            value=['Severe COVID Case Complications',
'covid_cases'],
            multi = True
            )
    ],
    style={'width': '48%', 'display': 'inline-block'})]),

    dcc.Graph(id='counties-map', figure=fig1) #figure= fig),#WHERE THE MAP WOULD BE
	])

if __name__ == '__main__':
	app.run_server(debug=True)


