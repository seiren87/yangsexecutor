import unittest
import os
import shutil
import argparse
from yangsrunner import SimpleExecutor


class Main(SimpleExecutor):

    def __init__(self):
        SimpleExecutor.__init__(self, setting_file='tests/setting.yml')

    def _arguments(self):
        return {'app': 'test_app'}


class Main2(SimpleExecutor):

    def __init__(self):
        SimpleExecutor.__init__(self, setting_file='tests/setting.yml')

    def _arguments(self):
        return {'app': 'test_a'}


class Main3(SimpleExecutor):

    def __init__(self):
        SimpleExecutor.__init__(self, setting_file='tests/setting.yml')

    def _arguments(self):
        args = argparse.ArgumentParser()

        return args.parse_args().__dict__


class SimpleExecutorTestCase(unittest.TestCase):

    def test_1_happy_path(self):
        Main().start()

        self.assertTrue(
            os.path.isdir('log/yangsrunner_test-test_app'),
            msg="Main1 Test App test"
        )

    def test_2_app_is_none(self):
        Main2().start()

        self.assertTrue(
            os.path.isdir('log/yangsrunner_test-none'),
            msg="Main2 Test App test"
        )

    def test_3_argument_is_empty(self):
        Main3().start()

        self.assertTrue(
            os.path.isdir('log/yangsrunner_test-none'),
            msg="Main3 Test App test"
        )

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree('log')
