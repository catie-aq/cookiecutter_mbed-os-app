import re
import sys


def check_project_slug():
    PROJECT_SLUG_REGEX = r"^[_a-zA-Z][-_a-zA-Z0-9]+$"

    project_slug = "{{ cookiecutter.project_slug }}"

    if not re.match(PROJECT_SLUG_REGEX, project_slug):
        print("ERROR: {} is not a valid project slug!".format(project_slug))

        # exits with status 1 to indicate failure
        sys.exit(1)

def main():
    check_project_slug()


if __name__ == '__main__':
    main()
