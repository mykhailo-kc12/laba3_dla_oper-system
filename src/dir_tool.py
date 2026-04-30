import argparse
import os
import pwd
import grp
import stat
from datetime import datetime


def parse_args():
    """
    Розбирає аргументи командного рядка для утиліти dir.

    wd - необов'язковий позиційний аргумент:
         каталог, вміст якого потрібно показати.
         Якщо не заданий, використовується поточний каталог.

    -l / --long - показувати детальну інформацію про об'єкти.
    -a / --all  - показувати приховані об'єкти, які починаються з крапки.
    """
    parser = argparse.ArgumentParser(
        description="Утиліта dir - спрощений аналог ls."
    )

    parser.add_argument(
        "wd",
        nargs="?",
        default=".",
        help="Робочий каталог для аналізу"
    )

    parser.add_argument(
        "-l",
        "--long",
        action="store_true",
        help="Показувати детальну інформацію"
    )

    parser.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="Показувати приховані файли та каталоги"
    )

    return parser.parse_args()


def get_file_type(file_mode):
    """
    Повертає символ типу об'єкта файлової системи.

    d - директорія
    - - звичайний файл
    l - символічне посилання
    """
    if stat.S_ISDIR(file_mode):
        return "d"
    if stat.S_ISLNK(file_mode):
        return "l"
    return "-"


def get_permissions(file_mode):
    """
    Повертає права доступу у форматі, схожому на ls -l.

    Наприклад:
    rwxr-xr--
    """
    permissions = []

    permission_flags = [
        stat.S_IRUSR, stat.S_IWUSR, stat.S_IXUSR,
        stat.S_IRGRP, stat.S_IWGRP, stat.S_IXGRP,
        stat.S_IROTH, stat.S_IWOTH, stat.S_IXOTH
    ]

    permission_chars = ["r", "w", "x", "r", "w", "x", "r", "w", "x"]

    for flag, char in zip(permission_flags, permission_chars):
        if file_mode & flag:
            permissions.append(char)
        else:
            permissions.append("-")

    return "".join(permissions)


def format_long_entry(path, name):
    """
    Формує один рядок детальної інформації про об'єкт.

    Виводяться:
    - тип об'єкта
    - права доступу
    - кількість жорстких посилань
    - власник
    - група
    - розмір у байтах
    - час останньої модифікації
    - ім'я об'єкта
    """
    full_path = os.path.join(path, name)

    # Використовуємо lstat, щоб для символічних посилань
    # отримати інформацію саме про посилання, а не про ціль.
    info = os.lstat(full_path)

    file_type = get_file_type(info.st_mode)
    permissions = get_permissions(info.st_mode)
    links_count = info.st_nlink
    owner_name = pwd.getpwuid(info.st_uid).pw_name
    group_name = grp.getgrgid(info.st_gid).gr_name
    size = info.st_size
    modified_time = datetime.fromtimestamp(info.st_mtime).strftime(
        "%Y-%m-%d %H:%M"
    )

    return (
        f"{file_type}{permissions} "
        f"{links_count} "
        f"{owner_name} "
        f"{group_name} "
        f"{size} "
        f"{modified_time} "
        f"{name}"
    )


def list_directory(path, show_all=False, long_format=False):
    """
    Виводить вміст каталогу.

    path - каталог для перегляду
    show_all - чи показувати приховані файли
    long_format - чи використовувати детальний формат
    """
    try:
        entries = sorted(os.listdir(path))
    except FileNotFoundError:
        print(f"Помилка: каталог '{path}' не знайдено.")
        return
    except NotADirectoryError:
        print(f"Помилка: '{path}' не є каталогом.")
        return
    except PermissionError:
        print(f"Помилка: немає доступу до каталогу '{path}'.")
        return

    for name in entries:
        # Якщо не вказано -a/--all, приховані файли не показуємо.
        if not show_all and name.startswith("."):
            continue

        # За умовою не потрібно виводити . та ..
        if name in {".", ".."}:
            continue

        if long_format:
            print(format_long_entry(path, name))
        else:
            print(name)


def main():
    """
    Точка входу в програму.
    """
    args = parse_args()
    list_directory(args.wd, show_all=args.all, long_format=args.long)


if __name__ == "__main__":
    main()
