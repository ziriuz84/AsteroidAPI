from setuptools import find_packages, setup

setup(
    name="asteroidAPI",
    version="0.0.1",
    description="API to retrieve asteroids data",
    url="https://github.com/ziriuz84/AsteroidAPI",
    author="Sirio Negri",
    author_email="ziriuz84@gmail.com",
    license="GPL v3",
    packages=find_packages("."),
    install_requires=["fastapi", "uvicorn[standard]"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GPL v3",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
    ],
    entry_points={"console_scripts": ["asteroidAPI=asteroidAPI:main"]},
)
