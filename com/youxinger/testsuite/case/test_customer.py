from com.youxinger.testsuite.bean.customer import CustomerVerifyData
from com.youxinger.testsuite.case.base_case import BaseCase
import logging


class TestCustomer(BaseCase):
    """
    一般会员注册充值测试
    """

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
        self._customer.update_post_verify_data()
        # 封装验证值
        customer_verify_data = CustomerVerifyData()
        customer_verify_data.i_remainder = 0
        customer_verify_data.i_card_level = 1
        customer_verify_data.i_swap_score = 500
        customer_verify_data.i_total_consume = 0
        self._customer.expectedData = customer_verify_data
        # 验证数据
        self._data_assertion()

    def test_2_after_customer_recharge(self):
        """
        会员充值测试
        :return:
        """
        logging.debug(u"test_after_customer_recharge")
        # 更新充值前的验证数据
        self._customer.update_pre_verify_data()
        # 充值操作
        self._customer.recharge(40000)
        # 更新充值后的验证数据
        self._customer.update_post_verify_data()
        # 封装验证值
        customer_verify_data = CustomerVerifyData()
        customer_verify_data.i_remainder = 40000
        customer_verify_data.i_card_level = 2
        customer_verify_data.i_swap_score = 40000
        customer_verify_data.i_total_consume = 0
        self._customer.expectedData = customer_verify_data
        # 验证数据
        self._data_assertion()
