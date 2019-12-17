# 导入柱状图-Bar
from pyecharts import Bar
from common import linkdatabase


def bar_chart(columns, title_one, data_one, title_two, data_two):
    # 设置行名
    # columns = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    # 设置数据
    # data1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
    # data2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
    # 设置柱状图的主标题与副标题
    bar = Bar("柱状图", "一年的降水量与蒸发量")
    # 添加柱状图的数据及配置项
    bar.add(title_one, columns, data_one, mark_line=["average"], mark_point=["max", "min"])
    bar.add(title_two, columns, data_two, mark_line=["average"], mark_point=["max", "min"])
    # 生成本地文件（默认为.html文件）
    bar.render('bar.html')


if __name__ == '__main__':
    # 设置行名
    sql = '''SELECT columnname  FROM `bar_table` GROUP BY columnname ORDER BY uniqueid'''
    c = linkdatabase.MySql(sql).select()
    columns = [str(c[i][0]) for i in range(len(c))]
    title_one = '降水量'
    # columns = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    # 设置数据
    sql1 = '''SELECT datavalue FROM `bar_table` WHERE datatype = "降水量" ORDER BY uniqueid'''
    a = linkdatabase.MySql(sql1).select()
    data1 = [float(a[i][0]) for i in range(len(a))]

    sql2 = '''SELECT datavalue FROM `bar_table` WHERE datatype = "蒸发量" ORDER BY uniqueid'''
    b = linkdatabase.MySql(sql2).select()
    data2 = [float(b[i][0]) for i in range(len(b))]
    title_two = '蒸发量'
    bar_chart(columns, title_one, data1, title_two, data2)
