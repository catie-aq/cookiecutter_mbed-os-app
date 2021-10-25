import subprocess
import os

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m[WARNING]: "
SUCCESS = "\x1b[1;32m[SUCCESS]: "


def git_init():
    return subprocess.check_call(["git", "init"])


def git_add_all():
    return subprocess.check_call(["git", "add", "."])


def git_commit():
    return subprocess.check_call(["git", "commit", "-m", "Initial commit"])


def create_repository():
    git_init()
    git_add_all()
    git_commit()


def remove_file(filepath):
    os.remove(filepath)


def main():
    if {{ cookiecutter.create_repository }}:
        create_repository()

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")

    print(
        SUCCESS + "Project generated in `{{ cookiecutter.project_slug }}`" + TERMINATOR
    )


if __name__ == "__main__":
    main()
