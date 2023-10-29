import json
import os
from datetime import datetime

# Путь к файлу для хранения заметок
data_file = 'notes.json'
# Функция для добавления заметки
def add_note(title, message):
    # Создаем заметку
    note = {
        'id': len(notes) + 1,
        'title': title,
        'message': message,
        'timestamp': datetime.now().isoformat()
    }
    # Добавляем заметку в список
    notes.append(note)
    print('Заметка успешно добавлена.')
# Функция для вывода всех заметок
def list_notes():
    for note in notes:
        print(f'{note["id"]}. {note["title"]} ({note["timestamp"]})')

# Функция для удаления заметки по ID
def delete_note(note_id):
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            print(f'Заметка с ID {note_id} успешно удалена.')
            return
    print(f'Заметка с ID {note_id} не найдена.')

# Функция для сохранения заметок в JSON файл
def save_notes():
    with open(data_file, 'w') as file:
        json.dump(notes, file)

# Проверяем, существует ли файл с данными, и загружаем заметки
if os.path.exists(data_file):
    with open(data_file, 'r') as file:
        notes = json.load(file)
else:
    notes = []
# Основной цикл приложения
while True:
    print('Выберите действие:')
    print('1. Добавить заметку')
    print('2. Вывести список заметок')
    print('3. Удалить заметку')
    print('4. Выйти')
    choice = input()

    if choice == '1':
        title = input('Введите заголовок заметки: ')
        message = input('Введите текст заметки: ')
        add_note(title, message)
        save_notes()
    elif choice == '2':
        list_notes()
    elif choice == '3':
        note_id = int(input('Введите ID заметки для удаления: '))
        delete_note(note_id)
        save_notes()
    elif choice == '4':
        print('До свидания!')
        break
    else:
        print('Неверный выбор. Попробуйте еще раз.')
