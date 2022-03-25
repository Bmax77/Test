import unittest
import requests
import os
import time


PORT=8080
class ServerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Build and deploy')
        os.system('minikube image build -t bmax1977/bin_server_test .')
        os.system('kubectl apply -f bin_server_k8s.yml')


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
                time.sleep(1)
                os.system(f'kubectl port-forward --address 127.0.0.1 deployment/bin-server {PORT}:8080 >/dev/null 2>&1 &')
                print('Waiting')

    def test_b_home(self):
        print('Test home page')
        response = requests.get('http://localhost:8080')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('<title>BIN Server</title>' in response.text)

    def test_c_card_ok(self):
        print('Check existing card number')
        response = requests.get('http://localhost:8080/cards/4584432849604450')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('["458443", "VISA", "DEBIT", "", "ZHELDORBANK JSB", "CA", "CAN", "Canada", "56.1304", "-106.347", "", ""]' in response.text)
    
    def test_d_card_wrong(self):
        print('Check wrong card number')
        response = requests.get('http://localhost:8080/cards/0584432849604450')
        self.assertEqual(response.status_code, 500)
        self.assertTrue('Not found' in response.text)

    @classmethod
    def tearDownClass(cls):
        os.system("kill $(ps aux | grep 'kubectl port-forward --address 127.0.0.1' | awk '{print $2}')")
        os.system('kubectl delete -f bin_server_k8s.yml')




if __name__ == '__main__':
    unittest.main()