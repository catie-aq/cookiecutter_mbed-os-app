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

Define your target (eg. `ZEST_CORE_STM32L4A6RG`) and toolchain:
```shell
mbed target ZEST_CORE_STM32L4A6RG
mbed toolchain GCC_ARM
```

Compile the project:
```shell
mbed compile
```

Program the target device (eg. `STM32L4A6RG` for the Zest_Core_STM32L4A6RG) with a J-Link
debug probe:
```shell
python dist/program.py STM32L4A6RG BUILD/ZEST_CORE_STM32L4A6RG/GCC_ARM/{{cookiecutter.project_slug}}.elf
```

Debug on the target device with a debug probe, eg. Segger J-Link and
[Ozone](https://www.segger.com/products/development-tools/ozone-j-link-debugger)
software.
