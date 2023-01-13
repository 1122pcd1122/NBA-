from pyecharts.commons.utils import JsCode

from pyecharts.charts import Scatter, Page
from pyecharts import options as opts

from db import mysql as db


def efficiency():
    listTeamData = db.queryAllTeamData()
    # 进攻效率
    listOffRtg = []
    for data in listTeamData:
        listOffRtg.append(data.off_rtg)

    # 防守效率
    listDefRtg = []
    for data in listTeamData:
        listDefRtg.append(data.def_rtg)

    # 球队名称
    listTeamName = []
    for data in listTeamData:
        listTeamName.append(data.name)

    print("所有球队进攻效率值")
    # list.sort(listOffRtg, reverse=True)
    print(listOffRtg)

    print("所有球队防守效率值")
    # listDefRtg = sorted(listDefRtg, reverse=False)
    print(listDefRtg)

    print("球队防守效率排序后:")
    sortListDefRtg = sorted(listDefRtg, reverse=False)
    print(sortListDefRtg)
    print("球队进攻效率排序后:")
    sortListOffRtg = sorted(listOffRtg, reverse=False)
    print(sortListOffRtg)

    x_data = listOffRtg  # x数据
    y_data = listDefRtg  # y数据
    c = (
        # 散点图
        # 初始化
        Scatter(init_opts=opts.InitOpts(width='1200px', height='600px'))
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(
            # 系列名称
            series_name="",
            # 系列数据
            y_axis=[list(z) for z in zip(y_data, x_data, listTeamName)],
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
            title_opts=opts.TitleOpts(title="本赛季所有球队进攻效率与防守效率散点图", subtitle="进攻效率越大越好,防守效率越小越好"),
            # x轴配置
            xaxis_opts=opts.AxisOpts(
                name='进攻效率',
                name_location='center',
                name_gap=30,
                # 坐标轴类型 'value': 数值轴
                type_="value",
                is_inverse=False,
                min_=sortListOffRtg[0] - 1,
                max_=sortListOffRtg[len(sortListOffRtg) - 1] + 1
            ),
            # y轴配置
            yaxis_opts=opts.AxisOpts(
                name='防守效率',
                # 坐标轴类型 'value': 数值轴
                name_location='center',
                name_gap=30,
                type_="value",
                is_inverse=True,
                # 最小值
                min_=sortListDefRtg[0] - 1,
                max_=sortListDefRtg[len(sortListDefRtg) - 1] + 1
            ),
            # 提示框配置项
            tooltip_opts=opts.TooltipOpts(formatter=JsCode(
                # 构造回调函数
                "function (params) {return '进攻效率'+ params.value[0] + ' : 防守效率' + params.value[1];}"
            ))
        )
    )

    c.render('html/allEfficiency.html')
    return c


if __name__ == '__main__':
    efficiency()
