import pandas as pd
import numpy as np
import random
from typing import (
  Tuple
)

def numerical(
  shape: Tuple[int, int]
) -> pd.DataFrame:
  return pd.DataFrame(
    lognuniform(size=shape).astype(int),
    columns=["col" + str(i + 1) for i in range(shape[1])]
  )

def mixed():
  return pd.DataFrame(
    {
      'Numbers': [np.random.randint(0, 100) for i in range (10)],
      'More numbers': [np.random.randint(0, 100) for i in range (10)],
      'Text': "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur nec".split(),
      'Mash': [
        "iswdufvbouwesdbnvg",
        "abc",
        "sdvcsdv",
        "sdvdssdvdvvn",
        "yumyumyum",
        "wqoe",
        "qphjpgh",
        "owperjgpowegjwjggg",
        "wepogjwpeog",
        "oi"
      ]
    }
  )

def lognuniform(low=0, high=10, size=None, base=np.e):
  return np.power(base, np.random.uniform(low, high, size))

def lorem(count: int) -> list:
  return ["Lorem", "Ipsum", random.choices(dummy_text, count - 2)]


dummy_text = """
  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut a orci vitae urna rhoncus bibendum convallis eget odio. Sed vitae vulputate eros. Quisque in felis leo. Suspendisse potenti. Phasellus convallis ex vitae tristique imperdiet. Integer semper ligula in nisi rhoncus gravida eget sit amet dolor. Cras id risus in risus ultricies vehicula. Pellentesque in sem facilisis arcu rhoncus maximus. Nam sollicitudin neque quis lectus euismod ultricies. Maecenas et tellus sit amet erat mattis auctor ac et eros. Maecenas id enim et neque pretium venenatis sit amet eu nulla. Quisque nec mauris lectus. Donec purus risus, rutrum eget risus eu, faucibus imperdiet ipsum.
  Phasellus eleifend tempor ligula. Nam ultricies augue mi. Maecenas id placerat neque, et congue neque. Duis ac rutrum arcu. Praesent ullamcorper lacus non nisl rhoncus tincidunt. Maecenas sit amet nisl eget metus faucibus congue. Etiam posuere eget neque tincidunt porttitor. Vestibulum diam nulla, tempus et commodo ac, fringilla id mi. Praesent convallis in velit quis molestie. Morbi ultricies elementum quam et vestibulum. Nam semper bibendum eros.
  Morbi sed ornare odio, eu sodales nisi. Vivamus quis erat mauris. Nulla sed pulvinar tellus, non viverra odio. Donec quis consequat velit, ut volutpat tellus. Etiam suscipit, orci at viverra ultrices, leo lorem ornare augue, at pretium neque odio vitae risus. Curabitur rhoncus sagittis placerat. In et odio varius, tincidunt diam sit amet, condimentum quam.
  Donec tempor urna vel enim dignissim auctor. Nullam nisl sem, pellentesque at mattis eget, dictum eget neque. Maecenas lectus orci, mattis quis nisi a, venenatis bibendum dui. Integer lacinia, nisl at sodales posuere, lectus libero hendrerit sapien, vel eleifend elit enim id tellus. Duis laoreet sapien metus, sit amet scelerisque felis dictum id. Sed nec ante augue. Vestibulum lobortis rhoncus purus. Phasellus rhoncus odio purus, eget vulputate sem iaculis porta. Quisque ultrices ligula vel diam mattis dictum. Pellentesque at convallis metus, eu sollicitudin lectus. Nunc enim neque, gravida vitae velit non, lacinia rhoncus nisi. Vivamus sed sodales metus, eu posuere diam. Praesent quis dolor vel ante tempor pharetra sit amet sit amet felis. Fusce imperdiet quam orci, id elementum elit fringilla pulvinar. In molestie dui sed enim hendrerit, nec molestie risus sodales.
  Maecenas posuere lectus velit, non lacinia orci bibendum sed. Mauris vestibulum urna id dui ornare imperdiet. Pellentesque rhoncus nisl egestas dolor scelerisque, a pellentesque mauris ullamcorper. Aliquam ullamcorper, magna non laoreet accumsan, sem quam sodales leo, sed malesuada eros sem non lorem. Praesent quis eros bibendum, sodales sem ac, maximus sem. Suspendisse a ultricies justo. Aliquam at nunc sit amet augue malesuada lobortis. Morbi sed est blandit turpis varius hendrerit ut ut odio. Duis egestas facilisis condimentum. Quisque auctor sollicitudin tellus. Proin et faucibus turpis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nullam sapien mauris, gravida at elementum et, condimentum quis nunc. 
"""