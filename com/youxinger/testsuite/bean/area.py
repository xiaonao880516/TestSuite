from com.youxinger.testsuite.bean.i_validate import IDataVerify


class AreaVerifyData(object):
    """
    大区数据验证类
    """
    area_sales_amount = 0  # 大区销售额


class Area(IDataVerify):
    """
    大区
    """
    area_name = ''  # 大区编号
    area_id = ''  # 大区id
    preVerifyData: AreaVerifyData = None  # 操作前数据
    postVerifyData: AreaVerifyData = None  # 操作后数据
    expectedData: AreaVerifyData = None  # 期待增加值

    def __init__(self):
        self.preVerifyData = AreaVerifyData()
        self.postVerifyData = AreaVerifyData()
        self.expectedData = AreaVerifyData()