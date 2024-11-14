from dash import Dash, html, dcc, Input, Output, callback
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import datetime
import requests
from statsmodels.sandbox.regression.ols_anova_original import names

API_KEY = "4bdffe70bdc080014891f627877a614b"
CITIES = [
    {"name": "Хабаровск", "lat": 48.4808, "lon": 135.0718},
    {"name": "Комсомольск-на-Амуре", "lat": 50.5503, "lon": 137.0084},
    {"name": "Николаевск-на-Амуре", "lat": 53.1466, "lon": 140.7135},
    {"name": "Советская Гавань", "lat": 48.9667, "lon": 140.2833},
    {"name": "Амурск", "lat": 50.2223, "lon": 136.9004}
]

# Функция для получения текущей погоды
def fetch_current_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={city['lat']}&lon={city['lon']}&appid={API_KEY}&units=metric&lang=ru"
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        return {
            "Температура": weather_data["main"]["temp"],
            "Влажность": weather_data["main"]["humidity"],
            "Скорость ветра": weather_data["wind"]["speed"],
            "Описание": weather_data["weather"][0]["description"].capitalize()
        }
    else:
        return {}

# Функция для получения прогноза погоды
def fetch_weather_forecast(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={city['lat']}&lon={city['lon']}&appid={API_KEY}&units=metric&lang=ru"
    response = requests.get(url)
    if response.status_code == 200:
        forecast_data = response.json()["list"]
        forecast_list = [{
            "Дата и время": datetime.datetime.fromtimestamp(item["dt"]),
            "Температура (°C)": item["main"]["temp"],
            "Влажность (%)": item["main"]["humidity"],
            "Скорость ветра (м/с)": item["wind"]["speed"],
            "Осадки (мм)": item.get("rain", {}).get("3h", 0)
        } for item in forecast_data]
        return pd.DataFrame(forecast_list)
    else:
        return pd.DataFrame()

app = Dash(name)

app.layout = html.Div([
    # Карта с населенными пунктами
    html.Div([
        dcc.Graph(id='city-map')
    ], style={'width': '100%', 'display': 'inline-block', 'vertical-align': 'top'}),

    # Карточки с текущей погодой для каждого города
    html.Div(id='weather-cards', style={
        'width': '100%', 'display': 'flex', 'flex-wrap': 'wrap', 'padding': '10px', 'justify-content': 'center'
    }),

    # Параметры выбора
    html.Div([
        html.Label("Выберите параметр погоды:"),
        dcc.Dropdown(
            id='weather-parameter',
            options=[
                {"label": "Температура (°C)", "value": "Температура (°C)"},
                {"label": "Влажность (%)", "value": "Влажность (%)"},
                {"label": "Скорость ветра (м/с)", "value": "Скорость ветра (м/с)"},
                {"label": "Осадки (мм)", "value": "Осадки (мм)"}
            ],
            value="Температура (°C)"
        ),
    ], style={'width': '49%', 'display': 'inline-block', 'padding': '10px'}),

    # График прогноза погоды
    html.Div([
        dcc.Graph(id='weather-forecast-graph')
    ], style={'width': '100%', 'display': 'inline-block', 'padding': '0 20'}),

    # Выбор дня
    html.Div(dcc.Slider(
        id='day-slider',
        min=0,
        max=5,
        step=1,
        value=0,
        marks={i: (datetime.date.today() + datetime.timedelta(days=i)).strftime('%Y-%m-%d') for i in range(6)}
    ), style={'width': '49%', 'padding': '0px 20px 20px 20px'})
])

# Callback для обновления карты с заметными метками
@app.callback(
    Output('city-map', 'figure'),
    Input('weather-parameter', 'value')
)
def update_map(weather_parameter):
    fig = px.scatter_mapbox(
        pd.DataFrame(CITIES),
        lat="lat",
        lon="lon",
        hover_name="name",
        zoom=5,
        center={"lat": 50.0, "lon": 136.0}
    )
    fig.update_layout(
        mapbox_style="open-street-map",
        margin={"r":0,"t":0,"l":0,"b":0}
    )
    fig.update_traces(marker=dict(size=12, color="blue", symbol="circle"))
    return fig

# Callback для отображения карточек с погодой
@app.callback(
    Output('weather-cards', 'children'),
    Input('city-map', 'clickData')
)
def update_weather_cards(clickData):
    cards = []
    for city in CITIES:
        weather = fetch_current_weather(city)
        cards.append(html.Div([
            html.H4(city['name']),
            html.P(f"Температура: {weather.get('Температура', 'N/A')}°C"),
            html.P(f"Влажность: {weather.get('Влажность', 'N/A')}%"),
            html.P(f"Скорость ветра: {weather.get('Скорость ветра', 'N/A')} м/с"),
            html.P(f"Описание: {weather.get('Описание', 'N/A')}")
        ], style={
            'border': '1px solid #ccc', 'border-radius': '5px', 'padding': '10px', 'margin': '5px',
            'width': '180px', 'box-shadow': '2px 2px 5px rgba(0,0,0,0.2)'
        }))
    return cards

# Callback для обновления прогноза погоды на выбранный день
@app.callback(
    Output('weather-forecast-graph', 'figure'),
    Input('day-slider', 'value'),
    Input('weather-parameter', 'value'),
    Input('city-map', 'clickData')
)
def update_forecast(day_offset, weather_parameter, clickData):
    selected_city = CITIES[0]  # Default to the first city if none is selected
    if clickData:
        city_name = clickData['points'][0]['hovertext']
        selected_city = next((city for city in CITIES if city["name"] == city_name), CITIES[0])

    forecast_df = fetch_weather_forecast(selected_city)
    selected_date = datetime.date.today() + datetime.timedelta(days=day_offset)
    day_data = forecast_df[forecast_df['Дата и время'].dt.date == selected_date]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=day_data['Дата и время'],
        y=day_data[weather_parameter],
        mode='lines+markers',
        hoverinfo='x+y',
        line=dict(width=2),
        marker=dict(size=6)
    ))

    fig.update_layout(
        title=f"{weather_parameter} в {selected_city['name']} на {selected_date.strftime('%Y-%m-%d')}",
        xaxis_title="Время",
        yaxis_title=weather_parameter,
        hovermode="x unified",
        margin={"r": 0, "t": 30, "l": 0, "b": 0}
    )

    return fig

if name == 'main':
    app.run(debug=True)
