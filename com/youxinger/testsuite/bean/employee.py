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

    def __init__(self):
        self.preVerifyData = EmployeeVerifyData()
        self.postVerifyData = EmployeeVerifyData()
        self.expectedData = EmployeeVerifyData()