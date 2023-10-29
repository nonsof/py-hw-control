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
