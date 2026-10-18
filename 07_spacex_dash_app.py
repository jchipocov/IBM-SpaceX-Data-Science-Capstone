# SpaceX Falcon 9 Launch Records Dashboard - IBM Skills Network lab
import pandas as pd
import dash
from dash import html, dcc, Input, Output
import plotly.express as px

# The CSV must be in the same folder as this script.
spacex_df = pd.read_csv('spacex_launch_dash.csv')

# Payload values are numeric in the lab dataset.
min_payload = spacex_df['Payload Mass (kg)'].min()
max_payload = spacex_df['Payload Mass (kg)'].max()

# Build options directly from the launch sites in the CSV.
site_options = [{'label': 'All Sites', 'value': 'ALL'}] + [
    {'label': site, 'value': site}
    for site in sorted(spacex_df['Launch Site'].dropna().unique())
]

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(
        'SpaceX Launch Records Dashboard',
        style={'textAlign': 'center', 'color': '#503D36', 'fontSize': 40}
    ),

    # TASK 1: launch site dropdown
    dcc.Dropdown(
        id='site-dropdown',
        options=site_options,
        value='ALL',
        placeholder='Select a Launch Site here',
        searchable=True,
        clearable=False
    ),
    html.Br(),

    # TASK 2: success counts pie chart
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    html.P('Payload range (Kg):'),

    # TASK 3: payload mass range slider
    dcc.RangeSlider(
        id='payload-slider',
        min=0,
        max=10000,
        step=1000,
        value=[0, 10000],
        marks={i: str(i) for i in range(0, 10001, 2000)}
    ),
    html.Br(),

    # TASK 4: payload vs launch outcome scatter chart
    html.Div(dcc.Graph(id='success-payload-scatter-chart'))
])


# TASK 2: pie chart updates when the launch site changes
@app.callback(
    Output('success-pie-chart', 'figure'),
    Input('site-dropdown', 'value')
)
def update_pie_chart(entered_site):
    if entered_site == 'ALL':
        # class=1 means successful landing; sum counts successes by launch site.
        success_counts = (
            spacex_df.groupby('Launch Site', as_index=False)['class']
            .sum()
            .rename(columns={'class': 'Successful Launches'})
        )
        fig = px.pie(
            success_counts,
            values='Successful Launches',
            names='Launch Site',
            title='Successful Launches by Launch Site'
        )
    else:
        site_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        outcome_counts = (
            site_df['class']
            .value_counts()
            .reindex([0, 1], fill_value=0)
            .rename(index={0: 'Failed', 1: 'Successful'})
            .reset_index()
        )
        outcome_counts.columns = ['Outcome', 'Count']
        fig = px.pie(
            outcome_counts,
            values='Count',
            names='Outcome',
            title=f'Successful vs. Failed Launches at {entered_site}'
        )
    return fig


# TASK 4: scatter chart updates when site or payload range changes
@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    Input('site-dropdown', 'value'),
    Input('payload-slider', 'value')
)
def update_scatter_chart(entered_site, payload_range):
    low, high = payload_range
    filtered_df = spacex_df[
        spacex_df['Payload Mass (kg)'].between(low, high)
    ]
    if entered_site != 'ALL':
        filtered_df = filtered_df[filtered_df['Launch Site'] == entered_site]

    # Booster Version Category is provided in the IBM lab's dashboard CSV.
    fig = px.scatter(
        filtered_df,
        x='Payload Mass (kg)',
        y='class',
        color='Booster Version Category',
        title=f'Payload vs. Launch Outcome — {"All Sites" if entered_site == "ALL" else entered_site}',
        labels={'class': 'Landing Success (0 = Failed, 1 = Successful)'}
    )
    return fig


if __name__ == '__main__':
    # Compatible with Dash 3 and accessible via the lab's port-8050 preview.
    app.run(host='0.0.0.0', port=8050, debug=True)
