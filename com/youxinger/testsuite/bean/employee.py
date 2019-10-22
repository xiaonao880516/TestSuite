from com.youxinger.testsuite.bean.i_validate import IDataVerify


class EmployeeVerifyData(object):
    """
    员工数据验证类
    """
    i_employee_sale_num = 0  # 员工业绩


class Employee(IDataVerify):
    """
    员工
    """
    employee_name = ''
    employee_id = ''
    employee_phone = ''
    employee_password = ''

    preVerifyData: EmployeeVerifyData = None  # 操作前数据
    postVerifyData: EmployeeVerifyData = None  # 操作后数据
    expectedData: EmployeeVerifyData = None  # 期待增加值

    def __init__(self, employee_name, employee_id, employee_phone, employee_password):
        self.employee_name = employee_name
        self.employee_id = employee_id
        self.employee_phone = employee_phone
        self.employee_password = employee_password
        self.preVerifyData = EmployeeVerifyData()
        self.postVerifyData = EmployeeVerifyData()

    def data_verify(self):
        if self.expectedData is not None:
            assert abs(
                self.postVerifyData.i_employee_sale_num - self.expectedData.i_employee_sale_num - self.preVerifyData.i_employee_sale_num) == 0, \
                "员工业绩检测失败,期待增加值:%d, 当前值:%d, 之前值:%d" % (
                    self.expectedData.i_employee_sale_num, self.postVerifyData.i_employee_sale_num, self.preVerifyData.i_employee_sale_num)