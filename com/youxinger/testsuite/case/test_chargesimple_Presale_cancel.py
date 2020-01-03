
from com.youxinger.testsuite.case.base_case import BaseCase
import logging
from com.youxinger.testsuite.service import market_service



class TestChargePreSaleGoodsCancel(BaseCase):
    """
    预售商品余额支付（一件预售商品 公司发货）
    转订单之前，取消预售商品
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

    def tearDown(self):
        super().tearDown()

    def test_1_ChargePreSaleGoods_order(self):
        """
       预售商品下单
       ‘何明锐预售’：YS6789N838655 公司发货 1件 累计积分
        :return:
        """
        logging.debug("test_1_rechargesskuds_order")
        params={
                          'member_id': self._customer.member_number, 'member_name': self._customer.name,
                          'member_phone': self._customer.phone,
                          'plateform_id': self._customer.platform.platform_id,
                          'special_employee_id': self._customer.employee.employee_id,
                          'pay_type': 'recharge',
                          'goods_info':{'sku_num':'1','sku_name':'何明锐预售','sku_id':'6434','tiaoma':'YS6789N838655','price':'1234.00','kuanhao':'','img':'https://lchapp.oss-cn-beijing.aliyuncs.com/2019112758736210149.png','sku_detail':''}
        }

        # 预售余额下单
        globals()['shopping_order_id']= market_service.presell_pos(params)
        #取消预售（转订单之前)
        market_service.cancel_booking( globals()['shopping_order_id'])
        # 更新充值后的验证数据
        self._test_data.update_post_verify_data()
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
                          , 0  # M216C237C0458门店库存
                          , 0  # M216C237C0464门店库存
                          , 0  # M116E248B0158门店库存
                          , 0  # M116E248B0164门店库存
                          , 0  # M316J232B01106门店库存
                          , 0  # M316J232B0176门店库存
                          , 0  # ZH02B215190T796242门店库存
                          , 1  # 门店到店次数期待增加值
                          , 0  # 门店新增会员数期待增加值
                          , 0  # 门店订单数期待增加值
                          , 0  # 门店退单数期待增加值
                          , 0  # 门店销售总额期待增加值
                          , 0 # 门店平台销售总额期待增加值
                          )
        # 验证数据
        self._data_assertion()



