# laba3_dla_oper-system

Лабораторна робота №3 з дисципліни "Операційні системи".

## Опис

Проєкт містить дві консольні утиліти на Python:

- `dir_tool.py` - спрощений аналог команди `ls`;
- `clean_tool.py` - пошук та видалення порожніх файлів і каталогів.

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

Утиліта `dir_tool.py` показує вміст каталогу.

| Команда | Пояснення |
|---|---|
| `python3 src/dir_tool.py` | показує вміст поточної папки |
| `python3 src/dir_tool.py -l` | показує вміст поточної папки у детальному форматі |
| `python3 src/dir_tool.py -a` | показує вміст поточної папки разом із прихованими файлами |
| `python3 src/dir_tool.py -l -a .` | показує докладну інформацію про поточну папку разом із прихованими елементами |
| `python3 src/dir_tool.py /tmp` | показує вміст каталогу `/tmp` |

## Запуск утиліти clean

Утиліта `clean_tool.py` шукає порожні файли та каталоги.  
Якщо каталог не вказано, програма працює з поточною папкою.

| Команда | Пояснення |
|---|---|
| `python3 src/clean_tool.py` | показує порожні файли та порожні каталоги у поточній папці |
| `python3 src/clean_tool.py --files` | показує тільки порожні файли |
| `python3 src/clean_tool.py --dirs` | показує тільки порожні каталоги |
| `python3 src/clean_tool.py --delete-files` | видаляє порожні файли у поточній папці |
| `python3 src/clean_tool.py --delete-dirs` | видаляє порожні каталоги у поточній папці |
| `python3 src/clean_tool.py . --files --dirs` | показує порожні файли та порожні каталоги у поточній папці |

## Ручне тестування

Для безпечної перевірки утиліти `clean_tool.py` краще створити окрему тестову папку, щоб не змінювати файли основного проєкту.

### Створення тестових даних

```bash
mkdir -p test_data/empty_dir
touch test_data/empty_file.txt
```

| Команда | Пояснення |
|---|---|
| `mkdir -p test_data/empty_dir` | створює папку `test_data`, а всередині неї порожню папку `empty_dir` |
| `touch test_data/empty_file.txt` | створює порожній файл `empty_file.txt` у папці `test_data` |

Після цього структура тестової папки буде такою:

```text
test_data/
├── empty_dir/
└── empty_file.txt
```

### Перевірка пошуку

```bash
python3 src/clean_tool.py test_data
python3 src/clean_tool.py test_data --files
python3 src/clean_tool.py test_data --dirs
```

| Команда | Пояснення |
|---|---|
| `python3 src/clean_tool.py test_data` | показує порожні файли та порожні каталоги у папці `test_data` |
| `python3 src/clean_tool.py test_data --files` | показує тільки порожні файли у папці `test_data` |
| `python3 src/clean_tool.py test_data --dirs` | показує тільки порожні каталоги у папці `test_data` |

### Перевірка видалення

```bash
python3 src/clean_tool.py test_data --delete-files
python3 src/clean_tool.py test_data --delete-dirs
```

| Команда | Пояснення |
|---|---|
| `python3 src/clean_tool.py test_data --delete-files` | видаляє порожні файли у папці `test_data` |
| `python3 src/clean_tool.py test_data --delete-dirs` | видаляє порожні каталоги у папці `test_data` |

## Перевірка стилю

```bash
flake8 src
```

| Команда | Пояснення |
|---|---|
| `flake8 src` | перевіряє файли у папці `src` на відповідність правилам стилю Python |

## Автор

Студент КС-12
ПІБ:Заваляєв Михайло Андрійович