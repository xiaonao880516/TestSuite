from com.youxinger.testsuite.bean.customer import CustomerVerifyData, Customer
from com.youxinger.testsuite.bean.employee import Employee
from com.youxinger.testsuite.bean.platform import Platform
from com.youxinger.testsuite.case.base_case import BaseCase
import logging
from com.youxinger.testsuite.service import customer_service
from com.youxinger.testsuite.utils.constant import CUSTOMER, EMPLOYEE, PLATFORM


class TestCustomer(BaseCase):
    """
    一般会员注册充值测试
    """

    customer: Customer = None
    employee: Employee = None
    platform: Platform = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # 注册新会员
        cls.employee = Employee(EMPLOYEE['employee_name'], EMPLOYEE['employee_id'], EMPLOYEE['employee_phone'], EMPLOYEE['employee_password'])
        cls.platform = Platform(PLATFORM['name'], PLATFORM['platform_id'])
        cls.customer = customer_service.register_customer(CUSTOMER, cls.employee, cls.platform)
        cls._test_data.customers.append(cls.customer)

    @classmethod
    def tearDownClass(cls):
        # 删除会员
        customer_service.del_customer(cls.customer)
        cls.customer = None
        super().tearDownClass()

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_1_after_customer_register(self):
        """
        注册会员测试
        :return:
        """
        logging.debug(u"test_after_customer_register")
        # 更新注册后的验证数据
        customer_service.update_customer_verify_data(True, self.customer)
        # 封装验证值
        customer_verify_data = CustomerVerifyData()
        customer_verify_data.i_remainder = 0
        customer_verify_data.i_card_level = 1
        customer_verify_data.i_swap_score = 500
        customer_verify_data.i_total_consume = 0
        self.customer.expectedData = customer_verify_data
        # 验证数据
        super()._data_assertion()

    def test_2_after_customer_recharge(self):
        """
        会员充值测试
        :return:
        """
        logging.debug(u"test_after_customer_recharge")
        # 更新充值前的验证数据
        customer_service.update_customer_verify_data(False, self.customer)
        # 充值操作
        customer_service.recharge_customer(self.customer, 40000)
        # 更新充值后的验证数据
        customer_service.update_customer_verify_data(True, self.customer)
        # 封装验证值
        customer_verify_data = CustomerVerifyData()
        customer_verify_data.i_remainder = 40000
        customer_verify_data.i_card_level = 2
        customer_verify_data.i_swap_score = 40000
        customer_verify_data.i_total_consume = 0
        self.customer.expectedData = customer_verify_data
        # 验证数据
        super()._data_assertion()
