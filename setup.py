from setuptools import setup
import re

# read the contents of your README file
from os import path

with open('README.md') as f:
    long_description = f.read()

verstr = "unknown"
try:
    verstrline = open('covid19_inference_adopted/_version.py', "rt").read()
except EnvironmentError:
    pass
else:
    VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
    mo = re.search(VSRE, verstrline, re.M)
    if mo:
        verstr = mo.group(1)
    else:
        raise RuntimeError("unable to find version in covid19_inference_adopted/_version.py")

setup(
    name='covid19_inference_adopted',
    author='Jonas Dehning, Johannes Zierenberg, F. Paul Spitzner, Michael Wibral, Joao Pinheiro Neto, Michael Wilczek, Viola Priesemann',
    author_email='jonas.dehning@ds.mpg.de',
    packages=['covid19_inference_adopted'],
    url='https://github.com/pinkiko89/covid19_inference_forecast_adoptedSIR.git',
    python_requires='>=3.6.0',
    version = verstr,
)
