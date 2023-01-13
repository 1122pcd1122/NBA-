import pandas as pd

from pyecharts.charts import Bar
from pyecharts import options as opts


# 三分投中数
def threePoint():
    player = pd.read_csv('../player.csv')

    # 三分投中数降序
    playerByPTS = player.sort_values('3P', ascending=False)[0:20]
    print(playerByPTS)

    # 前20名球员名字
    playerMaxName = playerByPTS.iloc[0:20, 1]
    # 投进三分球最多的前二十名
    playerMaxThreeScored = playerByPTS.iloc[0:20, 11]

    listPlayerMaxName = []

    for data in playerMaxName:
        listPlayerMaxName.append(data.split('.')[0])

    listName = []
    for data in listPlayerMaxName:
        name = data.split("*")[0]
        listName.append(name)

    bar = Bar(init_opts=opts.InitOpts(width="1200px", height="900px"))
    bar.add_xaxis(xaxis_data=listName)
    bar.add_yaxis(series_name="投中数", y_axis=list(playerMaxThreeScored))

    bar.set_global_opts(
        title_opts=opts.TitleOpts(title="本赛季三分球投中数前二十名", subtitle="根据投中数排名"),
        xaxis_opts=opts.AxisOpts(
            name="总投进数",
            name_textstyle_opts=opts.TextStyleOpts(font_size=12),
        ),
        yaxis_opts=opts.AxisOpts(
            name="球员",
            name_location='start',
            is_inverse=True,
            name_textstyle_opts=opts.TextStyleOpts(font_size=12),
            axislabel_opts={"rotate": 45}
        ),
    )
    bar.set_series_opts(label_opts=opts.LabelOpts(position="right", is_show=True))
    bar.reversal_axis()
    bar.render("html/threePoint.html")
    return bar


if __name__ == '__main__':
    threePoint()
