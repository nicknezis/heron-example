from setuptools import setup, find_packages

setup(
    name="my-topology-packages",
    packages=find_packages(
        where="src",
    ),
    package_dir={"": "src"},
    install_requires=[
        # use a more recent unofficial release
        "stormeye-heronpy==0.20.3",
        # latest official release is horribly out of date
        #"heronpy==0.17.8",
    ],
)
