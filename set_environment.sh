#!/bin/bash

ENV_NAME="resume"
CONDA_ACTIVATE_DIR=`which activate`

echo "setting $ENV_NAME environment"

# Create Conda Virtual Environment
conda create --name $ENV_NAME python=3.10 --y

# Activate Virtual Environment
source $CONDA_ACTIVATE_DIR $ENV_NAME

echo "python version is:"
python --version

echo "upgrading pip..."
pip install --upgrade pip

echo "conda env created and activated successfully"

# Install Required Packages
echo "Installing requirements.txt packages..."
pip install -r requirements.txt

echo "packages installed successfully"

conda deactivate

mkdir -p .streamlit/

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
[theme]\n\
primaryColor = '#d33682'\n\
backgroundColor = '#002b36'\n\
secondaryBackgroundColor = '#586e75'\n\
textColor = '#fff'\n\
" > .streamlit/config.toml
