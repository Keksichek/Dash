# Dash
![image](https://github.com/user-attachments/assets/3e748e51-dfc0-4f1f-a42e-b3983d499cc0)
### Инструкция по использованию панели мониторинга погодных данных

Этот проект — интерактивная панель для анализа и визуализации данных о погоде в населенных пунктах Хабаровского края. На панели представлены данные о температуре, давлении, облачности, явлениях и ветре в дневное и вечернее время для разных населенных пунктов, что позволяет исследовать погодные тренды и особенности в разных местах и временных диапазонах.

#### Запуск приложения

1. Скачайте репозиторий на свой компьютер:
   ```bash
   git clone https://github.com/ваш_репозиторий/weather-dashboard
   cd weather-dashboard
   ```

2. Установите все зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Запустите приложение:
   ```bash
   python app.py
   ```

4. Откройте веб-браузер и перейдите по адресу `http://127.0.0.1:8050`.

#### Функционал приложения

##### 1. Выбор города

- В верхней части панели представлен выпадающий список **"Выберите город"**. Вы можете выбрать один из городов, данные по которому загружены в систему. После выбора город фильтруется, и обновляются все визуализированные данные на панели.

##### 2. Установка временного периода

- Используйте компонент **"Выберите период"** для выбора диапазона дат, за который вы хотите просмотреть данные. Установите начальную и конечную дату для фильтрации данных по времени. Графики и таблицы будут отображать информацию только за выбранный период.

##### 3. Выбор погодного параметра

- В выпадающем списке **"Выберите параметр для отображения"** выберите один из следующих погодных параметров:
  - Температура (день)
  - Температура (вечер)
  - Давление (день)
  - Давление (вечер)
  - Облачность (день)
  - Облачность (вечер)
  - Явления (день)
  - Явления (вечер)
  - Ветер (день)
  - Ветер (вечер)
  
  Выбранный параметр отобразится на графике для выбранного города и периода времени.

##### 4. Отображение скользящего среднего

- Отметьте флажок **"Показать скользящее среднее (3 дня)"**, чтобы добавить на график линию скользящего среднего за три дня. Это поможет сгладить колебания данных и лучше рассмотреть общие тренды.

##### 5. Выбор типа графика

- Компонент **"Тип графика"** позволяет выбрать тип визуализации:
  - Линейный
  - Столбчатый
  
  Выберите один из типов для отображения данных в виде линейного графика или столбчатой диаграммы.

##### 6. Выбор цветовой темы

- В выпадающем списке **"Цветовая тема"** выберите один из вариантов оформления графика:
  - Светлая (по умолчанию)
  - Темная
  - Серая

##### 7. График погодных данных

- Основная часть панели — интерактивный график, отображающий данные по выбранному параметру, типу графика и цветовой теме. График обновляется автоматически при изменении любого из настроек.

##### 8. Таблица с данными

- Под графиком расположена таблица **"Данные по погоде для выбранного города"**, которая отображает все доступные погодные данные за выбранный период. Таблица обновляется автоматически при изменении города или диапазона дат.

#### Пример использования

1. Выберите город в выпадающем списке.
2. Установите интересующий вас период дат.
3. Выберите параметр, например, **"Температура (день)"**.
4. Если требуется, добавьте скользящее среднее для сглаживания данных.
5. Выберите тип графика — **"Линейный"** или **"Столбчатый"**.
6. Измените цветовую тему по своему вкусу.
7. Просмотрите график и таблицу данных для анализа.

#### Примечания

- Данные в проекте должны находиться в формате CSV и иметь правильные заголовки для корректного отображения.
- Если возникнут ошибки при запуске, убедитесь, что все зависимости установлены, а путь к файлу данных указан правильно в `app.py`.

#### Лицензия

Проект находится под лицензией MIT.

---

Этот README-файл служит для быстрого знакомства с панелью управления и позволяет легко настроить и запустить её для визуализации погодных данных.