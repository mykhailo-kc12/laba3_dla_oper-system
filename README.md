# laba3_dla_oper-system

Лабораторна робота №3 з дисципліни "Операційні системи".

## Опис

Проєкт містить дві консольні утиліти на Python:

- `dir_tool.py` - спрощений аналог команди `ls`
- `clean_tool.py` - пошук та видалення порожніх файлів і каталогів

## Структура проєкту

```text
laba3_dla_oper-system/
├── src/
│   ├── __init__.py
│   ├── dir_tool.py
│   └── clean_tool.py
├── .gitignore
└── README.md
```

## Запуск утиліти dir

```bash
python3 src/dir_tool.py
python3 src/dir_tool.py -l
python3 src/dir_tool.py -a
python3 src/dir_tool.py -l -a .
python3 src/dir_tool.py /tmp
```

## Запуск утиліти clean

```bash
python3 src/clean_tool.py
python3 src/clean_tool.py --files
python3 src/clean_tool.py --dirs
python3 src/clean_tool.py --delete-files
python3 src/clean_tool.py --delete-dirs
python3 src/clean_tool.py . --files --dirs
```

## Перевірка стилю

```bash
flake8 src
```

## Автор


Студент КС-12
ПІБ: Заваляэв Михайло Андрiйович


## Ручне тестування

Для перевірки роботи утиліт можна виконати такі команди:

```bash
python3 src/dir_tool.py
python3 src/dir_tool.py -l
python3 src/dir_tool.py -a
python3 src/clean_tool.py --files
python3 src/clean_tool.py --dirs

