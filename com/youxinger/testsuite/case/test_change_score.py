from com.youxinger.testsuite.bean.customer import CustomerVerifyData
from com.youxinger.testsuite.case.base_case import BaseCase
import logging
from com.youxinger.testsuite.service import market_service
from com.youxinger.testsuite.utils.constant import MEMBER_NUMBER_RE


class TestChangeScore(BaseCase):
    """
     会员增加积分和减少积分测试用例
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

    def test_1_decrease_integral(self):
        """
        :return: 会员扣减积分验证， 扣减10000积分
        """
        logging.debug("recharge_shopping_order")
        param={
            'member_number': MEMBER_NUMBER_RE,
            'direction': '2',
            'score': '10000',
            'reason': '自动化扣减积分'
        }

        market_service.change_score(param)
        # 更新充值后的验证数据
        self._test_data_re.update_post_verify_data()
        # 封装验证值
        self._customer_re.expectedData = CustomerVerifyData.expected_data(0, -10000, 0, 0)  # 更新会员验证值
        # 验证数据
        self._data_assertion_re()

    def test_2_Increase_integral(self):
        """
        :return: 会员增加积分验证， 增加10000积分
        """
        logging.debug("recharge_shopping_order")
        param={
            'member_number': MEMBER_NUMBER_RE,
            'direction': '1',
            'score': '10000',
            'reason': '自动化增加积分'
        }

        market_service.change_score(param)
        # 更新充值后的验证数据
        self._test_data_re.update_post_verify_data()
        # 封装验证值
        self._customer_re.expectedData = CustomerVerifyData.expected_data(0, 10000, 0, 0)  # 更新会员验证值
        # 验证数据
        self._data_assertion_re()

