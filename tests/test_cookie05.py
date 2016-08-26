import unittest
import os

from cookie05 import run_cookie05


class TestFunMethod(unittest.TestCase):
    def test_check(self):
        r = run_cookie05.check()
        self.assertIn(r, [True, False])

    def test_process_output(self):
        if os.name in ['posix']:
            r = run_cookie05.process_output_linux()
        else:
            r = run_cookie05.process_output_windows()
        self.assertGreater(len(r), 1)

    def test_pid(self):
        r = run_cookie05.most_cpu_pid()
        self.assertGreater(r, 1)

if __name__ == '__main__':
    unittest.main()
