from setuptools import setup
import os

packages = []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

with open(os.path.join(root_dir, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

for dirpath, dirnames, filenames in os.walk("emobpy"):
    # Ignore dirnames that start with '.'
    if "__init__.py" in filenames:
        pkg = dirpath.replace(os.path.sep, ".")
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, ".")
        packages.append(pkg)

requirements = [req for req in open("requirements.txt").read().split("\n") if len(req) > 0]

setup(
    name="emobpy",
    version="0.6.3",
    packages=packages,
    author="Carlos Gaete-Morales",
    author_email="cdgaete@gmail.com",
    maintainer="v0.5.7: Lukas Trippe, v0.6.0: Benedikt Tepe",
    install_requires=requirements,
    include_package_data=True,
    entry_points={"console_scripts": ["emobpy = emobpy.__main__:main",],},
    url="https://gitlab.com/diw-evu/emobpy/emobpy",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    description="Time series for battery electric vehicles modeling",
    classifiers=[
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
)
