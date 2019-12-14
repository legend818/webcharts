# 导入饼图Pie
from pyecharts import Pie
# 设置主标题与副标题，标题设置居中，设置宽度为900
pie = Pie("饼状图", "一年的降水量与蒸发量", title_pos='center', width=900)
# 设置行名
columns = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# 设置数据
data1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
data2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
# 加入数据，设置坐标位置为【25，50】，上方的colums选项取消显示
pie.add("降水量", columns, data1, center=[25, 50], is_legend_show=False)
# 加入数据，设置坐标位置为【75，50】，上方的colums选项取消显示，显示label标签
pie.add("蒸发量", columns, data2, center=[75, 50], is_legend_show=False, is_label_show=True)
# 保存图表
pie.render()
