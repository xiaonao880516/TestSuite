from com.youxinger.testsuite.case.base_case import BaseCase
import logging
from com.youxinger.testsuite.service import market_service
from com.youxinger.testsuite.utils.constant import WAREHOUSE, STORE


class TestGeneralGoods(BaseCase):
    """
    一般商品测试
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # 会员充值40000
        cls._customer.recharge(40000)

    def setUp(self):
        super().setUp()
        # 更新充值前的验证数据
        self._test_data.update_pre_verify_data()
        # 仓库变更为 余额仓
        market_service.edit_the_warehouse(WAREHOUSE, 2, 0.5, 1000000000, STORE['store_id'])
        globals()['yeq'] = market_service.balance_of_warehouse(WAREHOUSE['repository_id'])
        globals()['spq'] = market_service.search_information('M216C237C0458')

    def tearDown(self):
        super().tearDown()

    def test_1_add_the_warehouse(self):
        """
         门店申请补仓 补5个M216C237C0458
         补货成功 确认收货
        :return:
        """
        logging.debug("test_1_recharge_shopping_order")
        param = {'goods_list[0][tiaoma]': 'M216C237C0458',
                 'goods_list[0][goods_name]': '腰背夹',
                 'goods_list[0][num]': '5'}
        # 提交补仓申请
        globals()['application_id'] = market_service.standard_request(param)
        # 更新充值后的验证数据
        self._test_data.update_post_verify_data()
        sph = market_service.search_information('M216C237C0458')
        yeh = market_service.balance_of_warehouse(WAREHOUSE['repository_id'])
        # 封装验证值
        self.expectedData(0  # 会员消费额
                          , 0  # 会员积分
                          , 2  # 会员卡等级
                          , 0  # 会员余额
                          , 0  # 总揽到店次数
                          , 0  # 总揽新增会员数
                          , 0  # 总揽订单数
                          , 0  # 总揽退单数
                          , 0  # 总揽销售总额
                          , 0  # M216C237C0458总仓库存
                          , 0  # M216C237C0464总仓库存
                          , 0  # M116E248B0158总仓库存
                          , 0  # M116E248B0164总仓库存
                          , 0  # M316J232B01106总仓库存
                          , 0  # M316J232B0176总仓库存
                          , 0  # ZH02B215190T796242总仓库存
                          , 0  # 验证值
                          , 5  # M216C237C0458门店库存
                          , 0  # M216C237C0464门店库存
                          , 0  # M116E248B0158门店库存
                          , 0  # M116E248B0164门店库存
                          , 0  # M316J232B01106门店库存
                          , 0  # M316J232B0176门店库存
                          , 0  # ZH02B215190T796242门店库存
                          , 0  # 门店到店次数期待增加值
                          , 0  # 门店新增会员数期待增加值
                          , 0  # 门店订单数期待增加值
                          , 0  # 门店退单数期待增加值
                          , 0  # 门店销售总额期待增加值
                          , 0  # 门店平台销售总额期待增加值
                          )
        # 验证数据
        self._data_assertion()
        a = int(yeh) - int(globals()['yeq'])
        if a == -16900:
            logging.info('可补货金额正确')
            return True
        else:
            logging.info('可补货金额失败')
            print(a)
        b = int(sph) - int(globals()['sph'])
        if b == 5:
            logging.info('可补货金额正确')
            return True
        else:
            logging.info('可补货金额失败')
            print(b)

    def test_2_return_the_warehouse(self):
        """
        仓库申请退5个 M216C237C0458
        审核通过，退货成功
        :return:
        """
        logging.debug("test_1_recharge_shopping_order")
        param = {'goods_list[0][tiaoma]': 'M216C237C0458',
                 'goods_list[0][goods_name]': '腰背夹',
                 'goods_list[0][num]': '5'}
        return_id = market_service.return_request(param)
        sub_return_id = return_id + "_0"
        params = {"update_data": {"周测试二店仓库": [{"return_id": return_id, "sub_return_id": sub_return_id, "brand_name": "Makebody", "category_name": "背夹",
                  "tiaoma": "M216C237C0458", "goods_name": "腰背夹", "return_num": "5", "received_num": 5, "refused_num": 0, "price": "3380.00", "kucun": "4668",
                  "img":"", "return_goods_price": "16900.00", "received_goods_price": "0.00", "refused_goods_price": "0.00", "sku_info": " 深蓝色  58 ",
                  "repository_id":"zjh002", "store_id": "zjh002", "repo_num": "0", "type": "2", "repository_name": "周测试二店仓库"}]}, "refused_reason": ""}
        market_service.examine_and_approve(params)
        # 更新充值后的验证数据
        self._test_data.update_post_verify_data()
        sph = market_service.search_information('M216C237C0458')
        yeh = market_service.balance_of_warehouse(WAREHOUSE['repository_id'])
        # 封装验证值
        self.expectedData(0  # 会员消费额
                          , 0  # 会员积分
                          , 2  # 会员卡等级
                          , 0  # 会员余额
                          , 0  # 总揽到店次数
                          , 0  # 总揽新增会员数
                          , 0  # 总揽订单数
                          , 0  # 总揽退单数
                          , 0  # 总揽销售总额
                          , 0  # M216C237C0458总仓库存
                          , 0  # M216C237C0464总仓库存
                          , 0  # M116E248B0158总仓库存
                          , 0  # M116E248B0164总仓库存
                          , 0  # M316J232B01106总仓库存
                          , 0  # M316J232B0176总仓库存
                          , 0  # ZH02B215190T796242总仓库存
                          , 0  # 验证值
                          , -5  # M216C237C0458门店库存
                          , 0  # M216C237C0464门店库存
                          , 0  # M116E248B0158门店库存
                          , 0  # M116E248B0164门店库存
                          , 0  # M316J232B01106门店库存
                          , 0  # M316J232B0176门店库存
                          , 0  # ZH02B215190T796242门店库存
                          , 0  # 门店到店次数期待增加值
                          , 0  # 门店新增会员数期待增加值
                          , 0  # 门店订单数期待增加值
                          , 0  # 门店退单数期待增加值
                          , 0  # 门店销售总额期待增加值
                          , 0  # 门店平台销售总额期待增加值
                          )
        # 验证数据
        self._data_assertion()
        a = int(yeh) - int(globals()['yeq'])
        if a == 16900:
            logging.info('可补货金额正确')
            return True
        else:
            logging.info('可补货金额失败')
            print(a)
        b = int(sph) - int(globals()['sph'])
        if b == -5:
            logging.info('M216C237C0458库存正确')
            return True
        else:
            logging.info('M216C237C0458库存错误')
            print(b)