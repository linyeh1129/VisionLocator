<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
</p>
<p align="center">
    <h1 align="center">VisionLocator</h1>
</p>
<p align="center">
    <em><code>An UI automation testing tool based on YOLO, OCR, Appium, Allure</code></em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/linyeh1129/VisionLocator?style=default&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/linyeh1129/VisionLocator?style=default&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/linyeh1129/VisionLocator?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/linyeh1129/VisionLocator?style=default&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<hr>

##  Quick Links

> - [ Overview](#-overview)
> - [ Features](#-features)
> - [ Repository Structure](#-repository-structure)
> - [ Getting Started](#-getting-started)
>   - [ Installation](#-installation)
>   - [ Running VisionLocator](#-running-VisionLocator)
> - [ Project Roadmap](#-project-roadmap)
> - [ Contributing](#-contributing)
> - [ License](#-license)
> - [ Acknowledgments](#-acknowledgments)

---

##  Overview

<code>► Combine the features of Appium with YOLO and OCR. </code>

---

##  Features

<code>► ai_detect\
      ► ai_detect_text\
      ► ai_detect_not_exist</code>

---

##  Repository Structure

```
└── VisionLocator
    └── vision_locator
        ├── detect.py
        ├── detect_attribute.py
        └── remote.py
```



---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version 3.10`
* **OpenCV**: https://pypi.org/project/opencv-python/
* **ultralytics**: https://pypi.org/project/ultralytics/
* **pytesseract**: https://pypi.org/project/pytesseract/
* **tesseract-ocr**: https://github.com/tesseract-ocr/tesseract/

###  Installation

`pip install -i https://test.pypi.org/simple/ VisionLocator`

###  Running VisionLocator

Use the following command to run VisionLocator:

`python main.py`


---

##  Project Roadmap

- [X] `► First release`
- [ ] `► Improve performance`
- [ ] `► Optimize the compatibility of Android`
- [ ] `► Optimize the compatibility of Selenium`

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github/linyeh1129/VisionLocator/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github/linyeh1129/VisionLocator/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github/linyeh1129/VisionLocator/issues)**: Submit bugs found or log feature requests for Visionlocator.

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

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-quick-links)

---
