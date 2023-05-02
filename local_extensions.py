from jinja2.ext import Extension
from cookiecutter.utils import simple_filter


custom_targets = {
    "Z_Environment": {
        "custom_target_repo": "z-environment",
        "custom_target_repo_url": "https://gitlab.com/catie_6tron/z-environment.git",
        "mbed_os_target": "ZEST_CORE_STM32L496RG",
        "jlink_device": "stm32l496rg",
    },
    "Z_Motion": {
        "custom_target_repo": "z-motion",
        "custom_target_repo_url": "https://gitlab.com/catie_6tron/z-motion.git",
        "mbed_os_target": "ZEST_CORE_STM32L496RG",
        "jlink_device": "stm32l496rg",
    },
    "Zest_Core_FMLR-72": {
        "custom_target_repo": "zest-core-fmlr-72",
        "custom_target_repo_url": "https://gitlab.com/catie_6tron/zest-core-fmlr-72.git",
        "mbed_os_target": "ZEST_CORE_FMLR-72",
        "jlink_device": "stm32l071rz",
    },
    "Zest_Core_MTXDOT": {
        "custom_target_repo": "zest-core-mtxdot",
        "custom_target_repo_url": "https://gitlab.com/catie_6tron/zest-core-mtxdot.git",
        "mbed_os_target": "ZEST_CORE_MTXDOT",
        "jlink_device": "stm32l151cc",
    },
    "Zest_Core_nRF52832": {
        "custom_target_repo": "zest-core-nrf52832",
        "custom_target_repo_url": "https://gitlab.com/catie_6tron/zest-core-nrf52832.git",
        "mbed_os_target": "Zest_Core_nRF52832",
        "jlink_device": "nrf52832_xxaa",
    },
    "Zest_Core_STM32G474VE": {
        "custom_target_repo": "zest-core-stm32g474ve",
        "custom_target_repo_url": "https://gitlab.com/catie_6tron/zest-core-stm32g474ve.git",
        "mbed_os_target": "ZEST_CORE_STM32G474VE",
        "jlink_device": "stm32474ve",
    },
    "Zest_Core_STM32H743ZG": {
        "custom_target_repo": "zest-core-stm32h743zg",
        "custom_target_repo_url": "https://gitlab.com/catie_6tron/zest-core-stm32h743zg.git",
        "mbed_os_target": "ZEST_CORE_STM32H743ZG",
        "jlink_device": "stm32h743zg",
    },
    "Zest_Core_STM32H753ZI": {
        "custom_target_repo": "zest-core-stm32h753zi",
        "custom_target_repo_url": "https://gitlab.com/catie_6tron/zest-core-stm32h753zi.git",
        "mbed_os_target": "ZEST_CORE_STM32H753ZI",
        "jlink_device": "stm32h753zi",
    },
    "Zest_Core_STM32L496RG": {
        "custom_target_repo": "zest-core-stm32l496rg",
        "custom_target_repo_url": "https://gitlab.com/catie_6tron/zest-core-stm32l496rg.git",
        "mbed_os_target": "ZEST_CORE_STM32L496RG",
        "jlink_device": "stm32l496rg",
    },
    "Zest_Core_STM32L496ZG": {
        "custom_target_repo": "zest-core-stm32l496zg",
        "custom_target_repo_url": "https://gitlab.com/catie_6tron/zest-core-stm32l496zg.git",
        "mbed_os_tazget": "ZEST_CORE_STM32L496ZG",
        "jlink_device": "stm32l496zg",
    },
    "Zest_Core_STM32L4A6RG": {
        "custom_target_repo": "zest-core-stm32l4a6rg",
        "custom_target_repo_url": "https://gitlab.com/catie_6tron/zest-core-stm32l4a6rg.git",
        "mbed_os_target": "ZEST_CORE_STM32L4A6RG",
        "jlink_device": "stm32l4a6rg",
    },
    "Zest_Core_STM32L562VE": {
        "custom_target_repo": "zest-core-stm32l562ve",
        "custom_target_repo_url": "https://gitlab.com/catie_6tron/zest-core-stm32l562ve.git",
        "mbed_os_target": "ZEST_CORE_STM32L562VE",
        "jlink_device": "stm32l562ve",
    },
    "None": {
        "custom_target_repo": "",
        "custom_target_repo_url": "",
        "mbed_os_target": "YOUR_MBED_OS_TARGET",
        "jlink_device": "YOUR_JLINK_DEVICE",
    },
}


class CustomTargetExtension(Extension):
    """Jinja2 extension to get data about 6TRON custom targets."""

    def __init__(self, environment):
        """Initialize the extension with the given environment."""
        super(CustomTargetExtension, self).__init__(environment)

        def custom_target_repo(target):
            try:
                return custom_targets[target]["custom_target_repo"]
            except KeyError:
                return custom_targets["None"]["custom_target_repo"]

        def custom_target_repo_url(target):
            try:
                return custom_targets[target]["custom_target_repo_url"]
            except KeyError:
                return custom_targets["None"]["custom_target_repo_url"]

        def mbed_os_target(target):
            try:
                return custom_targets[target]["mbed_os_target"]
            except KeyError:
                return custom_targets["None"]["mbed_os_target"]

        def jlink_device(target):
            try:
                return custom_targets[target]["jlink_device"]
            except KeyError:
                return custom_targets["None"]["jlink_device"]

        environment.filters["custom_target_repo"] = custom_target_repo
        environment.filters["custom_target_repo_url"] = custom_target_repo_url
        environment.filters["mbed_os_target"] = mbed_os_target
        environment.filters["jlink_device"] = jlink_device
