# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

## Requirements

*List {{cookiecutter.project_name}} requirements here*

## Usage

To clone **and** deploy the project in one command, use `mbed import` and skip to
the target and toolchain definition:

    mbed import {{cookiecutter.git_url}} {{cookiecutter.project_slug}}

Alternatively:

* Clone to "{{cookiecutter.project_slug}}" and enter it:

    ```sh
    git clone {{cookiecutter.git_url}} {{cookiecutter.project_slug}}
    cd {{cookiecutter.project_slug}}
    ```

* Create an empty Mbed configuration file, otherwise Mbed CLI commands won't work:

    On Linux/macOS:

    ```sh
    touch .mbed on Linux/macOS
    ```

    Or on Windows:

    ```sh
    echo.> .mbed
    ```

* Deploy Mbed OS with:

    ```sh
    mbed deploy
    ```

* Define your target (eg. `ZEST_CORE_STM32L496RG`) and toolchain:

    ```sh
    mbed target ZEST_CORE_STM32L496RG
    mbed toolchain GCC_ARM
    ```

* Export to Eclipse IDE with:

    ```sh
    mbed export -i eclipse_6tron
    ```

## Compiling and programming without IDE

* Compile the project:

    ```sh
    mbed compile
    ```

* Program the target device (eg. `STM32L496RG` for the Zest_Core_STM32L496RG) with a
  J-Link debug probe:

    ```sh
    python dist/program.py STM32L496RG BUILD/ZEST_CORE_STM32L496RG/GCC_ARM/{{cookiecutter.project_slug}}.elf
    ```

