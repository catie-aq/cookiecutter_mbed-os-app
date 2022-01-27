import os
import subprocess

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m[WARNING]: "
SUCCESS = "\x1b[1;32m[SUCCESS]: "


def git_init():
    return subprocess.check_call(["git", "init"], stdout=subprocess.DEVNULL)


def git_add_all():
    return subprocess.check_call(["git", "add", "."], stdout=subprocess.DEVNULL)


def git_commit():
    return subprocess.check_call(
        ["git", "commit", "-m", "Initial commit"], stdout=subprocess.DEVNULL
    )


def create_repository():
    git_init()
    git_add_all()
    git_commit()


def remove_file(filepath):
    os.remove(filepath)


def main():
    if "{{ cookiecutter.custom_target }}" == "None":
        remove_file("{{ cookiecutter.custom_target_repo }}.lib")

    if {{ cookiecutter.create_repository }}:
        create_repository()

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")

    print(
        SUCCESS + "Project generated in `{{ cookiecutter.project_slug }}`" + TERMINATOR
        SUCCESS + "Deploy, code, compile and flash!" + TERMINATOR
    )


if __name__ == "__main__":
    main()
