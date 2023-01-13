from pyecharts.charts import Tab, Line, Grid
from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts
from pyecharts.options import global_options as opts
from db import mysql


def rankTable(records, title, fileStr):
    listRecord = records

    rows = []
    for data in listRecord:
        row = []
        record = mysql.queryNameByReferred(data.referred)
        row.append(record)
        row.append(data.division)
        row.append(data.won)
        row.append(data.lost)
        row.append(data.division_rank)
        row.append(data.winRate)

        rows.append(row)

    header = ['球队名称', '分区', '胜场', '败场', '分区排名', '胜率']

    table = Table()

    table.add(header, rows)
    table.set_global_opts(title_opts=ComponentTitleOpts(title=title, subtitle="根据胜率排名"))
    table.render(fileStr)
    return table


def winRateLine(records, title, fileStr):
    listRecord = records

    x_name = []
    for data in listRecord:
        x_name.append(mysql.queryNameByReferred(data.referred))

    print(x_name)

    y_winRate = []
    for data in listRecord:
        rate = round(data.won / (data.won + data.lost), 2)
        y_winRate.append(rate)

    print(y_winRate)

    line = Line(init_opts=opts.InitOpts(width="800px", height="400px"))
    line.set_global_opts(
        title_opts=opts.TitleOpts(title=title),
        tooltip_opts=opts.TooltipOpts(is_show=False),
        xaxis_opts=opts.AxisOpts(axislabel_opts={"rotate": 30}),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
    line.add_xaxis(xaxis_data=x_name)
    line.add_yaxis(series_name="", y_axis=y_winRate)
    line.render(fileStr)


if __name__ == '__main__':
    # tab = Tab()
    #
    # tab.add(rankTable(mysql.queryWestRecord(), "西部球队", "html/rankWest.html"), "西部球队")
    # tab.add(rankTable(mysql.queryEastRecord(), "东部球队", "html/rankEast.html"), "东部球队")
    # tab.render("html/rank_tab.html")
    gird = Grid()
    gird.add(rankTable(mysql.queryAllRecord(), "所有球队", "html/rankAllTeam.html"),grid_opts=opts.GridOpts(pos_left="55%"))
    gird.add(rankTable(mysql.queryAllRecord(), "所有球队", "html/rankAllTeam.html"),
             grid_opts=opts.GridOpts(pos_left="55%"))
    gird.render()