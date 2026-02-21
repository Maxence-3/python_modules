import sys, os


def in_venv() -> bool:
    if sys.prefix != sys.base_prefix:
        print("MATRIX STATUS: Welcome to the construct")
        return True
    else:
        print("MATRIX STATUS: You're still plugged in")
        return False


def python_info(in_venv: bool) -> None:
    print(f"Current Python: {sys.executable}")
    if in_venv:
        print(
            f"Virtual Environement: {os.path.basename(os.environ.get('VIRTUAL_ENV'))}"
        )
        print(f"Environement Path: {os.environ.get('VIRTUAL_ENV')}")
    else:
        print("Virtual Environement: None detected")


def venv_message(in_venv: bool) -> None:
    if in_venv:
        print("SUCCESS: You're in an isolated environement!")
        print("Safe to install packages without affecting the global system.")
    else:
        print("WARNING: You're in the global environement!")
        print("The machine can see everithing you install.")


def more_info(in_venv: bool) -> None:
    if in_venv:
        print("Package installation path")
        print(sys.path)
    else:
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate # On Windows\n")
        print("Then run this program again.")


if __name__ == "__main__":
    venv_statu = in_venv()

    print()

    python_info(venv_statu)

    print()

    venv_message(venv_statu)

    print()

    more_info(venv_statu)
