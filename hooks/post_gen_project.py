import subprocess
import os


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
    if {{ cookiecutter.create_repository }}:
        create_repository()

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")


if __name__ == "__main__":
    main()
