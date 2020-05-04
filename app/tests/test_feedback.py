"""app/tests/test_feedback.py
"""
import ast
import unittest

from flask import url_for

from run import app


class TestApp(unittest.TestCase):
    """TestApp
    """

    @classmethod
    def setUpClass(cls):
        app.config['SERVER_NAME'] = 'unittest.com:5000'
        cls.client = app.test_client()

    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_healthcheck(self):
        """test_healthcheck
        """
        res = self.client.get(url_for('feedback.healthcheck'))
        res_dict = ast.literal_eval(res.data.decode('utf-8'))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_dict['status'], 'healthy')


if __name__ == '__main__':
    unittest.main()
