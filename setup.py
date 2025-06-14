from setuptools import setup, find_packages
from pathlib import Path
# Lee el contenido de README.md para la descripción larga
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="conversor_unidades",
    version="2.1",
    description="A Python library for unit conversion: velocity, mass, distance, and temperature.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Alonso",
    url="https://github.com/alonsolo07/conversor_unidades_v2.0",
    packages=find_packages(exclude=["tests*", "docs*"]),
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.6",
)