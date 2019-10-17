from com.youxinger.testsuite.bean.i_validate import IDataVerify
import logging


class CustomerVerifyData(object):
    """
    会员数据验证类
    """
    i_total_consume = 0  # 会员消费额
    i_swap_score = 0  # 会员积分
    i_card_level = 0  # 会员卡等级
    i_remainder = 0  # 会员余额


class Customer(IDataVerify):
    """
    会员类
    """
    member_number = ""  # 会员编号
    name = ""  # 姓名
    phone = ""  # 手机号
    sex = ""
    birthday = ""
    openid = ""
    employee_number = ""
    platform_number = ""
    address = ""
    area = ""
    city = ""
    province = ""
    consignee = ""
    preVerifyData: CustomerVerifyData = None
    postVerifyData: CustomerVerifyData = None
    expectedData: CustomerVerifyData = None

    def __init__(self):
        self.preVerifyData = CustomerVerifyData()
        self.postVerifyData = CustomerVerifyData()
        self.expectedData = CustomerVerifyData()

    def data_verify(self):
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