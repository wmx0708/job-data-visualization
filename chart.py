import re
import numpy as np
import pandas as pd
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType
from pyecharts.charts import Pie, Bar, WordCloud, Page, Geo, Line, Grid, Liquid, Bar3D, Gauge
import jieba

job = pd.read_excel("job_clean.xlsx")
company = pd.read_excel("company_clean.xlsx")
# 岗位：关键字词云
# 薪资：平均薪资前十，总体薪资占比
# 学历：公司学历要求，总体学历占比,学历平均薪资，
# 地区：各城市职位数量占比
# 公司：公司薪资，公司标签，公司地区，公司经验

# ==============================地区=====================================
# city_count = {}  # 各城市职位数量占比
# for i in set(job["地区"]):
#     city_count[i] = list(job["地区"]).count(i)
# city_count = sorted(city_count.items(), key=lambda x: x[1], reverse=True)
# city_count.remove(("美国",2))
# city_count.remove(("日本",2))
# city_count.remove(("雄安",1))
# city_count.remove(("印度",1))
# city_count.remove(("不限",1))
# print(city_count)
# bar_city = (
#     Bar(opts.InitOpts(width='900px', height='500px',))  # 图片的大小，及主题风格
#         .add_xaxis([i[0] for i in reversed(city_count[0:10])])
#         .add_yaxis("", [i[1] for i in reversed(city_count[0:10])])
#         .reversal_axis()
#         .set_series_opts(label_opts=opts.LabelOpts(position="right"))  # 提示的位置
#         .set_global_opts(
#         title_opts=opts.TitleOpts(title="招聘岗位数量城市排名TOP10"),
#         visualmap_opts=opts.VisualMapOpts(is_show=False,type_="color", max_=1000,range_color=['#007799','#007799']),
#         xaxis_opts=opts.AxisOpts(
#             name='岗位数',
#             name_location='middle',
#             name_gap=35,
#             name_textstyle_opts=opts.TextStyleOpts(
#                 font_family='Times New Roman',
#                 font_size=14,
#                 color='black',
#             )
#         ),
#         yaxis_opts=opts.AxisOpts(
#             name='城市',
#             name_location='middle',  # 在轴上面所处的位置
#             name_gap=50,  # 调整距离
#             name_textstyle_opts=opts.TextStyleOpts(
#                 font_family='Times New Roman',
#                 font_size=14,
#                 color='black',
#                 #                     font_weight='bolder',
#             )
#         )
#     )
# )
# bar_city.chart_id="bar_city"
#
# word_city = (
#     WordCloud()
#         .add("城市职位数量词云图", city_count))
# word_city.chart_id="word_city"
#
# geo_city = (
#     Geo()
#     .add_schema(maptype="china")
#     .add("geo", city_count)
#     .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#     .set_global_opts(
#         visualmap_opts=opts.VisualMapOpts(),
#         title_opts=opts.TitleOpts(title="城市互联网岗位数量分配")
#     )
# )
# geo_city.chart_id="geo_city"
#
# page_city = (
#     Page(layout=Page.DraggablePageLayout, page_title="城市分布")
#         .add(bar_city)
#         .add(word_city)
#         .add(geo_city)
# ).render("page/page_city.html")
# Page.save_resize_html("page/page_city.html", cfg_file="json/city.json", dest="page/city.html")

