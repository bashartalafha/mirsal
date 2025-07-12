from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mirsal",
    version="0.1.3",  # ← bump this every time you re-upload
    packages=find_packages(),
    install_requires=[
        "flask",
        "pyngrok",
    ],
    entry_points={
        "console_scripts": [
            "mirsal=mirsal.cli:main",
        ],
    },
    author="Bashar T.",
    description="📄 Live log viewer with Ngrok + Flask",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bashartalafha/mirsal",  # ← GitHub main page
    project_urls={
        "Source Code": "https://github.com/bashartalafha/mirsal",
        "Bug Tracker": "https://github.com/bashartalafha/mirsal/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)

