import os

import data
import doctor as dr


def main() -> None:

    result = dr.plot(
        "line",
        [
            data.series.brownian(),
            data.series.brownian(),
            data.series.brownian(),
        ],
        options={
            "plot type": "ybar",
            "data source": "src/plots/example.dat",
            "caption": "Demonstration of the doctor-plot environment",
            "label": "example-plot",
        },
    )

    dr.render(result)


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
