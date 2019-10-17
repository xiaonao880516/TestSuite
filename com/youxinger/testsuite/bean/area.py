from com.youxinger.testsuite.bean.i_validate import IDataVerify
from com.youxinger.testsuite.bean.store import Store


class AreaVerifyData(object):
    """
    大区数据验证类
    """
    i_area_sales_amount = 0  # 大区销售额


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

    def __init__(self):
        self.preVerifyData = AreaVerifyData()
        self.postVerifyData = AreaVerifyData()
        self.expectedData = AreaVerifyData()

    def data_verify(self):
        assert abs(
            self.postVerifyData.i_area_sales_amount - self.expectedData.i_area_sales_amount - self.preVerifyData.i_area_sales_amount) == 0, \
            "大区销售额检测失败,期待增加值:%d, 当前值:%d, 之前值:%d" % (
                self.expectedData.i_area_sales_amount, self.postVerifyData.i_area_sales_amount, self.preVerifyData.i_area_sales_amount)

        if self.stores is not None:
            for store in self.stores:
                store.data_verify()