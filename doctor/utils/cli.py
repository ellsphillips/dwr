from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
import time

"""
Utility classes for Doctor
"""


def timer(f):
  def wrapper(*args, **kwargs):
    start = time.perf_counter()
    rv = f()
    end = time.time() - start
    end = time.perf_counter()
    print(f'{style.emoji["lightning"]} Finished in {style.announce}{end:.02f}s{style.end}')

  return wrapper


class Loader:
  def __init__(self, desc="Loading...", end="Done!", timeout=0.1):
    """
    A loader-like context manager

    Args:
        desc (str, optional): The loader's description. Defaults to "Loading...".
        end (str, optional): Final print. Defaults to "Done!".
        timeout (float, optional): Sleep time between prints. Defaults to 0.1.
    """
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
        f"\r{self.desc}{colour.CBOLD}{colour.CYELLOW} {c} {colour.CEND}",
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
  emoji = {
    "lightning": "⚡"
  }
  end = "\33[0m"
  warning = "\033[1m\33[91m"
  announce = "\033[1m\033[93m"
  comment = "\033[1m\33[94m"

class colour:
  CEND       = '\33[0m'
  CBOLD      = '\33[1m'
  CITALIC    = '\33[3m'
  CURL       = '\33[4m'
  CBLINK     = '\33[5m'
  CBLINK2    = '\33[6m'
  CSELECTED  = '\33[7m'

  CBLACK     = '\33[30m'
  CRED       = '\33[31m'
  CGREEN     = '\33[32m'
  CYELLOW    = '\33[33m'
  CBLUE      = '\33[34m'
  CVIOLET    = '\33[35m'
  CBEIGE     = '\33[36m'
  CWHITE     = '\33[37m'

  CBLACKBG   = '\33[40m'
  CREDBG     = '\33[41m'
  CGREENBG   = '\33[42m'
  CYELLOWBG  = '\33[43m'
  CBLUEBG    = '\33[44m'
  CVIOLETBG  = '\33[45m'
  CBEIGEBG   = '\33[46m'
  CWHITEBG   = '\33[47m'

  CGREY      = '\33[90m'
  CRED2      = '\33[91m'
  CGREEN2    = '\33[92m'
  CYELLOW2   = '\33[93m'
  CBLUE2     = '\33[94m'
  CVIOLET2   = '\33[95m'
  CBEIGE2    = '\33[96m'
  CWHITE2    = '\33[97m'

  CGREYBG    = '\33[100m'
  CREDBG2    = '\33[101m'
  CGREENBG2  = '\33[102m'
  CYELLOWBG2 = '\33[103m'
  CBLUEBG2   = '\33[104m'
  CVIOLETBG2 = '\33[105m'
  CBEIGEBG2  = '\33[106m'
  CWHITEBG2  = '\33[107m'