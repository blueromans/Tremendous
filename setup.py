import setuptools

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name='TremendousClient',
    version="0.0.7",
    author="Yaşar Özyurt",
    author_email="blueromans@gmail.com",
    description='Tremendous Api Client Python package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/blueromans/Tremendous.git',
    project_urls={
        "Bug Tracker": "https://github.com/blueromans/Tremendous/issues",
    },
    install_requires=['requests', 'python-dotenv'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['tremendous', 'tremendous.service'],
    python_requires=">=3.6",
)