# ===================================薪酬=========================================
# salary_count = {}  # 各职位薪酬
# for i in set(job["薪酬"]):
#     salary_count[i] = list(job["薪酬"]).count(i)
# salary_count.pop("3k")
# salary_count.pop("40k")
# salary_count["<=10k"] += 1
# salary_count["30k-40k"] += 2
# salary_count = sorted(salary_count.items(), key=lambda x: x[1], reverse=True)
# print(salary_count)
# rose_salary = (
#     Pie()
#     .add(
#         "",
#         salary_count,
#         radius=["30%", "75%"],
#         center=["50%", "50%"],
#         rosetype="radius",
#         label_opts=opts.LabelOpts(is_show=False),
#     )
#     #.set_global_opts(title_opts=opts.TitleOpts(title="Pie-玫瑰图示例"))
#     .set_global_opts(legend_opts=opts.LegendOpts(orient="vertical",pos_left=0,pos_top=0))
#     .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
# )
# rose_salary.chart_id="rose_salary"
#
# # 寻找平均薪资较高的方向
# job_s = pd.read_excel("job_clean1.xlsx")
# salary_sum = {}
# key_sum = {}
# for i in set(job_s["关键词"]):
#     salary_sum[i] = 0
#     key_sum[i] = 0
#     for j in range(len(job_s)):
#         if job_s["关键词"][j] == i and "-" in job_s["薪酬"][j]:
#             salary_sum[i] += int(job_s["薪酬"][j].split("-")[0])
#             key_sum[i] += 1
#     if key_sum[i] != 0:
#         salary_sum[i] = round(salary_sum[i] / key_sum[i], 2)
#     else:
#         salary_sum[i] = 0
# salary_sum = sorted(salary_sum.items(), key=lambda x: x[1], reverse=True)
# print(salary_sum)
#
# bar_salarytop10= (
#     Bar(opts.InitOpts(width='900px', height='500px'))  # 图片的大小，及主题风格
#         .add_xaxis([i[0] for i in salary_sum[0:10]])
#         .add_yaxis("", [i[1] for i in salary_sum[0:10]])
#         .set_series_opts(label_opts=opts.LabelOpts(position="top"))  # 提示的位置
#         .set_global_opts(
#         #title_opts=opts.TitleOpts(title="互联网薪资TOP10职位"),
#             visualmap_opts=opts.VisualMapOpts(is_show=False,type_="color", max_=35,min_=23,range_color=['#EEEE00','#CC0000']),
#         xaxis_opts=opts.AxisOpts(
#             name='关键词',
#             name_location='middle',
#             name_gap=35,
#             name_textstyle_opts=opts.TextStyleOpts(
#                 font_family='Times New Roman',
#                 font_size=18,
#                 color='black',
#             ),
#             axislabel_opts=opts.LabelOpts(rotate=+30),
#         ),
#         yaxis_opts=opts.AxisOpts(
#             name='薪资（k）',
#             name_location='middle',  # 在轴上面所处的位置
#             name_gap=35,  # 调整距离
#             name_textstyle_opts=opts.TextStyleOpts(
#                 font_family='Times New Roman',
#                 font_size=18,
#                 color='black',
#             )
#         )
#     )
# )
# bar_salarytop10.chart_id="bar_salarytop10"
#
# #各地区平均薪资折线
# salary_area = {}
# area_sum = {}
# for i in set(job_s["地区"]):
#     salary_area[i] = 0
#     area_sum[i] = 0
#     for j in range(len(job)):
#         if job_s["地区"][j] == i and "-" in job_s["薪酬"][j]:
#             salary_area[i] =salary_area[i]+ int(job_s["薪酬"][j].split("-")[0])
#             area_sum[i] += 1
#     if area_sum[i] != 0:
#         salary_area[i] = round(salary_area[i] / area_sum[i], 2)
#     else:
#         salary_area[i] = 0
# del(salary_area["不限"])
# del(salary_area["美国"])
# del(salary_area["印度"])
# del(salary_area["日本"])
# salary_area = sorted(salary_area.items(), key=lambda x: x[1], reverse=True)
# print(salary_area)
# line_salary = (
#     Line()
#     .add_xaxis([i[0] for i in salary_area[0:10]])
#     .add_yaxis("",[i[1] for i in salary_area[0:10]])
#     .set_global_opts(
#         xaxis_opts=opts.AxisOpts(
#             name='城市',
#             name_location='middle',
#             name_gap=35,
#             name_textstyle_opts=opts.TextStyleOpts(
#                 font_family='Times New Roman',
#                 font_size=18,
#                 color='black',
#             ),
#         ),
#         yaxis_opts=opts.AxisOpts(
#             name='薪资（k）',
#             name_location='middle',  # 在轴上面所处的位置
#             name_gap=35,  # 调整距离
#             name_textstyle_opts=opts.TextStyleOpts(
#                 font_family='Times New Roman',
#                 font_size=18,
#                 color='black',
#             )
#         )
#     )
#     #.set_global_opts(title_opts=opts.TitleOpts(title="地区薪资折线图"))
# )
# line_salary.chart_id="line_salary"
#
# #薪资职位词云
# salary_job = {}
# job_sum = {}
# for i in set(job_s["岗位名称"]):
#     salary_job[i] = 0
#     job_sum[i] = 0
#     for j in range(len(job)):
#         if job_s["岗位名称"][j] == i and "-" in job_s["薪酬"][j]:
#             salary_job[i] += int(job_s["薪酬"][j].split("-")[0])
#             job_sum[i] += 1
#     if job_sum[i]!=0:
#         salary_job[i] = round(salary_job[i] / job_sum[i], 2)
#     else:
#         salary_job[i] = 0
# salary_job = sorted(salary_job.items(), key=lambda x: x[1], reverse=True)
# print(salary_job)
# word_salary = (
#     WordCloud()
#         .add("互联网岗位薪资词云", salary_job))
# word_salary.chart_id="word_salary"
#
# page_salary = (
#     Page(layout=Page.DraggablePageLayout, page_title="薪资水平")
#         .add(rose_salary)
#         .add(bar_salarytop10)
#         .add(word_salary)
#         .add(line_salary)
# ).render("page/page_salary.html")
# Page.save_resize_html("page/page_salary.html", cfg_file="json/salary.json", dest="page/salary.html")

