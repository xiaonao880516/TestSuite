from com.youxinger.testsuite.bean.area import Area
from com.youxinger.testsuite.bean.i_validate import IDataVerify
from com.youxinger.testsuite.bean.repository import Repository


class GroupVerifyData(object):
    """
    总览验证数据
    """
    i_group_arrive_store_num = 0  # 总揽到店次数
    i_group_newvip_num = 0  # 总揽新增会员数
    i_group_order_num = 0  # 总揽订单数
    i_group_refund_num = 0  # 总揽退单数
    i_group_sale_num = 0  # 总揽销售总额


class Group(IDataVerify):
    """
    总览信息
    """
    areas: [Area] = None  # 要验证的大区列表
    repository: Repository = None  # 要验证的仓库
    preVerifyData: GroupVerifyData = None  # 操作前数据
    postVerifyData: GroupVerifyData = None  # 操作后数据
    expectedData: GroupVerifyData = None  # 期待增加值

    def __init__(self):
        self.preVerifyData = GroupVerifyData()
        self.postVerifyData = GroupVerifyData()
        self.expectedData = GroupVerifyData()

    def data_verify(self):
        assert abs(
            self.postVerifyData.i_group_arrive_store_num - self.expectedData.i_group_arrive_store_num - self.preVerifyData.i_group_arrive_store_num) == 0, \
            "总揽到店次数检测失败,期待增加值:%d, 当前值:%d, 之前值:%d" % (
                self.expectedData.i_group_arrive_store_num, self.postVerifyData.i_group_arrive_store_num, self.preVerifyData.i_group_arrive_store_num)
        assert abs(
            self.postVerifyData.i_group_newvip_num - self.expectedData.i_group_newvip_num - self.preVerifyData.i_group_newvip_num) == 0, \
            "总揽新增会员数检测失败,期待增加值:%d, 当前值:%d, 之前值:%d" % (
                self.expectedData.i_group_newvip_num, self.postVerifyData.i_group_newvip_num, self.preVerifyData.i_group_newvip_num)
        assert abs(
            self.postVerifyData.i_group_order_num - self.expectedData.i_group_order_num - self.preVerifyData.i_group_order_num) == 0, \
            "总揽订单数检测失败,期待增加值:%d, 当前值:%d, 之前值:%d" % (
                self.expectedData.i_group_order_num, self.postVerifyData.i_group_order_num, self.preVerifyData.i_group_order_num)
        assert abs(
            self.postVerifyData.i_group_refund_num - self.expectedData.i_group_refund_num - self.preVerifyData.i_group_refund_num) == 0, \
            "总揽退单数检测失败,期待增加值:%d, 当前值:%d, 之前值:%d" % (
                self.expectedData.i_group_refund_num, self.postVerifyData.i_group_refund_num, self.preVerifyData.i_group_refund_num)
        assert abs(
            self.postVerifyData.i_group_sale_num - self.expectedData.i_group_sale_num - self.preVerifyData.i_group_sale_num) == 0, \
            "总揽销售总额检测失败,期待增加值:%d, 当前值:%d, 之前值:%d" % (
                self.expectedData.i_group_sale_num, self.postVerifyData.i_group_sale_num, self.preVerifyData.i_group_sale_num)

        if self.repository is not None:
            self.repository.data_verify()

        if self.areas is not None:
            for area in self.areas:
                area.data_verify()