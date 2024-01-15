import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="VisionLocator",
    version="0.0.1",
    author="Lin Yeh",
    author_email="lin_yeh@outlook.com",
    description="An UI automation testing tool based on Appium, YOLO, OCR, Allure",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/linyeh1129/VisionLocator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
