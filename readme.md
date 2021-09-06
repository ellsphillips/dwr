[repo-card-api]: https://github-readme-stats.vercel.app/api/pin/?username=ellsphillips&theme=react&repo=doctor&card_width=100%
[repo-card]: https://github.com/ellsphillips/doctor
[doctor-build]: https://i.imgur.com/8iuEgjZ.gif
[doctor-logo]: https://raw.githubusercontent.com/ellsphillips/doctor/master/docs/assets/doctor-logo.svg

<p align="center">
  <a href="https://raw.githubusercontent.com/ellsphillips/doctor/master/docs/assets/doctor-logo.svg" rel="noopener" target="_blank"><img width="250" src="https://raw.githubusercontent.com/ellsphillips/doctor/master/docs/assets/doctor-logo.svg" alt="Material-UI logo"></a></p>
</p>

<h1 align="center">Doctor</h1>

An automated documentation assitant built in Python and TeX for procedural, data-driven reporting.

Doctor simplifies the reporting build process through an intuitive Python API and customisable LaTeX class to responsively markup Pythonic data objects to professionally typeset lightweight documents.

---

## Installation

Clone the repo

```bash
$ git clone https://github.com/ellsphillips/doctor.git

$ cd doctor
```

Install the requirements

```bash
$ pip install -r requirements.txt
```

## Usage

Once installed, you readily have access to Doctor's `table` and `plot` builder methods. Basic examples of each are listed here, but for more complex example usage and a complete list of options from the API, head over to our documentation.

```python
  import doctor

  table = doctor.table(
    data.numerical((8, 4)),
    column_format=[0.1, 0.2, 0.3, 0.4],
    caption="Example table generated by Python",
    short_caption="Shorter caption for TOC",
    label="tabledemo"
  )

  figure = doctor.plot(
    type = "timeseries",
    data = {
      "data1": data.series_brownian(points=20),
      "data2": data.series_brownian(points=34),
    },
    options = {
      "xlabel": "Horizontal",
      "ylabel": "Vertical",
      "caption": "Test caption",
      "shade": {
        "fill": "solid",
        "colour": "ONSpink",
        "domain": (9, "x_min"),
        "range": ("y_min", "y_max")
      }
    }
  )

  figure.export("path/to/file")

  doctor.build(outfile="report")
```

Define each of your LaTeX figures with a new builder method. If your IDE doesn't provide intellisense, please see the manual for reference.

![Build your PDF with Doctor][doctor-build]

## Outputs

[](#outputs)

You can inspect the result through the console with `doctor.get_result()`, or use the provided `write_to()` method to output your LaTeX result to a relative directory path.

```python
  table = doctor.table(...)

  doctor.write_to("path/to/file")
```

This generates a new file if the name space is undefined, otherwise overwrites the content of the file. Doctor assumes you organise your LaTeX code through `input{}` calls.

Reference the [architecture below](#architecture) for an example.

```latex
  \begin{doctor-table}{4}
    {% Column format
      >{{\raggedleft\arraybackslash\hsize=\hsize}}X
      >{{\raggedleft\arraybackslash\hsize=\hsize}}X
      >{{\raggedleft\arraybackslash\hsize=\hsize}}X
      >{{\raggedleft\arraybackslash\hsize=\hsize}}X
    }{% Column headers
      \bfseries Numbers &
      \bfseries More numbers &
      \bfseries Text &
      \bfseries Mash \\
    }{% Caption
      Example table generated by Python
    }{% Label
      test
    }
    25 & 43 &       Lorem & iswdufvbouwesdbnvg \\
    82 & 71 &       ipsum &                abc \\
    23 & 52 &       dolor &            sdvcsdv \\
    82 & 85 &         sit &       sdvdssdvdvvn \\
    93 & 63 &        amet &          yumyumyum \\
    83 & 35 & consectetur &               wqoe \\
    87 & 51 &  adipiscing &            qphjpgh \\
    79 & 41 &        elit &    owperjgpowegjwj \\
    84 & 88 &   Curabitur &        wepogjwpeog \\
    60 &  7 &         nec &                 oi \\
  \end{doctor-table}
```

## Architecture

[](#architecture)

```shell
  doctor/
  ├── data
  │   ├── __init__.py
  │   └── data.py
  ├── demo
  │   ├── src
  │   │   └── ...
  │   ├── doctor.cls
  │   ├── main.tex
  │   └── report.pdf
  ├── doctor
  │   ├── builder
  │   │   ├── plot
  │   │   └── table
  │   ├── utils
  │   │   ├── __init__.py
  │   │   ├── cli.py
  │   │   └── tex.py
  │   ├── __init__.py
  │   └── doctor.py
  └── app.py
```

<img src="https://raw.githubusercontent.com/ellsphillips/doctor-assets/main/map.svg" alt="Choropleth example">
