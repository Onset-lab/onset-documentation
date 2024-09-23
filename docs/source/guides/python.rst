Python
====================

.. role:: bash(code)
   :language: bash

.. role:: python(code)
   :language: python

.. role:: json(code)
   :language: json


What is Python?
---------------

Python is a versatile, high-level programming language known for its simplicity, readability, and ease of use.
It supports multiple programming paradigms, including object-oriented, procedural, and functional programming.
Python's rich ecosystem of libraries and frameworks makes it ideal for tasks ranging from web development and
data analysis to artificial intelligence and automation. Its robust community support and extensive documentation
allow developers to quickly learn and implement solutions. Python's clear syntax encourages code readability,
making it a popular choice for both beginners and experienced developers.

In the lab, we recommend to use python 3.10.

.. note::
    If python 3.10 is not available, you can install it using the following command:
    ``sudo add-apt-repository ppa:deadsnakes/ppa && sudo apt-get update && sudo apt-get install python3.10``

**Ressources:**
    - Step-by-Step Python tutorial `[link] <https://www.w3schools.com/python/python_intro.asp>`__
    - Introduction to Python `[link] <https://www.programiz.com/python-programming/first-program>`__
    - Mix of basic and advanced tutorials `[link] <https://www.learnpython.org/>`__


Integrated Development Environment (IDE)
----------------------------------------

We recommend using Visual Studio Code (VSCode) as your primary code editor for Python development. VSCode is a
lightweight, open-source editor that offers powerful features like IntelliSense, integrated debugging, Git support,
and an extensive marketplace for extensions. Its Python extension enhances the development experience with
features such as code linting, auto-completion, and seamless integration with virtual environments. VSCode's
intuitive interface and rich set of tools make it a great choice for developers of all skill levels, ensuring a
smooth and productive Python development workflow.

To install Visual Studio Code, download the `.deb` file from the `official website <https://code.visualstudio.com/download>`__
and run the following command: ``sudo dpkg -i code_*.deb``

In VSCode, you can install the Python extensions by clicking on the Extensions icon in the sidebar, searching for:

- autoDocstring
- Black Formatter
- Pylance
- Python
- Python Debugger
  
Optionnaly, you can install the following extensions:

- reStructuredText
- Github Actions

In the lab, we recommend to use the following settings in VSCode:

* In File > Preferences > Settings:
    * Click on the "Open settings (JSON)" button (top right button with an arrow on a blank page)
      to open the `settings.json` file.
    * Add the following lines to the end of the file:

    .. code-block:: json
        :caption: settings.json

        ...
        "[python]": {
                "editor.rulers": [
                    100
                ],
                "editor.defaultFormatter": "ms-python.black-formatter",
                "editor.formatOnSave": true
                "formatting.blackArgs": [
                    "--line-length",
                    "100"
                ]
            },

Virtual Environment
-------------------

Virtualenv is a tool that helps to create isolated Python environments, allowing you to manage dependencies for
different projects without conflict.

1. To install virtualenv, run the following command: ``pip install virtualenvwrapper``
2. Create a directory for all your virtual environments: ``mkdir ~/my_envs``
3. In your ``~/.bashrc`` file, add the following lines: 
   
  .. code-block:: bash
    
    export WORKON_HOME=$HOME/my_envs
    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.10
    source /usr/local/bin/virtualenvwrapper.sh

1. To create a virtual environment, run the following command: ``mkvirtualenv venv`` or ``mkvirtualenv -p python3.10 venv`` 
   or ``mkvirtualenv -p YOUR_PYTHON_VERSION venv``.
2. To activate the virtual environment, run the following command: ``workon venv``
3. To deactivate the virtual environment, run the following command: ``deactivate``

For example, to create a virtual environment named `onsetpy`, run the following commands:

.. code-block:: bash
    :caption: Create a virtual environment for onsetpy

    #1. Create a virtual environment
    mkvirtualenv onsetpy

    #2. Activate the virtual environment
    workon onsetpy

    # 4. Install onsetpy
    git clone git@github.com:Onset-lab/onsetpy.git
    cd onsetpy
    pip install -e .

    # 5. Run a script
    python onset_mean_std_connectivity_matrix.py -h

    # 6. Deactivate the virtual environment
    deactivate