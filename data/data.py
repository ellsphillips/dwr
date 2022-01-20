import random
from typing import List, Tuple, Union

import numpy as np
from pandas import DataFrame


def series_lognuniform(
    points: int = 10, places: Union[int, Tuple[int, int]] = 4
) -> List[float]:
    return [
        *lognuniform(
            size=points,
            low=places[0] if isinstance(places, tuple) else 0,
            high=places[1] if isinstance(places, tuple) else places,
            base=10,
        )
    ]


def series_brownian(points: int = 100, horizon: float = 1.0) -> List[str]:
    """
    Using Brownian motion's defining characteristic of independent, normally,
    distributed increments [Bt2 - Bt1 ~ Normal(mu=0, sigma=t2-t1)]
    """
    times: List[float] = np.linspace(0.0, horizon, points)
    delta_t = times[1] - times[0]
    delta_b: float = np.sqrt(delta_t) * np.random.normal(size=(points - 1,))
    b_initial: List[float] = np.zeros(shape=(1,))
    b: List[float] = np.concatenate((b_initial, np.cumsum(delta_b, axis=0)), axis=0)

    return [f"{data:.5f}" for data in b.flatten()]


def numerical(shape: Tuple[int, int] = (10, 10)) -> DataFrame:
    return DataFrame(
        lognuniform(size=shape), columns=["col" + str(i + 1) for i in range(shape[1])]
    )


def mixed():
    return DataFrame(
        {
            "Numbers": [lognuniform() for _ in range(10)],
            "More numbers": [lognuniform() for _ in range(10)],
            "Text": lorem(10),
            "Mash": [
                "iswdufvbouwesdb",
                "abc",
                "sdvcsdv",
                "sdvdssdvdvvn",
                "yumyumyum",
                "wqoe",
                "qphjpgh",
                "owperjgpowegjwjgwh",
                "wepogjwpeog",
                "oi",
            ],
        }
    )


def lognuniform(
    low: int = 0, high: int = 10, size: Union[int, None] = None, base: float = np.e
) -> float:
    return np.power(base, np.random.uniform(low, high, size)).astype(int)


def lorem(count: int) -> List[str]:
    return ["Lorem", "ipsum", *random.choices(dummy_text.split(), k=count - 2)]


dummy_text = """
  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut a orci vitae urna rhoncus bibendum convallis eget odio. Sed vitae vulputate eros. Quisque in felis leo. Suspendisse potenti. Phasellus convallis ex vitae tristique imperdiet. Integer semper ligula in nisi rhoncus gravida eget sit amet dolor. Cras id risus in risus ultricies vehicula. Pellentesque in sem facilisis arcu rhoncus maximus. Nam sollicitudin neque quis lectus euismod ultricies. Maecenas et tellus sit amet erat mattis auctor ac et eros. Maecenas id enim et neque pretium venenatis sit amet eu nulla. Quisque nec mauris lectus. Donec purus risus, rutrum eget risus eu, faucibus imperdiet ipsum.
  Phasellus eleifend tempor ligula. Nam ultricies augue mi. Maecenas id placerat neque, et congue neque. Duis ac rutrum arcu. Praesent ullamcorper lacus non nisl rhoncus tincidunt. Maecenas sit amet nisl eget metus faucibus congue. Etiam posuere eget neque tincidunt porttitor. Vestibulum diam nulla, tempus et commodo ac, fringilla id mi. Praesent convallis in velit quis molestie. Morbi ultricies elementum quam et vestibulum. Nam semper bibendum eros.
  Morbi sed ornare odio, eu sodales nisi. Vivamus quis erat mauris. Nulla sed pulvinar tellus, non viverra odio. Donec quis consequat velit, ut volutpat tellus. Etiam suscipit, orci at viverra ultrices, leo lorem ornare augue, at pretium neque odio vitae risus. Curabitur rhoncus sagittis placerat. In et odio varius, tincidunt diam sit amet, condimentum quam.
  Donec tempor urna vel enim dignissim auctor. Nullam nisl sem, pellentesque at mattis eget, dictum eget neque. Maecenas lectus orci, mattis quis nisi a, venenatis bibendum dui. Integer lacinia, nisl at sodales posuere, lectus libero hendrerit sapien, vel eleifend elit enim id tellus. Duis laoreet sapien metus, sit amet scelerisque felis dictum id. Sed nec ante augue. Vestibulum lobortis rhoncus purus. Phasellus rhoncus odio purus, eget vulputate sem iaculis porta. Quisque ultrices ligula vel diam mattis dictum. Pellentesque at convallis metus, eu sollicitudin lectus. Nunc enim neque, gravida vitae velit non, lacinia rhoncus nisi. Vivamus sed sodales metus, eu posuere diam. Praesent quis dolor vel ante tempor pharetra sit amet sit amet felis. Fusce imperdiet quam orci, id elementum elit fringilla pulvinar. In molestie dui sed enim hendrerit, nec molestie risus sodales.
  Maecenas posuere lectus velit, non lacinia orci bibendum sed. Mauris vestibulum urna id dui ornare imperdiet. Pellentesque rhoncus nisl egestas dolor scelerisque, a pellentesque mauris ullamcorper. Aliquam ullamcorper, magna non laoreet accumsan, sem quam sodales leo, sed malesuada eros sem non lorem. Praesent quis eros bibendum, sodales sem ac, maximus sem. Suspendisse a ultricies justo. Aliquam at nunc sit amet augue malesuada lobortis. Morbi sed est blandit turpis varius hendrerit ut ut odio. Duis egestas facilisis condimentum. Quisque auctor sollicitudin tellus. Proin et faucibus turpis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nullam sapien mauris, gravida at elementum et, condimentum quis nunc. 
"""
