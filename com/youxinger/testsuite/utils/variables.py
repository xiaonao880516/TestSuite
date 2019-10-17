import datetime

# 前端登录tid临时变量
foregroundTID = ""
# 后台登录tid临时变量
backgroundTID = ""

s_start_datetime = datetime.datetime.now().strftime("%Y-%m-%d")
s_end_date_time = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
s_month_date_time = datetime.datetime.now().strftime("%Y-%m")