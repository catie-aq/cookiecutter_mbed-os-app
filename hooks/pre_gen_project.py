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
    """Generate board configuration:
      - "custom_target_repo": custom target repository name
      - "custom_target_repo_url": custom target repository URL
      - "mbed_os_target": Mbed OS target name
      - "jlink_device": J-Link device name

    Dummy function, generate with Jinja2:

    {% if cookiecutter.custom_target == "Z_Environment" %}
        {{ cookiecutter.update({ "custom_target_repo": "z-environment" }) }}
        {{ cookiecutter.update({ "custom_target_repo_url": "https://gitlab.com/catie_6tron/z-environment.git" }) }}
        {{ cookiecutter.update({ "mbed_os_target": "ZEST_CORE_STM32L496RG" }) }}
        {{ cookiecutter.update({ "jlink_device": "stm32l496rg" }) }}
    {% elif cookiecutter.custom_target == "Z_Motion" %}
        {{ cookiecutter.update({ "custom_target_repo": "z-motion" }) }}
        {{ cookiecutter.update({ "custom_target_repo_url": "https://gitlab.com/catie_6tron/z-motion.git" }) }}
        {{ cookiecutter.update({ "mbed_os_target": "ZEST_CORE_STM32L496RG" }) }}
        {{ cookiecutter.update({ "jlink_device": "stm32l496rg" }) }}
    {% elif cookiecutter.custom_target == "Zest_Core_FMLR-72" %}
        {{ cookiecutter.update({ "custom_target_repo": "zest-core-fmlr-72" }) }}
        {{ cookiecutter.update({ "custom_target_repo_url": "https://gitlab.com/catie_6tron/zest-core-fmlr-72.git" }) }}
        {{ cookiecutter.update({ "mbed_os_target": "ZEST_CORE_FMLR-72" }) }}
        {{ cookiecutter.update({ "jlink_device": "stm32l071rz" }) }}
    {% elif cookiecutter.custom_target == "Zest_Core_MTXDOT" %}
        {{ cookiecutter.update({ "custom_target_repo": "zest-core-mtxdot" }) }}
        {{ cookiecutter.update({ "custom_target_repo_url": "https://gitlab.com/catie_6tron/zest-core-mtxdot.git" }) }}
        {{ cookiecutter.update({ "mbed_os_target": "ZEST_CORE_MTXDOT" }) }}
        {{ cookiecutter.update({ "jlink_device": "stm32l151cc" }) }}
    {% elif cookiecutter.custom_target == "Zest_Core_nRF52832" %}
        {{ cookiecutter.update({ "custom_target_repo": "zest-core-nrf52832" }) }}
        {{ cookiecutter.update({ "custom_target_repo_url": "https://gitlab.com/catie_6tron/zest-core-nrf52832.git" }) }}
        {{ cookiecutter.update({ "mbed_os_target": "Zest_Core_nRF52832" }) }}
        {{ cookiecutter.update({ "jlink_device": "nrf52832_xxaa" }) }}
    {% elif cookiecutter.custom_target == "Zest_Core_STM32G474VE" %}
        {{ cookiecutter.update({ "custom_target_repo": "zest-core-stm32g474ve" }) }}
        {{ cookiecutter.update({ "custom_target_repo_url": "https://gitlab.com/catie_6tron/zest-core-stm32g474ve.git" }) }}
        {{ cookiecutter.update({ "mbed_os_target": "ZEST_CORE_STM32G474VE" }) }}
        {{ cookiecutter.update({ "jlink_device": "stm32474ve" }) }}
    {% elif cookiecutter.custom_target == "Zest_Core_STM32H753ZI" %}
        {{ cookiecutter.update({ "custom_target_repo": "zest-core-stm32h753zi" }) }}
        {{ cookiecutter.update({ "custom_target_repo_url": "https://gitlab.com/catie_6tron/zest-core-stm32h753zi.git" }) }}
        {{ cookiecutter.update({ "mbed_os_target": "ZEST_CORE_STM32H753ZI" }) }}
        {{ cookiecutter.update({ "jlink_device": "stm32h753zi" }) }}
    {% elif cookiecutter.custom_target == "Zest_Core_STM32L496RG" %}
        {{ cookiecutter.update({ "custom_target_repo": "zest-core-stm32l496rg" }) }}
        {{ cookiecutter.update({ "custom_target_repo_url": "https://gitlab.com/catie_6tron/zest-core-stm32l496rg.git" }) }}
        {{ cookiecutter.update({ "mbed_os_target": "ZEST_CORE_STM32L496RG" }) }}
        {{ cookiecutter.update({ "jlink_device": "stm32l496rg" }) }}
    {% elif cookiecutter.custom_target == "Zest_Core_STM32L496ZG" %}
        {{ cookiecutter.update({ "custom_target_repo": "zest-core-stm32l496zg" }) }}
        {{ cookiecutter.update({ "custom_target_repo_url": "https://gitlab.com/catie_6tron/zest-core-stm32l496zg.git" }) }}
        {{ cookiecutter.update({ "mbed_os_tazget": "ZEST_CORE_STM32L496ZG" }) }}
        {{ cookiecutter.update({ "jlink_device": "stm32l496zg" }) }}
    {% elif cookiecutter.custom_target == "Zest_Core_STM32L4A6RG" %}
        {{ cookiecutter.update({ "custom_target_repo": "zest-core-stm32l4a6rg" }) }}
        {{ cookiecutter.update({ "custom_target_repo_url": "https://gitlab.com/catie_6tron/zest-core-stm32l4a6rg.git" }) }}
        {{ cookiecutter.update({ "mbed_os_target": "ZEST_CORE_STM32L4A6RG" }) }}
        {{ cookiecutter.update({ "jlink_device": "stm32l4a6rg" }) }}
    {% elif cookiecutter.custom_target == "Zest_Core_STM32L562VE" %}
        {{ cookiecutter.update({ "custom_target_repo": "zest-core-stm32l562ve" }) }}
        {{ cookiecutter.update({ "custom_target_repo_url": "https://gitlab.com/catie_6tron/zest-core-stm32l562ve.git" }) }}
        {{ cookiecutter.update({ "mbed_os_target": "ZEST_CORE_STM32L562VE" }) }}
        {{ cookiecutter.update({ "jlink_device": "stm32l562ve" }) }}
    {% else %}
        {{ cookiecutter.update({ "custom_target_repo": "" }) }}
        {{ cookiecutter.update({ "custom_target_repo_url": "" }) }}
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
