---
title: '6.2 pip and Packages'
teaching: 18
exercises: 12
---

:::::::::::::::::::::::::::::::::::::: questions

- How do I install and use third-party packages?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Install, list and remove packages with pip.
- Fetch data from the web with requests.
- Create a simple package of your own.

::::::::::::::::::::::::::::::::::::::::::::::::

## Python PIP - Python Package Manager

### What is PIP ?

PIP stands for Preferred installer program. We use _pip_ to install different Python packages.
Package is a Python module that can contain one or more modules or other packages. A module or modules that we can install to our application is a package.
In programming, we do not have to write every utility program, instead we install packages and import them to our applications.

### Installing PIP

pip comes with Python, so you normally already have it. Open a terminal (in PyCharm: **View > Tool Windows > Terminal**) and check it:

```bash
python -m pip --version
```

```output
pip 25.0.1 from C:\...\site-packages\pip (python 3.12)
```

If you see a version number, pip is installed. Your number may be a little higher or lower. To upgrade pip to the newest version, run:

```bash
python -m pip install --upgrade pip
```

We write `python -m pip` rather than just `pip`, because it makes sure pip installs packages for the same Python that runs your code.

Let us check some of the packages used in the Python community for different purposes. Just to let you know that there are lots of packages available for use with different applications.

### Installing packages using pip

Let us try to install _numpy_, called numeric python. It is one of the most popular packages in machine learning and data science community.

- NumPy is the fundamental package for scientific computing with Python. It contains among other things:
  - a powerful N-dimensional array object
  - sophisticated (broadcasting) functions
  - tools for integrating C/C++ and Fortran code
  - useful linear algebra, Fourier transform, and random number capabilities

```bash
python -m pip install numpy
```

