from typing import Optional, Tuple, Union

import pandas as pd

from ...utils.cli import *
from ...utils.tex import TeXDefaults as tex


class Bar():
    """
    """
    def __init__(
        self,
        data: dict = None,
        options: dict = None
    ) -> None:
        self.data = data
        self.options = options
        self.plot_declarations: list = []

        if data is None:
            log.warning("I'm not much good without data, you know...")

    @staticmethod
    def _template() -> None:
        r"""
        \begin{doctor-bar}[%
        plot type={ybar},
        data source={src/plots/bar.dat},
        somebool=false,
        caption={Hello, world!},
        label={bar-test},
        xmin=0,
        xmax=12,
        ymin=0,
        ymax=35,
        ]%
        \addplot+[%
            nodes near coords,
            point meta=explicit symbolic,
            mark=none,
            ons-blue,
            very thick
        ] table [x=index, y=values, meta=values]%
        {\doctordatasource};
        \end{doctor-bar}
        """
        pass

    @property
    def env_begin(self) -> str:
        """
        Define plotting environment start.
        """
        return r"\begin{doctor-bar}%"

    @property
    def env_end(self) -> str:
        """
        Define plotting environment end.
        """
        return r"\end{doctor-bar}%"

    @property
    def env_body(self) -> str:
        """
        Render and compile all plotting syntax declarations sequentially between
        begin and end environment definitions.

        Args:
        None.

        Returns:
        Compilation of all plots declared in `self.data` input dict as formatted
        TeX macros.

        Raises:
        None.
        """
        [self.add_plot() for _ in list(self.data)]
        return "\n%\n".join(syn for syn in self.plot_declarations)
