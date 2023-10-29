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
