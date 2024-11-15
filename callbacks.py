from dash import Input, Output
import plotly.express as px
import pandas as pd

def register_callbacks(app, weather_data):

    @app.callback(
        Output('weather-graph', 'figure'),
        [
            Input('city-dropdown', 'value'),
            Input('parameter-dropdown', 'value'),
            Input('date-picker-range', 'start_date'),
            Input('date-picker-range', 'end_date'),
            Input('moving-average', 'value'),
            Input('graph-type', 'value'),
            Input('color-theme', 'value')
        ]
    )
    def update_graph(selected_city, selected_parameter, start_date, end_date, moving_average, graph_type, color_theme):
        # Логика фильтрации и построения графика

    @app.callback(
        Output('table-container', 'children'),
        [
            Input('city-dropdown', 'value'),
            Input('date-picker-range', 'start_date'),
            Input('date-picker-range', 'end_date')
        ]
    )
    def update_table(selected_city, start_date, end_date):
        # Логика фильтрации и обновления таблицы
