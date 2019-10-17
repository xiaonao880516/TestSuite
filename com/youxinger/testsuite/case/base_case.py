import unittest
from com.youxinger.testsuite.bean.group import Group
from com.youxinger.testsuite.utils import variables
from com.youxinger.testsuite.service import login_service, repository_service
import logging
from com.youxinger.testsuite.utils.constant import GOODS_CODE
from com.youxinger.testsuite.service.customer_service import Customer

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


class TestData(object):
    """
    测试数据封装类
    """
    customers: [Customer] = None  # 要验证的会员列表
    group: Group = None  # 要验证的总览数据

    def __init__(self):
        self.customers = []


class BaseCase(unittest.TestCase):
    """
    测试用例基类, 用于登录等操作
    """
    # 封装测试数据
    _test_data = TestData()

    @classmethod
    def setUpClass(cls):
        """
         在所有的测试用例执行之前，只执行一次
        :return:
        """
        logging.debug(u"setUpClass")
        # 前台登录
        login_service.foreground_login()
        # 后台登陆
        login_service.background_login()

    @classmethod
    def tearDownClass(cls):
        """
        在所有的测试用例执行之后，只执行一次
        :return:
        """
        logging.debug(u"tearDownClass")
        variables.foregroundTID = ""
        variables.backgroundTID = ""

    def setUp(self):
        """
        测试用例执行前的初始化操作
        :return:
        """
        logging.debug(u"setUp")
        pass

    def tearDown(self):
        """
        测试用例执行完之后的收尾操作
        :return:
        """
        logging.debug(u"tearDown")

    # 初始化执行操作之后的数据
    def _post_data_update(self):
        store_repository = repository_service.get_store_repository_by_tid(variables.foregroundTID, GOODS_CODE)
        main_repository = repository_service.get_main_repository(GOODS_CODE)

    def _data_assertion(self):
        """
        数据验证操作
        :param test_data:要验证的数据
        :return:
        """
        if self._test_data.customers is not None:
            for customer in self._test_data.customers:
                customer.data_verify()

