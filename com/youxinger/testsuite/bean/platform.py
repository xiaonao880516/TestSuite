from com.youxinger.testsuite.bean.i_validate import IDataVerify


class PlatVerifyData(object):
    """
    平台验证数据
    """
    i_platform1_sale_num = 0  # 平台业绩


class Platform(IDataVerify):
    """
    平台
    """
    platform_name = ''  # 平台名称
    platform_id = ''  # 平台id
    preVerifyData: PlatVerifyData = None  # 操作前数据
    postVerifyData: PlatVerifyData = None  # 操作后数据
    expectedData: PlatVerifyData = None  # 期待增加值

    def __init__(self):
        self.preVerifyData = PlatVerifyData()
        self.postVerifyData = PlatVerifyData()
        self.expectedData = PlatVerifyData()