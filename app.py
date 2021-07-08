from doctor.utils.cli import style, timer
import os
import pandas as pd
import numpy as np

import doctor
import data

@timer
def main():
  os.system('cls' if os.name == 'nt' else 'clear')
  print("\n"*100)
  print(f"The {style.announce}Doctor{style.end} was called...\n")

  table = doctor.table(
    data.numerical((8, 4)),
    column_format=[0.1, 0.2, 0.3, 0.4],
    caption="Example table generated by Python",
    short_caption="Shorter caption for TOC",
    label="tabledemo"
  )

  # doctor.build(outfile="report", quick=True)

  #

  figure = doctor.plot(
    data = {
      "data1": data.timeseries_singleton(points=20, places=(1,3)),
      "data2": data.timeseries_singleton(points=20, places=(1,3)),
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

  print(figure.id_data())

  print(figure.build_dataframe())
  

if __name__ == "__main__":
  main()
