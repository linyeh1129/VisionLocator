from operator import itemgetter
import re
import cv2
import pytesseract
from selenium.webdriver import ActionChains
from re import Pattern
from vision_locator.remote import Remote


class DetectAttribute:
    coordinate: tuple = None
    __crop: str = None
    __action: ActionChains = None

    def __init__(self, ai_infos: dict):
        info = list(ai_infos.values())[0]
        self.coordinate = itemgetter('x', 'y')(info)
        self.__crop = itemgetter('crop')(info)
        self.__action = ActionChains(Remote.driver)

    def text(self, search: Pattern = None, remove: Pattern = None, segment: bool = True) -> str:
        img = cv2.imread(self.__crop)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        config = '--psm 4' if segment else '--psm 7'

        txt = str(pytesseract.image_to_string(img, config=config)).replace('\n', '')

        if search:
            txt = re.search(search, txt)
            if not txt:
                raise Exception(f'text search pattern not contains:{search}')
            txt = txt.group(0)

        txt = re.sub(remove, '', txt).strip() if remove else txt
        return txt

    def click(self):
        x, y = self.coordinate
        self.__action.w3c_actions.pointer_action.move_to_location(x, y).click()
        self.__action.perform()

    def input(self, value: str):
        self.__click()

        self.__action.w3c_actions.key_action.send_keys(value)
        self.__action.perform()
