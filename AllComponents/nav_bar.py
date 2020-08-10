import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


nav_bar = html.Div(
    [
    html.Div(className='navbar', 
        children=[
            html.Img(src='https://raw.githubusercontent.com/community-insight-impact/covid_community_vulnerability/master/CVI%20Logo%20FINAL%20ONE%20smaller.png',
        style={'height':'28px','margin':8}), #html.A("COVID-19 Community Vulnerability Index"), 
            html.H2("COVID-19 Community Vulnerability Index  ", style={'font-size':18, 'vertical-align': 'middle', 'color': 'white'}),
            html.Div(className='dropdown', 
            children=[html.Button(className='dropbtn', children= html.Span(children=[html.P('Menu ',  style = {'display':'inline-block'}) ,#style={'margin-bottom': -10}),
                html.I(className="fa fa-caret-down", **{'aria-hidden': 'true'}, style = {'display':'inline-block', 'marginTop': '10px', 'marginLeft':'5px'})], style = {'display':'flex'})), 
                    html. Div(className='dropdown-content', children=
                        [html.A('About', href='https://github.com/community-insight-impact/covid_community_vulnerability', target="_blank"), 
                        html.A('Dataset', href='https://github.com/community-insight-impact/covid_community_vulnerability/blob/master/data/full_dataset.md', target="_blank"),
                        html.A('Methodology', href='https://github.com/community-insight-impact/covid_community_vulnerability/blob/master/documentation/methodology.md', target="_blank")])#, style = {'display':'inline-block'})
            ], style={'zIndex': 1000}),
        ], style={'display':'flex', 'zIndex': 1}),#, html.Div('hi, testing', style={'color':'black', 'margin-top':10})
        #choose_filters
        ]) #style={'zIndex': 1})#choose_filters])


