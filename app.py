from dash import Dash, html, dcc
from data_loader import load_data
from layout import create_layout
from callbacks import register_callbacks

# Путь к файлу данных
file_path = 'Путь к файлу.csv'
weather_data = load_data(file_path)

# Инициализация приложения
app = Dash(__name__)

# Установка макета
app.layout = create_layout(weather_data)

# Регистрация обратных вызовов
register_callbacks(app, weather_data)

# Запуск приложения
if __name__ == '__main__':
    app.run_server(debug=True)
