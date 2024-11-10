# Домашнее задание 2 по конфигурационному управлению
## Лысаков Ярослав, ИКБО-50-23
## Этапы запуска проекта репозитория
1. Скачать программу [Graphviz](https://graphviz.org/download/) для визуализации графов зависимостей.
2. Загрузить репозиторий на компьютер. 'git clone https://github.com/YarLys/DependenciesVisualizer'
3. Перейти в каталог репозитория. 'cd DependenciesVisualizer'
4. Отредактировать yaml файл, указав в нём путь к репозиторию для построения графа и хэш файла.
5. Запустить main.py 

## Описание задания
Разработать инструмент командной строки для визуализации графа зависимостей, включая транзитивные зависимости. Сторонние средства для получения зависимостей использовать нельзя.
Зависимости определяются для git-репозитория. Для описания графа зависимостей используется представление Graphviz. Визуализатор должен выводить результат на экран в виде графического изображения графа.
Построить граф зависимостей для коммитов, в узлах которого находятся списки файлов и папок. Граф необходимо строить только для тех коммитов, где фигурирует файл с заданным хеш-значением.

### Конфигурационый файл
Конфигурационный файл имеет формат yaml и содержит:
• Путь к программе для визуализации графов.
• Путь к анализируемому репозиторию.
• Файл с заданным хеш-значением в репозитории.

## Реализованные функции
# def init(path)
Функция, которая считывает yaml файл и получает из него необходимые данные.
# def get_commits()
Функция, которая при помощи ввода команды в терминале получает список всех коммитов и сохраняет их в удобном для последующей работы формате.
# def select_commits()
Функция, которая отбирает коммиты, в которых фигурирует файл с заданным хэш значением.
# def check_dirs()
Функция, которая проходится по всем объектам коммита рекурсивно. Проверяет совпадение хэшей файлов с искомым.
# def build_graph()
Функция, которая по отобранным коммитам формирует файл с расширением .dot.
# def show_graph(dot_graph)
Функция, которая создаёт изображение по описанию графа и демонстрирует его.

## Примеры работы программы
Граф зависимостей тестового репозитория
![dependencies](https://github.com/user-attachments/assets/d50516c5-2889-4a82-af4a-3b006a56a5c6)

Граф зависимостей для репозиотрия https://github.com/YarLys/SchoolList_Client с заданным хэшом файла MainActivity.java
![dependencies](https://github.com/user-attachments/assets/cadb5d76-e234-41c9-845f-39aabac15b1a)

## Тестирование программы
![image](https://github.com/user-attachments/assets/d756d2f1-3b76-44e0-83da-06ee6c047843)
![image](https://github.com/user-attachments/assets/a77be8c5-6dd5-4cf2-88ea-fbbb61f7837b)
