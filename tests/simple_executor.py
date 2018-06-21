import unittest
import os
from yangsrunner import SimpleExecutor


class Main(SimpleExecutor):

    def __init__(self):
        SimpleExecutor.__init__(self, setting_file='tests/setting.yml')

    def _arguments(self):
        return {'app': 'test_app'}


class SimpleExecutorTestCase(unittest.TestCase):

    def test_main_run(self):
        Main().start()

        self.assertTrue(
            os.path.isdir('log/yangsrunner_test-test_app'),
            msg="Main1 Test App test"
        )


class Main2(SimpleExecutor):

    def __init__(self):
        SimpleExecutor.__init__(self, setting_file='tests/setting.yml')

    def _arguments(self):
        return {'app': 'test_a'}


class SimpleExecutor2TestCase(unittest.TestCase):

    def test_main_run(self):
        Main2().start()

        self.assertTrue(
            os.path.isdir('log/yangsrunner_test-none'),
            msg="Main1 Test App test"
        )
