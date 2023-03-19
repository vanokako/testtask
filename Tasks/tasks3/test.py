from Tasks.tasks1.test import get_customers
from Tasks.tasks2.test import get_correct_filenames

TECHNIC = [
    ('Ноутбук', 1500, 'Татьяна', '89002001020'),
    ('Смартфон', 500, 'Анна', '89202202325'),
    ('Проектор ', 300, 'Андрей', '89505205656'),
    ('Принтер', 750, 'Игорь', '89303303236'),
    ('Планшет', 2300, 'Игорь', '89303303236'),
    ('Смартфон', 1000, 'Андрей', '89505205656'),
    ('Ноутбук', 4800, 'Татьяна', '89002001020'),
    ('Наушники', 780, 'Марина', '89562002350'),
    ('Сканер', 550, 'Сергей', '89808564559'),
    ('Планшет', 1200, 'Анна', '89202202325'),
    ('Ноутбук', 1100, 'Игорь', '89303303236'),
    ('Смартфон', 3500, 'Татьяна', '89002001020')
]

FILENAMES_WITH_EXTENSIONS = ["tes.txt", "QwErTyAsdFGC.jpeg", "shortname.a"]
FILENAMES_WITHOUT_EXTENSIONS = ["tes", "QwErTyAsdFhC.jpg", "shortname"]


if __name__ == "__main__":
    customers = get_customers(TECHNIC)
    for customer in customers:
        print(customer)

    print(get_correct_filenames(FILENAMES_WITH_EXTENSIONS, use_extension=True))
    print(get_correct_filenames(FILENAMES_WITHOUT_EXTENSIONS))
