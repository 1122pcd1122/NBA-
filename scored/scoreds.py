import pandas as pd

from pyecharts.charts import Bar
from pyecharts import options as opts


# 得分榜
def scored():
    player = pd.read_csv('player.csv')

    # 得分榜降序排行
    playerByPTS = player.sort_values('PTS', ascending=False)

    # 前20名球员名字
    playerMaxName = playerByPTS.iloc[0:20, 1]
    playerMaxScored = playerByPTS.iloc[0:20, 29]

    listPlayerMaxName = list(playerMaxName)
    listName = []
    for data in listPlayerMaxName:
        name = data.split("*")[0]
        listName.append(name)

    bar = Bar(init_opts=opts.InitOpts(width="1200px", height="900px"))
    bar.add_xaxis(xaxis_data=listName)
    bar.add_yaxis(series_name="总得分", y_axis=list(playerMaxScored))

    bar.set_global_opts(
        title_opts=opts.TitleOpts(title="本赛季得分榜前二十名", subtitle="根据得分排名"),
        xaxis_opts=opts.AxisOpts(
            name="总得分",
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
    bar.render("scored/html/scored.html")
    return bar


if __name__ == '__main__':
    scored()
