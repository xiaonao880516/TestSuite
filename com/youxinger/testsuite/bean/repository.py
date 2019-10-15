from com.youxinger.testsuite.bean.i_validate import IDataVerify


class GoodVerifyData(object):
    """
    商品数据验证类
    """
    s_tiaoma: str = None  # 商品条码
    i_pre_quantity = 0  # 操作之前库存值
    i_expected_quantity = 0  # 期待库存变化值
    i_post_quantity = 0  # 操作之后库存值

    def __init__(self, tiaoma):
        self.s_tiaoma = tiaoma
        if self.s_tiaoma is None:
            self.s_tiaoma = '未知'


class Repository(IDataVerify):
    """
    仓库数据验证类
    """
    s_repo_name: str = None  # 仓库名称
    goods: [GoodVerifyData] = None  # 要验证的会员列表

    def __init__(self, repo_name):
        self.s_repo_name = repo_name
        self.goods = []

    def data_verify(self):
        if self.goods is not None:
            for good in self.goods:
                assert abs(good.i_post_quantity - good.i_pre_quantity - good.i_expected_quantity) == 0, \
                    "%s仓库%s商品，库存检测失败,期待增加值:%d, 当前值:%d, 之前值:%d" % (self.s_repo_name, good.s_tiaoma,
                                                                 good.i_expected_quantity, good.i_post_quantity, good.i_pre_quantity)

