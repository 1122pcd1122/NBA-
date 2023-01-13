from pyecharts.commons.utils import JsCode

from pyecharts.charts import Scatter
from pyecharts import options as opts
import pandas as pd


# 得分效率
def scoredScatter():
    player = pd.read_csv('player.csv')

    # 得分榜降序排行
    playerByPTS = player.sort_values('PTS', ascending=False)[0:20]
    print(playerByPTS)

    # 前20名球员名字
    playerMaxName = playerByPTS.iloc[0:20, 1]
    # 投进两分球最多的前二十名
    playerMaxTwoScored = playerByPTS.iloc[0:20, 29]
    # 出手数
    playerMaxTwoAttempt = playerByPTS.iloc[0:20, 9]
    # 投篮命中率
    playerMaxPercentage = playerByPTS.iloc[0:20, 17]

    listPlayerName = list(playerMaxName)
    listName = []
    for data in listPlayerName:
        name = data.split("*")[0]
        listName.append(name)

    x_data = list(playerMaxTwoScored)  # x数据
    x_data.sort()
    y_data = list(playerMaxPercentage)  # y数据
    c = (
        # 散点图
        # 初始化
        Scatter(init_opts=opts.InitOpts(width="1200px", height="600px"))
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(
            # 系列名称
            series_name="",
            # 系列数据
            y_axis=[list(z) for z in zip(y_data, x_data, listName, list(playerMaxTwoAttempt))],
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
            title_opts=opts.TitleOpts(title="本赛季得分前20名的得分效率"),
            # x轴配置
            xaxis_opts=opts.AxisOpts(
                name='得分',
                name_location='center',
                # 坐标轴类型 'value': 数值轴
                type_="value",
                is_inverse=False,
                split_number=5,
                min_=int(x_data[0] - 10)

            ),
            # y轴配置
            yaxis_opts=opts.AxisOpts(
                name='真实命中率',
                # 坐标轴类型 'value': 数值轴
                name_location='center',
                name_gap=30,
                type_="value",
                is_inverse=False,
                # 最小值
                min_=round(float(y_data[len(y_data) - 1]) - 0.05, 2),
            ),
            # 提示框配置项
            tooltip_opts=opts.TooltipOpts(formatter=JsCode(
                # 构造回调函数
                "function (params) {return '命中数:'+ params.value[0] + "
                "' 出手数:' + params.value[4] +' 命中率' + params.value[1];}"
            ))
        )
            .render("scored/html/scoredScatter.html")
    )
    return c


if __name__ == '__main__':
    scoredScatter()

