from com.youxinger.testsuite.bean.i_validate import IDataVerify


class StoreVerifyData(object):
    """
    门店数据验证类
    """
    store_arrive_store_num = 0  # 门店到店次数
    store_bhm_percent = ""  # 门店测量成单率
    store_newvip_num = 0  # 门店新增会员数
    store_newvip_order_percent = ""  # 门店新会员成单率
    store_order_num = 0  # 门店订单数
    store_refund_num = 0  # 门店退单数
    store_sale_num = 0  # 门店销售总额
    store_plat_sale_num: 0  # 门店平台销售总额


class Store(IDataVerify):
    """
    门店类
    """
    store_id = ""  # 门店编号
    store_name = ""  # 门店名称
    preVerifyData: StoreVerifyData = None  # 操作前数据
    postVerifyData: StoreVerifyData = None  # 操作后数据
    expectedData: StoreVerifyData = None  # 期待增加值

    def __init__(self):
        self.preVerifyData = StoreVerifyData()
        self.postVerifyData = StoreVerifyData()
        self.expectedData = StoreVerifyData()