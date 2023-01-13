import pandas as pd

from pyecharts.charts import Bar
from pyecharts import options as opts


# 投篮命中率
def scoredPercentage():
    player = pd.read_csv('player.csv')

    # 得分榜降序排行
    playerByPTS = player.sort_values('PTS', ascending=False).iloc[0:20]
    playerByPTS = playerByPTS.sort_values('eFG%', ascending=False)
    print(playerByPTS)

    # 前20名球员名字
    playerMaxTwenty = playerByPTS.iloc[0:20, [1, 17]]
    playerMaxTwoName = playerMaxTwenty.iloc[0:20, 0]
    # 两分钱命中率
    playerMaxTwpPercentage = playerMaxTwenty.iloc[0:20, 1]

    listPlayerName = list(playerMaxTwoName)
    listName = []
    for data in listPlayerName:
        name = data.split("*")[0]
        listName.append(name)

    bar = Bar(init_opts=opts.InitOpts(width="1200px", height="900px"))
    bar.add_xaxis(xaxis_data=listName)
    bar.add_yaxis(series_name="真实命中率", y_axis=list(playerMaxTwpPercentage))

    bar.set_global_opts(
        title_opts=opts.TitleOpts(title="本赛季投篮前二十名的真实命中率"),
        xaxis_opts=opts.AxisOpts(
            name="命中率",
            name_textstyle_opts=opts.TextStyleOpts(font_size=12),
        ),
        yaxis_opts=opts.AxisOpts(
            name="球员",
            name_location='start',
            is_inverse=True,
            name_textstyle_opts=opts.TextStyleOpts(font_size=12),
            axislabel_opts={"rotate": 30}
        ),
    )
    bar.set_series_opts(label_opts=opts.LabelOpts(position="right", is_show=True))
    bar.reversal_axis()
    bar.render(path="scored/html/scoredPercentage.html")
    return bar


if __name__ == '__main__':
    scoredPercentage()
