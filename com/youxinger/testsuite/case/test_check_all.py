import requests
import unittest
from com.youxinger.testsuite.utils import constant


class TestCheckAll(unittest.TestCase):

    def test_check_all(self):
        url = constant.DOMAIN + "/health/check-all"
        r = requests.get(url)
        json_data = r.json()
        assert json_data['tatoltime'] < 3, "check_all 测试"