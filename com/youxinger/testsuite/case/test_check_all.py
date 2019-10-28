import requests
import unittest
from com.youxinger.testsuite.utils import constant
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


class TestCheckAll(unittest.TestCase):

    def test_check_all(self):
        logging.debug("test_check_all")
        url = constant.DOMAIN + "/health/check-all"
        r = requests.get(url)
        json_data = r.json()
        assert json_data['tatoltime'] < 3, "check_all 测试"
