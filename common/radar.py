from pyecharts import Radar
radar = Radar("雷达图", "一年的降水量与蒸发量")
# 由于雷达图传入的数据得为多维数据，所以这里需要做一下处理
radar_data1 = [[2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]]
radar_data2 = [[2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]]
# 设置column的最大值，为了雷达图更为直观，这里的月份最大值设置有所不同
schema = [
    ("Jan", 5), ("Feb",10), ("Mar", 10),
    ("Apr", 50), ("May", 50), ("Jun", 200),
    ("Jul", 200), ("Aug", 200), ("Sep", 50),
    ("Oct", 50), ("Nov", 10), ("Dec", 5)
]
# 传入坐标
radar.config(schema)
radar.add("降水量", radar_data1)
# 一般默认为同一种颜色，这里为了便于区分，需要设置item的颜色
radar.add("蒸发量", radar_data2, item_color="#1C86EE")
radar.render()