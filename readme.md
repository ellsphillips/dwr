<h1 stylecolor: #FFD866>Doctor</h1>

<svg fill="none" viewBox="0 0 400 400" width="400" height="400" xmlns="http://www.w3.org/2000/svg">
    <foreignObject width="100%" height="100%">
        <div xmlns="http://www.w3.org/1999/xhtml">
            <style>
            h1 {
                color: #FFD866;
            }
            </style>
            <h1>Doctor</h1>
        </div>
    </foreignObject>
</svg>

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
