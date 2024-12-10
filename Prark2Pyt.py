# Данные пользователей и предметов
users = [
    {'username': 'student1', 'password': '12345', 'role': 'user', 'class': '10A', 'history': []},
    {'username': 'admin', 'password': 'admin', 'role': 'admin'}
]

subjects = [
    {'subject': 'Математика', 'teacher': 'Иванов И.И.', 'lessons_count': 30, 'rating': 4.8},
    {'subject': 'Физика', 'teacher': 'Петров П.П.', 'lessons_count': 25, 'rating': 4.5},
]

# Вспомогательные функции
def login():
    print("Добро пожаловать в учебную систему!")
    username = input("Логин: ")
    password = input("Пароль: ")
    for user in users:
        if user['username'] == username and user['password'] == password:
            return user
    print("Неверный логин или пароль. Попробуйте снова.")
    return None

def print_menu(role):
    if role == 'user':
        print("\nВыберите действие:")
        print("1. Просмотреть доступные предметы")
        print("2. Найти предмет по учителю")
        print("3. Сортировать предметы по количеству уроков")
        print("4. Фильтрация предметов по критериям")
        print("5. Посмотреть историю посещений")
        print("6. Изменить пароль")
        print("7. Записать посещение урока")
        print("8. Выйти")
    elif role == 'admin':
        print("\nВыберите действие:")
        print("1. Добавить предмет")
        print("2. Удалить предмет")
        print("3. Редактировать предмет")
        print("4. Управление пользователями")
        print("5. Выйти")

# Функции для пользователей
def view_subjects():
    print("\nСписок доступных предметов:")
    print("{:<20} {:<20} {:<15} {:<10}".format("Предмет", "Учитель", "Уроков", "Рейтинг"))
    print("-" * 65)
    for subj in subjects:
        print("{:<20} {:<20} {:<15} {:<10}".format(subj['subject'], subj['teacher'], subj['lessons_count'], subj['rating']))

def search_by_teacher():
    teacher_name = input("Введите имя учителя для поиска: ")
    results = list(filter(lambda subj: teacher_name in subj['teacher'], subjects))
    if results:
        print("\nРезультаты поиска:")
        print("{:<20} {:<20} {:<15} {:<10}".format("Предмет", "Учитель", "Уроков", "Рейтинг"))
        print("-" * 65)
        for subj in results:
            print("{:<20} {:<20} {:<15} {:<10}".format(subj['subject'], subj['teacher'], subj['lessons_count'], subj['rating']))
    else:
        print("Предметы с таким учителем не найдены.")

def sort_by_lessons():
    sorted_subjects = sorted(subjects, key=lambda subj: subj['lessons_count'], reverse=True)
    print("\nПредметы, отсортированные по количеству уроков:")
    print("{:<20} {:<20} {:<15} {:<10}".format("Предмет", "Учитель", "Уроков", "Рейтинг"))
    print("-" * 65)
    for subj in sorted_subjects:
        print("{:<20} {:<20} {:<15} {:<10}".format(subj['subject'], subj['teacher'], subj['lessons_count'], subj['rating']))

def filter_subjects():
    teacher_name = input("Введите имя учителя для фильтрации (оставьте пустым для пропуска): ")
    min_lessons = input("Введите минимальное количество уроков (оставьте пустым для пропуска): ")
    
    filtered_subjects = subjects
    if teacher_name:
        filtered_subjects = list(filter(lambda subj: teacher_name in subj['teacher'], filtered_subjects))
    if min_lessons.isdigit():
        filtered_subjects = list(filter(lambda subj: subj['lessons_count'] >= int(min_lessons), filtered_subjects))
    
    if filtered_subjects:
        print("\nРезультаты фильтрации:")
        print("{:<20} {:<20} {:<15} {:<10}".format("Предмет", "Учитель", "Уроков", "Рейтинг"))
        print("-" * 65)
        for subj in filtered_subjects:
            print("{:<20} {:<20} {:<15} {:<10}".format(subj['subject'], subj['teacher'], subj['lessons_count'], subj['rating']))
    else:
        print("Нет предметов, соответствующих критериям.")

