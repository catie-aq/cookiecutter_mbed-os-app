import subprocess


def git_init():
    return subprocess.check_call(["git", "init"])


def git_add_all():
    return subprocess.check_call(["git", "add", "."])


def git_commit():
    return subprocess.check_call(["git", "commit", "-m", "Initial commit"])


def get_mbed_os_commit(version):
    return subprocess.check_output(
        ["git", "ls-remote", "https://github.com/ARMmbed/mbed-os.git", "-refs", version]
    )


def create_repository():
    git_init()
    git_add_all()
    git_commit()


def main():
    if {{ cookiecutter.create_repository }}:
        create_repository()

    if "{{ cookiecutter.mbed_os_version }}" != "latest":
        commit = get_mbed_os_commit("{{ cookiecutter.mbed_os_version }}").decode()
        if commit:
            with open("mbed-os.lib", "a") as file:
                file.write("#{}".format(commit.split("\t")[0]))
        else:
            print("[Warning] Mbed OS version does not exist")


if __name__ == "__main__":
    main()
