import random 
import json

wins = 0 
losses = 0 

def start_game(): 
    global wins, losses
    number = random.randint(1,100)
    attempts = 0

    while True: 
        try: 
            guess = int(input())
            attempts += 1

            if guess < number: 
                print("Більше!")
            elif guess > number: 
                print("Менше!")
            else: 
                print(f"Ви вгадали число {number} за {attempts} спроб!")
                if attempts <= 5: 
                    wins += 1
                    print("🎉 Ви перемогли!")
                else:
                    losses += 1
                    print("🤖 Переміг комп'ютер!")
                break
        except: 
            print("Введіть ціле число!")

def show_result(): 
    print(f"\n  Результати: \n\tПеремог - {wins}\n\tПрогращів - {losses}")

def save_data(): 
    with open("result.json", "w") as file: 
        json.dump({"wins": wins, "losses": losses}, file, indent=4)
        print("Результати збережено у файл.")

def load_data(): 
    global wins, losses
    try: 
        with open("result.json", "r") as file: 
            data = json.load(file)
            wins = data.get("wins", 0)
            losses = data.get("losses", 0)
            print("Результати завантажено з файлу.")
    except: 
        print("Файл не знайдено. Починаємо гру з нуля.")


def menu():
    load_data()
    while True:
        print("\n--- МЕНЮ ---")
        print("1. Почати нову гру")
        print("2. Показати результати")
        print("3. Зберегти результати")
        print("4. Завантажити результати")
        print("0. Вийти")
        
        choice = input("Ваш вибір: ")
        if choice == "1":
            start_game()
        elif choice == "2":
            show_result()
        elif choice == "3":
            save_data()
        elif choice == "4":
            load_data()
        elif choice == "0":
            print("👋 До побачення!")
            break
        else:
            print("❗ Невірний вибір. Спробуйте ще раз.")

# Запуск
if __name__ == "__main__":
    menu()
