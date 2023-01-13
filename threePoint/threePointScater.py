from pyecharts.commons.utils import JsCode

from pyecharts.charts import Scatter
from pyecharts import options as opts
import pandas as pd


# 三分效率
def threePointScatter():
    player = pd.read_csv('../player.csv')

    # 三分榜降序排行
    playerByPTS = player.sort_values('3P', ascending=False)[0:20]
    print(playerByPTS)

    # 前20名球员名字
    playerMaxName = playerByPTS.iloc[0:20, 1]
    # 投进三分球最多的前二十名
    playerMaxThreeScored = playerByPTS.iloc[0:20, 11]
    # 出手数
    playerMaxThreeAttempt = playerByPTS.iloc[0:20, 12]
    # 投篮命中率
    playerMaxPercentage = playerByPTS.iloc[0:20, 13]


    listPlayerName = []

    for data in playerMaxName:
        listPlayerName.append(data.split('.')[0])
    listName = []
    for data in listPlayerName:
        name = data.split("*")[0]
        listName.append(name)

    x_data = list(playerMaxThreeAttempt)  # x数据
    xData = sorted(x_data)
    y_data = list(playerMaxPercentage)  # y数据
    yData = sorted(y_data)

    listPercentage = []
    for data in playerMaxPercentage:
        listPercentage.append(format(float(data), '.0%'))
    c = (
        # 散点图
        # 初始化
        Scatter(init_opts=opts.InitOpts(width="1200px", height="600px"))
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(
            # 系列名称
            series_name="",
            # 系列数据
            y_axis=[list(z) for z in zip(y_data, x_data, listName, list(playerMaxThreeScored), listPercentage)],
            # 标记的大小
            symbol_size=20,
            # 标记的图形
            symbol=None,
            # 是否选中图例
            is_selected=True,
            # 系列 label 颜色
            color='#00CCFF',
            # 标签配置项
            label_opts=opts.LabelOpts(formatter=JsCode(
                # 构造回调函数
                "function(params){return params.value[3];}"
            )),  # 不显示标签

        )
            # 系统配置项
            .set_series_opts()
            # 全局配置项
            .set_global_opts(
            title_opts=opts.TitleOpts(title="本赛季三分投中数的前二十名的三分效率图"),
            # x轴配置
            xaxis_opts=opts.AxisOpts(
                name='三分出手数',
                name_location='center',
                # 坐标轴类型 'value': 数值轴
                type_="value",
                is_inverse=False,
                split_number=10,
                min_=xData[0] - 10
            ),
            # y轴配置
            yaxis_opts=opts.AxisOpts(
                name='三分命中率',
                # 坐标轴类型 'value': 数值轴
                name_location='center',
                name_gap=30,
                type_="value",
                is_inverse=False,
                min_=round(float(yData[0]) - 0.05, 2)
            ),
            # 提示框配置项
            tooltip_opts=opts.TooltipOpts(formatter=JsCode(
                # 构造回调函数
                "function (params) {return '命中数:'+ params.value[4] + "
                "' 出手数:' + params.value[0] +' 命中率' + params.value[5];}"
            ))
        ).render("html/threePointScatter.html")
    )

    return c


if __name__ == '__main__':
    threePointScatter()