def update_password(user):
    new_password = input("Введите новый пароль: ")
    user['password'] = new_password
    print("Пароль успешно изменен.")

def view_history(user):
    print("\nИстория посещений:")
    if user['history']:
        for visit in user['history']:
            print(f"Предмет: {visit}")
    else:
        print("История пуста.")

def add_to_history(user):
    print("\nСписок доступных предметов для записи в историю:")
    print("{:<20} {:<20} {:<15} {:<10}".format("Предмет", "Учитель", "Уроков", "Рейтинг"))
    print("-" * 65)
    for subj in subjects:
        print("{:<20} {:<20} {:<15} {:<10}".format(subj['subject'], subj['teacher'], subj['lessons_count'], subj['rating']))
    
    subject_name = input("Введите название предмета для записи посещения: ")
    for subj in subjects:
        if subj['subject'] == subject_name:
            user['history'].append(subject_name)
            print(f"Посещение предмета '{subject_name}' добавлено в историю.")
            return
    print("Предмет не найден.")

# Функции для админа
def add_subject():
    subject = input("Название предмета: ")
    teacher = input("Имя учителя: ")
    lessons_count = int(input("Количество уроков: "))
    rating = float(input("Рейтинг предмета: "))
    subjects.append({'subject': subject, 'teacher': teacher, 'lessons_count': lessons_count, 'rating': rating})
    print("Предмет успешно добавлен.")

def delete_subject():
    subject = input("Введите название предмета для удаления: ")
    global subjects
    subjects = list(filter(lambda subj: subj['subject'] != subject, subjects))
    print("Предмет успешно удален.")

def edit_subject():
    subject = input("Введите название предмета для редактирования: ")
    for subj in subjects:
        if subj['subject'] == subject:
            subj['teacher'] = input("Новое имя учителя: ")
            subj['lessons_count'] = int(input("Новое количество уроков: "))
            subj['rating'] = float(input("Новый рейтинг: "))
            print("Данные предмета обновлены.")
            return
    print("Предмет не найден.")

def manage_users():
    global users  
    print("\nСписок пользователей:")
    for user in users:
        print(f"{user['username']} - Роль: {user['role']}")
    action = input("Добавить/Удалить пользователя (add/remove): ").strip().lower()
    if action == 'add':
        username = input("Логин: ")
        password = input("Пароль: ")
        role = input("Роль (user/admin): ")
        users.append({'username': username, 'password': password, 'role': role})
        print("Пользователь успешно добавлен.")
    elif action == 'remove':
        username = input("Введите логин для удаления: ").strip()
        if not username:
            print("Ошибка: логин не может быть пустым.")
            return
        users = list(filter(lambda user: user['username'] != username, users))
        print("Пользователь успешно удален.")

# Основной цикл
def main():
    while True:
        user = login()
        if user:
            while True:
                print_menu(user['role'])
                choice = input("Ваш выбор: ")
                if user['role'] == 'user':
                    if choice == '1':
                        view_subjects()
                    elif choice == '2':
                        search_by_teacher()
                    elif choice == '3':
                        sort_by_lessons()
                    elif choice == '4':
                        filter_subjects()
                    elif choice == '5':
                        view_history(user)
                    elif choice == '6':
                        update_password(user)
                    elif choice == '7':
                        add_to_history(user) 
                    elif choice == '8':
                        print("Выход из системы.")
                        break
                    else:
                        print("Неверный выбор. Попробуйте снова.")
                elif user['role'] == 'admin':
                    if choice == '1':
                        add_subject()
                    elif choice == '2':
                        delete_subject()
                    elif choice == '3':
                        edit_subject()
                    elif choice == '4':
                        manage_users()
                    elif choice == '5':
                        print("Выход из системы.")
                        break
                    else:
                        print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
