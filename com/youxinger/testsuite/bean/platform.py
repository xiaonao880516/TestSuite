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

    def __init__(self, platform_name, platform_id):
        self.platform_name = platform_name
        self.platform_id = platform_id
        self.preVerifyData = PlatVerifyData()
        self.postVerifyData = PlatVerifyData()
        self.expectedData = PlatVerifyData()

    def data_verify(self):
        assert abs(
            self.postVerifyData.i_platform1_sale_num - self.expectedData.i_platform1_sale_num - self.preVerifyData.i_platform1_sale_num) == 0, \
            "平台业绩检测失败,期待增加值:%d, 当前值:%d, 之前值:%d" % (
                self.expectedData.i_platform1_sale_num, self.postVerifyData.i_platform1_sale_num, self.preVerifyData.i_platform1_sale_num)