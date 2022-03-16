import os

import doctor as dr


def main() -> None:

    cfg = dr.read_config("./doctor/config/config.yaml")

    #

    tabular = dr.table(
        dr.data.table(
            [
                dr.data.text.lorem(10),
                dr.data.text.lorem(10),
                dr.data.text.lorem(10),
                dr.data.text.lorem(10),
            ]
        )
    )

    render = dr.render(tabular)

    dr.save(render, "/path/to/save_dir")

    #

    figure = dr.plot(
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

    dr.render(figure)


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    print(f"Doctor {dr.__version__}", dr.__doc__, sep="\n")
    main()
