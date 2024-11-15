from dash import html, dcc

def create_layout(weather_data):
    cities = weather_data['ID города'].unique()
    return html.Div([
        html.H1("Погода в населенных пунктах Хабаровского края"),
        html.Label("Выберите город:"),
        dcc.Dropdown(
            id='city-dropdown',
            options=[{'label': f'Город {city}', 'value': city} for city in cities],
            value=cities[0]
        ),
        # Остальные элементы интерфейса (дата-пикер, выпадающий список, графики)
    ])
