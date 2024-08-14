import unittest
import requests
from fake_useragent import UserAgent

class TestAPIs(unittest.TestCase):

    # 手机号归属地查询
    def test_trademark(self):
        ua = UserAgent()
        url = 'https://api.oioweb.cn/api/common/teladress?mobile=18168055183'
        response = requests.get(url, headers={"User-Agent": ua.random})
        res = response.json()
        print(res)

        # 断言
        self.assertEqual(response.status_code, 200)
        city = res['result']['city']
        self.assertEqual(city,'南京市')

    # 货币汇率查询
    def test_exchange_rate(self):
        ua = UserAgent()
        url = 'https://api.oioweb.cn/api/common/ExchangeRateQueryInterface'
        response = requests.get(url, headers={"User-Agent": ua.random})
        res = response.json()
        # print(res)

        # 断言
        self.assertEqual(response.status_code, 200)
        data_list = res['result']['data']
        # 找到人民币对欧元的汇率并输出
        for data in data_list:
            if data['n'] == '欧元':
                print(data['v'])

if __name__ == '__main__':
    unittest.main()