# ====================================学历========================================
# 总体学历百分比统计
# edu_count = {}  # 各学历职位数量占比
# for i in set(job["学历"]):
#     edu_count[i] = list(job["学历"]).count(i)
# edu_count.pop("本科")
# edu_count["本科及以上"] += 1
# for i in edu_count:
#     edu_count[i] = round(edu_count[i] / len(job["学历"]), 4)
# edu_count = sorted(edu_count.items(), key=lambda x: x[1], reverse=True)
# print(edu_count)
# lq = []
# name = []
# color = [["#FF0000", "#FF8800", "#E63F00"], ["#FFBB00", "#FFDD55", "#DDAA00"],
#          ["#77FF00", "#CCFF99", "#55AA00"], ["#00DDDD", "#AAFFEE", "#00AAAA"],
#          ["#5500FF", "#99BBFF", "#2200AA"], ["#A500CC", "#D1BBFF", "#7A0099"]]
# # center = [["33.3%", "16.67%"], ["66.7%", "16.67%"], ["16.67%", "50%"], ["83.33%", "50%"], ["33.3%", "83.33%"],
# #           ["66.7%", "83.33%"]]
# # lq_edu = Grid(init_opts=opts.InitOpts(height="500px", width="500px"))
# for i in range(6):
#     lq.append(
#         Liquid()
#             .add("lq", [edu_count[i][1]],
#                  color=[color[i][0]], background_color=color[i][1],
#                  outline_itemstyle_opts={"color": color[i][2]},
#                  is_outline_show=False,
#                  label_opts=opts.LabelOpts(font_size=20, color=color[i][2], position="inside"),
#                  )
#             .set_global_opts(title_opts=opts.TitleOpts(title=edu_count[i][0],
#                                                        pos_left="center", pos_bottom="0%",
#                                                        title_textstyle_opts=opts.TextStyleOpts(font_size=20,
#                                                                                                color="#666666")))
#     )
#     lq[i].chart_id = "lq%d" % i
#     # lq[i].render("%d.html" % i)
#
# #     lq_edu = lq_edu.add(lq[i], grid_opts=opts.GridOpts(pos_left=center[i][0],pos_top=center[i][1]))
# # lq_edu.render("a.html")
#
# # 大厂学历要求统计
# company_edu = {}
# for i in set(company["关键词"]):
#     company_edu[i[0:2]] = {}
#     for j in set(company["学历"]):
#         company_edu[i[0:2]][j] = 0
#
# for i in set(company["关键词"]):
#     for j in range(len(company["学历"])):
#         if company["关键词"][j] == i:
#             company_edu[i[0:2]][company["学历"][j]] += 1
#
# for i in set(company["关键词"]):
#     for j in set(company["学历"]):
#         if company_edu[i[0:2]][j] == 0:
#             del (company_edu[i[0:2]][j])
# for i in set(company["关键词"]):
#     company_edu[i[0:2]] = [list(z) for z in zip(company_edu[i[0:2]].keys(), company_edu[i[0:2]].values())]
# print(company_edu)
#
# pos = [["23.3", "24"], ["48.3", "24"], ["73.3", "24"], ["23.3", "49"], ["48.3", "49"], ["73.3", "49"], ["23.3", "74"],
#        ["48.3", "74"], ["73.3", "74"]]
# name = ["百度", "华为", "腾讯", "阿里", "字节", "京东", "小米", "寻梦", "美团"]
#
#
# def graphic(pos, index):
#     return opts.GraphicGroup(
#         graphic_item=opts.GraphicItem(left=f'{pos[0]}%', top=f'{pos[1]}%'),
#         children=[
#             opts.GraphicText(
#                 graphic_textstyle_opts=opts.GraphicTextStyleOpts(
#                     text=name[index],
#                     font=f"bold 15px Microsoft YaHei",
#                     graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
#                         fill="#666666"
#                     ),
#                 ),
#             )
#         ],
#     )
#
#
# graphic_list = [graphic(pos[i], i) for i in range(len(pos))]
# pie_edu = (
#     Pie(init_opts=opts.InitOpts(theme=ThemeType.WALDEN))
#         .add(
#         "百度",
#         company_edu["百度"],
#         center=["25%", "25%"],
#         radius=[30, 40],
#         label_opts=opts.LabelOpts(is_show=False),
#     )
#         .add(
#         "华为",
#         company_edu["华为"],
#         center=["50%", "25%"],
#         radius=[30, 40],
#         label_opts=opts.LabelOpts(is_show=False),
#     )
#         .add(
#         "腾讯",
#         company_edu["腾讯"],
#         center=["75%", "25%"],
#         radius=[30, 40],
#         label_opts=opts.LabelOpts(is_show=False),
#     )
#         .add(
#         "阿里",
#         company_edu["阿里"],
#         center=["25%", "50%"],
#         radius=[30, 40],
#         label_opts=opts.LabelOpts(is_show=False),
#     )
#         .add(
#         "字节",
#         company_edu["字节"],
#         center=["50%", "50%"],
#         radius=[30, 40],
#         label_opts=opts.LabelOpts(is_show=False),
#     )
#         .add(
#         "京东",
#         company_edu["京东"],
#         center=["75%", "50%"],
#         radius=[30, 40],
#         label_opts=opts.LabelOpts(is_show=False),
#     )
#         .add(
#         "小米",
#         company_edu["小米"],
#         center=["25%", "75%"],
#         radius=[30, 40],
#         label_opts=opts.LabelOpts(is_show=False),
#     )
#         .add(
#         "寻梦",
#         company_edu["寻梦"],
#         center=["50%", "75%"],
#         radius=[30, 40],
#         label_opts=opts.LabelOpts(is_show=False),
#     )
#         .add(
#         "美团",
#         company_edu["美团"],
#         center=["75%", "75%"],
#         radius=[30, 40],
#         label_opts=opts.LabelOpts(is_show=False),
#     )
#         .set_global_opts(
#         title_opts=opts.TitleOpts(title="大厂学历要求统计"),
#         legend_opts=opts.LegendOpts(
#             type_="scroll", pos_top="20%", pos_left=0, orient="vertical",
#             textstyle_opts=opts.TextStyleOpts(color="black")
#         ),
#         # graphic_opts=opts.GraphicText(graphic_item=opts.GraphicItem(left="23.3%",top="24%"),
#         #                               graphic_textstyle_opts=opts.GraphicTextStyleOpts(
#         #                                   text="百度",
#         #                               font='16px "Microsoft YaHei"')),
#         graphic_opts=graphic_list,
#     )
# )
# pie_edu.chart_id = "pie_edu"
#
# # 学历薪资职位数
# for i in range(len(job["学历"])):
#     if job["学历"][i] == "本科":
#         job.replace("本科", "本科及以上",inplace=True)
# edu_sal = {(i, j): 0 for i in set(job["学历"]) for j in set(job["薪酬"])}
# print(edu_sal)
# for i in set(job["学历"]):
#     for j in set(job["薪酬"]):
#         for k in range(len(job)):
#             if job["学历"][k] == i and job["薪酬"][k] == j:
#                 edu_sal[(i, j)] += 1
# print(sorted(edu_sal.items(), key=lambda x: x[1], reverse=True))
# edu_sal = [[list(edu_sal.keys())[i][0], list(edu_sal.keys())[i][1], list(edu_sal.values())[i]] for i in
#            range(len(edu_sal))]
# print(edu_sal)
# bar3D_edu_sal = (
#     Bar3D()
#         .add(
#         "",
#         edu_sal,
#         xaxis3d_opts=opts.Axis3DOpts(np.array(edu_sal)[:, 0], type_="category"),
#         yaxis3d_opts=opts.Axis3DOpts(np.array(edu_sal)[:, 1], type_="category"),
#         zaxis3d_opts=opts.Axis3DOpts(type_="value"),
#     )
#         .set_global_opts(
#         visualmap_opts=opts.VisualMapOpts(max_=500, is_show=False),
#         title_opts=opts.TitleOpts(title="学历薪酬职位数量统计"),
#     )
# )
# bar3D_edu_sal.chart_id = "bar3D_edu_sal"
#
# page_education = (
#     Page(layout=Page.DraggablePageLayout, page_title="学历要求")
#         .add(pie_edu)
#         .add(lq[0])
#         .add(lq[1])
#         .add(lq[2])
#         .add(lq[3])
#         .add(lq[4])
#         .add(lq[5])
#         .add(bar3D_edu_sal)
# ).render("page/page_education.html")
# Page.save_resize_html("page/page_education.html", cfg_file="json/education.json", dest="page/education.html")

