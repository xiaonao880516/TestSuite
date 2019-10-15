from com.youxinger.testsuite.bean.customer import CustomerVerifyData, Customer
from com.youxinger.testsuite.case.base_case import BaseCase
from com.youxinger.testsuite.case.base_case import TestData
import logging
from com.youxinger.testsuite.service import customer_service
from com.youxinger.testsuite.utils.constant import CUSTOMER


class TestCustomer(BaseCase):
    """
    一般会员注册充值测试
    """

    customer: Customer = None

    def setUp(self):
        super().setUp()
        # 注册新会员
        self.customer = customer_service.register_customer(CUSTOMER)

    def tearDown(self):
        super().tearDown()
        # 删除会员
        customer_service.del_customer(self.customer)
        self.customer = None

    def test_after_customer_register(self):
        """
        注册会员测试
        :return:
        """
        logging.debug(u"test_after_customer_register")
        # 封装测试数据
        test_data = TestData()
        test_data.customers.append(self.customer)
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
        super()._data_assertion(test_data)

    def test_after_customer_recharge(self):
        """
        会员充值测试
        :return:
        """
        logging.debug(u"test_after_customer_recharge")
        # 封装测试数据
        test_data = TestData()
        test_data.customers.append(self.customer)
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
        customer_verify_data.i_swap_score = 40500
        customer_verify_data.i_total_consume = 0
        self.customer.expectedData = customer_verify_data
        # 验证数据
        super()._data_assertion(test_data)
