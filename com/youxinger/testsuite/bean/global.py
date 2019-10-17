from com.youxinger.testsuite.bean.i_validate import IDataVerify


class GlobalVerifyData(object):
    """
    总览验证数据
    """
    i_global_arrive_store_num = 0  # 总揽到店次数
    i_global_newvip_num = 0  # 总揽新增会员数
    i_global_order_num = 0  # 总揽订单数
    i_global_refund_num = 0  # 总揽退单数
    i_global_sale_num = 0  # 总揽销售总额


class Global(IDataVerify):
    """
    总览信息
    """
    preVerifyData: GlobalVerifyData = None  # 操作前数据
    postVerifyData: GlobalVerifyData = None  # 操作后数据
    expectedData: GlobalVerifyData = None  # 期待增加值

    def __init__(self):
        self.preVerifyData = GlobalVerifyData()
        self.postVerifyData = GlobalVerifyData()
        self.expectedData = GlobalVerifyData()