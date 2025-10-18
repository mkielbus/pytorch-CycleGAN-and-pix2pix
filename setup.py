from setuptools import setup, find_packages


def get_description():
    return "Deep Learning library for colorizing and restoring old images and video"


def get_long_description():
    with open("README.md") as f:
        return f.read()


setup(
    name="pytorch-CycleGAN-and-pix2pix",
    version="1.0.0",
    packages=find_packages(exclude=["tests"]),
    url="https://github.com/mkielbus/pytorch-CycleGAN-and-pix2pix.git",
    license="MIT License",
    description=get_description(),
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
