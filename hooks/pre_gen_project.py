import re
import sys


def check_project_slug():
    PROJECT_SLUG_REGEX = r"^[_a-zA-Z][-_a-zA-Z0-9]+$"

    project_slug = "{{ cookiecutter.project_slug }}"

    if not re.match(PROJECT_SLUG_REGEX, project_slug):
        print("ERROR: {} is not a valid project slug!".format(project_slug))

        # exits with status 1 to indicate failure
        sys.exit(1)


def check_board():
    """Generate `mbed_os_target` and `jlink_device` configuration from board selection.

    Dummy function, generate with Jinja2:

    {% if cookiecutter.board == "Zest_Core_STM32L4A6RG" %}
        {{ cookiecutter.update({ "mbed_os_target": "ZEST_CORE_STM32L4A6RG" }) }}
        {{ cookiecutter.update({ "jlink_device": "stm32l4a6rg" }) }}
    {% elif cookiecutter.board == "Z_Environment" %}
        {{ cookiecutter.update({ "mbed_os_target": "ZEST_CORE_STM32L496RG" }) }}
        {{ cookiecutter.update({ "jlink_device": "stm32l496rg" }) }}
    {% elif cookiecutter.board == "Z_Motion" %}
        {{ cookiecutter.update({ "mbed_os_target": "ZEST_CORE_STM32L496RG" }) }}
        {{ cookiecutter.update({ "jlink_device": "stm32l496rg" }) }}
    {% elif cookiecutter.board == "Zest_Core_MTXDOT" %}
        {{ cookiecutter.update({ "mbed_os_target": "ZEST_CORE_MTXDOT" }) }}
        {{ cookiecutter.update({ "jlink_device": "stm32l151cc" }) }}
    {% elif cookiecutter.board == "Zest_Core_STM32G474VE" %}
        {{ cookiecutter.update({ "mbed_os_target": "ZEST_CORE_STM32G474VE" }) }}
        {{ cookiecutter.update({ "jlink_device": "stm32474ve" }) }}
    {% elif cookiecutter.board == "Zest_Core_STM32H753ZI" %}
        {{ cookiecutter.update({ "mbed_os_target": "ZEST_CORE_STM32H753ZI" }) }}
        {{ cookiecutter.update({ "jlink_device": "stm32h753zi" }) }}
    {% elif cookiecutter.board == "Zest_Core_STM32L496RG" %}
        {{ cookiecutter.update({ "mbed_os_target": "ZEST_CORE_STM32L496RG" }) }}
        {{ cookiecutter.update({ "jlink_device": "stm32l496rg" }) }}
    {% elif cookiecutter.board == "Zest_Core_STM32L496ZG" %}
        {{ cookiecutter.update({ "mbed_os_tazget": "ZEST_CORE_STM32L496ZG" }) }}
        {{ cookiecutter.update({ "jlink_device": "stm32l496zg" }) }}
    {% elif cookiecutter.board == "Zest_Core_STM32L562VE" %}
        {{ cookiecutter.update({ "mbed_os_target": "ZEST_CORE_STM32L562VE" }) }}
        {{ cookiecutter.update({ "jlink_device": "stm32l562ve" }) }}
    {% elif cookiecutter.board == "Zest_Core_nRF52832" %}
        {{ cookiecutter.update({ "mbed_os_target": "Zest_Core_nRF52832" }) }}
        {{ cookiecutter.update({ "jlink_device": "nrf52832_xxaa" }) }}
    {% else %}
        {{ cookiecutter.update({ "mbed_os_target": "YOUR_MBED_OS_TARGET" }) }}
        {{ cookiecutter.update({ "jlink_device": "YOUR_JLINK_DEVICE" }) }}
    {% endif %}
    """
    pass


def main():
    check_project_slug()
    check_board()


if __name__ == "__main__":
    main()
