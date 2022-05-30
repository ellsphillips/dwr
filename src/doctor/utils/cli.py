import re
import time
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from types import TracebackType
from typing import Dict, List, Optional, Tuple, Type, Union


class Loader:
    """
    A loader-like context manager

    Args:
        desc (str, optional): The loader's description. Defaults to "Loading...".
        end (str, optional): Final print. Defaults to "Done!".
        timeout (float, optional): Sleep time between prints. Defaults to 0.1.
    """

    def __init__(
        self, desc: str = "Loading...", end: str = "Done!", timeout: float = 0.1
    ):
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc}{Style.announce} {c} {Style.end}", flush=True, end="")
            time.sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def __exit__(
        self,
        exctype: Optional[Type[BaseException]],
        excinst: Optional[BaseException],
        exctb: Optional[TracebackType],
    ):
        # handle exceptions with those variables ^
        self.stop()


class Style:
    emoji: Dict[str, str] = {
        "lightning": "⚡",
        "checkmark": "✔",
        "cross": "❌",
        "write": "📁",
    }
    end: str = "\33[0m"
    bold: str = "\033[1m"
    italic: str = "\033[3m"
    warning: str = bold + "\33[91m"
    output: str = bold + "\33[92m"
    announce: str = bold + "\033[93m"
    notice: str = bold + "\33[94m"
    comment: str = bold + "\33[96m"


class Log:
    """
    Handle console logging types.
    """

    delimiters = "[...]"
    l, r = delimiters.split("...")

    def __init__(self, content: str, style: str = "announce") -> None:
        self.content = content
        self.style = style

    @staticmethod
    def highlighter(
        input_str: str,
        colour: str,
        l_delim: str = "[",
        r_delim: str = "]",
    ):
        matches = re.compile(f"[({l_delim}^]{r_delim}*)]")

        composition: List[str] = []

        def repl(m: re.Match[str]):
            composition.append(m.group(0))
            return f"{colour}{m[1]}{Style.end}"

        out_str = matches.sub(repl, input_str)

        return f"{out_str}\n"

    @staticmethod
    def warning(input_str: str) -> None:
        elements = [
            f"{Style.emoji['cross']} ",
            f"{Style.warning}",
            f"{input_str}",
            f"{Style.end}",
        ]
        print("".join([item for item in elements if item]))

    @staticmethod
    def output(file_path: str) -> None:
        print(
            "".join(
                [
                    f"{Style.emoji['write']} ",
                    "File generated at ",
                    f"{Style.output}",
                    f"{file_path}",
                    f"{Style.end}\n",
                ]
            )
        )

    @staticmethod
    def announce(input_str: str) -> None:
        print(Log.highlighter(input_str, Style.announce))

    @staticmethod
    def comment(input_str: str) -> None:
        print(Log.highlighter(input_str, Style.comment))

    @staticmethod
    def notice(input_str: str) -> None:
        print(f"{Style.notice}{input_str}{Style.end}\n")

    @staticmethod
    def prettify(
        value: Union[str, Tuple[str], List[str], Dict[str, str]],
        tab: str = " " * 2,
        line_end: str = "\n",
        indent: int = 0,
    ) -> str:
        newline = line_end + tab * (indent + 1)

        if isinstance(value, dict):
            items = [
                newline
                + repr(key)
                + ": "
                + Log.prettify(value[key], tab, line_end, indent + 1)
                for key in value
            ]
            return f"{{{','.join(items) + line_end + tab * indent}}}"

        elif isinstance(value, list):
            items = [
                newline + Log.prettify(item, tab, line_end, indent + 1)
                for item in value
            ]
            return f"[{','.join(items) + line_end + tab * indent}]"

        elif isinstance(value, tuple):
            items = [
                newline + Log.prettify(item, tab, line_end, indent + 1)
                for item in value
            ]
            return f"({','.join(items) + line_end + tab * indent})"

        else:
            return repr(value)

    @staticmethod
    def pretty(value: Union[str, Tuple[str], List[str], Dict[str, str]]) -> None:
        print(Log.prettify(value))
