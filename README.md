# Cookiecutter Mbed OS Application
[Cookiecutter](https://github.com/audreyr/cookiecutter) template for a Mbed OS
application.

## Requirements
Install `cookiecutter` from the command line:

```shell
pip install --user cookiecutter
```

## Usage
Generate a new Mbed OS application from template:

```
cookiecutter gl:catie_6tron/cookiecutter-mbed-os-app
```

## Template variables
- `project_name`: name of the project
- `project_short_description`: one-line description of the project
- `project_slug`: GitLab project slug as in https://gitlab.com/project_namespace/project_slug
- `project_namespace`: GitLab project namespace as in https://gitlab.com/project_namespace/project_slug
- `git_url`: GitLab URL as in https://gitlab.com/project_namespace/project_slug.git
- `copyright_holder`: copyright holder used in headers
- `copyright_year`: copyright year used in headers
- `target`: default Mbed OS target
- `toolchain`: default Mbed OS toolchain
