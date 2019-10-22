from com.youxinger.testsuite.bean.employee import Employee
from com.youxinger.testsuite.bean.i_validate import IDataVerify
from com.youxinger.testsuite.bean.platform import Platform
from com.youxinger.testsuite.bean.repository import Repository


class StoreVerifyData(object):
    """
    门店数据验证类
    """
    i_store_arrive_store_num = 0  # 门店到店次数
    f_store_bhm_percent = 0.0  # 门店测量成单率
    i_store_newvip_num = 0  # 门店新增会员数
    f_store_newvip_order_percent = 0.0  # 门店新会员成单率
    i_store_order_num = 0  # 门店订单数
    i_store_refund_num = 0  # 门店退单数
    f_store_sale_num = 0  # 门店销售总额
    f_store_sale_percent = 0.0  # 门店销售完成比
    f_store_plat_sale_num = 0  # 门店平台销售总额
    f_store_plat_sale_percent = 0.0  # 门店平台销售业绩占比


class Store(IDataVerify):
    """
    门店类
    """
    store_id = ""  # 门店编号
    store_name = ""  # 门店名称
    __platforms: [Platform] = None  # 要验证的平台列表
    repository: Repository = None  # 要验证的仓库
    employees: [Employee] = None  # 要验证的员工列表
    preVerifyData: StoreVerifyData = None  # 操作前数据
    postVerifyData: StoreVerifyData = None  # 操作后数据
    expectedData: StoreVerifyData = None  # 期待增加值

    def __init__(self):
        self.preVerifyData = StoreVerifyData()
        self.postVerifyData = StoreVerifyData()
        self.__platforms = []

    def add_platform(self, platform: Platform):
        if platform is not None:
            platform.store_id = self.store_id
            self.__platforms.append(platform)

    def update_pre_verify_data(self):
        """
        更新操作之前的数据
        :return:
        """
        if self.repository is not None:
            self.repository.update_pre_verify_data()

        if self.__platforms is not None:
            for platform in self.__platforms:
                platform.update_pre_verify_data()

        if self.employees is not None:
            for employee in self.employees:
                employee.update_pre_verify_data()

    def update_post_verify_data(self):
        """
        更新操作之后的数据
        :return:
        """
        if self.repository is not None:
            self.repository.update_post_verify_data()

        if self.__platforms is not None:
            for platform in self.__platforms:
                platform.update_post_verify_data()

        if self.employees is not None:
            for employee in self.employees:
                employee.update_post_verify_data()

    def data_verify(self):
        if self.expectedData is not None:
            assert abs(
                self.postVerifyData.i_store_arrive_store_num - self.expectedData.i_store_arrive_store_num - self.preVerifyData.i_store_arrive_store_num) == 0, \
                "门店到店次数检测失败,期待增加值:%d, 当前值:%d, 之前值:%d" % (
                    self.expectedData.i_store_arrive_store_num, self.postVerifyData.i_store_arrive_store_num, self.preVerifyData.i_store_arrive_store_num)
            assert abs(
                self.postVerifyData.f_store_bhm_percent - self.expectedData.f_store_bhm_percent - self.preVerifyData.f_store_bhm_percent) == 0, \
                "门店测量成单率检测失败,期待增加值:%d, 当前值:%d, 之前值:%d" % (
                    self.expectedData.f_store_bhm_percent, self.postVerifyData.f_store_bhm_percent, self.preVerifyData.f_store_bhm_percent)
            assert abs(
                self.postVerifyData.i_store_newvip_num - self.expectedData.i_store_newvip_num - self.preVerifyData.i_store_newvip_num) == 0, \
                "门店新增会员数检测失败,期待增加值:%d, 当前值:%d, 之前值:%d" % (
                    self.expectedData.i_store_newvip_num, self.postVerifyData.i_store_newvip_num, self.preVerifyData.i_store_newvip_num)
            assert abs(
                self.postVerifyData.f_store_bhm_percent - self.expectedData.f_store_bhm_percent - self.preVerifyData.f_store_bhm_percent) == 0, \
                "总揽到店次数检测失败,期待增加值:%d, 当前值:%d, 之前值:%d" % (
                    self.expectedData.f_store_bhm_percent, self.postVerifyData.f_store_bhm_percent, self.preVerifyData.f_store_bhm_percent)
            assert abs(
                self.postVerifyData.i_store_order_num - self.expectedData.i_store_order_num - self.preVerifyData.i_store_order_num) == 0, \
                "门店订单数检测失败,期待增加值:%d, 当前值:%d, 之前值:%d" % (
                    self.expectedData.i_store_order_num, self.postVerifyData.i_store_order_num, self.preVerifyData.i_store_order_num)
            assert abs(
                self.postVerifyData.i_store_refund_num - self.expectedData.i_store_refund_num - self.preVerifyData.i_store_refund_num) == 0, \
                "门店退单数检测失败,期待增加值:%d, 当前值:%d, 之前值:%d" % (
                    self.expectedData.i_store_refund_num, self.postVerifyData.i_store_refund_num, self.preVerifyData.i_store_refund_num)
            assert abs(
                self.postVerifyData.f_store_sale_num - self.expectedData.f_store_sale_num - self.preVerifyData.f_store_sale_num) == 0, \
                "门店销售总额检测失败,期待增加值:%d, 当前值:%d, 之前值:%d" % (
                    self.expectedData.f_store_sale_num, self.postVerifyData.f_store_sale_num, self.preVerifyData.f_store_sale_num)
            assert abs(
                self.postVerifyData.f_store_plat_sale_num - self.expectedData.f_store_plat_sale_num - self.preVerifyData.f_store_plat_sale_num) == 0, \
                "门店平台销售总额检测失败,期待增加值:%d, 当前值:%d, 之前值:%d" % (
                    self.expectedData.f_store_plat_sale_num, self.postVerifyData.f_store_plat_sale_num, self.preVerifyData.f_store_plat_sale_num)

        if self.repository is not None:
            self.repository.data_verify()

        if self.__platforms is not None:
            for platform in self.__platforms:
                platform.data_verify()

        if self.employees is not None:
            for employee in self.employees:
                employee.data_verify()