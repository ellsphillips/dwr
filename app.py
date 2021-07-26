import os

import doctor
import data

@doctor.timer
def main():
  """
  Scripting environment for Python data to TeX markup conversion.
  """
  table = doctor.table(
    data.numerical((20, 8)),
    column_format=[0.1, 0.2, 0.3, 0.4],
    caption="Example table generated by Python",
    short_caption="Shorter caption for TOC",
    label="tabledemo"
  )

  #

  figure = doctor.plot(
    data = {
      "data1": data.series_lognuniform(points=20, places=4),
      "data2": data.series_lognuniform(points=34, places=4),
    },
    options = {
      "xlabel": "Horizontal",
      "ylabel": "Vertical",
      "caption": "Test caption",
      "shade": {
        "fill": "solid",
        "colour": "ONSpink",
        "regions": [[9, 27], [50, "end"]]
      }
    }
  )

  figure.add_shade(
    domain=(figure.axis_bound("x", "min"), 10),
    range=(figure.axis_bound("y", "min"), figure.axis_bound("y", "max")),
    fill="hatch"
  )

  print(figure.get_result())

  # figure.export("graphs/auto-gen")

  # doctor.build(outfile="report", quick=False)

if __name__ == "__main__":
  os.system('cls' if os.name == 'nt' else 'clear')
  doctor.log.announce("The [Doctor] was called...")
  doctor.log.notice(f"Version: ({doctor.__version__})")

  main()

  print(data.series_brownian())
