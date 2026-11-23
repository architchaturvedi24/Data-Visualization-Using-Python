
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Step 1: Load dataset
df = px.data.iris()

# Step 2: Create Dash Application
app = Dash(__name__)

# Step 3: Define Layout
app.layout = html.Div([
    html.H1("Iris Flower Analysis Dashboard"),

    html.Label("Select Flower Species"),

    dcc.Dropdown(
        id="species_dropdown",
        options=[
            {"label": "Setosa", "value": "setosa"},
            {"label": "Versicolor", "value": "versicolor"},
            {"label": "Virginica", "value": "virginica"}
        ],
        value="setosa",
        clearable=False
    ),

    dcc.Graph(id="iris_graph")
])

# Step 4: Create Callback
@app.callback(
    Output(component_id='iris_graph',
           component_property='figure'),

    Input(component_id='species_dropdown',
          component_property='value')
)

def update_figure(selected_species):

    # Filter Dataset
    filtered_df = df[df['species'] == selected_species]

    # Generate Graph
    fig = px.scatter(
        filtered_df,
        x="sepal_width",
        y="sepal_length",
        color="species",
        title=f"Iris Analysis: {selected_species}"
    )

    return fig


# Step 5: Run Application
if __name__ == '__main__':
    app.run(debug=True)
