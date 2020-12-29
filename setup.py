import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Qmusic",
    version="0.0.1",
    author="Joppe Wolters (svenskithesource)",
    author_email="joppe.wolters@icloud.com",
    description="An unofficial Qmusic API Wrapper.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/svenskithesource/qmusic",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["requests", "python-dateutil"]
)
