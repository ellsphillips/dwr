from .environment import Environment


def render(environment: Environment) -> None:
    print(
        "\n".join(
            [
                environment.begin + environment.options,
                environment.body,
                environment.end,
            ]
        )
    )
