class TeXDefaults:
    """
    Ensure user has all supporting TeX content to pair with Dwr.
    """

    document = {"path": "document/", "name": "main"}

    requirements = {
        "inputenc": ["utf8"],
        "fontenc": ["T1"],
        "textcomp": [],
        "gensymb": [],
        "babel": ["english"],
        "ragged2e": ["document"],
        "float": [],
        "bm": [],
        "amsfonts": [],
        "cancel": [],
        "varwidth": [],
        "blindtext": [],
        "underscore": [],
        "lipsum": [],
        "geometry": ["a4paper,left=2.5cm,right=2.5cm,bottom=3cm,top=4cm"],
        "graphicx": [],
        "caption": [],
        "fp": [],
        "epstopdf": [],
        "framed": [],
        "amsmath": [],
        "textpos": ["absolute"],
        "fancyhdr": [],
        "xkeyval": [],
        "alphalph": [],
        "ifthen": [],
        "appendix": [],
        "titletoc": [],
        "etoolbox": [],
        "emptypage": [],
        "afterpage": [],
        "hyperref": ["verbose"],
        "tcolorbox": [],
        "tikz": [],
        "tkz-euclide": [],
        "pgfplots": [],
        "collcell": [],
        "booktabs": [],
        "longtable": [],
        "multirow": [],
        "multicol": [],
        "colortbl": [],
        "hhline": [],
        "dcolumn": [],
        "tabularx": [],
        "ctable": [],
        "xltabular": [],
        "silence": [],
    }

    libraries = [
        r"\usepgfplotslibrary{fillbetween}",
        r"\usetikzlibrary{intersections}",
        r"\pgfplotsset{compat=1.12}",
    ]
