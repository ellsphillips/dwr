from dwr.environment import Environment


def render(environment: Environment) -> str:
    result = "\n".join(
        [
            environment.begin + environment.options,
            environment.body,
            environment.end,
        ]
    )
    print("\n", result)
    return result
