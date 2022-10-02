from dataclasses import dataclass
from typing import List

import yaml


@dataclass
class ConfigAbout:
    author: str
    description: str


@dataclass
class ConfigPaths:
    report: str


@dataclass
class ConfigPlot:
    colours: List[str]
    opacities: List[str]


@dataclass
class ConfigTable:
    size: str


@dataclass
class DwrConfig:
    about: ConfigAbout
    paths: ConfigPaths
    plot: ConfigPlot
    table: ConfigTable


def read_config(config_path: str) -> DwrConfig:
    with open(config_path, "r", encoding="utf8") as file:
        config = yaml.safe_load(file)
        return DwrConfig(**config)
