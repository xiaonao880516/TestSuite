import logging
from com.youxinger.testsuite.bean.i_validate import IDataVerify
from com.youxinger.testsuite.bean.store import Store


class AreaVerifyData(object):
    """
    大区数据验证类
    """
    f_area_sales_amount = 0  # 大区销售额

    @classmethod
    def expected_data(cls, f_area_sales_amount):
        """
        创建预期值对象
        :param f_area_sales_amount: 大区销售额
        :return:
        """
        exp_value = cls()
        exp_value.f_area_sales_amount = f_area_sales_amount
        return exp_value


class Area(IDataVerify):
    """
    大区
    """
    area_name = ''  # 大区编号
    area_id = ''  # 大区id
    stores: [Store] = None  # 要验证的门店列表
    preVerifyData: AreaVerifyData = None  # 操作前数据
    postVerifyData: AreaVerifyData = None  # 操作后数据
    expectedData: AreaVerifyData = None  # 期待增加值

    def __init__(self, area_name, area_id):
        self.area_name = area_name
        self.area_id = area_id
        self.preVerifyData = AreaVerifyData()
        self.postVerifyData = AreaVerifyData()
        self.stores = []

    def update_expected_store_verify_data(self, expected_store_list):
        """
        更新期待门店验证值
        :return:
        """
        if expected_store_list is not None:
            for store in self.stores:
                store.expectedData = expected_store_list.get(store.store_id)

    def update_pre_verify_data(self):
        """
        更新操作之前的数据
        :return:
        """
        from com.youxinger.testsuite.service import financial_data_service
        financial_data_service.get_update_area_data(self.area_id, self.preVerifyData)
        if self.stores is not None:
            for store in self.stores:
                store.update_pre_verify_data()

    def update_post_verify_data(self):
        """
        更新操作之后的数据
        :return:
        """
        from com.youxinger.testsuite.service import financial_data_service
        financial_data_service.get_update_area_data(self.area_id, self.postVerifyData)
        if self.stores is not None:
            for store in self.stores:
                store.update_post_verify_data()

    def data_verify(self):
        if self.expectedData is not None:
            assert abs(
                self.postVerifyData.f_area_sales_amount - self.expectedData.f_area_sales_amount - self.preVerifyData.f_area_sales_amount) < 2, \
                "大区销售额检测失败,期待增加值:%d, 当前值:%d, 之前值:%d" % (
                    self.expectedData.f_area_sales_amount, self.postVerifyData.f_area_sales_amount, self.preVerifyData.f_area_sales_amount)
        else:
            logging.debug("Area:"+self.area_name+", 无预期值，无需进行数据验证")

        if self.stores is not None:
            for store in self.stores:
                store.data_verify()