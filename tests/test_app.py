import pytest
from dash import Dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash.testing.wait as wait
import plotly.express as px
import pandas as pd
import os

# Load the formatted sales data
data_file = 'data/formatted_sales_data.csv'
df = pd.read_csv(data_file)

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Create the Dash application
app = Dash(__name__)

# Define the layout of the app
app.layout = html.Div(
    children=[
        html.H1(
            children='Soul Foods Pink Morsel Sales Visualizer',
            style={'textAlign': 'center', 'color': '#4CAF50'}
        ),
        
        html.Div(
            children='Select Region:',
            style={'fontSize': '20px', 'marginBottom': '10px'}
        ),

        dcc.RadioItems(
            id='region-radio',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all',
            style={'marginBottom': '20px'}
        ),
        
        dcc.Graph(
            id='sales-line-chart'
        )
    ],
    style={'width': '80%', 'margin': '0 auto'}
)

# Callback to update the line chart based on selected region
@app.callback(
    Output('sales-line-chart', 'figure'),
    [Input('region-radio', 'value')]
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]
    
    fig = px.line(filtered_df, x='date', y='sales', title='Pink Morsel Sales Over Time', labels={'date': 'Date', 'sales': 'Sales'})
    return fig

# Define the test functions
@pytest.mark.parametrize("element_id", [
    "h1",  # Header
    "region-radio",  # Region Picker
    "sales-line-chart"  # Visualization
])
def test_elements_present(dash_duo, element_id):
    # Start the Dash app server
    dash_duo.start_server(app)
    
    # Wait for the element to be present in the DOM
    dash_duo.wait_for_element_by_id(element_id, timeout=10)
    
    # Verify the element is present in the DOM
    assert dash_duo.find_element(f"#{element_id}")

if __name__ == '__main__':
    app.run_server(debug=True)
