import unittest
import requests
from fake_useragent import UserAgent
import logging
import os

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 使用环境变量管理API的URL
BASE_URL = os.getenv('API_BASE_URL', 'https://api.oioweb.cn')

class TestAPIs(unittest.TestCase):

    def setUp(self):
        self.ua = UserAgent()

    # 手机号归属地查询
    def test_trademark(self):
        url = f'{BASE_URL}/api/common/teladress?mobile=18168055183'
        response = self.make_request(url)
        res = response.json()
        logger.info(res)

        # 断言
        self.assertEqual(response.status_code, 200)
        city = res['result']['city']
        self.assertEqual(city, '南京市')

    # 货币汇率查询
    def test_exchange_rate(self):
        url = f'{BASE_URL}/api/common/ExchangeRateQueryInterface'
        response = self.make_request(url)
        res = response.json()
        logger.info(res)

        # 断言
        self.assertEqual(response.status_code, 200)
        data_list = res['result']['data']
        # 找到人民币对欧元的汇率并输出
        for data in data_list:
            if data['n'] == '欧元':
                logger.info(data['v'])
                break
        else:
            self.fail("欧元汇率未找到")

    def make_request(self, url):
        try:
            response = requests.get(url, headers={"User-Agent": self.ua.random}, timeout=10)
            response.raise_for_status()  # 抛出HTTPError异常
            return response
        except requests.RequestException as e:
            logger.error(f"请求失败: {e}")
            self.fail(f"请求失败: {e}")

if __name__ == '__main__':
    unittest.main()
