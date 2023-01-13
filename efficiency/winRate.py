from pyecharts.charts import Bar
from pyecharts import options as opts
from db import mysql


def winRate():
    listRecord = mysql.queryAllRecord()

    # 球队名
    listName = []
    for data in listRecord:
        record = mysql.queryNameByReferred(data.referred)
        listName.append(record.name)

    # 胜率
    listWinRate = []
    for data in listRecord:
        listWinRate.append(data.winRate)

    print(listWinRate)

    # 排名
    listAllRank = []
    rank = 1
    for data in listRecord:
        listAllRank.append(rank)
        rank = rank + 1
    rank = 0

    # 场次
    listSessions = []
    for data in listRecord:
        listSessions.append(data.won + data.lost)

    bar = Bar(init_opts=opts.InitOpts(width="1300px", height="1100px"))
    bar.add_xaxis(xaxis_data=listName)
    bar.add_yaxis(series_name="球队胜率", y_axis=listWinRate)

    bar.set_global_opts(
        title_opts=opts.TitleOpts(title="联盟所有球队排名", subtitle="根据胜率排名"),
        xaxis_opts=opts.AxisOpts(
            name="球队胜率",
            name_textstyle_opts=opts.TextStyleOpts(font_size=12),
        ),
        yaxis_opts=opts.AxisOpts(
            name="球队名称",
            is_inverse=True,
            name_textstyle_opts=opts.TextStyleOpts(font_size=12),
            axislabel_opts={"rotate": 45}
        )
    )
    bar.set_series_opts(label_opts=opts.LabelOpts(position="right", is_show=True))
    bar.reversal_axis()
    bar.render("html/winRate.html")
    return bar