## This project will be reorganized to these links below ##
- core features
	- https://github.com/linyeh1129/vloc
- optional functions:
	- https://github.com/linyeh1129/vloc_plugin_selenium
	- https://github.com/linyeh1129/vloc_plugin_playwright


<p align="center">
	<img src="https://img.shields.io/badge/license-MIT-green&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/linyeh1129/VisionLocator?style=default&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/linyeh1129/VisionLocator?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/linyeh1129/VisionLocator?style=default&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<hr>

<h2 id="-quick-links">Quick Links</h2>

> - [ Overview](#-overview)
> - [ Features](#-features)
> - [ Repository Structure](#-repository-structure)
> - [ Getting Started](#-getting-started)
>	- [ Requirements](#-requirements)
>	- [ Installation](#-installation)
> - [ Basic Usage](#-basic-usage)
> - [ Project Roadmap](#-project-roadmap)
> - [ Contributing](#-contributing)
> - [ License](#-license)
> - [ Acknowledgments](#-acknowledgments)

---

<h2 id="-overview">Overview</h2>

- An UI automation testing tool based on YOLO, OCR, Appium, Allure.

---

<h2 id="-features">Features</h2>

- Detect UI elements by YOLO.
- Query elements by Tesseract.
- Interact with UI elements by Appium.

---

<h2 id="-repository-structure">Repository Structure</h2>

```
└── VisionLocator
    └── vision_locator
        ├── detect.py
        ├── detect_attribute.py
        └── remote.py
```



---

<h2 id="-getting-started">Getting Started</h2>

<h3 id="-requirements">Requirements</h3>

* **Python**: `version 3.10`
* **OpenCV**: https://pypi.org/project/opencv-python/
* **ultralytics**: https://pypi.org/project/ultralytics/
* **pytesseract**: https://pypi.org/project/pytesseract/
* **tesseract-ocr**: https://github.com/tesseract-ocr/tesseract/
* **allure-pythome-commons**: https://pypi.org/project/allure-python-commons/
  
<h3 id="-installation">Installation</h3>

`pip install -i https://test.pypi.org/simple/ VisionLocator`

---

<h2 id="-basic-usage">Basic Usage</h2>

- Initiate:

```python
from vision_locator.remote import Remote
Remote.driver = webdriver.Remote(appium_server, capabilities) # initiate Appium web driver.
Remote.windows_size = Remote.driver.get_window_size() # get the Appium window size.
Remote.device_resolution = {'width':1290, 'height':2796} # setup the testing device's real resolution.
Remote.ai_model = 'pre_trained_model_folder' # setup path which saves the .pt files.
```
- Detect element:
```python
from vision_locator.detect import ai_detect
element = ai_detect(label=Label.example,
                    model='best',
                    numbers=1,
                    sort_axis=['y','x'],
                    sort_group=None,
                    timeout=None,
                    show=False)

| Argument   | Description                                                      |
| ---------- | ---------------------------------------------------------------- |
| label      | Enum, this class should be a mapping of the label's index.       |
| model      | Str, name of the pre-trained file, default='best'.               |
| numbers    | Int, an expected number of YOLO predict, default=1.              |
| sort_axis  | List, sorting the detected elements by order, default=['y', 'x'] |
| sort_group | Int, sorting the elements by group, default=None.                |
| timeout    | Int, default=None (set default timeout).                         |
| show       | Bool, to show the YOLO predict screen, default=False.            |

```
- Detect element by text:

```python
from vision_locator.detect import ai_detect_text
element = ai_detect_text(label=Label.example,
                         model='best',
                         numbers=1,
                         text='example',
                         segment=False,
                         timeout=None,
                         show=False)

| Argument   | Description                                                      |
| ---------- | ---------------------------------------------------------------- |
| label      | Enum, this class should be a mapping of the label's index.       |
| model      | Str, name of the pre-trained file, default='best'.               |
| numbers    | Int, an expected number of YOLO predict, default=1.              |
| text       | Str | List[Str], regex search text in detected elements.         |
| segment    | Bool, OCR config for multiple lines, default=False.              |
| timeout    | Int, default=None (set default timeout).                         |
| show       | Bool, to show the YOLO predict screen, default=False.            |

```
- Detect element not exist

```python
from vision_locator.detect import ai_detect_not_exist
ai_detect_not_exist(label=Label.example,
                    models='best',
                    numbers=1,
                    delay_start=1,
                    timeout=1)

| Argument   | Description                                                      |
| ---------- | ---------------------------------------------------------------- |
| label      | Enum, this class should be a mapping of the label's index.       |
| model      | Str, name of the pre-trained file, default='best'.               |
| numbers    | Int, an expected number of YOLO predict, default=1.              |
| delay_start| Int, a waiting time before YOLO predict default=1.               |
| timeout    | Int, default=None (set default timeout).                         |
```

- Slide
  
```python
from vision_locator.detect import slide_up, slide_down, slide_e2e

| Function   | Description                                                      |
| ---------- | ---------------------------------------------------------------- |
| slide_up   | Action by Appium to slide up.                                    |
| slide_down | Action by Appium to slide down.                                  |
| slide_e2e  | Action by Appium to slide from element to element.               |


```

- Click, Input, Text
  
```python
from vision_locator.detect import ai_detect, ai_detect_text

element detected by ai_detect, ai_detect_text can be click(), input(), text()

| Function   | Description                                                      |
| ---------- | ---------------------------------------------------------------- |
| click      | Action by Appium to click.                                       |
| input      | Action by Appium to send_keys.                                   |
| text       | Action by OCR to query the text inside the element.              |

```


---

<h2 id="-project-roadmap">Project Roadmap</h2>

- [X] `► First release`
- [ ] `► Optimize the compatibility of Android`
- [ ] `► Improve performance`
- [ ] `► Optimize the compatibility of Selenium`

---

<h2 id="-contributing">Contributing</h2>

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github/linyeh1129/VisionLocator/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github/linyeh1129/VisionLocator/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github/linyeh1129/VisionLocator/issues)**: Submit bugs found or log feature requests for VisionLocator.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone https://github.com/linyeh1129/VisionLocator
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

<h2 id="-license">License</h2>

This project is protected under the MIT License. For more details, refer to the [LICENSE](https://github.com/linyeh1129/VisionLocator/blob/main/LICENSE.txt).

---

<h2 id="-acknowledgments">Acknowledgments</h2>

- Appium Document: https://appium.io/docs/en/2.2/
- ultralytics: https://www.ultralytics.com/
- tesseract-ocr: https://github.com/tesseract-ocr/tesseract

[**Return**](#-quick-links)

---
