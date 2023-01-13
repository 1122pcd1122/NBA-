import pandas as pd

from pyecharts.charts import Bar
from pyecharts import options as opts


# 两分投中数排行榜
def twoPoint():
    player = pd.read_csv('../player.csv')

    # 两分榜降序排行
    playerByPTS = player.sort_values('2P', ascending=False)

    # 前20名球员名字
    playerMaxName = playerByPTS.iloc[0:20, 1]
    # 投进两分球最多的前二十名
    playerMaxTwoScored = playerByPTS.iloc[0:20, 14]

    listPlayerName = []
    for data in playerMaxName:
        listPlayerName.append(data.split('.')[0])

    listName = []
    for data in listPlayerName:
        name = data.split("*")[0]
        listName.append(name)

    bar = Bar(init_opts=opts.InitOpts(width="1200px", height="900px"))
    bar.add_xaxis(xaxis_data=listName)
    bar.add_yaxis(series_name="总得分", y_axis=list(playerMaxTwoScored))

    bar.set_global_opts(
        title_opts=opts.TitleOpts(title="本赛季两分球投中数前二十名", subtitle="根据投中数排名"),
        xaxis_opts=opts.AxisOpts(
            name="总投进数",
            name_textstyle_opts=opts.TextStyleOpts(font_size=12),
        ),
        yaxis_opts=opts.AxisOpts(
            name="球员",
            name_location='start',
            is_inverse=True,
            name_textstyle_opts=opts.TextStyleOpts(font_size=12),
            axislabel_opts={"rotate": 48}
        ),
    )
    bar.set_series_opts(label_opts=opts.LabelOpts(position="right", is_show=True))
    bar.reversal_axis()
    bar.render("html/twoPoint.html")
    return bar


if __name__ == '__main__':
    twoPoint()
