# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Can we predict unemployment in the United States?

            How people decide upon their careers has always been a fascinating topic for me.  
            More interesting though is how that decision, their ethnicity, education or even location impact employment.  
            I welcomed the daunting task to predict employment status of an individual in the United States.  
            """
        ),
        dcc.Link(dbc.Button('Try it Out!', color='primary'), href='/predictions')
    ],
    md=4,
)




column2 = dbc.Col(
    [    ]
)

layout = dbc.Row([column1, column2])