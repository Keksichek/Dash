from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# Загрузка данных и установка названий колонок на русском языке
file_path = 'Путь к файлу.csv'  # Замените на путь к вашему файлу
column_names = [
    'ID города', 'Дата', 'Температура (день)', 'Давление (день)', 'Облачность (день)',
    'Явление (день)', 'Ветер (день)', 'Температура (вечер)', 'Давление (вечер)',
    'Облачность (вечер)', 'Явление (вечер)', 'Ветер (вечер)'
]
weather_data = pd.read_csv(file_path, names=column_names)
weather_data['Дата'] = pd.to_datetime(weather_data['Дата'])  # Преобразование даты

# Инициализация приложения
app = Dash(__name__)

# Уникальные идентификаторы городов
cities = weather_data['ID города'].unique()


# Функция для создания стилизованной таблицы из данных
def generate_table(dataframe):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col, style={'padding': '10px', 'border-bottom': '2px solid black'}) for col in
                     dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col], style={'padding': '10px', 'text-align': 'center'}) for col in
                dataframe.columns
            ]) for i in range(len(dataframe))
        ])
    ], style={'border-collapse': 'collapse', 'width': '100%', 'margin-top': '20px'})


# Макет приложения
app.layout = html.Div([
    html.H1("Погода в населенных пунктах Хабаровского края"),

    # Выпадающий список для выбора города
    html.Label("Выберите город:"),
    dcc.Dropdown(
        id='city-dropdown',
        options=[{'label': f'Город {city}', 'value': city} for city in cities],
        value=cities[0]
    ),

    # Диапазон дат
    html.Br(),
    html.Label("Выберите период:"),
    dcc.DatePickerRange(
        id='date-picker-range',
        start_date=weather_data['Дата'].min(),
        end_date=weather_data['Дата'].max(),
        display_format='YYYY-MM-DD'
    ),

    # Выбор параметра для отображения
    html.Br(),
    html.Label("Выберите параметр для отображения:"),

    dcc.Dropdown(
        id='parameter-dropdown',
        options=[
            {'label': 'Температура (день, °C)', 'value': 'Температура (день)'},
            {'label': 'Температура (вечер, °C)', 'value': 'Температура (вечер)'},
            {'label': 'Давление (день, мм рт. ст.)', 'value': 'Давление (день)'},
            {'label': 'Давление (вечер, мм рт. ст.)', 'value': 'Давление (вечер)'},
            {'label': 'Облачность (день)', 'value': 'Облачность (день)'},
            {'label': 'Облачность (вечер)', 'value': 'Облачность (вечер)'},
            {'label': 'Явления (день)', 'value': 'Явление (день)'},
            {'label': 'Явления (вечер)', 'value': 'Явление (вечер)'},
            {'label': 'Ветер (день)', 'value': 'Ветер (день)'},
            {'label': 'Ветер (вечер)', 'value': 'Ветер (вечер)'}
        ],
        value='Температура (день)'
    ),

    # Скользящее среднее
    html.Br(),
    dcc.Checklist(
        id='moving-average',
        options=[{'label': 'Показать скользящее среднее (3 дня)', 'value': 'show'}],
        value=[]
    ),

    # Тип графика
    html.Br(),
    html.Label("Тип графика:"),
    dcc.RadioItems(
        id='graph-type',
        options=[
            {'label': 'Линейный', 'value': 'line'},
            {'label': 'Столбчатый', 'value': 'bar'}
        ],
        value='line',
        inline=True
    ),

    # Цветовая тема
    html.Br(),
    html.Label("Цветовая тема:"),
    dcc.Dropdown(
        id='color-theme',
        options=[
            {'label': 'Светлая', 'value': 'plotly_white'},
            {'label': 'Темная', 'value': 'plotly_dark'},
            {'label': 'Серая', 'value': 'ggplot2'}
        ],
        value='plotly_white'
    ),

    # Компонент графика
    dcc.Graph(id='weather-graph'),

    # Заголовок для таблицы
    html.H4("Данные по погоде для выбранного города"),

    # Динамическая таблица, которая будет обновляться при выборе города
    html.Div(id='table-container')
])


# Callback для обновления графика
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
    # Фильтрация данных по городу и дате
    city_data = weather_data[(weather_data['ID города'] == selected_city) &
                             (weather_data['Дата'] >= start_date) &
                             (weather_data['Дата'] <= end_date)]

    # Если выбрано скользящее среднее, рассчитываем его
    if 'show' in moving_average:
        city_data['Moving_Avg'] = city_data[selected_parameter].rolling(window=3).mean()
        y_data = 'Moving_Avg'
    else:
        y_data = selected_parameter

    # Создание графика на основе выбора типа
    if graph_type == 'line':
        fig = px.line(city_data, x='Дата', y=y_data, title=f'{selected_parameter} для города {selected_city}')
    elif graph_type == 'bar':
        fig = px.bar(city_data, x='Дата', y=y_data, title=f'{selected_parameter} для города {selected_city}')

    fig.update_layout(template=color_theme, transition_duration=500)
    return fig


# Callback для обновления таблицы
@app.callback(
    Output('table-container', 'children'),
    [Input('city-dropdown', 'value'), Input('date-picker-range', 'start_date'), Input('date-picker-range', 'end_date')]
)
def update_table(selected_city, start_date, end_date):
    # Фильтрация данных по выбранному городу и дате
    city_data = weather_data[(weather_data['ID города'] == selected_city) &
                             (weather_data['Дата'] >= start_date) &
                             (weather_data['Дата'] <= end_date)]
    return generate_table(city_data)


# Запуск сервера приложения
if __name__ == '__main__':
    app.run_server(debug=True)
