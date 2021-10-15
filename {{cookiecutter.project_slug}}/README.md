# {{cookiecutter.project_name}}
{{cookiecutter.project_short_description}}

## Requirements
### Hardware requirements
The following boards are required:
- *List {{cookiecutter.project_name}} hardware requirements here*

### Software requirements
{{cookiecutter.project_name}} makes use of the following libraries (automatically
imported by `mbed deploy` or `mbed import`):
- *List {{cookiecutter.project_name}} software requirements here*

## Usage
To clone **and** deploy the project in one command, use `mbed import` and skip to the
target and toolchain definition:
```shell
mbed import {{cookiecutter.git_url}} {{cookiecutter.project_slug}}
```

Alternatively:

- Clone to "{{cookiecutter.project_slug}}" and enter it:
  ```shell
  git clone {{cookiecutter.git_url}} {{cookiecutter.project_slug}}
  cd {{cookiecutter.project_slug}}
  ```

- Deploy software requirements with:
  ```shell
  mbed deploy
  ```

- Set Mbed project root path:
  ```shell
  mbed config root .
  ```

Define your target and toolchain:
```shell
mbed target {{ cookiecutter.mbed_os_target }}
mbed toolchain {{ cookiecutter.toolchain }}
```

Compile the project:
```shell
mbed compile
```

Program the target device with a Segger J-Link debug probe and
[`sixtron_flash`](https://gitlab.com/catie_6tron/6tron-flash) tool:
```shell
sixtron_flash {{ cookiecutter.jlink_device }} BUILD/{{ cookiecutter.mbed_os_target }}/{{ cookiecutter.toolchain}}/{{cookiecutter.project_slug}}.elf
```

Debug on the target device with the probe and Segger
[Ozone](https://www.segger.com/products/development-tools/ozone-j-link-debugger)
software.
