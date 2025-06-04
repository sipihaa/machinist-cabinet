from flask import Flask, render_template, redirect, url_for, request, session, flash


app = Flask(__name__)
app.secret_key = 'slava_rodu_aue'

# Пример пользователей (в реальности берётся из БД)
USERS = {
    'ivan': {
        'password': '123',
        'name': 'Иван Иванов'
    }
}


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in USERS and USERS[username]['password'] == password:
            session['user'] = username
            return redirect(url_for('home'))
        else:
            flash('Неверный логин или password')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/')
def home():
    if 'user' not in session:
        return redirect(url_for('login'))

    # Демонстрационные данные
    return render_template(
        'home.html',
        name="Иван",
        last_training="01.04.2025",
        current_status="Активен",
        unread_materials=3
    )

@app.route('/personal_info')
def personal_info():
    # Демонстрационные данные для личной информации
    data = {
        'birth_date': '01.01.1985',
        'table_number': '123456',
        'enlistment_date': '01.06.2020',
        'enterprise': 'РЖД',
        'position': 'Машинист СПС',
        'appointment_date': '01.02.2021',
        'category': 'I',
        'email': 'machinist@example.com'
    }
    return render_template('personal_info.html', data=data)

@app.route('/route_lists')
def route_lists():
    # Пример списка маршрутных листов
    routes = [
        {'date': '01.04.2025', 'status': 'Активен', 'details': 'Маршрут №1'},
        {'date': '31.03.2025', 'status': 'Завершён', 'details': 'Маршрут №2'},
    ]
    return render_template('route_lists.html', routes=routes)

@app.route('/brigades')
def brigades():
    # Пример списка бригад
    brigades = [
        {'name': 'Бригада А', 'members': ['Иван', 'Пётр', 'Сергей']},
        {'name': 'Бригада Б', 'members': ['Алексей', 'Дмитрий']},
    ]
    return render_template('brigades.html', brigades=brigades)

@app.route('/events')
def events():
    # Пример журнала мероприятий
    events = [
        {'date': '01.04.2025', 'event': 'Предрейсовый инструктаж'},
        {'date': '31.03.2025', 'event': 'Очередной инструктаж'},
    ]
    return render_template('events.html', events=events)

@app.route('/training')
def training():
    # Пример списка инструктажей и учеб
    trainings = [
        {'name': 'Предрейсовый инструктаж'},
        {'name': 'Очередной инструктаж'},
        {'name': 'Инструктаж по изменению ТРА станций'},
        {'name': 'Техническая учеба'},
    ]
    return render_template('training.html', trainings=trainings)


if __name__ == '__main__':
    app.run(debug=True)
