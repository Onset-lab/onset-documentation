# Python
## What is Python?

Python is a versatile, high-level programming language known for its simplicity, readability, and ease of use. It supports multiple programming paradigms, including object-oriented, procedural, and functional programming. Its extensive ecosystem of libraries and frameworks makes it ideal for tasks ranging from web development to data analysis, artificial intelligence, and automation. Python’s active community and abundant documentation help developers learn quickly and implement effective solutions. Its clear syntax promotes code readability, making it a popular choice for both beginners and experienced developers.

> **Note**  
> In our lab, we recommend using Python 3.10.  
> If Python 3.10 is not available, you can install it with the following command:  
> ```bash
> sudo add-apt-repository ppa:deadsnakes/ppa && sudo apt-get update && sudo apt-get install python3.10
> ```

**Useful resources:**
- [Step-by-step Python tutorial](https://www.w3schools.com/python/python_intro.asp)
- [Introduction to Python](https://www.programiz.com/python-programming/first-program)
- [Basic and advanced tutorials](https://www.learnpython.org/)

---

## Integrated Development Environment (IDE)

We recommend using Visual Studio Code (VSCode) as the main editor for Python development. VSCode is a lightweight, open-source editor offering powerful features such as IntelliSense, built-in debugging, Git integration, and a vast extension marketplace. The Python extension enhances the development experience with tools like linting, auto-completion, and seamless integration with virtual environments. VSCode’s intuitive interface and numerous tools make it an excellent choice for all skill levels.

To install Visual Studio Code, download the `.deb` file from the [official website](https://code.visualstudio.com/download) and run:
```bash
sudo dpkg -i code_*.deb
```

In VSCode, install the following Python extensions via the Extensions icon in the sidebar:

- autoDocstring
- Black Formatter
- Pylance
- Python
- Python Debugger

Optional:
- reStructuredText
- Github Actions

**Recommended settings in VSCode:**

In `File > Preferences > Settings`, click "Open Settings (JSON)" (icon at the top right) to open `settings.json` and add:

```json
"[python]": {
    "editor.rulers": [
        100
    ],
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.formatOnSave": true,
    "formatting.blackArgs": [
        "--line-length",
        "100"
    ]
},
```

---

## Virtual Environment

`virtualenv` allows you to create isolated Python environments to manage dependencies for each project.

1. Install virtualenvwrapper:
    ```bash
    pip install virtualenvwrapper
    ```
2. Create a folder for your environments:
    ```bash
    mkdir ~/my_envs
    ```
3. Add to your `~/.bashrc`:
    ```bash
    export WORKON_HOME=$HOME/my_envs
    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.10
    source /usr/local/bin/virtualenvwrapper.sh
    ```
4. Create a virtual environment:
    ```bash
    mkvirtualenv venv
    # or for a specific version:
    mkvirtualenv -p python3.10 venv
    ```
5. Activate the environment:
    ```bash
    workon venv
    ```
6. Deactivate the environment:
    ```bash
    deactivate
    ```

**Example: create an environment for `onsetpy`**

```bash
# 1. Create the virtual environment
mkvirtualenv onsetpy

# 2. Activate the environment
workon onsetpy

# 3. Install onsetpy
git clone git@github.com:Onset-lab/onsetpy.git
cd onsetpy
pip install -e .

# 4. Run a script
python onset_create_epinsight_report -h

# 5. Deactivate the environment
deactivate
```
