from pymongo import MongoClient
from pymongo.errors import PyMongoError, ConnectionFailure
# Підключення до MongoDB
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["cats_database"]
    collection = db["cats"]
    # Перевірка з'єднання
    client.admin.command('ismaster')
    print("MongoDB підключено успішно")
except ConnectionFailure:
    print("Не вдалося підключитися до MongoDB, перевірте з'єднання")

def create_document():
    try:
        name = input("enter cat's name: ")
        age = int(input("cat's age"))
        features = input("enter cat's features: ")
        features = features.split(",")
        document = {"name": name, "age": age, "features": features}
        collection.insert_one(document)
    except PyMongoError as e:
        print("error with mongodb: {e}")
    
def read_all_documents():
    documents = list(collection.find({}))
    for doc in documents:
        print(doc)

def read_document_by_name():
    name = input("enter cat's name: ")
    document = collection.find_one({"name": name})
    print(document)

def update_document_age():
    try:
        name = input("Введіть ім'я тварини для оновлення віку: ")
        age = int(input("Введіть новий вік тварини: "))
        result = collection.update_one({"name": name}, {"$set": {"age": age}})
        if result.modified_count > 0:
            print("Вік тварини оновлено.")
        else:
            print("Тварина не знайдена або вік вже встановлено.")
    except PyMongoError as e:
        print(f"Помилка при роботі з MongoDB: {e}")
    except ValueError as e:
        print(f"Помилка введення: {e}")

def add_feature_to_document():
    try:
        name = input("Введіть ім'я тварини для додавання особливості: ")
        feature = input("Введіть особливість, яку хочете додати: ")
        result = collection.update_one({"name": name}, {"$addToSet": {"features": feature}})
        if result.modified_count > 0:
            print("Особливість додано до тварини.")
        else:
            print("Тварина не знайдена або особливість вже присутня.")
    except PyMongoError as e:
        print(f"Помилка при роботі з MongoDB: {e}")
    except ValueError as e:
        print(f"Помилка введення: {e}")

def delete_document():
    try:
        name = input("Введіть ім'я тварини для видалення: ")
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print("Документ видалено.")
        else:
            print("Тварина не знайдена.")
    except PyMongoError as e:
        print(f"Помилка при роботі з MongoDB: {e}")

def delete_all_documents():
    collection.delete_many({})
    print("Усі документи видалено.")

def main():
    while True:
        print("\nДоступні дії:")
        print("1 - Створити запис про тварину")
        print("2 - Показати всі записи")
        print("3 - Пошук запису за ім'ям тварини")
        print("4 - Оновити вік тварини")
        print("5 - Додати особливість до тварини")
        print("6 - Видалити запис про тварину")
        print("7 - Видалити всі записи")
        print("8 - Вийти")
        choice = input("Виберіть дію: ")
        if choice == "1":
            create_document()
        elif choice == "2":
            read_all_documents()
        elif choice == "3":
            read_document_by_name()
        elif choice == "4":
            update_document_age()
        elif choice == "5":
            add_feature_to_document()
        elif choice == "6":
            delete_document()
        elif choice == "7":
            delete_all_documents()
        elif choice == "8":
            break
        else:
            print("Некоректний вибір. Спробуйте ще раз.")
if __name__ == "__main__":
    main()