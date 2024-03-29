# Cookiecutter Mbed OS Application

[Cookiecutter](https://github.com/audreyr/cookiecutter) template for an Mbed OS application.

## Requirements

Install Cookiecutter from the command line with [pipx](https://pypa.github.io/pipx/):

```shell
pipx install cookiecutter
```

## Usage

Generate a new Mbed OS application from template:

```shell
cookiecutter gh:catie-aq/cookiecutter_mbed-os-app
```

## Template variables

- `project_name`: name of the project
- `project_short_description`: one-line description of the project
- `project_slug`: GitHub project slug as in https://github.com/catie-aq/project_slug
- `git_url`: GitHub URL as in https://github.com/catie-aq/project_slug.git
- `copyright_holder`: copyright holder used in headers
- `copyright_year`: copyright year used in headers
- `open_source_license`: project license
- `custom_target`: select default 6TRON custom target
- `toolchain`: default Mbed OS toolchain
- `create_repository`: if true, creates a Git repository, adds all files and makes first
  commit
