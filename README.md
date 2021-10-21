# Conreq App Store Manager

This repo is used to add and save Conreq Community App Store listings. You can clone this repo to run the App Store Manager to add new listings. Create a pull request to save your changes to this repository.

## Software Required

-   Install [Python 3.9+](https://www.python.org/downloads/)
    -   Make sure to select "Add Python 3.x to PATH" during installation.
    -   Easiest if this is the only version of python on your computer
-   _Optional_: Install [Visual Studio Code](https://code.visualstudio.com/) (Suggested, but any editor would work)

## Installing and Running the App Store Manager

1. Pull the repository from GitHub.
2. Open a terminal (ex. Command Prompt or PowerShell) as administrator at the root of the repository.
3. _If using Windows_
    - Type `set-executionpolicy remotesigned` and select Yes to All to allow external Python scripts to run on your computer.
4. Type `python -m venv .venv` to create a Python virtual environment called ".venv".
5. Type `./.venv/Scripts/activate` to enter the virtual environment.
6. Type `pip install -r requirements.txt` to install all Python dependencies within the virtual environment.
7. Type `python manage.py run_conreq` to run the webserver.
