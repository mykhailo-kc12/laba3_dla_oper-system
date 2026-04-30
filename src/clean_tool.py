import argparse
import os


def parse_args():
    """
    Розбирає аргументи командного рядка для утиліти clean.

    wd - каталог, у якому виконується пошук.
         Якщо не заданий, використовується поточний каталог.

    --files      - показувати порожні файли
    --dirs       - показувати порожні каталоги
    --delete-files - видаляти знайдені порожні файли
    --delete-dirs  - видаляти знайдені порожні каталоги

    Якщо користувач не вказує жодної опції, програма за замовчуванням
    показує і порожні файли, і порожні каталоги.
    """
    parser = argparse.ArgumentParser(
        description="Пошук і видалення порожніх файлів та каталогів."
    )

    parser.add_argument(
        "wd",
        nargs="?",
        default=".",
        help="Каталог для аналізу"
    )

    parser.add_argument(
        "--files",
        action="store_true",
        help="Показувати порожні файли"
    )

    parser.add_argument(
        "--dirs",
        action="store_true",
        help="Показувати порожні каталоги"
    )

    parser.add_argument(
        "--delete-files",
        action="store_true",
        help="Видаляти порожні файли"
    )

    parser.add_argument(
        "--delete-dirs",
        action="store_true",
        help="Видаляти порожні каталоги"
    )

    return parser.parse_args()


def find_empty_files(root_path):
    """
    Повертає список усіх порожніх файлів у каталозі та підкаталогах.
    """
    empty_files = []

    for current_root, _, files in os.walk(root_path):
        for file_name in files:
            full_path = os.path.join(current_root, file_name)

            # Перевіряємо, що це звичайний файл і він має розмір 0 байт.
            if os.path.isfile(full_path) and os.path.getsize(full_path) == 0:
                empty_files.append(full_path)

    return empty_files


def find_empty_dirs(root_path):
    """
    Повертає список усіх порожніх каталогів у каталозі та підкаталогах.

    topdown=False потрібен для того, щоб спочатку обробити вкладені каталоги,
    а вже потім їх батьківські каталоги.
    """
    empty_dirs = []

    for current_root, dirs, files in os.walk(root_path, topdown=False):
        # Каталог вважаємо порожнім, якщо в ньому немає ні файлів, ні каталогів.
        if not dirs and not files:
            empty_dirs.append(current_root)

    return empty_dirs


def print_list(title, items):
    """
    Друкує заголовок і список знайдених об'єктів.
    """
    print(title)

    if not items:
        print("Нічого не знайдено.")
        return

    for item in items:
        print(item)


def delete_files(files):
    """
    Видаляє список порожніх файлів.
    """
    for file_path in files:
        try:
            os.remove(file_path)
            print(f"Видалено файл: {file_path}")
        except OSError as error:
            print(f"Помилка при видаленні файлу '{file_path}': {error}")


def delete_dirs(dirs):
    """
    Видаляє список порожніх каталогів.
    """
    for dir_path in dirs:
        try:
            os.rmdir(dir_path)
            print(f"Видалено каталог: {dir_path}")
        except OSError as error:
            print(f"Помилка при видаленні каталогу '{dir_path}': {error}")


def main():
    """
    Точка входу в програму.
    """
    args = parse_args()

    if not os.path.isdir(args.wd):
        print(f"Помилка: '{args.wd}' не є каталогом.")
        return

    empty_files = find_empty_files(args.wd)
    empty_dirs = find_empty_dirs(args.wd)

    # Якщо не задано жодної опції, за замовчуванням просто показуємо все.
    if not (
        args.files or
        args.dirs or
        args.delete_files or
        args.delete_dirs
    ):
        print_list("Порожні файли:", empty_files)
        print_list("Порожні каталоги:", empty_dirs)
        return

    if args.files:
        print_list("Порожні файли:", empty_files)

    if args.dirs:
        print_list("Порожні каталоги:", empty_dirs)

    if args.delete_files:
        delete_files(empty_files)

    if args.delete_dirs:
        delete_dirs(empty_dirs)


if __name__ == "__main__":
    main()
