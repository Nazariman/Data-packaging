import json
import pickle

# Основна структура: назва гурту -> список альбомів
music_data = {}

def add_band(name):
    if name not in music_data:
        music_data[name] = []
        print(f"Гурт '{name}' додано.")
    else:
        print(f"Гурт '{name}' вже існує.")

def add_album(band, album):
    if band in music_data:
        music_data[band].append(album)
        print(f"Альбом '{album}' додано до гурту '{band}'.")
    else:
        print(f"Гурту '{band}' не знайдено. Спочатку додайте гурт.")

def save_json(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(music_data, f, ensure_ascii=False, indent=4)
    print("Дані збережено у форматі JSON.")

def load_json(filename):
    global music_data
    with open(filename, 'r', encoding='utf-8') as f:
        music_data = json.load(f)
    print("Дані завантажено з JSON.")

def save_pickle(filename):
    with open(filename, 'wb') as f:
        pickle.dump(music_data, f)
    print("Дані збережено у форматі pickle.")

def load_pickle(filename):
    global music_data
    with open(filename, 'rb') as f:
        music_data = pickle.load(f)
    print("Дані завантажено з pickle.")

# Приклад використання:
if __name__ == "__main__":
    add_band("Okean Elzy")
    add_album("Okean Elzy", "Gloria")
    add_album("Okean Elzy", "Supersymetriya")

    add_band("The Beatles")
    add_album("The Beatles", "Abbey Road")

    save_json("bands.json")
    save_pickle("bands.pkl")

    # load_json("bands.json")
    # load_pickle("bands.pkl")