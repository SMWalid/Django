import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import requests
import pandas as pd

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Fetch data from the Django API
def fetch_data():
    sources_response = requests.get("http://127.0.0.1:8000/api/sources/")
    datasets_response = requests.get("http://127.0.0.1:8000/api/physicaldatasets/")
    
    sources = sources_response.json()
    datasets = datasets_response.json()

    return sources, datasets

sources, datasets = fetch_data()

# Build the layout of the Dash app
app.layout = dbc.Container([
    html.H1("Sources"),
    html.Ul([html.Li(f"{source['source_name']} ({source['source_type']})") for source in sources]),
    
    html.H1("Physical Data Sets"),
    html.Ul([html.Li(f"{dataset['pds_path']} (Source ID: {dataset['pds_source']})") for dataset in datasets])
])

# Run the Dash app
if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
