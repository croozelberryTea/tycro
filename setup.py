from setuptools import setup

setup(
    name="tycro",
    packages=["tycro", "link_shortener"],
    include_package_data=True,
    install_requires=["flask", "firebase_admin"],
)
