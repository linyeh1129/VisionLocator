import re
from re import Pattern
from datetime import datetime
from enum import Enum
import os
import time
from typing import Union, List
import allure
from vision_locator.remote import Remote
from vision_locator.detect_attribute import DetectAttribute


def slide_up(start: float = 0.8, end: float = 0.1, duration=0):
    size = Remote.windows_size
    x = int(size['width']*0.5)
    y1 = int(size['height']*start)
    y2 = int(size['height']*end)
    Remote.driver.swipe(start_x=x, start_y=y1, end_x=x, end_y=y2, duration=duration)


def slide_down(start: float = 0.1, end: float = 0.8, duration=0):
    size = Remote.windows_size
    x = int(size['width']*0.5)
    y1 = int(size['height']*start)
    y2 = int(size['height']*end)
    Remote.driver.swipe(start_x=x, start_y=y1, end_x=x, end_y=y2, duration=duration)


def slide_e2e(start: DetectAttribute, end: DetectAttribute, duration=1000):
    x1, y1 = start.coordinate
    x2, y2 = end.coordinate
    Remote.driver.swipe(start_x=x1, start_y=y1, end_x=x2, end_y=y2, duration=duration)


def ai_detect_not_exist(label: Enum, numbers: int = 1, model='best', delay_start: int = 1, timeout: int = None):
    time.sleep(delay_start)
    time_stamp = datetime.now().strftime('%Y.%m.%d %H.%M.%S')
    temp = f'.history/.ai/temp.png'

    if not timeout:
        timeout = 60  # self.config.WAIT_TO_FIND_ELEMENT_TIMEOUT[self.env.environment_code]

    for i in range(timeout):
        name = f'[{label.name}] {time_stamp} retry {i}'
        Remote.driver.get_screenshot_as_file(temp)
        predict = Remote.ai_model[model].predict(source=temp, project='.history', name=name, classes=label.value, max_det=numbers, conf=0.2, save=True, save_crop=True, show=True)

        os.remove(temp)
        check_predict = len(*[p.boxes.cls for p in predict])

        if not check_predict:
            allure.attach.file(f'.history/{name}/temp.png', f'AI check not exist {name}')
            return True
        else:
            time.sleep(timeout / timeout)

    allure.attach.file(f'.history/{name}/temp.png', f'AI check exist {name}')
    return False


def ai_detect_text(label: Enum,
                   numbers: int,
                   text: Union[Pattern, List[Pattern]],
                   model:str='best',
                   segment: bool = False,
                   timeout: int = None,
                   show: bool = False) -> Union[DetectAttribute, List[DetectAttribute]]:
    text = [text] if type(text) is str else text
    detect = ai_detect(label=label, model=model, numbers=numbers, timeout=timeout, show=show)

    result = []
    for t in text:
        found = next((d for d in detect if re.search(t, d.text(segment=segment))), None)

        if not found:
            raise Exception(f'AI not detect text:{text} in label:{label}')

        if len(text) == 1:
            return found

        result.append(found)
    return result


def ai_detect(label: Enum,
              numbers: int = 1,
              model='best',
              sort_axis: list = ['y', 'x'],
              sort_group: int = None,
              timeout: int = None,
              show: bool = False) -> Union[DetectAttribute, List[DetectAttribute]]:

    time_stamp = datetime.now().strftime('%Y.%m.%d %H.%M.%S')
    temp = f'.history/.ai/temp.png'

    if not timeout:
        timeout = 8
        # TODO: Remote.timeout

    for i in range(timeout):
        name = f'[{label.name}] {time_stamp} retry {i}'
        Remote.driver.get_screenshot_as_file(temp)
        predict = Remote.ai_model[model].predict(source=f'.history/.ai/temp2.png', project='.history', name=name, classes=label.value, max_det=numbers, conf=0.2, save=True, save_crop=True, show=show)

        os.remove(temp)
        check_predict = len(*[p.boxes.cls for p in predict])

        if check_predict:
            break
        else:
            time.sleep(timeout / timeout)

    if not check_predict:
        allure.attach.file(f'.history/{name}/temp.png', f'AI not detect {name}')
        raise Exception(f'AI not detect label:{label}')

    allure.attach.file(f'.history/{name}/temp.png', name)
    crop_path = f'.history/{name}/crops/{label.name}'
    crop_list = [f'{crop_path}/{i}' for i in os.listdir(crop_path)]
    crop_list = __custom_sort(crop_list)

    if check_predict == 1:
        info = __convert_ai_infos(label, predict, crop_list, sort_axis, sort_group)[0]
        return DetectAttribute(ai_infos=info)

    else:
        infos = __convert_ai_infos(label, predict, crop_list, sort_axis, sort_group)
        results = []
        for info in infos:
            element = DetectAttribute(ai_infos=info)
            results.append(element)
        return results


def __convert_ai_infos(label, predict, crop_list, sort_axis, sort_group) -> list:
    window = Remote.windows_size
    resolution = Remote.device_resolution
    x_scale = window['width']/resolution['width']
    y_scale = window['height']/resolution['height']

    infos = []
    for p in predict:
        for i, (x1, y1, x2, y2), conf, crop in zip(p.boxes.cls, p.boxes.xyxy, p.boxes.conf, crop_list):
            x, y = int((x1+x2)/2*x_scale), int((y1+y2)/2*y_scale)
            infos.append({label.__class__(int(i)).name: {'x': x, 'y': y, 'conf': round(float(conf), 2), 'crop': crop}})
        infos = __sort_ai_infos(infos, label.__class__(int(i)).name, sort_axis, sort_group)
    return infos


def __sort_ai_infos(infos: list, label_name: str, sort_axis: list, sort_group: int) -> list:
    infos.sort(key=lambda i: (i[label_name][sort_axis[0]]))

    if sort_group:
        result = []
        i = 0

        while i < len(infos):
            temp = infos[i:i+sort_group]
            temp.sort(key=lambda i: (i[label_name][sort_axis[1]]))
            result.extend(temp)
            i += sort_group

        return result
    return infos


def __custom_sort(items: list) -> list:
    def convert(text): return int(text) if text.isdigit() else 0
    def custom_key(key): return [convert(i) for i in re.split('([0-9]+)', key)]
    return sorted(items, key=custom_key)
