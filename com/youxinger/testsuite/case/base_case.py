import unittest

from com.youxinger.testsuite.bean.i_validate import IDataVerify
from com.youxinger.testsuite.bean.repository import Repository
from com.youxinger.testsuite.bean.store import Store
from com.youxinger.testsuite.bean.area import Area
from com.youxinger.testsuite.bean.employee import Employee
from com.youxinger.testsuite.bean.lc_global import LCGlobal
from com.youxinger.testsuite.bean.platform import Platform
from com.youxinger.testsuite.utils import variables
from com.youxinger.testsuite.service import login_service
import logging
from com.youxinger.testsuite.utils.constant import GOODS_CODE, EMPLOYEE, PLATFORM, CUSTOMER, AREA, STORE
from com.youxinger.testsuite.service.customer_service import Customer

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


class TestData(IDataVerify):
    """
    测试数据封装类
    """
    customers: [Customer] = None  # 要验证的会员列表
    lc_global: LCGlobal = None  # 要验证的总览数据

    def __init__(self):
        self.customers = []

    def data_verify(self):
        """
        数据验证操作
        :return:
        """
        if self.customers is not None:
            for customer in self.customers:
                customer.data_verify()

        if self.lc_global is not None:
            self.lc_global.data_verify()

    def update_pre_verify_data(self):
        """
        更新操作之前的数据
        :return:
        """
        if self.customers is not None:
            for customer in self.customers:
                customer.update_pre_verify_data()

        if self.lc_global is not None:
            self.lc_global.update_pre_verify_data()

    def update_post_verify_data(self):
        """
        更新操作之后的数据
        :return:
        """
        if self.customers is not None:
            for customer in self.customers:
                customer.update_post_verify_data()

        if self.lc_global is not None:
            self.lc_global.update_post_verify_data()


class BaseCase(unittest.TestCase):
    """
    测试用例基类, 用于登录等操作
    """
    # 封装测试数据
    _test_data = None
    _customer: Customer = None
    _employee: Employee = None
    _platform: Platform = None
    _global: LCGlobal = None
    _global_repo = None
    _area: Area = None
    _store: Store = None
    _store_repo = None

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
        cls._test_data = TestData()
        # 注册新会员
        cls._employee = Employee(EMPLOYEE['employee_name'], EMPLOYEE['employee_id'], EMPLOYEE['employee_phone'], EMPLOYEE['employee_password'])
        cls._platform = Platform(PLATFORM['name'], PLATFORM['platform_id'])
        cls._customer = Customer.register(CUSTOMER, cls._employee, cls._platform)
        cls._test_data.customers.append(cls._customer)

        cls._store_repo = Repository(STORE['name'], variables.foregroundTID, GOODS_CODE)
        cls._store = Store(STORE['name'], STORE['store_id'])
        cls._store.add_platform(cls._platform)
        cls._store.add_employee(cls._employee)
        cls._store.repository = cls._store_repo
        cls._area = Area(AREA['name'], AREA['area_id'])
        cls._area.stores.append(cls._store)
        cls._global_repo = Repository.lc_global(GOODS_CODE)
        cls._global = LCGlobal(cls._global_repo)
        cls._global.areas.append(cls._area)
        cls._test_data.lc_global = cls._global
        pass

    @classmethod
    def tearDownClass(cls):
        """
        在所有的测试用例执行之后，只执行一次
        :return:
        """
        logging.debug(u"tearDownClass")
        # 删除会员
        cls._customer.delete()
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

    def _data_assertion(self):
        self._test_data.data_verify()


