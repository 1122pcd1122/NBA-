from pyecharts.charts import Bar
from pyecharts import options as opts
from db import mysql


def eastWinRate():
    listEastRecord = mysql.queryEastRecord()
    for data in listEastRecord:
        print(data.winRate)

    listName = []
    for data in listEastRecord:
        record = mysql.queryNameByReferred(data.referred)
        listName.append(record.name)

    listWinRate = []
    for data in listEastRecord:
        listWinRate.append(data.winRate)

    bar = Bar(init_opts=opts.InitOpts(width="1200px", height="1000px"))
    bar.add_xaxis(xaxis_data=listName)
    bar.add_yaxis(series_name="球队胜率", y_axis=listWinRate)

    bar.set_global_opts(
        title_opts=opts.TitleOpts(title="东部球队排名", subtitle="根据胜率排名", pos_left='left', ),
        xaxis_opts=opts.AxisOpts(
            name="球队胜率",
            name_textstyle_opts=opts.TextStyleOpts(font_size=12),
        ),
        yaxis_opts=opts.AxisOpts(
            name="球队名称",
            is_inverse=True,
            name_textstyle_opts=opts.TextStyleOpts(font_size=12),
            axislabel_opts={"rotate": 48}
        ),
        # 设置图例
        legend_opts=opts.LegendOpts(
            is_show=True,  # 展示图例
            pos_left='center',  # 位置 --居中
        )
    )
    bar.set_series_opts(label_opts=opts.LabelOpts(position="right", is_show=True))
    bar.reversal_axis()
    bar.render("html/eastWinRate.html")

    return bar