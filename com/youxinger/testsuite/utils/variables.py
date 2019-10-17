import datetime


foregroundTID = ""  # 前端登录tid临时变量
backgroundTID = ""  # 后台登录tid临时变量
s_start_datetime = datetime.datetime.now().strftime("%Y-%m-%d")  # 今天的年-月-日
s_end_date_time = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")  # 明天的年-月-日
s_month_date_time = datetime.datetime.now().strftime("%Y-%m")  # 今天的年-月