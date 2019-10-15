import unittest

from com.youxinger.testsuite.bean.repository import Repository
from com.youxinger.testsuite.utils import variables
from com.youxinger.testsuite.service import login_service, repository_service
import logging
# import logging.config
from com.youxinger.testsuite.utils.constant import GOODS_CODE
from typing import List
from com.youxinger.testsuite.service.customer_service import Customer
import copy
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


class TestData(object):
    """
    测试数据封装类
    """
    customers: [Customer] = None  # 要验证的会员列表
    repositories: [Repository] = None  # 要检测的仓库库存列表
    M216C237C0458QuantityRepo = 0  # M216C237C0458门店库存
    M216C237C0464QuantityRepo = 0  # M216C237C0464门店库存
    M116E248B0158QuantityRepo = 0  # M116E248B0158门店库存
    M116E248B0164QuantityRepo = 0  # M116E248B0164门店库存
    M316J232B01106QuantityRepo = 0  # M316J232B01106门店库存
    M316J232B0176QuantityRepo = 0  # M316J232B0176门店库存
    M216C237C0458MainStoreQuantityRepo = 0  # M216C237C0458总仓库存
    M216C237C0464MainStoreQuantityRepo = 0  # M216C237C0464总仓库存
    M116E248B0158MainStoreQuantityRepo = 0  # M116E248B0158总仓库存
    M116E248B0164MainStoreQuantityRepo = 0  # M116E248B0164总仓库存
    M316J232B01106MainStoreQuantityRepo = 0  # M316J232B01106总仓库存
    M316J232B0176MainStoreQuantityRepo = 0  # M316J232B0176总仓库存
    ZH02B215190T796242MainStoreQuantityRepo = 0  # ZH02B215190T796242总仓库存
    global_arrive_store_num = 0  # 总揽到店次数
    global_newvip_num = 0  # 总揽新增会员数
    global_order_num = 0  # 总揽订单数
    global_refund_num = 0  # 总揽退单数
    global_sale_num = 0  # 总揽销售总额
    province_sales_amount = 0  # 湖北大区销售额
    city1_arrive_store_num = 0  # 武汉到店次数
    city1_bhm_percent = ""  # 武汉测量成单率
    city1_newvip_num = 0  # 武汉新增会员数
    city1_newvip_order_percent = ""  # 武汉新会员成单率
    city1_order_num = 0  # 武汉订单数
    city1_refund_num = 0  # 武汉退单数
    city1_sale_num = 0  # 武汉销售总额
    city1_plat_sale_num: 0  # 武汉平台销售总额
    city2_arrive_store_num = 0  # 重庆到店次数
    city2_newvip_num = 0  # 重庆新增会员数
    city2_order_num = 0  # 重庆订单数
    city2_refund_num = 0  # 重庆退单数
    city2_sale_num = 0  # 重庆销售总额
    city2_plat_sale_num: 0  # 重庆平台销售总额
    platform1_sale_num = 0  # 武大樱花平台业绩
    platform2_sale_num = 0  # 光谷社区平台业绩
    platform3_sale_num = 0  # 巴山蜀水平台业绩
    platform4_sale_num = 0  # 三地火锅平台业绩
    employee_sale_num = 0  # 店长业绩

    def __init__(self):
        self.customers = []
        self.repositories = []


class BaseCase(unittest.TestCase):
    """
    测试用例基类, 用于登录等操作
    """

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

    @staticmethod
    def _data_assertion(test_data: TestData):
        """
        数据验证操作
        :param test_data:要验证的数据
        :return:
        """
        if test_data is None:
            return
        if test_data.customers is not None:
            for customer in test_data.customers:
                customer.data_verify()

