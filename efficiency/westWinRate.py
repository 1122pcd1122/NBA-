from pyecharts.charts import Bar
from pyecharts import options as opts
from db import mysql


def westWinRate():
    listWestRecord = mysql.queryWestRecord()
    for data in listWestRecord:
        print(data.winRate)

    listName = []
    for data in listWestRecord:
        record = mysql.queryNameByReferred(data.referred)
        listName.append(record.name)

    listWinRate = []
    for data in listWestRecord:
        listWinRate.append(data.winRate)

    bar = Bar(init_opts=opts.InitOpts(width="1200px", height="1000px"))
    bar.add_xaxis(xaxis_data=listName)
    bar.add_yaxis(series_name="球队胜率", y_axis=listWinRate)

    bar.set_global_opts(
        title_opts=opts.TitleOpts(title="西部球队排名", subtitle="根据胜率排名"),
        xaxis_opts=opts.AxisOpts(
            name="球队胜率",
            name_textstyle_opts=opts.TextStyleOpts(font_size=12),
        ),
        yaxis_opts=opts.AxisOpts(
            name="球队名称",
            is_inverse=True,
            name_textstyle_opts=opts.TextStyleOpts(font_size=12),
            axislabel_opts={"rotate": 48}
        )
    )
    bar.set_series_opts(label_opts=opts.LabelOpts(position="right", is_show=True))
    bar.reversal_axis()
    bar.render("html/westWinRate.html")

    return bar