# =================================经验===========================================
#
# exp_count = {}  # 各职位工作经验
# for i in set(job["工作经验"]):
#     exp_count[i]=list(job["工作经验"]).count(i)
#     #exp_count[i] = round(list(job["工作经验"]).count(i) / job["工作经验"].shape[0], 2)
# exp_count = sorted(exp_count.items(), key=lambda x: x[1], reverse=True)
# print(exp_count)
#
# pie_exp = (
#     Pie(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
#         .add("", exp_count,center=["60%","60%"])
#         .set_global_opts(legend_opts=opts.LegendOpts(orient="vertical", pos_left=0, pos_top="20%"))
#         .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
# )
# pie_exp.chart_id = "pie_exp"
#
# company_exp= {i: {j.split(" ")[0]:0 for j in set(company["关键词"])} for i in set(company["工作经验"])}
# print(company_exp)
# for i in set(company["工作经验"]):
#     for j in set(company["关键词"]):
#         for k in range(len(company)):
#             if company["工作经验"][k] == i and company["关键词"][k] == j:
#                 company_exp[i][j.split(" ")[0]] += 1
# #print(sorted(company_exp.items(), key=lambda x: x[1], reverse=True))
# # exp_sal = [[list(company_exp.keys())[i][0], list(company_exp.keys())[i][1], list(company_exp.values())[i]] for i in
# #            range(len(company_exp))]
# company_exp={i:[[list(company_exp[i].keys())[j],list(company_exp[i].values())[j]] for j in range(len(company_exp[i]))] for i in company_exp}
# print(company_exp)
# print([i[0] for i in company_exp["1-3年"]])
# print([i[1] for i in company_exp["经验不限"]])
#
# bar_exp = (
#     Bar(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
#         .add_xaxis([i[0] for i in company_exp["1-3年"]])
#         .add_yaxis("经验不限", [i[1] for i in company_exp["经验不限"]])
#         .add_yaxis("一年以下", [i[1] for i in company_exp["一年以下"]])
#         .add_yaxis("1-3年", [i[1] for i in company_exp["1-3年"]])
#         .add_yaxis("3-5年", [i[1] for i in company_exp["3-5年"]])
#         .add_yaxis("5-10年", [i[1] for i in company_exp["5-10年"]])
#         .add_yaxis("10年以上", [i[1] for i in company_exp["10年以上"]])
#         .set_global_opts(
#         xaxis_opts=opts.AxisOpts(
#             name='公司',
#             name_location='middle',
#             name_gap=35,
#             name_textstyle_opts=opts.TextStyleOpts(
#                 font_family='Times New Roman',
#                 font_size=18,
#                 color='black',
#             ),
#             axislabel_opts=opts.LabelOpts(interval=0)
#         ),
#         yaxis_opts=opts.AxisOpts(
#             name='岗位数',
#             name_location='middle',  # 在轴上面所处的位置
#             name_gap=35,  # 调整距离
#             name_textstyle_opts=opts.TextStyleOpts(
#                 font_family='Times New Roman',
#                 font_size=18,
#                 color='black',
#             )
#         )
#     )
#     #.set_global_opts(visualmap_opts=opts.VisualMapOpts(range_color=["#5599FF","#5599FF"],is_show=False))
# )
# bar_exp.chart_id="bar_exp"
#
# # 经验薪资关系统计
# # 各地区平均薪资折线
# job_s = pd.read_excel("job.xlsx")
# exp_sal = {}
# exp_sum = {}
# for i in set(job_s["工作经验"]):
#     exp_sal[i] = 0
#     exp_sum[i] = 0
#     for j in range(len(job_s)):
#         if job_s["工作经验"][j] == i and "-" in job_s["薪酬"][j]:
#             exp_sal[i] = exp_sal[i] + int(job_s["薪酬"][j].split("-")[0])
#             exp_sum[i] += 1
#     if exp_sum[i] != 0:
#         exp_sal[i] = round(exp_sal[i] / exp_sum[i], 2)
#     else:
#         exp_sal[i] = 0
# exp_sal = sorted(exp_sal.items(), key=lambda x: x[1], reverse=True)
# print(exp_sal)
# line_exp = (
#     Line(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
#         .add_xaxis([i[0] for i in exp_sal[0:10]])
#         .add_yaxis("", [i[1] for i in exp_sal[0:10]])
#         .set_global_opts(
#         xaxis_opts=opts.AxisOpts(
#             name='工作经验',
#             name_location='middle',
#             name_gap=35,
#             name_textstyle_opts=opts.TextStyleOpts(
#                 font_family='Times New Roman',
#                 font_size=18,
#                 color='black',
#             ),
#         ),
#         yaxis_opts=opts.AxisOpts(
#             name='薪资（k）',
#             name_location='middle',  # 在轴上面所处的位置
#             name_gap=35,  # 调整距离
#             name_textstyle_opts=opts.TextStyleOpts(
#                 font_family='Times New Roman',
#                 font_size=18,
#                 color='black',
#             )
#         )
#     )
#     # .set_global_opts(title_opts=opts.TitleOpts(title="地区薪资折线图"))
# )
# line_exp.chart_id = "line_exp"
#
# # 学历薪资职位数
# exp_sal = {(i, j): 0 for i in set(job["工作经验"]) for j in set(job["薪酬"])}
# print(exp_sal)
# for i in set(job["工作经验"]):
#     for j in set(job["薪酬"]):
#         for k in range(len(job)):
#             if job["工作经验"][k] == i and job["薪酬"][k] == j:
#                 exp_sal[(i, j)] += 1
# print(sorted(exp_sal.items(), key=lambda x: x[1], reverse=True))
# exp_sal = [[list(exp_sal.keys())[i][0], list(exp_sal.keys())[i][1], list(exp_sal.values())[i]] for i in
#            range(len(exp_sal))]
# print(exp_sal)
#
# Bar3D_exp_sal = (
#     Bar3D()
#         .add(
#         "",
#         exp_sal,
#         xaxis3d_opts=opts.Axis3DOpts(np.array(exp_sal)[:, 0], type_="category"),
#         yaxis3d_opts=opts.Axis3DOpts(np.array(exp_sal)[:, 1], type_="category"),
#         zaxis3d_opts=opts.Axis3DOpts(type_="value"),
#     )
#         .set_global_opts(
#         visualmap_opts=opts.VisualMapOpts(max_=500, is_show=False),
#         title_opts=opts.TitleOpts(title="工作经验薪酬职位数量统计"),
#     )
# )
# Bar3D_exp_sal.chart_id = "Bar3D_exp_sal"
#
# page_experiment = (
#     Page(layout=Page.DraggablePageLayout, page_title="工作经验")
#         .add(pie_exp)
#         .add(bar_exp)
#         .add(line_exp)
#         .add(Bar3D_exp_sal)
# ).render("page/page_experiment.html")
# Page.save_resize_html("page/page_experiment.html", cfg_file="json/experiment.json", dest="page/experiment.html")

