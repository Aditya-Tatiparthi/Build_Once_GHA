# import pickle as Flask
# import numpy as np
# import pandas as pd
# from flask import Flask, request, render_template


# APP = Flask(__name__, template_folder='templates')
# MODEL = Flask.load(open('model.pkl', 'rb'))
import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="hive",
    version="0.0.1",
    author="Ron LEsteve",
    author_email="ronlesteve@ronlesteve.com",
    description="Package to create Hive",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
