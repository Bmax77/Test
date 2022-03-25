import unittest
import requests
import os


class ServerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Build and deploy')
        os.system('./build.sh > /dev/null 2>&1')

    # @unittest.expectedFailure()
    def test_a_readiness(self):
        print('Wait start server')
        response = ''
        while(response == ''):
            try:
                response = requests.get('http://localhost:8080/health/readiness')
                if(response != ""):
                    print('Test readiness probe')
                    self.assertEqual(response.status_code, 200)
                    self.assertEqual(response.text, 'Ready')
            except:
                nop = ''
                
    # @unittest.expectedFailure()
    def test_b_home(self):
        print('Test home page')
        response = requests.get('http://localhost:8080')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(' <title>BIN Server</title>' in response.text)

    @classmethod
    def tearDownClass(cls):
        response = requests.get('http://localhost:8080/stop')
        # print(response)


if __name__ == '__main__':
    unittest.main()