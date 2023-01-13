from pyecharts.commons.utils import JsCode

from pyecharts.charts import Scatter
from pyecharts import options as opts
import pandas as pd


# 两分效率图
def twoPointScatter():
    player = pd.read_csv('../player.csv')

    # 得分榜降序排行
    playerByPTS = player.sort_values('2P', ascending=False)

    # 前20名球员名字
    playerMaxName = playerByPTS.iloc[0:20, 1]
    # 投进两分球最多的前二十名
    playerMaxTwoScored = playerByPTS.iloc[0:20, 14]
    # 出手数
    playerMaxTwoAttempt = playerByPTS.iloc[0:20, 15]
    # 投篮命中率
    playerMaxPercentage = playerByPTS.iloc[0:20, 16]

    listPlayerName = []
    for data in playerMaxName:
        listPlayerName.append(data.split('.')[0])

    listName = []
    for data in listPlayerName:
        name = data.split("*")[0]
        listName.append(name)

    x_data = list(playerMaxTwoScored)  # x数据
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
            title_opts=opts.TitleOpts(title="本赛季两分命中数前20名的两分命中率与两分投中数比较"),
            # x轴配置
            xaxis_opts=opts.AxisOpts(
                name='两分投中数',
                name_location='center',
                # 坐标轴类型 'value': 数值轴
                type_="value",
                is_inverse=False,
                max_=x_data[0] + 5,
                min_=x_data[len(x_data) - 1] - 5,
                split_number=5
            ),
            # y轴配置
            yaxis_opts=opts.AxisOpts(
                name='两分命中率',
                # 坐标轴类型 'value': 数值轴
                name_location='center',
                name_gap=30,
                type_="value",
                is_inverse=False,
                # 最小值
                min_=round(float(y_data[len(y_data) - 1]) - 0.2, 2),
            ),
            # 提示框配置项
            tooltip_opts=opts.TooltipOpts(formatter=JsCode(
                # 构造回调函数
                "function (params) {return '命中数:'+ params.value[0] + "
                "' 出手数:' + params.value[4] +' 命中率' + params.value[1];}"
            ))
        )
            .render("html/twoPointScatter.html")

    )
    return c


if __name__ == '__main__':
    twoPointScatter()
