# Асинхронный парсер PEP.
### О проекте.
Парсер выводит собранную информацию в два файла `.csv`:
- В первый файл выводится список всех PEP: номер, название и статус.
- Второй файл содержит сводку по статусам PEP — сколько найдено документов в каждом статусе (статус, количество). В последней строке этого файла в колонке «Статус» стоит слово Total, а в колонке «Количество» — общее количество всех документов.
___
### При создании проекта использовалось:
- язык программирования Python 3;
- фреймворк Scrapy.
___
Чтобы развернуть проект необходимо следующие:
- Клонировать репозиторий со своего GitHub и перейти в него в командной строке:

```
git clone git@github.com:levisserena/scrapy_parser_pep.git
```
>*Активная ссылка на репозиторий под этой кнопкой* -> [КНОПКА](https://github.com/levisserena/scrapy_parser_pep)
- Перейдите в папку с проектом:
```
cd scrapy_parser_pep
```
- Создать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/bin/activate
```

- Запустите парсер:

```
scrapy crawl pep
```
___
### Результаты парсинга:
Файлы сохранятся в директорию `result`.
Названия файлов с меткой времени. Например:
```
pep_2024-09-25T08-18-44.csv
status_summary_2024-09-25_12-19-01.csv
```
___
### Информация об авторах.
Акчурин Лев Ливатович.<br>Студент курса Яндекс Практикума Python-разработчик плюс.<br>
[Страничка GitHub](https://github.com/levisserena)
___
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)