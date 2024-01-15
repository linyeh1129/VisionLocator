
from appium.webdriver.webdriver import WebDriver
import os
from typing import Dict
from ultralytics import YOLO


class RemoteMeta:

    def __init__(cls, *args, **kwargs):
        pass

    @property
    def device_resolution(cls) -> dict:
        return None if 'GLOBAL_DEVICE_RESOLUTION' not in globals() else GLOBAL_DEVICE_RESOLUTION

    @device_resolution.setter
    def device_resolution(cls, resolution: dict):
        global GLOBAL_DEVICE_RESOLUTION
        GLOBAL_DEVICE_RESOLUTION = resolution

    @property
    def windows_size(cls) -> dict:
        return None if 'GLOBAL_WINDOWS_SIZE' not in globals() else GLOBAL_WINDOWS_SIZE

    @windows_size.setter
    def windows_size(cls, size: dict):
        global GLOBAL_WINDOWS_SIZE
        GLOBAL_WINDOWS_SIZE = size

    @property
    def driver(cls) -> WebDriver:
        return None if 'GLOBAL_DRIVER' not in globals() else GLOBAL_DRIVER

    @driver.setter
    def driver(cls, web_driver: WebDriver):
        if web_driver:
            global GLOBAL_DRIVER
            GLOBAL_DRIVER = web_driver

        else:
            del GLOBAL_DRIVER

    @property
    def ai_model(cls) -> Dict[str, YOLO]:
        return None if 'GLOBAL_AI_MODEL' not in globals() else GLOBAL_AI_MODEL

    @ai_model.setter
    def ai_model(cls, path: str) -> Dict[str, YOLO]:
        if path:
            model_dict = {i.replace('.pt', ''): f'{path}/{i}' for i in os.listdir(path) if '.pt' in i}

            for k, v in model_dict.items():
                model = YOLO(v, task='detect')
                model.predict(source='.history/.ai/blank.png', classes=0, max_det=1)
                model_dict.update({k: model})

            global GLOBAL_AI_MODEL
            GLOBAL_AI_MODEL = model_dict

        else:
            del GLOBAL_AI_MODEL


class Remote(metaclass=RemoteMeta):
    pass
