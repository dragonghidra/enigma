from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="enigma-hashcat",
    version="2.0.0",
    author="Enigma Hashcat Team",
    author_email="team@enigma-hashcat.org",
    description="Modern password recovery toolkit for 2025",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dragonghidra/enigma",
    packages=find_packages(include=["python", "python.*"]),
    package_dir={"": "."},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "Topic :: Security :: Cryptography",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "enigma-hashcat=hashcat:main",
        ],
    },
    keywords="hashcat, password, recovery, security, cryptography",
    project_urls={
        "Bug Reports": "https://github.com/dragonghidra/enigma/issues",
        "Source": "https://github.com/dragonghidra/enigma",
        "Documentation": "https://github.com/dragonghidra/enigma/wiki",
    },
)