import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load the formatted sales data
data_file = 'data/formatted_sales_data.csv'
df = pd.read_csv(data_file)

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Sort data by date
df = df.sort_values('date')

# Create a Dash application
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Soul Foods Pink Morsel Sales Visualizer'),

    dcc.Graph(
        id='sales-line-chart',
        figure=px.line(df, x='date', y='sales', title='Pink Morsel Sales Over Time', labels={'date': 'Date', 'sales': 'Sales'})
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
