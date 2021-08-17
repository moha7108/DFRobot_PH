import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DFRobot_EC_PH_ADC",
    keywords = 'Raspberry Pi, Raspi, Python, GPIO, PH, EC, DFRobot, Gravity, Sensor',
    version="0.1.0",
    author="Mohamed Debbagh",
    author_email="moha7108@protonmail.com",
    description="This package is a fork of the DFRobot_PH package, modified for python3 and packaged for pip",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/moha7108/RPi_control_center",
    project_urls={
        "Bug Tracker": "https://github.com/moha7108/RPi_control_center/issues",
        "Github": "https://github.com/moha7108/RPi_control_center",
        "GitLab[Source]":"https://gitlab.com/moha7108/rpi-control-center"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 3 - Alpha",
    ],
    license='GNU GPLv3',
    packages=['rpi_control_center'],
    python_requires=">=3.6",
    install_requires=[
          'logzero',
          'RPi.GPIO'
      ]
)