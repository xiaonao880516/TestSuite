from com.youxinger.testsuite.bean.customer import CustomerVerifyData
from com.youxinger.testsuite.case.base_case import BaseCase
from com.youxinger.testsuite.utils.constant import REFERRAL_PHONE
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
        self._customer.expectedData = CustomerVerifyData.expected_data(0, 500, 1, 0)
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
        self._referral.update_pre_verify_data()
        # 充值操作
        self._customer.top_up(40000, REFERRAL_PHONE)
        # 更新充值后的验证数据
        self._customer.update_post_verify_data()
        self._referral.update_post_verify_data()
        # 封装验证值
        self._customer.expectedData = CustomerVerifyData.expected_data(0, 40000, 2, 40000)
        self._referral.expectedData = CustomerVerifyData.expected_data(0, 40000, 5, 0)
        # 验证数据
        self._data_assertion()