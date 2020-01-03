from com.youxinger.testsuite.bean.customer import CustomerVerifyData
from com.youxinger.testsuite.case.base_case import BaseCase
import logging
from com.youxinger.testsuite.service import market_service
from com.youxinger.testsuite.utils.constant import MEMBER_NUMBER_RE


class TestCashWithdrawal(BaseCase):
    """
     会员余额提现,积分提现100，余额提现100
     会员编号：46a1add730 ,15877801465
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

    def tearDown(self):
        super().tearDown()

    def test_1_cash_withdrawal(self):
        """
        :return:
        """
        logging.debug("recharge_shopping_order")
        param={
            'member_number': MEMBER_NUMBER_RE,
            'amount': '100',
            'score': '100',
            'minus_introducer_score': '2',
            'introducer_arr': []
        }

        market_service.cash_refund(param)
        # 更新充值后的验证数据
        self._test_data_re.update_post_verify_data()
        # 封装验证值
        self._customer_re.expectedData = CustomerVerifyData.expected_data(0, -100, 0, -100)  # 更新会员验证值
        # 验证数据
        self._data_assertion_re()

