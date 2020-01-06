from com.youxinger.testsuite.bean.customer import CustomerVerifyData
from com.youxinger.testsuite.case.base_case import BaseCase
import logging
from com.youxinger.testsuite.service import market_service


class TestCashWithdrawal(BaseCase):
    """
     会员余额转出,会员：15877801465转到
     会员：15877801461
     转出余额为100
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # 会员充值40000
        cls._customer_re.recharge(40000)

    def setUp(self):
        super().setUp()
        # 更新充值前的验证数据
        self._test_data_re.update_pre_verify_data()
        self._test_data.update_pre_verify_data()

    def tearDown(self):
        super().tearDown()

    def test_1_recharge_shopping_order(self):
        """
        :return:
        """
        logging.debug("recharge_shopping_order")
        param={
            'member_number': self._customer_re.member_number,
            'amount': '100',
            'phone':  self._customer.phone,

        }

        market_service.remainder_roll_out(param)
        # 更新充值后的验证数据
        self._test_data_re.update_post_verify_data()
        self._test_data.update_post_verify_data()
        # 封装验证值
        self._customer_re.expectedData = CustomerVerifyData.expected_data(0, 0, 0, -100)  # 更新会员验证值
        self._customer.expectedData = CustomerVerifyData.expected_data(0, 0, 0, 100)  # 更新会员验证值
        # 验证数据
        self._data_assertion_re()
        self._data_assertion()

