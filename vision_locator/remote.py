from appium.webdriver.webdriver import WebDriver
import os
from typing import Dict
from ultralytics import YOLO
from PIL import Image
import re
from pathlib import Path


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

            # history folder
            try:
                os.makedirs('.history/.ai')
            except:
                pass

            # img for predict initiated
            if not Path('.history/.ai/blank.png').is_file():
                with Image.new('RGB', (128, 128)) as img:
                    img.save('.history/.ai/blank.png')

            pt_path = [dir.as_posix() for dir in Path(path).rglob('*.pt')]
            pt_name = [(re.search(r'\/(\w+).pt', dir)).group(1) for dir in pt_path]
  
            yolos = [YOLO(dir, task='detect') for dir in pt_path]
            yolo_dict = dict(zip(pt_name, yolos))

            # initiate predict
            yolos[0].predict(source='.history/.ai/blank.png', classes=0, max_det=1)

            global GLOBAL_AI_MODEL
            GLOBAL_AI_MODEL = yolo_dict

        else:
            del GLOBAL_AI_MODEL


class Remote(metaclass=RemoteMeta):
    pass
