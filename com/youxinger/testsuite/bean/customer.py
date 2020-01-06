from com.youxinger.testsuite.bean.employee import Employee
from com.youxinger.testsuite.bean.i_validate import IDataVerify
import logging

from com.youxinger.testsuite.bean.platform import Platform


class CustomerVerifyData(object):
    """
    会员数据验证类
    """
    i_total_consume = 0  # 会员消费额
    i_swap_score = 0  # 会员积分
    i_card_level = 0  # 会员卡等级
    i_remainder = 0  # 会员余额

    @classmethod
    def expected_data(cls, i_total_consume, i_swap_score, i_card_level, i_remainder):
        """
        创建预期值对象
        :param i_total_consume: 会员消费额
        :param i_swap_score: 会员积分
        :param i_card_level: 会员卡等级
        :param i_remainder: 会员余额
        :return:
        """
        exp_value = cls()
        exp_value.i_total_consume = i_total_consume
        exp_value.i_swap_score = i_swap_score
        exp_value.i_card_level = i_card_level
        exp_value.i_remainder = i_remainder
        return exp_value


class Customer(IDataVerify):
    """
    会员类
    """
    member_number = ""  # 会员编号
    name = ""  # 姓名
    phone = ""  # 手机号
    sex = ""  # 性别
    birthday = ""  # 生日
    openid = ""  # 微信openid
    address = ""  # 收货地址
    area = ""  # 收货地区
    city = ""  # 收货城市
    province = ""  # 收货省
    consignee = ""  # 收货人
    employee = None  # 员工信息
    platform = None  # 平台信息
    preVerifyData: CustomerVerifyData = None  # 操作前数据
    postVerifyData: CustomerVerifyData = None  # 操作后数据
    expectedData: CustomerVerifyData = None  # 期待增加值

    def __init__(self):
        self.preVerifyData = CustomerVerifyData()
        self.postVerifyData = CustomerVerifyData()

    def update_pre_verify_data(self):
        """
        更新操作之前的数据
        :return:
        """
        from com.youxinger.testsuite.service import customer_service
        customer_service.update_customer_verify_data(False, self)

    def update_post_verify_data(self):
        """
        更新操作之后的数据
        :return:
        """
        from com.youxinger.testsuite.service import customer_service
        customer_service.update_customer_verify_data(True, self)

    def recharge(self, remainder):
        """
        会员充值
        :param remainder:
        :return:
        """
        from com.youxinger.testsuite.service import customer_service
        customer_service.recharge_customer(self, remainder)

    def top_up(self, remainde, referral):
        """
        会员充值,填写转介绍
        :param remainder:
        :return:
        """
        from com.youxinger.testsuite.service import customer_service
        customer_service.top_up_customer(self, remainde, referral)

    @staticmethod
    def register(customer_info, employee: Employee, platform: Platform):
        """
        会员注册
        :param customer_info:
        :param employee:
        :param platform:
        :return:
        """
        try:
            from com.youxinger.testsuite.service import customer_service
            return customer_service.register_customer(customer_info, employee, platform)
        except Exception as e:
            logging.error("注册会员失败, %s" % e)


    @staticmethod
    def require(phone):
        """
        会员查询
        :param referral:转介绍人的手机号
        :return:
        """
        try:
            from com.youxinger.testsuite.service import customer_service
            return customer_service.get_customer_by_phone(phone)
        except Exception as e:
            logging.error("查找会员失败, %s" % e)

    def delete(self):
        from com.youxinger.testsuite.service import customer_service
        customer_service.del_customer(self)

    def data_verify(self):
        if self.expectedData is None:
            logging.debug("Customer:" + self.name + ", 无预期值，无需进行数据验证")
            return
        assert abs(
            self.postVerifyData.i_total_consume - self.expectedData.i_total_consume - self.preVerifyData.i_total_consume) < 2, \
            "会员消费额检测失败,期待增加值:%d, 当前值:%d, 之前值:%d" % (
                self.expectedData.i_total_consume, self.postVerifyData.i_total_consume, self.preVerifyData.i_total_consume)
        assert abs(self.postVerifyData.i_remainder - self.expectedData.i_remainder - self.preVerifyData.i_remainder) < 2, \
            "会员余额检测失败,期待增加值:%d, 当前值:%d, 之前值:%d" % (
                self.expectedData.i_remainder, self.postVerifyData.i_remainder, self.preVerifyData.i_remainder)
        assert abs(self.postVerifyData.i_swap_score - self.expectedData.i_swap_score - self.preVerifyData.i_swap_score) < 2, \
            "会员积分检测失败,期待增加值:%d, 当前值:%d, 之前值:%d" % (
            self.expectedData.i_swap_score, self.postVerifyData.i_swap_score, self.preVerifyData.i_swap_score)

        # 检测会员卡级别
        card_level_assert_dict = {1: self.__card_level_1,
                                  2: self.__card_level_2,
                                  3: self.__card_level_3,
                                  4: self.__card_level_4,
                                  5: self.__card_level_5}
        card_level_assert = card_level_assert_dict.get(self.expectedData.i_card_level, self.__card_level_0)
        card_level_assert()

    def __card_level_0(self):
        logging.info(u"不检测会员卡, 当前会员卡级别为: %d" % self.postVerifyData.i_card_level)

    def __card_level_1(self):
        assert self.postVerifyData.i_card_level == 1, "会员卡级别检测失败,期待值:1, 当前值:%d, 之前值:%d" % (
            self.postVerifyData.i_card_level, self.preVerifyData.i_card_level)

    def __card_level_2(self):
        assert self.postVerifyData.i_card_level == 2, "会员卡级别检测失败,期待值:2, 当前值:%d, 之前值:%d" % (
            self.postVerifyData.i_card_level, self.preVerifyData.i_card_level)

    def __card_level_3(self):
        assert self.postVerifyData.i_card_level == 3, "会员卡级别检测失败,期待值:3, 当前值:%d, 之前值:%d" % (
            self.postVerifyData.i_card_level, self.preVerifyData.i_card_level)

    def __card_level_4(self):
        assert self.postVerifyData.i_card_level == 4, "会员卡级别检测失败,期待值:4, 当前值:%d, 之前值:%d" % (
            self.postVerifyData.i_card_level, self.preVerifyData.i_card_level)

    def __card_level_5(self):
        assert self.postVerifyData.i_card_level == 5, "会员卡级别检测失败,期待值:5, 当前值:%d, 之前值:%d" % (
            self.postVerifyData.i_card_level, self.preVerifyData.i_card_level)