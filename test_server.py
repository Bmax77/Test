import unittest
import requests
import os


class ServerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Build and deploy')
        os.system('minikube image build -t bmax1977/bin_server_test .')

    # @unittest.expectedFailure()
    @unittest.skip("demonstrating skipping")
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
    @unittest.skip("demonstrating skipping")
    def test_b_home(self):
        print('Test home page')
        response = requests.get('http://localhost:8080')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(' <title>BIN Server</title>' in response.text)

    @unittest.skip("demonstrating skipping")
    @classmethod
    def tearDownClass(cls):
        response = requests.get('http://localhost:8080/stop')
        # print(response)


if __name__ == '__main__':
    unittest.main()