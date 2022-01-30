import os

import doctor as dr


def main() -> None:
    
    cfg = dr.read_config("./doctor/config/config.yaml")

    print(cfg.about)

    result = dr.plot(
        "line",
        [
            dr.data.series.brownian(),
            dr.data.series.brownian(),
            dr.data.series.brownian(),
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
