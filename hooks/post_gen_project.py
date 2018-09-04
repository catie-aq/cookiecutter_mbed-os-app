import subprocess


def init():
    return subprocess.check_call(["git", "init"])

def add_all():
    return subprocess.check_call(["git", "add", "."])

def commit():
    return subprocess.check_call(["git", "commit", "-m", "Initial commit"])

def main():
    init()
    add_all()
    commit()


if __name__ == '__main__':
    main()
