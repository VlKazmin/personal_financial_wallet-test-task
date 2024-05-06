import sys

from io import StringIO


class Capturing(list):
    """
    Class for capturing function stdout.
    Usage:
     with Capturing() as func_output:
         func()

    check func() output in func_output variable
    """

    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout
