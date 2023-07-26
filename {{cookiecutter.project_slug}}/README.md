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
{% if cookiecutter.custom_target == "None" -%}
To clone **and** deploy the project in one command, use `mbed import` and skip to the
target and toolchain definition:
{% else -%}
To clone **and** deploy the project in one command, use `mbed import` and skip to the
target enabling instructions:
{% endif -%}
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

{% if cookiecutter.custom_target == "None" -%}
- Clone custom target repository if necessary:
  ```shell
  git clone YOUR_CUSTOM_TARGET_REPOSITORY your-custom-target
  ```

Define your target and toolchain:
```shell
cp your-custom-target/custom_targets.json . # In case of custom target
mbed target {{cookiecutter.__mbed_os_target}}
mbed toolchain {{cookiecutter.toolchain}}
```

{% else -%}
Enable the custom target:
```shell
cp {{ cookiecutter.__custom_target_repo }}/custom_targets.json .
```

{% endif -%}

Compile the project:
```shell
mbed compile
```

Program the target device with a Segger J-Link debug probe and
[`sixtron_flash`](https://github.com/catie-aq/6tron_flash) tool:
```shell
sixtron_flash {{cookiecutter.__jlink_device}} BUILD/{{cookiecutter.__mbed_os_target}}/{{cookiecutter.toolchain}}/{{cookiecutter.project_slug}}.elf
```

Debug on the target device with the probe and Segger
[Ozone](https://www.segger.com/products/development-tools/ozone-j-link-debugger)
software.
