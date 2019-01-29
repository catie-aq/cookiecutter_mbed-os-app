import subprocess


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

def main():
    if {{ cookiecutter.create_repository }}:
        create_repository()


if __name__ == '__main__':
    main()
