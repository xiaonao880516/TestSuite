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
    repo_name: str = None  # 仓库名称
    tid: str = None  # 前台登录tid，用来确认哪个门店哪个仓库
    verify_good_list: {GoodVerifyData} = None  # 要验证的商品列表

    def __init__(self, repo_name: str, tid: str, goods_code: list):
        """
        创建门店仓
        :param repo_name:
        :param tid:
        :param goods_code:
        """
        self.repo_name = repo_name
        self.tid = tid
        self.verify_good_list = dict()
        for code in goods_code:
            good_verify_data = GoodVerifyData(code)
            self.verify_good_list[code] = good_verify_data

    @classmethod
    def lc_global(cls, goods_code: list):
        """
        创建总仓
        :param goods_code:
        :return:
        """
        return cls('总仓', '', goods_code)

    def update_pre_verify_data(self):
        """
        更新操作之前的数据
        :return:
        """
        from com.youxinger.testsuite.service import repository_service
        if self.repo_name == "总仓":
            repository_service.get_global_repository(False, self.verify_good_list)
        else:
            repository_service.get_store_repository_by_tid(False, self.tid, self.verify_good_list)

    def update_post_verify_data(self):
        """
        更新操作之后的数据
        :return:
        """
        from com.youxinger.testsuite.service import repository_service
        if self.repo_name == "总仓":
            repository_service.get_global_repository(True, self.verify_good_list)
        else:
            repository_service.get_store_repository_by_tid(True, self.tid, self.verify_good_list)

    def update_expected_verify_data(self, expected_good_list):
        """
        更新期待库存值
        :return:
        """
        if expected_good_list is not None:
            for code in expected_good_list:
                good = self.verify_good_list.get(code)
                if good is not None:
                    good.i_expected_quantity = expected_good_list.get(code)

    def data_verify(self):
        if self.verify_good_list is not None:
            for code in self.verify_good_list:
                good = self.verify_good_list[code]
                assert abs(good.i_post_quantity - good.i_pre_quantity - good.i_expected_quantity) == 0, \
                    "%s仓库%s商品，库存检测失败,期待增加值:%d, 当前值:%d, 之前值:%d" % (self.repo_name, good.s_tiaoma,
                                                                  good.i_expected_quantity, good.i_post_quantity, good.i_pre_quantity)

