from dataclasses import dataclass
from typing import List

import yaml


@dataclass
class CfgAbout:
    author: str
    description: str


@dataclass
class CfgPaths:
    report: str


@dataclass
class CfgPlot:
    colours: List[str]
    opacities: List[str]


@dataclass
class CfgTable:
    size: str


@dataclass
class DoctorConfig:
    about: CfgAbout
    paths: CfgPaths
    plot: CfgPlot
    table: CfgTable


def read_config(config_path: str) -> DoctorConfig:
    with open(config_path, "r", encoding="utf8") as file:
        config = yaml.safe_load(file)
        return DoctorConfig(**config)


def read_yaml_file(filename: str):
    with open(filename, "r", encoding="utf8") as stream:
        try:
            print(yaml.safe_load(stream))
        except yaml.YAMLError as exc:
            print(exc)


read_yaml_file("./doctor/config/config.yaml")

cfg = read_config("./doctor/config/config.yaml")

print(cfg.about)
