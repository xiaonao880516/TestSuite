from com.youxinger.testsuite.bean.i_validate import IDataVerify


class PlatVerifyData(object):
    """
    平台验证数据
    """
    f_platform_sale_num = 0.0  # 平台业绩


class Platform(IDataVerify):
    """
    平台
    """
    platform_name = ''  # 平台名称
    platform_id = ''  # 平台id
    store_id = ''  # 门店id
    preVerifyData: PlatVerifyData = None  # 操作前数据
    postVerifyData: PlatVerifyData = None  # 操作后数据
    expectedData: PlatVerifyData = None  # 期待增加值

    def __init__(self, platform_name, platform_id):
        self.platform_name = platform_name
        self.platform_id = platform_id
        self.preVerifyData = PlatVerifyData()
        self.postVerifyData = PlatVerifyData()

    def update_pre_verify_data(self):
        """
        更新操作之前的数据
        :return:
        """
        from com.youxinger.testsuite.service import financial_data_service
        financial_data_service.get_update_platform_data(self.store_id, self.platform_id, self.preVerifyData)

    def update_post_verify_data(self):
        """
        更新操作之后的数据
        :return:
        """
        from com.youxinger.testsuite.service import financial_data_service
        financial_data_service.get_update_platform_data(self.store_id, self.platform_id, self.postVerifyData)

    def data_verify(self):
        if self.expectedData is not None:
            assert abs(
                self.postVerifyData.f_platform_sale_num - self.expectedData.f_platform_sale_num - self.preVerifyData.f_platform_sale_num) < 0.02, \
                "平台业绩检测失败,期待增加值:%d, 当前值:%d, 之前值:%d" % (
                    self.expectedData.f_platform_sale_num, self.postVerifyData.f_platform_sale_num, self.preVerifyData.f_platform_sale_num)