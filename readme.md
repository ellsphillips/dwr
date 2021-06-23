# Doctor

An automated documentation assitant for Pythonic data markup to LaTeX.

Procedurally generate PDF reports from `pandas` DataFrame, `list` and `dictionary` objects to beautiful, flexible LaTeX documents.

## Installation

Clone the repo

```
git clone https://github.com/ellsphillips/doctor.git

cd doctor
```

Install the requirements

```
pip install -r requirements.txt
```

## Architecture

```shell
  doctor/
  ├── data
  │   ├── __init__.py
  │   ├── data.py
  ├── demo
  │   ├── src
  │   │   └── ...
  │   ├── doctor.cls
  │   ├── main.tex
  │   ├── report.pdf
  ├── doctor
  │   ├── builder
  │   │   ├── plot
  │   │   └── table
  │   ├── utils
  │   │   ├── __init__.py
  │   │   ├── cli.py
  │   │   └── tex.py
  │   ├── __init__.py
  │   ├── doctor.py
  └── app.py
```