# ==================================大厂==================================
# # 各大厂平均薪资
# company_sal = {}
# company_sum = {}
# for i in set(company["关键词"]):
#     company_sal[i[0:2]] = 0
#     company_sum[i] = 0
#     for j in range(len(company)):
#         if company["关键词"][j] == i and company["薪酬"][j] != "面议":
#             company_sal[i[0:2]] = company_sal[i[0:2]] + int(company["薪酬"][j])
#             company_sum[i] += 1
#     if company_sum[i] != 0:
#         company_sal[i[0:2]] = round(company_sal[i[0:2]] / company_sum[i], 2)
#     else:
#         company_sal[i[0:2]] = 0
# # company_sal = sorted(company_sal.items(), key=lambda x: x[1], reverse=True)
# company_sal = [[list(company_sal.keys())[i], list(company_sal.values())[i]] for i in range(len(company_sal))]
# print(company_sal)
# line_company = (
#     Line(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
#         .add_xaxis([i[0] for i in company_sal])
#         .add_yaxis("", [i[1] for i in company_sal])
#         .set_global_opts(
#         xaxis_opts=opts.AxisOpts(
#             name='大厂',
#             name_location='middle',
#             name_gap=35,
#             name_textstyle_opts=opts.TextStyleOpts(
#                 font_family='Times New Roman',
#                 font_size=18,
#                 color='black',
#             ),
#         ),
#         yaxis_opts=opts.AxisOpts(
#             name='薪资（k）',
#             name_location='middle',  # 在轴上面所处的位置
#             name_gap=35,  # 调整距离
#             name_textstyle_opts=opts.TextStyleOpts(
#                 font_family='Times New Roman',
#                 font_size=18,
#                 color='black',
#             )
#         )
#     )
# )
#
# bar_company = (
#     Bar(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
#         .add_xaxis([i[0] for i in company_sal])
#         .add_yaxis("", [i[1] for i in company_sal])
#         .set_global_opts(
#         xaxis_opts=opts.AxisOpts(
#             name='大厂',
#             name_location='middle',
#             name_gap=35,
#             name_textstyle_opts=opts.TextStyleOpts(
#                 font_family='Times New Roman',
#                 font_size=18,
#                 color='black',
#             ),
#         ),
#         yaxis_opts=opts.AxisOpts(
#             name='薪资（k）',
#             name_location='middle',  # 在轴上面所处的位置
#             name_gap=35,  # 调整距离
#             name_textstyle_opts=opts.TextStyleOpts(
#                 font_family='Times New Roman',
#                 font_size=18,
#                 color='black',
#             )
#         )
#     )
#         .set_global_opts(visualmap_opts=opts.VisualMapOpts(range_color=["#99bbff", "#99bbff"], is_show=False,pos_left="70%"))
#         .set_series_opts(label_opts=opts.LegendOpts(is_show=False))
# ).overlap(line_company)
# bar_company.chart_id = "bar_company"
#
# # 大厂工作经验与薪资情况
# company_exp_sal = {(i.split(" ")[0], j): 0 for i in set(company["关键词"]) for j in set(company["工作经验"])}
# company_exp_sum = {(i.split(" ")[0], j): 0 for i in set(company["关键词"]) for j in set(company["工作经验"])}
# print(company_exp_sal)
# for i in set(company["关键词"]):
#     for j in set(company["工作经验"]):
#         for k in range(len(company)):
#             if company["关键词"][k] == i and company["工作经验"][k] == j and company["薪酬"][k] != "面议":
#                 company_exp_sal[(i.split(" ")[0], j)] += int(company["薪酬"][k])
#                 company_exp_sum[(i.split(" ")[0], j)] += 1
#         if company_exp_sum[(i.split(" ")[0], j)] != 0:
#             company_exp_sal[(i.split(" ")[0], j)] = round(
#                 company_exp_sal[(i.split(" ")[0], j)] / company_exp_sum[(i.split(" ")[0], j)], 2)
#         else:
#             company_exp_sal[(i.split(" ")[0], j)] = 0
# print(sorted(company_exp_sal.items(), key=lambda x: x[1], reverse=True))
# company_exp_sal = [
#     [list(company_exp_sal.keys())[i][0], list(company_exp_sal.keys())[i][1], list(company_exp_sal.values())[i]]
#     for i in
#     range(len(company_exp_sal))]
# print(company_exp_sal)
#
# Bar3D_company_exp_sal = (
#     Bar3D()
#         .add(
#         "",
#         company_exp_sal,
#         xaxis3d_opts=opts.Axis3DOpts(np.array(company_exp_sal)[:, 0], type_="category", interval=0),
#         yaxis3d_opts=opts.Axis3DOpts(np.array(company_exp_sal)[:, 1], type_="category"),
#         zaxis3d_opts=opts.Axis3DOpts(type_="value"),
#     )
#         .set_global_opts(
#         visualmap_opts=opts.VisualMapOpts(max_=50, is_show=False),
#         title_opts=opts.TitleOpts(title="大厂开发岗位经验与薪酬统计"),
#     )
# )
# Bar3D_company_exp_sal.chart_id = "Bar3D_company_exp_sal"
#
# # 各地区大厂数量
# company_area = {i.split(" ")[0]: {j: 0 for j in set(company["地区"])} for i in set(company["关键词"])}
# print(company_area)
# for i in set(company["关键词"]):
#     for j in set(company["地区"]):
#         for k in range(len(company)):
#             if company["关键词"][k] == i and company["地区"][k] == j and j != "中国":
#                 company_area[i.split(" ")[0]][j] += 1
#         if company_area[i.split(" ")[0]][j] == 0:
#             del (company_area[i.split(" ")[0]][j])
# # print(sorted(company_exp.items(), key=lambda x: x[1], reverse=True))
# # exp_sal = [[list(company_exp.keys())[i][0], list(company_exp.keys())[i][1], list(company_exp.values())[i]] for i in
# #            range(len(company_exp))]
# company_area = {
#     i: [[list(company_area[i].keys())[j], list(company_area[i].values())[j]] for j in range(len(company_area[i]))] for i
#     in company_area}
# print(company_area)
#
# geo_company = (
#     Geo()
#         .add_schema(maptype="china")
#         .add("京东", company_area["京东"])
#         .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#         .set_global_opts(
#         # visualmap_opts=opts.VisualMapOpts(), title_opts=opts.TitleOpts(title="Geo-基本示例")
#     )
#         .add_schema(maptype="china")
#         .add("阿里巴巴", company_area["阿里巴巴"])
#         .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#         .set_global_opts(
#         # visualmap_opts=opts.VisualMapOpts(), title_opts=opts.TitleOpts(title="Geo-基本示例")
#     )
#         .add_schema(maptype="china")
#         .add("华为", company_area["华为"])
#         .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#         .set_global_opts(
#         # visualmap_opts=opts.VisualMapOpts(), title_opts=opts.TitleOpts(title="Geo-基本示例")
#     )
#         .add_schema(maptype="china")
#         .add("字节跳动", company_area["字节跳动"])
#         .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#         .set_global_opts(
#         # visualmap_opts=opts.VisualMapOpts(), title_opts=opts.TitleOpts(title="Geo-基本示例")
#     )
#         .add_schema(maptype="china")
#         .add("小米", company_area["小米"])
#         .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#         .set_global_opts(
#         # visualmap_opts=opts.VisualMapOpts(), title_opts=opts.TitleOpts(title="Geo-基本示例")
#     )
#         .add_schema(maptype="china")
#         .add("美团", company_area["美团"])
#         .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#         .set_global_opts(
#         visualmap_opts=opts.VisualMapOpts(), title_opts=opts.TitleOpts(title="Geo-基本示例")
#     )
#         .add_schema(maptype="china")
#         .add("腾讯", company_area["腾讯"])
#         .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#         .set_global_opts(
#         # visualmap_opts=opts.VisualMapOpts(), title_opts=opts.TitleOpts(title="Geo-基本示例")
#     )
#         .add_schema(maptype="china")
#         .add("百度", company_area["百度"])
#         .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#         .set_global_opts(
#         # visualmap_opts=opts.VisualMapOpts(), title_opts=opts.TitleOpts(title="Geo-基本示例")
#     )
#         .add_schema(maptype="china")
#         .add("寻梦", company_area["寻梦"])
#         .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
# )
# geo_company.chart_id="geo_company"
#
# word_company = {}
# for i in range(len(company["标签"])):
#     for j in company["标签"][i].split():
#         if j not in word_company:
#             word_company[j] = 1
#         else:
#             word_company[j] += 1
# word_company=sorted(word_company.items(), key=lambda x: x[1], reverse=True)
# print(word_company)
# wordcloud_company = (
#     WordCloud()
#         .add("互联网岗位薪资词云", word_company))
# wordcloud_company.chart_id="wordcloud_company"
#
# page_company = (
#     Page(layout=Page.DraggablePageLayout, page_title="大厂信息")
#         .add()
#         .add(geo_company)
#         .add(bar_company)
#         .add(Bar3D_company_exp_sal)
#         .add(wordcloud_company)
# ).render("page/page_company.html")
# Page.save_resize_html("page/page_company.html", cfg_file="json/company.json", dest="page/company.html")

