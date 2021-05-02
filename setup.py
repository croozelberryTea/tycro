from setuptools import setup

setup(
    name="tycro",
    packages=["tycro"],
    include_package_data=True,
    install_requires=["flask", "firebase_admin"],
)
