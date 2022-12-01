from io import StringIO
import sys

class ConsoleOutput:
    def __init__(self):
        self.logs = []
        self.errors = []

    def __enter__(self):
        self._stdout = sys.stdout
        self._stderr = sys.stderr
        sys.stdout = self._stringio_stdout = StringIO()
        sys.stderr = self._stringio_stderr = StringIO()
        return self
    
    def __exit__(self, *args):
        self.logs = self._stringio_stdout.getvalue().splitlines()
        self.errors = self._stringio_stderr.getvalue().splitlines()
        
        del self._stringio_stdout
        del self._stringio_stderr

        sys.stdout = self._stdout
        sys.stderr = self._stderr
