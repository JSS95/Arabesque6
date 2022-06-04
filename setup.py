from setuptools import setup, find_packages  # type: ignore[import]


VERSION_FILE = "arabesque6/version.py"


def get_version():
    with open(VERSION_FILE, "r") as f:
        exec(compile(f.read(), VERSION_FILE, "exec"))
    return locals()["__version__"]


def read_readme():
    with open("README.md", encoding="utf-8") as f:
        content = f.read()
    return content


def read_requirements(path):
    with open(path, "r") as f:
        ret = f.read().splitlines()
    return ret


def get_extras_require():
    ret = {}
    return ret


setup(
    name="arabesque6",
    version=get_version(),
    python_requires=">=3.6",
    description="Package for converting QVideoFrame to NDArray with Qt6",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        (
            "License :: OSI Approved :: "
            "GNU Library or Lesser General Public License (LGPL)"
        ),
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Software Development :: Widget Sets",
    ],
    author="Jisoo Song",
    author_email="jeesoo9595@snu.ac.kr",
    maintainer="Jisoo Song",
    maintainer_email="jeesoo9595@snu.ac.kr",
    url="https://github.com/JSS95/arabesque6",
    license="LGPL",
    packages=find_packages(),
    install_requires=read_requirements("requirements/install.txt"),
    extras_require=get_extras_require(),
)
