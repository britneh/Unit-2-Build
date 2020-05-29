from joblib import load
pipeline = load('assets/pipeline.joblib')
# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            Input your demographics to predict your employment status. 

            """
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [dcc.Markdown('#### Industry'), 
        dcc.Dropdown(
            id='Industry', 
            options = [
                {'label': 'Professional and business services', 'value': 'Professional and business services'}, 
                {'label': 'Educational and health services', 'value': 'Educational and health services'}, 
                {'label': 'Public administration', 'value': 'Public administration'}, 
                {'label': 'Leisure and hospitality', 'value': 'Leisure and hospitality'}, 
                {'label': 'Manufacturing', 'value': 'Manufacturing'}, 
                {'label': 'Trade', 'value': 'Trade'}, 
                {'label': 'Financial', 'value': 'Financial'}, 
                {'label': 'Construction', 'value': 'Construction'},
                {'label': 'Other', 'value': 'Other'},
                {'label': 'Transportation and utilities ', 'value': 'Transportation and utilities '},
            ], 
            value = 'Africa', 
            className='mb-5', 
        ), 
    ],
    md=4,
)

layout = dbc.Row([column1, column2])