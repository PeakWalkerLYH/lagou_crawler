#! /usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 绘出散点图
def draw_scatter(x, y, name):
    # 获取月薪最大值
    max_value = max(x)
    # 获取规模，即公司人数的最大值
    max_people = max(y)
    # 图片大小
    plt.figure(figsize=(12., 9))
    # 图片标题
    plt.title(f'{name}', fontsize=25)
    # 绘制散点图
    plt.scatter(x, y, color='r', alpha=0.1, linewidths=15)
    # x轴标签
    plt.xlabel("月薪 / 千", fontsize=20)
    # y轴标签
    plt.ylabel("人数 / 个", fontsize=20)
    # x轴刻度
    plt.xticks(np.arange(0, max_value + 1, 2), fontsize=20, rotation=-30)
    # y轴刻度
    plt.yticks(np.arange(0, max_people + 1, 125), fontsize=20)
    # 显示图片网格
    plt.grid()
    # 保存图像到指定路径
    plt.savefig(f'./1.scatter/{name}.png')
    # 显示图片
    plt.show()

# 绘出柱状图
def draw_bar(x, y, name):
    # 柱状图的颜色
    list_color = ['r', 'b', 'm', 'g', 'y', 'c']
    # 图片大小
    plt.figure(figsize=(12, 9))
    # 图片标题
    plt.title("公司对学历要求状况", fontsize=25)
    # 获取学历要求数量的最大值
    max_study = max(y)
    # 遍历每一根条形图柱子
    length = len(x)
    for i in range(length):
        plt.bar(x[i], y[i], color=list_color[i], width=0.4, edgecolor='k', hatch='\\', alpha=0.5, joinstyle='round',
                linewidth=3)
    # x轴标签
    plt.xlabel("学历", fontsize=20)
    # y轴标签
    plt.ylabel("数量 / 个", fontsize=20)
    # x轴刻度
    plt.xticks(fontsize=20)
    # y轴刻度
    plt.yticks(np.arange(0, max_study + 1, 10), fontsize=20)
    # 显示图片网格
    plt.grid()
    # 保存图像到指定路径
    plt.savefig(f'./2.bar/{name}.png')
    # 显示图片
    plt.show()

# 散点图
def scatter_views(df):
    # 获取最低薪资
    lowest_salary = df['工资'].str.replace("k","").str.split("-").str[0].astype('int')
    # 获取最高薪资
    highest_salary = df['工资'].str.replace("k","").str.split("-").str[1].astype('int')
    # 将类似于2000人以上、1000-2000人、低于500人这样的格式转换成XXX-XXX的格式
    def avg_p(x):
        if "-" in x:
            value1 = x.split("-")[0]
            value2 = x.split("-")[1]
            value = (int(value1)+int(value2))/2
        elif "少于" in x:
            value = int(x.split("于")[1])
        elif "以上" in x:
            value = int(x.split("以")[0])

        return value
    # 保存薪资格式转换后的数据
    avg_people = df['规模'].str.replace("人", "").apply(avg_p)
    # 最低薪资转换成列表
    x1 = lowest_salary.tolist()
    # 最高薪资转换成列表
    x2 = highest_salary.tolist()
    # 公司规模
    y = avg_people
    # 标题名字
    flag = ["最低薪资与公司人数关系", "最高薪资与公司人数关系"]
    # 调用绘制散点图函数
    draw_scatter(x1, y, flag[0])
    # 调用绘制散点图函数
    draw_scatter(x2, y, flag[1])

# 柱状图
def bar_views(df):
    # 不同学历要求的名称
    x = df['学历'].value_counts().index.tolist()
    # 不同学历要求的数量
    y = df['学历'].value_counts().tolist()
    # 标题名字
    name = '公司学历要求'
    # 调用柱状图函数
    draw_bar(x, y, name)


def main(name):
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
    # 读取数据
    df = pd.read_csv(f"./datas/{name}.xlsx", header=None)
    df.columns = ['城市', '公司', '规模', '学历', '岗位', '工资', '经验']
    # 薪资与公司规模的关系
    scatter_views(df)
    # 调用柱状图函数
    bar_views(df)


if __name__ == '__main__':
    print("提示：", "输入datas文件夹下的文件名，不带文件后缀")
    name = input('请输入文件名：')
    main(name)
