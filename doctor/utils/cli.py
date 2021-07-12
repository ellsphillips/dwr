from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
import time
import re

"""
Utility classes for Doctor
"""


def timer(f):
  def wrapper(*args, **kwargs):
    start = time.perf_counter()
    rv = f()
    end = time.perf_counter()
    print(f'{style.emoji["lightning"]} Finished in {style.announce}{end - start:.02f}s{style.end}\n')

  return wrapper


class Loader:
  """
  A loader-like context manager

  Args:
      desc (str, optional): The loader's description. Defaults to "Loading...".
      end (str, optional): Final print. Defaults to "Done!".
      timeout (float, optional): Sleep time between prints. Defaults to 0.1.
  """
  def __init__(
    self,
    desc: str = "Loading...",
    end: str = "Done!",
    timeout: float = 0.1
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
      print(
        f"\r{self.desc}{style.announce} {c} {style.end}",
        flush=True,
        end=""
      )
      time.sleep(self.timeout)

  def __enter__(self):
    self.start()

  def stop(self):
    self.done = True
    cols = get_terminal_size((80, 20)).columns
    print("\r" + " " * cols, end="", flush=True)
    print(f"\r{self.end}", flush=True)

  def __exit__(self, exc_type, exc_value, tb):
    # handle exceptions with those variables ^
    self.stop()


class style:
  emoji: dict = {
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
  comment: str = bold + "\33[94m"
  notice: str = bold + "\33[95m"


class log:
  """
  Handle console logging types.
  """

  delimiters = "[...]"

  def __init__(
    self,
    content: str,
    style: str = "announce"
  ) -> None:
    self.content = content
    self.style = style

  def warning():
    elements = [
      f"{style.emoji['cross']}",
      f"{style.warning}",
      "I'm not much good without data, you know...",
      f"{style.end}"
    ]
    print(
      "".join([item for item in elements if item])
    )

  def output(file_path: str):
    print(
      "".join([
        f"{style.emoji['write']} ",
        "Data file generated at ",
        f"{style.output}",
        f"{file_path}",
        f"{style.end}\n"
      ])
    )

  def announce():
    pass

  def comment(input_str: str):
    matches = re.compile(r'\[([^]]*)\]')

    l = []
    def repl(m):
      l.append(m.group(0))
      return f'{style.comment}{m[1]}{style.end}'

    out_str = matches.sub(repl, input_str)

    print(f"{out_str}\n")

  def notice():
    pass

