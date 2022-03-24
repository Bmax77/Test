import unittest
import requests

# print('f' in 'blablabla')

class ServerTests(unittest.TestCase):
    def test_readiness(self):
        response = requests.get('http://localhost:8080/health/readiness')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'Ready')

    def test_home(self):
        response = requests.get('http://localhost:8080')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(' <title>BIN Server</title>' in response.text)


if __name__ == '__main__':
    unittest.main()