import logging

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

    @classmethod
    def expected_data(cls, i_store_arrive_store_num, i_store_newvip_num, i_store_order_num, i_store_refund_num,
                      f_store_sale_num, f_store_plat_sale_num):
        """
        创建预期值对象
        :param i_store_arrive_store_num: 门店到店次数期待增加值
        :param i_store_newvip_num: 门店新增会员数期待增加值
        :param i_store_order_num: 门店订单数期待增加值
        :param i_store_refund_num: 门店退单数期待增加值
        :param f_store_sale_num: 门店销售总额期待增加值
        :param f_store_plat_sale_num: 门店平台销售总额期待增加值
        :return:
        """
        exp_value = cls()
        exp_value.i_store_arrive_store_num = i_store_arrive_store_num
        exp_value.i_store_newvip_num = i_store_newvip_num
        exp_value.i_store_order_num = i_store_order_num
        exp_value.i_store_refund_num = i_store_refund_num
        exp_value.f_store_sale_num = f_store_sale_num
        exp_value.f_store_plat_sale_num = f_store_plat_sale_num
        return exp_value


class Store(IDataVerify):
    """
    门店类
    """
    store_id = ""  # 门店编号
    store_name = ""  # 门店名称
    __platforms: [Platform] = None  # 要验证的平台列表
    repository: Repository = None  # 要验证的仓库
    __employees: [Employee] = None  # 要验证的员工列表
    preVerifyData: StoreVerifyData = None  # 操作前数据
    postVerifyData: StoreVerifyData = None  # 操作后数据
    expectedData: StoreVerifyData = None  # 期待增加值

    def __init__(self, store_name, store_id):
        self.store_id = store_id
        self.store_name = store_name
        self.preVerifyData = StoreVerifyData()
        self.postVerifyData = StoreVerifyData()
        self.__platforms = []
        self.__employees = []

    def add_platform(self, platform: Platform):
        if platform is not None:
            platform.store_id = self.store_id
            self.__platforms.append(platform)

    def add_employee(self, employee: Employee):
        if employee is not None:
            employee.store_id = self.store_id
            self.__employees.append(employee)

    def update_pre_verify_data(self):
        """
        更新操作之前的数据
        :return:
        """
        from com.youxinger.testsuite.service import financial_data_service
        financial_data_service.get_update_store_data(self.store_id, self.preVerifyData)
        if self.repository is not None:
            self.repository.update_pre_verify_data()

        if self.__platforms is not None:
            for platform in self.__platforms:
                platform.update_pre_verify_data()

        if self.__employees is not None:
            for employee in self.__employees:
                employee.update_pre_verify_data()

    def update_post_verify_data(self):
        """
        更新操作之后的数据
        :return:
        """
        from com.youxinger.testsuite.service import financial_data_service
        financial_data_service.get_update_store_data(self.store_id, self.postVerifyData)
        if self.repository is not None:
            self.repository.update_post_verify_data()

        if self.__platforms is not None:
            for platform in self.__platforms:
                platform.update_post_verify_data()

        if self.__employees is not None:
            for employee in self.__employees:
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
        else:
            logging.debug("Store:"+self.store_name+", 无预期值，无需进行数据验证")

        if self.repository is not None:
            self.repository.data_verify()

        if self.__platforms is not None:
            for platform in self.__platforms:
                platform.data_verify()

        if self.__employees is not None:
            for employee in self.__employees:
                employee.data_verify()