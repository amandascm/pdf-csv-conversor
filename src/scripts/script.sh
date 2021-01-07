#!/bin/bash

#install virtualenv (python)
python3 -m pip install --user virtualenv

#check if virtual environment has already been created
DIR=".venv"
if [ ! -d "$DIR" ]; then
    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip install -r requirements.txt
    deactivate
fi
#activate virtual environment and run program
source .venv/bin/activate
python main.py
deactivate