Let us start using numpy. Open the Python interactive shell (type `python` in the terminal, or use PyCharm's **Python Console**) and import numpy as follows:

```python
>>> import numpy
>>> numpy.__version__
'2.5.3'
>>> lst = [1, 2, 3, 4, 5]
>>> np_arr = numpy.array(lst)
>>> np_arr
array([1, 2, 3, 4, 5])
>>> len(np_arr)
5
>>> np_arr * 2
array([ 2,  4,  6,  8, 10])
>>> np_arr + 2
array([3, 4, 5, 6, 7])
>>>
```

Your numpy version may be different; that is fine.

Pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language. Let us install the big brother of numpy, _pandas_:

```bash
python -m pip install pandas
```

```python
>>> import pandas
>>>
```

If the import gives no error, pandas is installed.

This section is not about numpy nor pandas, here we are trying to learn how to install packages and how to import them. If it is needed, we will talk about different packages in other sections.

Let us import a web browser module, which can help us to open any website. We do not need to install this module, it is already installed by default with Python 3. For instance if you like to open any number of websites at any time or if you like to schedule something, this _webbrowser_ module can be used.

```python
import webbrowser # web browser module to open websites

# list of urls: python
url_lists = [
    'https://www.python.org',
    'https://adci.edu.au',
    'https://docs.python.org/3/',
    'https://pypi.org',
]

# opens the above list of websites in a different tab
for url in url_lists:
    webbrowser.open_new_tab(url)
```

### Uninstalling Packages

If you do not like to keep the installed packages, you can remove them using the following command.

```bash
python -m pip uninstall packagename
```

### List of Packages

To see the installed packages on our machine. We can use pip followed by list.

```bash
python -m pip list
```

### Show Package

To show information about a package

```bash
python -m pip show packagename
```

```bash
python -m pip show requests
```

```output
Name: requests
Version: 2.34.2
Summary: Python HTTP for Humans.
Home-page:
Author:
Author-email: Kenneth Reitz <me@kennethreitz.org>
License: Apache-2.0
Location: C:\...\site-packages
Requires: certifi, charset_normalizer, idna, urllib3
Required-by:
```

If we want even more details, just add --verbose

```bash
python -m pip show --verbose requests
```

### PIP Freeze

Generate installed Python packages with their version and the output is suitable to use it in a requirements file. A requirements.txt file is a file that should contain all the installed Python packages in a Python project.

```bash
python -m pip freeze
```

```output
certifi==2026.7.22
idna==3.20
numpy==2.5.3
pandas==3.0.6
requests==2.34.2
urllib3==2.8.0
```

Your list and version numbers will differ. The pip freeze gave us the packages used, installed and their version. We use it with requirements.txt file for deployment.

### Reading from URL

By now you are familiar with how to read or write on a file located on your local machine. Sometimes, we would like to read from a website using url or from an API.
API stands for Application Program Interface. It is a means to exchange structured data between servers primarily as json data. To open a network connection, we need a package called _requests_ - it allows to open a network connection and to implement CRUD(create, read, update and delete) operations. In this section, we will cover only reading or getting part of a CRUD.

Let us install _requests_:

```bash
python -m pip install requests
```

We will see _get_, _status_code_, _headers_, _text_ and _json_ methods in _requests_ module:
  - _get()_: to open a network and fetch data from url - it returns a response object
  - _status_code_: After we fetched data, we can check the status of the operation (success, error, etc)
  - _headers_: To check the header types
  - _text_: to extract the text from the fetched response object
  - _json_: to extract json data

Let's read a text file from Project Gutenberg: the play *Romeo and Juliet*.

```python
import requests # importing the request module

url = 'https://www.gutenberg.org/cache/epub/1112/pg1112.txt' # text from a website

response = requests.get(url) # opening a network and fetching a data
print(response)                          # <Response [200]>
print(response.status_code)              # 200 - status code, success
print(response.headers['Content-Type'])  # text/plain; charset=utf-8
print(response.text[:47])                # The Project Gutenberg eBook of Romeo and Juliet
```

- Let us read from an API. PyPI, the website pip installs packages from, has a JSON API that describes every package: https://pypi.org/pypi/requests/json

```python
import requests

url = 'https://pypi.org/pypi/requests/json'  # information about the requests package
response = requests.get(url)  # opening a network and fetching a data
print(response)              # <Response [200]>
print(response.status_code)  # 200
package = response.json()    # change the JSON into a Python dictionary
print(package['info']['name'])     # requests
print(package['info']['version'])  # e.g. 2.34.2 - the newest version when you run it
print(package['info']['summary'])  # Python HTTP for Humans.
```

We use _json()_ method from response object, if the we are fetching JSON data. For txt, html, xml and other file formats we can use _text_.

### Creating a Package

We organize a large number of files in different folders and sub-folders based on some criteria, so that we can find and manage them easily. As you know, a module can contain multiple objects, such as classes, functions, etc. A package can contain one or more relevant modules. A package is actually a folder containing one or more module files. Let us create a package named mypackage, using the following steps:

Create a new folder named mypackage inside IntroToProgramming folder
Create an empty **__init__**.py file in the mypackage folder.
Create modules arithmetics.py and greet.py with following code:

```python
# mypackage/arithmetics.py
# arithmetics.py
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

def subtract(a, b):
    return (a - b)

def multiple(a, b):
    return a * b

def division(a, b):
    return a / b

def remainder(a, b):
    return a % b

def power(a, b):
    return a ** b
```

```python
# mypackage/greet.py
# greet.py
def greet_person(firstname, lastname):
    return f'{firstname} {lastname}, welcome to Intro to Programming!'
```

The folder structure of your package should look like this:

```output
─ mypackage
    ├── __init__.py
    ├── arithmetics.py
    └── greet.py
```

Now let's open the python interactive shell and try the package we have created:

Open the Python interactive shell from your IntroToProgramming folder (the folder that contains mypackage):

```python
>>> from mypackage import arithmetics
>>> arithmetics.add_numbers(1, 2, 3, 5)
11
>>> arithmetics.subtract(5, 3)
2
>>> arithmetics.multiple(5, 3)
15
>>> arithmetics.division(5, 3)
1.6666666666666667
>>> arithmetics.remainder(5, 3)
2
>>> arithmetics.power(5, 3)
125
>>> from mypackage import greet
>>> greet.greet_person('Jack', 'Wilson')
'Jack Wilson, welcome to Intro to Programming!'
>>>
```

As you can see our package works perfectly. The package folder contains a special file called **__init__**.py - it stores the package's content. If we put **__init__**.py in the package folder, python start recognizes it as a package.
The **__init__**.py exposes specified resources from its modules to be imported to other python files. An empty **__init__**.py file makes all functions available when a package is imported. The **__init__**.py is essential for the folder to be recognized by Python as a package.

### Further Information About Packages

- Database
  - SQLAlchemy or SQLObject - Object oriented access to several different database systems
    - _pip install SQLAlchemy_
- Web Development
  - Django - High-level web framework.
    - _pip install django_
  - Flask - micro framework for Python based on Werkzeug, Jinja 2. (It's BSD licensed)
    - _pip install flask_
- HTML Parser
  - [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - HTML/XML parser designed for quick turnaround projects like screen-scraping, will accept bad markup.
    - _pip install beautifulsoup4_
  - PyQuery - implements jQuery in Python; faster than BeautifulSoup, apparently.

- XML Processing
  - ElementTree - The Element type is a simple but flexible container object, designed to store hierarchical data structures, such as simplified XML infosets, in memory. --Note: Python 2.5 and up has ElementTree in the Standard Library
- GUI
  - PyQt - Bindings for the cross-platform Qt framework.
  - TkInter - The traditional Python user interface toolkit.
- Data Analysis, Data Science and Machine learning
  - Numpy: Numpy(numeric python) is known as one of the most popular machine learning library in Python.
  - Pandas: is a data analysis, data science and a machine learning library in Python that provides data structures of high-level and a wide variety of tools for analysis.
  - SciPy: SciPy is a machine learning library for application developers and engineers. SciPy library contains modules for optimization, linear algebra, integration, image processing, and statistics.
  - Scikit-Learn: It is NumPy and SciPy. It is considered as one of the best libraries for working with complex data.
  - TensorFlow: is a machine learning library built by Google.
  - Keras: is considered as one of the coolest machine learning libraries in Python. It provides an easier mechanism to express neural networks. Keras also provides some of the best utilities for compiling models, processing data-sets, visualization of graphs, and much more.
- Network:
  - requests: is a package which we can use to send requests to a server(GET, POST, DELETE, PUT)
    - _pip install requests_

::::::::::::::::::::::::::::::::::::: challenge

## Exercises

1. Read this url and find the 10 most frequent words. romeo_and_juliet = 'https://www.gutenberg.org/cache/epub/1112/pg1112.txt'
2. Read the cat breeds API, cat_breeds_api = 'https://catfact.ninja/breeds?limit=100', and create a frequency table of the country each breed comes from (the data is in the 'data' key).
3. Use the PyPI JSON API (https://pypi.org/pypi/PACKAGE_NAME/json) to print the newest version and the summary of numpy, pandas and requests.
4. UCI is one of the most common places to get data sets for data science and machine learning. Read the content of UCI (https://archive.ics.uci.edu/datasets). Without additional libraries it will be difficult, so you may try it with BeautifulSoup4

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: keypoints

- Use python -m pip so packages install for the Python you run.
- pip freeze lists installed packages for a requirements.txt file.
- A folder with an __init__.py file is a package.

::::::::::::::::::::::::::::::::::::::::::::::::