#不想写了以下代码不用运行
# # ===========================================关键词====================================
# keyword = ["软件"]
# salary_range = set(job["薪酬"])
# salary_range.remove("3k")
# salary_range.remove("40k")
# edu_range = set(job["学历"])
# edu_range.remove("本科")
# for i in range(len(keyword)):
#     keyword_salary = {j: 0 for j in salary_range for k in range(len(job)) if job["关键词"][k] == keyword[i]}
#     for j in salary_range:
#         for k in range(len(job)):
#             if job["关键词"][k] == keyword[i] and job["薪酬"][k] == j:
#                 keyword_salary[j] += 1
#     keyword_salary = sorted(keyword_salary.items(), key=lambda x: x[1], reverse=True)
#     print(keyword_salary)
#
#     keyword_edu = {j: 0 for j in edu_range for k in range(len(job)) if job["关键词"][k] == keyword[i]}
#     for j in edu_range:
#         for k in range(len(job)):
#             if job["关键词"][k] == keyword[i] and job["学历"][k] == j:
#                 keyword_edu[j] += 1
#     keyword_edu = sorted(keyword_edu.items(), key=lambda x: x[1], reverse=True)
#     print(keyword_edu)
#
#     keyword_name = {j: 0 for j in set(job["岗位名称"]) for k in range(len(job)) if job["关键词"][k] == keyword[i]}
#     print(keyword_name)
#     for j in set(job["岗位名称"]):
#         for k in range(len(job)):
#             if job["关键词"][k] == keyword[i] and job["岗位名称"][k] == j:
#                 keyword_name[j] += 1
#     keyword_name = sorted(keyword_name.items(), key=lambda x: x[1], reverse=True)
#     print(keyword_name)
#
#     pie_keywordsalary = (
#         Pie()
#             .add(
#             "",
#             keyword_salary,
#             radius=["30%", "75%"],
#             rosetype="radius",
#             label_opts=opts.LabelOpts(is_show=False),
#         )
#             .set_global_opts(title_opts=opts.TitleOpts(title="薪酬统计"),
#                              legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%") )
#             .render("1.html")
#     )
#
#     bar_company = (
#         Bar(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
#             .add_xaxis([i[0] for i in keyword_edu])
#             .add_yaxis("", [i[1] for i in keyword_edu])
#             .set_global_opts(
#             xaxis_opts=opts.AxisOpts(
#                 name='学历',
#                 name_location='middle',
#                 name_gap=35,
#                 name_textstyle_opts=opts.TextStyleOpts(
#                     font_family='Times New Roman',
#                     font_size=18,
#                     color='black',
#                 ),
#             ),
#             yaxis_opts=opts.AxisOpts(
#                 name='岗位数',
#                 name_location='middle',  # 在轴上面所处的位置
#                 name_gap=35,  # 调整距离
#                 name_textstyle_opts=opts.TextStyleOpts(
#                     font_family='Times New Roman',
#                     font_size=18,
#                     color='black',
#                 )
#             )
#         )
#             .set_global_opts(
#             visualmap_opts=opts.VisualMapOpts(range_color=["#99bbff", "#99bbff"], is_show=False, pos_left="70%"))
#             .set_series_opts(label_opts=opts.LegendOpts(is_show=False))
#     ).render("2.html")
#
#     keyword_wordcloud=(
#         WordCloud()
#             .add("", keyword_name)).render("3.html")

c = (
    Gauge()
    .add(
        "业务指标",
        [("完成率", 55.5)],
        split_number=5,
        axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
                color=[(0.3, "#67e0e3"), (0.7, "#37a2da"), (1, "#fd666d")], width=30
            )
        ),
        detail_label_opts=opts.LabelOpts(formatter="{value}"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Gauge-分割段数-Label"),
        legend_opts=opts.LegendOpts(is_show=True),
    )
    .render("gauge_splitnum_label.html")
)