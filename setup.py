import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DFRobot_EC_PH_ADC",
    keywords = 'Raspberry Pi, Raspi, Python, GPIO, PH, EC, DFRobot, Gravity, Sensor',
    version="0.1.1",
    author="Mohamed Debbagh",
    author_email="moha7108@protonmail.com",
    description="This package is a fork of the DFRobot_PH package, modified for python3 and packaged for pip",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/moha7108/DFRobot_PH",
    project_urls={
        "Bug Tracker": "https://github.com/moha7108/DFRobot_PH/issues",
        "Github": "https://github.com/moha7108/DFRobot_PH",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 3 - Alpha",
    ],
    license='GNU LGPL-2.1',
    packages=['DFRobot'],
    python_requires=">=2",
    install_requires=[
          'smbus'
      ]
)
