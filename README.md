# Word Cloud

Generates a word cloud image based on an input text file.

> Expects `.odt` file as input and saves as `.png`.

## Requirements

- Python 3.10+
- Pyenv
- Pip

## Setup

```shell
PROJECT_NAME=word-cloud
PYTHON_VERSION=$(<.python-version)

# setup python virtual env
pyenv install ${PYTHON_VERSION}
pyenv local ${PYTHON_VERSION}
python -m venv "${PROJECT_NAME}-env"
source "${PROJECT_NAME}-env/bin/activate"

# install deps
pip install -r requirements.txt
```

> You can deactivate the virtual env by runnning: `deactivate`

## Usage

```shell
# from an ODT file, saving to default path `outputs/wordcloud.png`
python bin/generate.py --input_file /path/to/input.odt

# specifying the output file
python bin/generate.py --input_file /path/to/input.odt --output_file /path/to/output.png

# passing words to be filtered out from the output
python bin/generate.py --input_file /path/to/input.odt --custom_stopwords word1 word2 word3
```
