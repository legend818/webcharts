from pyecharts import Scatter
scatter = Scatter("散点图", "一年的降水量与蒸发量")
# 设置数据
data1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
data2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
# xais_name是设置横坐标名称，这里由于显示问题，还需要将y轴名称与y轴的距离进行设置
scatter.add("降水量与蒸发量的散点分布", data1, data2, xaxis_name="降水量", yaxis_name="蒸发量",
            yaxis_name_gap=40)
scatter.render()