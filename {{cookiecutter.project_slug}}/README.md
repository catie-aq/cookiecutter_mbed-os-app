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

This repository use MbedOS as RTOS framework. While next steps describes how to use Mbed CLI 1 commands to setup the project, it is highly recommended that users read [MbedOS official documentation](https://os.mbed.com/docs/mbed-os/v6.16/build-tools/create.html).

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

- If necessary, eg using a 6TRON Zest Core, clone the custom target repository:

  ```shell
  git clone YOUR_CUSTOM_TARGET_REPOSITORY your-custom-target
  ```
* ... and enable the custom target by copying `custom_targets.json` from the custom target folder into the root of your project.

Define your target and toolchain:

```shell
cp your-custom-target/custom_targets.json . # In case of custom target
mbed target {{cookiecutter.__mbed_os_target}}
mbed toolchain {{cookiecutter.toolchain}}
```

{% else -%}
Enable the custom target:

* Linux:

  ```shell
  cp {{ cookiecutter.__custom_target_repo }}/custom_targets.json .
  ```

* Windows:

  ```shell
  copy {{ cookiecutter.__custom_target_repo }}\custom_targets.json .
  ```

{% endif -%}

Compile the project:

```shell
mbed compile
```

Program the target device with a Segger J-Link debug probe and

[`sixtron_flash`](https://github.com/catie-aq/6tron-flash) tool:

```shell
sixtron_flash
```

Debug on the target device with the probe and Segger [Ozone](https://www.segger.com/products/development-tools/ozone-j-link-debugger) software.
