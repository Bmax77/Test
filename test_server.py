import unittest
import requests
import os
import time
import HtmlTestRunner


class ServerTests(unittest.TestCase):

    url = None

    @classmethod
    def setUpClass(cls):
        print('Build and deploy')
        os.system('minikube image build -t bmax1977/bin_server_test .')
        os.system('kubectl apply -f bin_server_k8s.yml')
        p = os.popen('minikube service bin-server --url')
        ServerTests.url = p.read()
        print(ServerTests.url)
        p.close()
        server_wait = 0
        response = ''
        while(response == ''):
            try:
                response = requests.get(f'{ServerTests.url}/health/readiness')
            except:
                time.sleep(1)
                if server_wait == 10:
                    raise
                server_wait = server_wait + 1
                print('Waiting start server: %ds\r'%server_wait, end = '')

    def test_a_readiness(self):
        response = requests.get(f'{ServerTests.url}/health/readiness')
        if(response != ""):
            print('Test readiness probe')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.text, 'Ready')

    # @unittest.skip("demonstrating skipping")
    def test_b_home(self):
        print('Test home page')
        response = requests.get(ServerTests.url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('<title>BIN Server</title>' in response.text)

    # @unittest.skip("demonstrating skipping")
    def test_c_card_ok(self):
        print('Check existing card number')
        response = requests.get(f'{ServerTests.url}/cards/4584431234123412')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('["458443", "VISA", "DEBIT", "", "ZHELDORBANK JSB", "CA", "CAN", "Canada", "56.1304", "-106.347", "", ""]' in response.text)

    # @unittest.skip("demonstrating skipping")
    def test_d_card_absent(self):
        print('Check absent card number')
        response = requests.get(f'{ServerTests.url}/cards/0584431234123412')
        self.assertEqual(response.status_code, 404)
        self.assertTrue('Not found' in response.text)

    # @unittest.skip("demonstrating skipping")
    def test_e_card_wrong(self):
        print('Check wrong card number')
        response = requests.get(f'{ServerTests.url}/cards/458443123412abcd')
        self.assertEqual(response.status_code, 500)
        self.assertTrue('Internal server error' in response.text)

    @classmethod
    def tearDownClass(cls):
        os.system('kubectl delete -f bin_server_k8s.yml')




if __name__ == '__main__':
    unittest.main(
    testRunner=HtmlTestRunner.HTMLTestRunner(
        open_in_browser=True,
        combine_reports=True,
        template_args={}
    )
)
