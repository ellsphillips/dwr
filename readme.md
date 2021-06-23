<style>
  :root{
    --doctor-primary: #FFD866;
    --doctor-secondary: #3572A5;
  }

  h1, h2, h3 {
    color: var(--doctor-primary);
  }

  :is(h1, h2, h3):not(:first-of-type) {
    margin-top: 2em;
  }

  blockquote {
    border: var(--doctor-primary) 2px solid;
    padding: 1.5em;
    margin-bottom: 2em;
  }

  ::marker {
    color: var(--doctor-primary);
  }
</style>

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
